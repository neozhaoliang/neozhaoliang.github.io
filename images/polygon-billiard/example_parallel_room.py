import matplotlib.pyplot as plt


from billiard import create_parallel_room, Vec2, palette

# create a room with two parallel mirrors (x=-1 and x=1)
room = create_parallel_room()

# position of the assassin
assin = Vec2(-0.2, 0)
# position of the target
target = Vec2(0.66, 10)
# the first reflection of the target
target1 = room.mirrors[0].reflect(target)

# get all virtual targets in some range
odd_targets = [target1 + Vec2(4 * i, 0) for i in range(-5, 6)]
even_targets = [target + Vec2(4 * i, 0) for i in range(-5, 6)]
# get all virtual guards that block the assassin from shooting the virtual targets
odd_guards = [assin.midpoint(x) for x in odd_targets]
even_guards = [assin.midpoint(x) for x in even_targets]

# draw the reflection trajectory of the assassin to the virtual targets
for x in even_targets:
    _, guard = room.draw_trajectory(assin, x)
    even_guards.append(guard)
for x in odd_targets:
    _, guard = room.draw_trajectory(assin, x)
    odd_guards.append(guard)

marker_style = {"markersize": 7, "lw": 0.5, "markeredgecolor": "k"}
plt.plot(
    *zip(*even_targets), "o", color=palette[0], **marker_style, label="Even targets"
)
plt.plot(*zip(*odd_targets), "o", color=palette[1], **marker_style, label="Odd targets")
assin.plot("ro", **marker_style, label="Assassin")

marker_style["markersize"] = 5
marker_style["lw"] = 0.3
plt.plot(*zip(*even_guards), "o", color=palette[0], **marker_style, label="Even Guards")
plt.plot(*zip(*odd_guards), "o", color=palette[1], **marker_style, label="Odd Guards")

for mirror in room.mirrors:
    mirror.plot("k-", lw=1)

xmin, xmax = -9, 9
ymin, ymax = -0.5, 11
ax = plt.gca()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.axis("off")
ax.set_aspect("equal")
plt.tight_layout()
plt.legend()
plt.savefig("parallel.svg", dpi=300)
