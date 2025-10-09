import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This is the _beginning_ of the **hard** math analysis""")
    return


@app.cell
def _():
    a = 6
    return (a,)


@app.cell
def _(a):
    b = a + 1
    return (b,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's **mix** some variables!""")
    return


@app.cell
def _(a, b):
    a + b
    return


@app.cell
def _(a, b):
    z = a + b
    return (z,)


@app.cell
def _(z):
    z * 3
    return


if __name__ == "__main__":
    app.run()
