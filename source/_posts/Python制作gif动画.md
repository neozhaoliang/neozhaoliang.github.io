---
title: "碉堡的小程序：用 Python 制作演示各种算法的 GIF 动画"
date: 2017-10-02
categories: [pywonderland 项目]
tags:
  - Python
  - 算法
  - PyWonderland
  - 动画
  - 迷宫
  - Hilbert 曲线
  - Conway 生命游戏
  - Langton 蚂蚁
url: "gifmaze-cn"
---

本文要介绍的是我写的一个有趣的 Python 小程序，一个脱离了低级趣味的程序，一个有益于广大人民了解算法的程序。代码在 [Github](https://github.com/neozhaoliang/pywonderland/tree/master/src/gifmaze) 上。

这个程序可以用来制作各种各样的算法动画，包含但不限于：

<!-- more -->

+ Wilson 均匀生成树算法：

    <img style="margin:0px auto;display:block" src="/images/gifmaze/wilson-bfs.gif" />
    
+ Prim 算法：

    <img style="margin:0px auto;display:block" src="/images/gifmaze/prim.gif" />
    
+ Kruskal 算法：

    <img style="margin:0px auto;display:block" src="/images/gifmaze/kruskal.gif" />
    
+ Langton 蚂蚁：
   
    <img style="margin:0px auto;display:block" src="/images/gifmaze/langton-ant.gif" />

+ Hilbert 曲线：
   
    <img style="margin:0px auto;display:block" src="/images/gifmaze/hilbert.gif" />
    
+ Conway 的生命游戏 (gosper glider gun)：
   
    <img style="margin:0px auto;display:block" src="/images/gifmaze/gosperglidergun.gif" />

以上这些动画有一个共同特点：它们都位于二维的网格图上，这也是这个程序的一个限制。

这个程序有如下特点：

1. 所有代码全部由纯 Python 写成，没有用到任何第三方库或者外部软件，也不包含任何 `draw`, `fill` 之类的函数调用，仅使用了内置的 `struct`, `random` 模块和一些内置函数。后来的版本中为了显示进度条引入了 `tqdm`；为了把整个动画嵌入一张背景图片引入了 `pillow`，这些都属于特效，本质不需要。

2. 实现了一个小型但高效的 gif 编码器，**通过直接将动画过程编码为字节流**，可以在数秒之内生成高度优化的动态图。比如前面那张 Langton ant 的动图，它包含 2300 帧，但是大小只有 158KB，而且只需要一秒多一点就可以生成。这是这个程序最让人意外的一点：Python 生成图像的慢是出了名的，它居然能在几秒内生成一张包含几千帧的 gif 动图？这是个大新闻啊！

3. 严格遵循 GIF89a 协议，生成的图片在 chrome, firefox, IE 和 Eog 中都可以正常显示。

程序运行的相当快，生成一副 600x400 像素，演示 Wilson 算法的动图只要数秒，得到的文件包含 1000~3000 帧，但大小不超过 1M 左右。没想到吧？

其实程序最初的版本比现在要慢 5x~10x 倍左右，而且绝大部分功能都放在一个庞大的类里面 (20+个方法)，现在的代码是经过不计其数次的修改，反复绞尽脑汁优化以后才得到的。

这个程序是怎么来的呢？许多年前我在网上闲逛的时候，偶然发现了一个网站：[https://bl.ocks.org/mbostock](https://bl.ocks.org/mbostock)，当时我对上面展示的各种丰富炫酷的动态效果惊羡不已，尤其是其中对 [Wilson 算法的演示](https://bl.ocks.org/mbostock/11357811)，让我对此算法有了更直观和深入的理解。我立刻萌发了用 Python 制作一个 gif 版的动画演示的想法，但是思考了许久也不知道从何入手。这里困难的地方在于 Wilson 算法是一个随机算法，其运行时间是不确定的，一个动画里面可能包含数千帧，如果采用把每一帧保存为图像再合并到一起的话，最终得到的文件会非常庞大，而且这种纯暴力的做法逼格太 low，我实在不屑于采用。限于能力不足，这个想法只好被暂时压在心底，但是一直念念不忘。过了几年后，在一个偶然的机会我接触到了 gif 图像的编码协议，豁然开朗：为什么不直接把动画过程编码为字节流呢？通过精确定位每一帧的位置，控制 LZW 压缩过程的编码长度，文件过大的问题是可以解决的！前后捣鼓了半个月，反复研究协议细节，debug 了无数次后，这才作出了上面的效果。后来慢慢又加上了其它迷宫算法和元胞自动机的演示。

理解代码的关键有这么几个：

1. 由于 gif 图像的每一帧占据的是整个图像窗口的一个矩形子区域，在一个包含很多帧的动图中，相邻的两帧之间的变动可能很小，没有必要每次都将整个图像所占区域全部编码。我们只需要记录帧和帧之间的变化情况，得出每一帧所占的矩形子区域，每次编码时只针对这个子区域编码即可，这样就大大减小了生成的文件体积。

2. 采用变长的 LZW 压缩算法。GIF89a 协议允许每个打包的数据块指明其所使用的最小码字的长度 (仅适用于本块数据)，如果你确定这一帧图像用到的颜色很少，比如只有 4 种颜色，那么 2 个比特就足以表示这 4 种颜色，从而最小编码长度可以设置为 2。这样根据具体情况采用不同的编码长度能有效减少文件体积。

3. 因为要频繁的进行字节流的操作，所以每次将编码后的数据先写入一个 `BytesIO` 对象中，放在内存里，最后一次性输出到硬盘。由于优化的好，动图大小普遍不超过 3M，所以放在内存里不是问题。

代码的组织结构是简单的三层论：顶层是抽象的 `Maze` 类，其本质就是一个 2D 网格图，用来跑各种图算法，它不关心动图的任何细节。底层是 `GIFSurface` 类，负责维护 gif 图片的全局信息，比如图片宽高，循环次数，背景颜色，全局调色板等。中间层是 `Animation` 类，用来控制帧的信息，在算法运行过程中它按照一定的频率将 `Maze` 染色并编码写入 `GIFSurface`。

目前程序的核心代码加起来大约在 1000 行左右，但是如果牺牲一些可读性和功能的话，是可以压缩到 500 行以内的。我曾经把这个项目投稿到 github 上的 [500lines](https://github.com/aosabook/500lines) 上，可惜未能入选。这个项目涉及的知识确实有一些门槛，读者短时间内理解起来可能有困难，但是我始终觉得它的优雅、奇妙并不逊色于那些大神们的作品。
