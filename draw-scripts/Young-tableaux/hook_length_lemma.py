import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

pp = [1, 2, 3, 3, 5, 5, 6, 7]

figure = plt.figure(figsize=(4, 4), dpi=300)
ax = figure.add_axes([0, 0, 1, 1])
ax.axis([-0.5, pp[-1] + 1, -0.5, len(pp) + 0.5])
ax.axis("off")

for height, lamb_i in enumerate(pp):
    for x in range(lamb_i):
        patch = Rectangle(xy=(x, height), width=1, height=1, ec="k", lw=0.5, fill=False)
        ax.add_patch(patch)

fs = 10
ax.text(-0.2, -0.3, "$(0,0)$", ha="center", va="center", fontsize=fs)
ax.text(0.5, -0.2, "$0$", ha="center", va="center", fontsize=fs)
ax.text(1.2, 0.5, "$1$", ha="center", va="center", fontsize=fs)
ax.text(1.5, 0.8, "$2$", ha="center", va="center", fontsize=fs)
ax.text(2.2, 1.5, "$3$", ha="center", va="center", fontsize=fs)
ax.text(8.0, 7.5, r"$\lambda_1+\lambda_1'-1$", ha="center", va="center", fontsize=fs)
ax.text(7.2, 8.3, r"$\lambda_1+\lambda_1'$", ha="center", va="center", fontsize=fs)
C = plt.Circle((0, 0), 0.05, ec="k", fc="w")
ax.add_patch(C)
C = plt.Circle((7, 8), 0.05, ec="k", fc="w")
ax.add_patch(C)

pathch = Rectangle(xy=(0, 2), width=1, height=1, fc=(0, 0.2, 0.8))
ax.add_patch(pathch)
ax.text(0.5, 2.5, "$v$", ha="center", va="center", fontsize=fs, color="w")
pathch = Rectangle(xy=(4, 7), width=1, height=1, fc=(0.8, 0.2, 0))
ax.add_patch(pathch)
ax.text(4.5, 7.5, "$u$", ha="center", va="center", fontsize=fs, color="w")
ax.text(
    3.3, 2.5, "$h_v$", ha="center", va="center", fontsize=fs + 1, color=(0, 0.2, 0.8)
)
ax.text(
    4.5,
    3.7,
    r"$\lambda_1+\lambda_1'-1 - h_u$",
    ha="center",
    va="center",
    fontsize=fs + 1,
    color=(0.8, 0.2, 0),
)
figure.savefig("hook_length_lemma.svg", bbox_inches="tight")
