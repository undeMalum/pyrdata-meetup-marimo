# Repository for my [PyrData Talk](https://www.linkedin.com/events/pyrdataspotkanie-57373625006636826625)

[Presentation](https://docs.google.com/presentation/d/1he-Mqk-vlo-VN_dmaD-ibY6HcFWIkysmqmDzNe387yQ/edit?usp=sharing)

Every file with `*.py` can be run with:
```bash
uvx run marimo run --sandbox url/to/the/file.py
```

## Code I want to copy for my presentation:
1. Git-Friendliness:

```python
z = a + b
```

```python
z * 3
```

2. Reproducibility

```markdown
We need more ~~pure~~ graphical math!
```

```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
```

```python
def fib_list(n: int) -> list[int]:
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
```

```python
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
```

```python
n = 20
plot_fib(n)
```

## Demos
**1. Tender Analysis App:**
```bash
uvx run marimo edit --sandbox https://github.com/undeMalum/pyrdata-meetup-marimo/blob/main/tender_browser.py
```
