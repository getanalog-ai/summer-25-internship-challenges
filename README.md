# Analog Challenges

This repository hosts a collection of challenging programming problems designed to test problem-solving and engineering skills. Each puzzle is self-contained within its own directory.

Select one of the challenge that most interests you and submit your completion if you are interested in internship opportunities at Maple AI.

## Getting Started

To attempt a challenge:

1. **Navigate** to the challenge's directory (e.g., `cd challenge-1`).
2. **Read** the `problem.md` file within that directory. It contains the detailed problem statement, input/output format, scoring rules, and submission requirements.
3. **Use** the provided starter code (if available, often a `.py` file like `codec.py`).
4. **Implement** your solution according to the specifications in `problem.md`.

## Running & Testing

Some challenge include instructions for running your solution locally within their `problem.md` file. Typically, this involves running a script and providing input data via `STDIN`. You can use uv to manage allowed dependencies, or globally install them if you prefer.

For example, for the `challenge-1` puzzle:

```bash
uv run --with tiktoken challenge-1/codec.py < challenge-1/sample_graph.json
```

Refer to the specific challenge's `problem.md` for exact commands and any sample data provided.
