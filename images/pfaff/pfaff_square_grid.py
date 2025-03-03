# coding: utf-8
import matplotlib.pyplot as plt


def pfaff():
    fig = plt.figure(figsize=(3.5, 3.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-0.3, 7.3, -0.3, 7.3])

    ## 水平网格线
    for x in range(8):
        for y in range(7):
            ax.plot([y, y + 1], [x, x], "k-", lw=1)

    ## 竖直网格线
    for x in range(7):
        for y in range(8):
            ax.plot([y, y], [x, x + 1], "k-", lw=1)

    # 所有顶点画点
    for x in range(8):
        for y in range(8):
            ax.plot(y, x, "ko", markersize=6)

    ## 水平标记
    for x in range(8):
        for y in range(7):
            if x % 2 == 1:
                ax.plot(y + 0.5, x, "r>", markersize=6)
            else:
                ax.plot(y + 0.5, x, "g<", markersize=6)

    ## 竖直网格线
    for x in range(7):
        for y in range(8):
            ax.plot(y, x + 0.5, "bv", markersize=6)

    fig.savefig("pfaff.svg")


def onerow():
    fig = plt.figure(figsize=(4, 0.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-0.5, 7.5, -0.5, 0.5])
    for x in range(8):
        ax.plot(x, 0, "ko", markersize=6)
    for x in range(7):
        ax.plot([x, x + 1], [0, 0], "k-", lw=1)
    for x in range(7):
        ax.plot(x + 0.5, 0, "g<", markersize=6)
    fig.savefig("rowback.svg")


def rowback():
    fig = plt.figure(figsize=(4, 0.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-0.5, 7.5, -0.5, 0.5])
    for x in range(8):
        ax.plot(x, 0, "ko", markersize=6)
    for x in range(7):
        ax.plot([x, x + 1], [0, 0], "k-", lw=1)
    for x in range(7):
        ax.plot(x + 0.5, 0, "g<", markersize=6)
    fig.savefig("rowback.svg")


def row():
    fig = plt.figure(figsize=(4, 0.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-0.5, 7.5, -0.5, 0.5])
    for x in range(8):
        ax.plot(x, 0, "ko", markersize=6)
    for x in range(7):
        ax.plot([x, x + 1], [0, 0], "k-", lw=1)
    for x in range(7):
        ax.plot(x + 0.5, 0, "r>", markersize=6)
    fig.savefig("row.svg")


def col():
    fig = plt.figure(figsize=(4, 0.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.axis([-0.5, 7.5, -0.5, 0.5])
    for x in range(8):
        ax.plot(x, 0, "ko", markersize=6)
    for x in range(7):
        ax.plot([x, x + 1], [0, 0], "k-", lw=1)
    for x in range(7):
        ax.plot(x + 0.5, 0, "b>", markersize=6)
    fig.savefig("col.svg")


pfaff()
row()
rowback()
col()
