# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:

    import marimo as mo

    from fibonacci_tdd_kata import fibonacci_opti


@app.cell
def _():
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range below and see how Fibonacci classifies each number
    in it, both as a list and as a chart of the distribution of
    outputs. This notebook consumes the published CS_fibonacci_tdd_kata
    package — it does not reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    results = [fibonacci_opti(n) for n in range(lo, hi + 1)]
    results
    return


if __name__ == "__main__":
    app.run()
