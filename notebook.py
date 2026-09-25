import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest 

    return mo, pytest


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
    ## Case 2 bis: refactoring of the first implementation
    """)
    return


@app.function
def fibonacci(n):
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci excepts a positive integer")
        
    if n>1 :
        return fibonacci(n-1)+fibonacci(n-2)
        
    else :
        return n


@app.cell
def test_first_fibo_cases_int_positive():
    assert fibonacci(0)==0
    assert fibonacci(1)==1
    assert fibonacci(2)==1 
    return


@app.cell
def test_invalid_input_rejection(pytest):
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci('test')
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Case 3 : optimization
    """)
    return


@app.cell
def _():
    # assertions with larger values
    assert fibonacci(10) == 55
    assert fibonacci(50) == 12586269025
    assert fibonacci(100) == 354224848179261915075
    return


@app.cell
def _():
    fibo_values = {}

    def fibonacci_opti(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Fibonacci excepts a positive integer")

        if n in fibo_values:
            return fibo_values[n]

        elif n > 1:
            fibo_values[n] = fibonacci_opti(n-1) + fibonacci_opti(n-2)
            return fibo_values[n]
        else :
            return n

    return (fibonacci_opti,)


@app.cell
def _(fibonacci_opti):
    # assertions with larger values
    assert fibonacci_opti(10) == 55
    assert fibonacci_opti(50) == 12586269025
    assert fibonacci_opti(100) == 354224848179261915075

    print(fibonacci_opti(1000))
    return


if __name__ == "__main__":
    app.run()
