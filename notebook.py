import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # TDD-Kata : Fibonacci function

    The Fibonacci sequence is defined by
        F(0) = 0
        F(1) = 1
        F(n) = F(n−1) + F(n−2)    for n ≥ 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Case 1 : no implementation
    """)
    return


@app.function
def fibo_v1(n):
    pass


@app.cell
def _():
    assert fibo_v1(0)==0
    assert fibo_v1(1)==1
    assert fibo_v1(2)==1 
    return


if __name__ == "__main__":
    app.run()
