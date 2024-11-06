import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 18

pi = np.pi

fig, ax = plt.subplots(1, figsize=(4, 4))
ax.set_aspect("equal")
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xticks([-pi, 0, pi])
ax.set_yticks([-pi, pi])
ax.set_xticklabels(["$-\pi$", "$0$", "$\pi$"])
ax.set_yticklabels(["$-\pi$", "$\pi$"])
ax.set(ylim=(-pi, pi), xlim=(-pi, pi))

x = [-pi, 0, pi, 0, -pi]
y = [0, pi, 0, -pi, 0]
X = [-pi, pi, pi, -pi]
Y = [-pi, -pi, pi, pi]
S = [(x, y) for x, y in zip(X, Y)]
S = patches.Polygon(
    S, facecolor="pink", edgecolor="r", label="$|u|\leq\pi,|v|\leq\pi$", lw=1
)

T = [(x, y) for x, y in zip(x, y)]
T = patches.Polygon(T, facecolor="white", edgecolor="b", label="$|u|+|v|\leq\pi$", lw=1)
ax.add_patch(S)
ax.add_patch(T)
fig.tight_layout()
plt.legend()
plt.show()
fig.savefig("region.svg")
