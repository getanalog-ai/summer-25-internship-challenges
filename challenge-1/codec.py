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
        decode(encode(g)) == canonicalise(g)
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
    print(f"#tokens: {_token_count(blob)}", file=sys.stderr)
