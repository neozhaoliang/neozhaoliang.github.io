import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

plt.rcParams["font.size"] = 18
plt.rcParams["text.usetex"] = True


def string_diagram(fname, labels, active=None):
    n = len(labels) + 1
    if active is None:
        active = [0] * n
    positions = np.arange(n).astype(float)
    if n % 2 == 1:
        positions -= (n - 1) / 2
    else:
        positions -= n / 2 - 0.5

    positions /= 4.0
    left = positions[0]
    end = positions[-1]

    plt.plot([left, end], [0, 0], "k-", lw=1)
    for x, is_active in zip(positions, active):
        if is_active:
            plt.plot(x, 0, "wo", ms=16, markeredgewidth=1, markeredgecolor="k")
        plt.plot(x, 0, "yo", ms=8, markeredgewidth=1.5, markeredgecolor="k")
    for i in range(len(labels)):
        if labels[i] == "3":
            continue
        plt.text(
            (positions[i] + positions[i + 1]) / 2,
            0.01,
            f"${labels[i]}$",
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.axis("off")
    plt.axis("equal")
    plt.axis([left - 0.1, end + 0.1, -0.1, 0.1])
    plt.savefig(fname, bbox_inches="tight")


string_diagram(
    "37.svg",
    "37",
    active=[
        1,
        0,
        0,
    ],
)
