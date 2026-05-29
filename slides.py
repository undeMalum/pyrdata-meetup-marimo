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
        align="center",
    )
    return


@app.cell
def _(media, mo):
    mo.vstack(
        [
            mo.image(
                "https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg",
                height=500,
                width=500,
            ),
            mo.image(media / "stars.png", height=60, width=600),
        ],
        align="center",
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


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.iframe(
                "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/no_re-execution.html"
            ),
            mo.md(
                """## Math ain't mathing:
    * $a = 6$
    * $b = a + 1 = 7$
    * so $a + b = 13$, not $12$!
            """
            ),
        ],
        # align="center"
    )
    return


@app.cell
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/delete_b.html"
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.iframe(
                "https://undemalum.github.io/portfolio/notebooks/hidden_states/jupyter/delete_b.html"
            ),
            mo.md("#Where is $b$ defined?"),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo Solution
    """)
    return


@app.cell
def _(mo):
    mo.iframe("https://undemalum.github.io/pyrdata-meetup-marimo/")
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.image(
                "https://undemalum.github.io/portfolio/notebooks/hidden_states/dags/marimo_dag.svg"
            )
        ]
    )
    return


@app.cell
def _(mo):
    mo.iframe("https://undemalum.github.io/pyrdata-meetup-marimo/")
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.image(
                "https://undemalum.github.io/portfolio/notebooks/hidden_states/dags/marimo_delete_b.svg"
            )
        ]
    )
    return


@app.cell
def _(media, mo):
    mo.vstack(
        [mo.image(media / "graph.png", width=750, height=500)], align="center"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - ## No hidden states
    - ## Plain errors
    - ## Clearly defined order:
      - ## Like Python scripts?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Git-Friendliness
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
        "https://undemalum.github.io/portfolio/notebooks/git_friendliness/jupyter/add_changes.html"
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.iframe(
                "https://undemalum.github.io/portfolio/notebooks/git_friendliness/jupyter/add_changes.html"
            ),
            mo.md(
                """```bash
    git add content/posts/marimo-overview/math_analysis.ipynb
    git commit -m "Add changes to Jupyter Notebook and run it"
    git push
    ```
                """
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # *.ipynb
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```json
    {
      "cells": [
        {
          "cell_type": "markdown",
          "id": "d6605f7b",
          "source": ["This is the _beginning_ of the **hard** math analysis"]
        },
        {
          "cell_type": "code",
          "execution_count": 1,
          "id": "a8feff8f",
          "source": ["a = 5"]
        }
      ],
      "metadata": {
        "kernelspec": { "display_name": "Python 3 (ipykernel)", "name": "python3" },
        "language_info": { "name": "python", "version": "3.11.6" }
      },
      "nbformat": 4,
      "nbformat_minor": 5
    }

    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```
    +  {
    +   "cell_type": "code",
    +   "execution_count": 4,
    +   "id": "882cd319-f4e1-4a19-befc-8ffae114f7d1",
    +   "metadata": {},
    +   "outputs": [],
    +   "source": [
    +    "z = a + b"
    +   ]
    +  },
    +  {
    +   "cell_type": "code",
    +   "execution_count": 6,
    +   "id": "97318bef-729c-489a-81bc-d8237d10f1ea",
    +   "metadata": {},
    +   "outputs": [
    +    {
    +     "data": {
    +      "text/plain": [
    +       "33"
    +      ]
    +     },
    +     "execution_count": 6,
    +     "metadata": {},
    +     "output_type": "execute_result"
    +    }
    +   ],
    +   "source": [
    +    "z * 3"
    +   ]
    +  }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    z = a + b
    z * 3
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Case in point
    """)
    return


@app.cell
def _(media, mo):
    mo.hstack(
        [
            mo.image(media / "codebase.png"),
            mo.vstack(
                [
                    mo.md("## Jupyter Notebook:"),
                    mo.image(media / "diffs.png"),
                    mo.image(media / "load.png"),
                ],
                justify="center",
                align="center",
            ),
        ],
        align="center",
        justify="center",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # *.py?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```python
    import marimo

    __generated_with = "0.16.1"
    app = marimo.App(width="medium")


    @app.cell
    def _():
        import marimo as mo
        return (mo,)


    @app.cell(hide_code=True)
    def _(mo):
        mo.md(r"\"\"This is the _beginning_ of the **hard** math analysis"\"\")
        return


    @app.cell
    def _(a):
        b = a + 1
        return (b,)


    if __name__ == "__main__":
        app.run()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        "https://undemalum.github.io/portfolio/notebooks/git_friendliness/marimo/add_changes.html"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```bash
    git add notebook.py
    git commit -m "Add changes to Marimo and run it"
    git push
    ```
    """)
    return


@app.cell
def _(media, mo):
    mo.hstack(
        [
            mo.md(
                """
    ```
    +@app.cell
    +def _(a, b):
    +    z = a + b
    +    return (z,)
    +
    +
    +@app.cell
    +def _(z):
    +    z * 3
    +    return
    ```
            """
            ),
            mo.image(media / "z.png"),
        ],
        justify="center",
        align="center",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - ##Easier code reviews
    - ##Cleaner merge conflicts
    - ##Reliable GitHub rendering
    - ##Meaningful git history
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Reproducibility
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
        "https://undemalum.github.io/portfolio/notebooks/reproducibility/jupyter/plotting.html"
    )
    return


@app.cell
def _(media, mo):
    mo.vstack([mo.image(media / "imports.png")], align="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dependency managment in Python...
    """)
    return


@app.cell
def _(mo):
    mo.hstack(
        [
            mo.md(
                """
    - uv?
    - conda?
    - poetry?
    - pip + venv?
                        """
            ),
            mo.md(
                """
    - requirements.txt?
    - setup.py?
    - Pipfile?
    - environment.yml?
                        """
            ),
        ],
        # align="center",
        justify="center",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## (1) Clone the repo
    git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

    ## (2) Go into the project folder
    cd /path/to/cloned/project

    ## (3) Sync dependencies
    uv sync

    ## (4) Activate the virtual environment
    source .venv/bin/activate       # Linux/MacOS

    .venv/Scripts/Activate.ps1      # Windows

    ## (5) Finally, launch Jupyter
    jupyter notebook
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - ## Many notebooks don’t declare dependencies at all
    - ## Those that do, often declare them incorrectly.

    #Conclusion: the majority of Jupyter notebooks in the wild **are not reproducible**.
    """)
    return


@app.cell
def _(mo):
    mo.iframe("https://undemalum.github.io/portfolio/notebooks/reproducibility/jupyter/error.html")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `ModuleNotFoundError`
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #
    """)
    return


if __name__ == "__main__":
    app.run()
