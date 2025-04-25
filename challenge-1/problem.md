# Token‑Tight Context Codec

Can you beat `JSON` at its own game?
Compress a labelled graph so aggressively that, after the `cl100k_base` tokenizer, it costs fewer context tokens than the raw `JSON` by a large margin—yet can still be decoded back bit‑perfectly.

## 1 Problem statement

Large‑context LLMs still make you pay per token. A classic property‑graph in minified `JSON`:

```jsonc
{
  "nodes": [
    {"id": "A17", "desc": "Start"},
    {"id": "B42", "desc": "Compute Fibonacci"},
    {"id": "C13", "desc": "Return"}
  ],
  "edges": [
    {"u": "A17", "v": "B42"},
    {"u": "B42", "v": "C13"}
  ]
}
```

already burns 40+ tokens in `cl100k_base`—before the model even reads any prompt.

You must invent an injective textual encoding that, given such a `JSON` graph, emits a single `ASCII` string `S` that

can be decoded uniquely and loss‑lessly back to the exact `JSON` object (ordering of keys/arrays may change but the information must be identical), and

is short in tokenizer‑tokens.

The judge will compare your `decode(encode(J))` with the original object and compute

$$\text{Score} = \frac{T_{\text{baseline}}}{T_{\text{yours}}}, \qquad T = \text{\#tokens by } \texttt{tiktoken.get\_encoding("cl100k\_base")}$$

Higher is better; ≥ 1.00 beats the baseline (straight minified `JSON`).

## 2 Input format

Your program receives exactly one `JSON` object on `STDIN` with:

| Field | Type | Meaning |
|---|---|---|
| `nodes` | array | Length `N` ≤ 100 000 <ul><li>`id`: string, arbitrary `UTF‑8` ≤ 64 bytes, unique</li><li>`desc`: string, `UTF‑8` ≤ 256 bytes</li></ul> |
| `edges` | array | Length `M` ≤ 300 000 <ul><li>`u`,`v`: string, IDs of incident nodes (graph is directed, multiple edges allowed)</li></ul> |

No guarantees on ordering or connectedness.

## 3 Output format

Print one line containing your encoded string
(`ASCII` bytes 32–126 only; no newlines, no trailing spaces).

## 4 Correctness requirements

Injectivity: your decoder must perfectly reconstruct every node `id`, `desc`, and every edge (including multiplicities and direction).

Determinism: `encode` must return the same string for identical input.

Runtime: `encode` + `decode` together ≤ 2 s and ≤ 1 GB RAM on the largest test.

## 5 Scoring

For each hidden test `t`

`T_baseline(t)` – tokens in minified `JSON`

`T_you(t)` – tokens in your `encode` output

Your raw score is the geometric mean of `T_baseline`/`T_you` over all tests.
Leaderboard ranks by raw score, then total runtime.

## 6 Submission API expected by the judge

Upload a single `codec.py` that provides

```py
def encode(graph: dict) -> str: ...
def decode(blob: str) -> dict: ...
```

The judge will `import codec`, call `encode`, run `decode`, verify equality, then tokenise the `blob`.

## Starter Skeleton(`codec.py`)

```py
import json
import sys
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")


# ---------- public API ---------- #
def encode(graph: dict) -> str:
    """
    Return an ASCII string that can be decoded back to `graph`.
    Replace the body with your own codec.
    """
    # naïve baseline: minified JSON (≈ baseline score ≈ 1.00)
    return json.dumps(graph, separators=(",", ":"))


def decode(blob: str) -> dict:
    """
    Inverse of `encode`. Must satisfy:
        `decode(encode(g))` == `canonicalise(g)`
    """
    return json.loads(blob)


# ---------- local runner ---------- #
def _token_count(s: str) -> int:
    return len(enc.encode(s))


if __name__ == "__main__":
    raw = sys.stdin.read()
    g = json.loads(raw)
    blob = encode(g)
    rebuilt = decode(blob)

    assert rebuilt == g, "round‑trip failed"
    print(blob)
    print(f"#tokens: { _token_count(blob) }", file=sys.stderr)
```

Run locally:

```bash
python codec.py < sample_graph.json
```

## 8. Advice & checkpoints

| Milestone | Idea sketches |
|---|---|
| ≤ 0.90× | Drop quotes & commas via custom `base‑N` / `BPE‑aware` alphabet. |
| ≤ 0.60× | Canonicalise `IDs` to integers, `Δ‑encode` edges, `front‑code` descs. |
| ≤ 0.35× | `Mixed‑radix` arithmetic code + `tokenizer merge` exploitation. |
| ≤ 0.25× | Dictionary rebuild from `desc‑suffix` tree, `entropy‑code` edge list. |

Remember: `token count`, not `byte count`, is the objective—study the merge rules!

Good luck & happy squeezing.
