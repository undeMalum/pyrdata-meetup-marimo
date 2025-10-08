import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _():
    URL = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"
    return (URL,)


@app.cell
def _(URL, mo, pl):
    df = pl.read_csv(URL)
    mo.plain(df)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, mo):
    pokemon_table = mo.ui.table(df)
    pokemon_table
    return (pokemon_table,)


@app.cell
def _(pokemon_table):
    pokemon_table.value
    return


@app.cell
def _(df, mo):
    mo.ui.dataframe(df)
    return


@app.cell
def _(df, mo):
    mo.ui.data_explorer(df)
    return


if __name__ == "__main__":
    app.run()
