# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.23.8",
# ]
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium", layout_file="layouts/slides.slides.json")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from pathlib import Path

    media = Path.cwd() / "media"
    return (media,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo as the successor to Jupyter Notebook.
    - Mateusz Konat, P.I.W.O, 30.05.2025
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Who uses Jupyter Notebook?

    - JupyterLab
    - Google Colab
    - IDE extensions
    - ... and so on.
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.image(
                "https://undemalum.github.io/portfolio/posts/marimo-overview/images/jupytes_explanation.jpg",
                # width=600,
                # height=500
            ),
        ],
        align="center"
    )
    return


@app.cell
def _(media, mo):
    mo.vstack(
        [
            mo.image(
                "https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg",
                height=500,
                width=500
            ),
            mo.image(
                media / "stars.png",
                height=60,
                width=600
            )
        ],
        align="center"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo VS Jupyter Notebook

    1. Agenda (Problem Definition + Marimo Solution)
       - Hidden Stated
       - Git-Friendlines
       - Reporducibility
    2. Demos

    ### Inspired by: *Large-scale Study about Quality and Reproducibility of Jupyter Notebooks*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Hidden States
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Problem Definition
    """)
    return


@app.cell
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/setup.html"
    )
    return


@app.cell
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/initial_run.html"
    )
    return


@app.cell
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/no_re-execution.html"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Math ain't mathing:
    * $a = 6$
    * $b = a + 1 = 7$
    * so $a + b = 13$, not $12$!
    """)
    return


@app.cell
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/delete_b.html"
    )
    return


@app.cell
def _(mo):
    mo.code_editor()
    return


@app.cell
def _(mo):
    mo.code_editor()
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.image("https://undemalum.github.io/portfolio/notebooks/hidden_states/dags/marimo_dag.svg")
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.image("https://undemalum.github.io/portfolio/notebooks/hidden_states/dags/marimo_delete_b.svg")
        ]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
