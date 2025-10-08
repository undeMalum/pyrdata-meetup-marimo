# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib==3.10.6",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.16.1"
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
    a = 5
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We need more ~~pure~~ graphical math!""")
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    return MaxNLocator, pd, plt


@app.function
def fib_list(n: int) -> list[int]:
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


@app.cell
def _(MaxNLocator, pd, plt):
    def plot_fib(n: int) -> None:
        fibs = fib_list(n)
        df = pd.DataFrame({"n": list(range(1, n+1)), "fib": fibs})

        # Plot inline
        plt.figure(figsize=(10, 4))
        plt.xlabel("n (index)")
        plt.ylabel("Fib(n)")
        plt.plot(df["n"], df["fib"], marker="o")
        plt.xlabel("n (index)")
        plt.ylabel("Fib(n)")
        plt.title(f"First {n} Fibonacci numbers")
        plt.grid(True)
        ax = plt.gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.tight_layout()
        plt.show()
    return (plot_fib,)


@app.cell
def _(mo):
    fib_slider = mo.ui.slider(2, 20, 1)
    fib_slider
    return (fib_slider,)


@app.cell
def _(fib_slider, plot_fib):
    plot_fib(fib_slider.value)
    return


if __name__ == "__main__":
    app.run()
