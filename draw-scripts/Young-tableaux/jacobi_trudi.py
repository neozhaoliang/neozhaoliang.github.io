import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams.update({"text.usetex": True, "font.family": "Courier"})


class PlanePartition(object):
    def __init__(self, array, xmin, xmax, ymax):
        self.array = array
        self.xmin = xmin
        self.xmax = xmax
        self.ymax = ymax
        self.colors = "rgbc"
        self.paths = [self.gauss_path(row) for row in array]

    def gauss_path(self, path):
        result = [(0, 1)]
        for i, val in enumerate(path):
            result += [(i, val), (i + 1, val)]
        result.append((i + 1, self.ymax))
        return result

    def nonintersect_path_system(self):
        fig = plt.figure(figsize=(6, 4), dpi=300)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis([self.xmin - 1, self.xmax + 1, -0.5, self.ymax])
        ax.axis("off")

        frames = 121

        # dotted lines
        dots = []

        for i in range(0, self.ymax + 1):
            dots.extend(ax.plot([self.xmin, self.xmax], [i, i], "k--", lw=0.5))

        for i in range(self.xmin, self.xmax + 1):
            dots.extend(ax.plot([i, i], [0, self.ymax], "k--", lw=0.5))

        dots.extend(ax.plot([self.xmin, self.xmax], [0, 0], "k-"))

        # the paths
        lines = []
        for i in range(len(self.paths)):
            lines.extend(ax.plot([], [], "-", lw=2, color=self.colors[i]))

        for i, path in enumerate(self.array):
            n = len(path)
            ax.text(n - 0.2, -0.5, r"$\lambda_{}$".format(i + 1))

        for k in range(self.xmin, 1):
            ax.text(k - 0.2, -0.5, "{}".format(k))

        for k in range(1, self.ymax + 1):
            ax.text(self.xmin - 0.5, k - 0.1, "$x_{}$".format(k))

        texts = [
            [ax.text(x=0, y=0, s="{}".format(x), color=col) for x in arr]
            for arr, col in zip(self.array, self.colors)
        ]

        def init():
            for l in lines:
                l.set_data([], [])

            for arr in texts:
                for t in arr:
                    t.set_position((100, 100))
            return dots + lines + [t for arr in texts for t in arr]

        def animate(t):
            t = t / (frames - 1.0)
            t *= 5
            for i, path in enumerate(self.paths):
                xs, ys = zip(*path)
                if t < 2:
                    xx = xs
                    lines[i].set_data(xx, ys)
                elif t < 3:
                    xx = [z + (t - 2) * (-1 - i) for z in xs]
                    lines[i].set_data(xx, ys)
                else:
                    xx = [z + (-1 - i) for z in xs]
                    lines[i].set_data(xx, ys)

                arr = self.array[i]
                for ind, val in enumerate(arr):
                    te = texts[i][ind]
                    te.set_position((xx[ind * 2] + 0.4, val + 0.2))

            fig.canvas.draw()
            return lines

        anim = FuncAnimation(
            fig, animate, init_func=init, interval=20, frames=frames, blit=True
        )
        anim.save("nonintersecting_paths.gif", fps=30)


pp = PlanePartition([[1, 1, 1, 1, 2], [2, 2, 3, 3], [3, 4, 4], [4, 5]], -5, 5, 6)

pp.nonintersect_path_system()
