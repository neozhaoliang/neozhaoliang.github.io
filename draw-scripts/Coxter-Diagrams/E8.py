import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

plt.rcParams["font.size"] = 16
plt.rcParams["text.usetex"] = True


plt.plot([0, 6], [0, 0], "k-", lw=1)
plt.plot([4, 4], [0, 1], "k-", lw=1)
for x in range(7):
    plt.plot(x, 0, "o", color=(1, 1, 0), ms=9, markeredgewidth=1.5, markeredgecolor="k")
plt.plot(4, 1, "o", color=(1, 1, 0), ms=9, markeredgewidth=1.5, markeredgecolor="k")
for x in range(7):
    plt.text(x, -0.4, f"${x+1}$", ha="center", va="bottom")

plt.text(4, 1.1, "$8$", ha="center", va="bottom")
plt.gca().axis("off")
plt.gca().set_aspect("equal")
plt.axis([-0.1, 6.1, -0.2, 1.25])
plt.savefig("e8-dynkin.svg", bbox_inches="tight")
