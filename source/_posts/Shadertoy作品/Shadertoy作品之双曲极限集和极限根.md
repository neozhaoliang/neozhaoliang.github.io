---
title: "Shadertoy 作品：Kleinian 群的极限集与无限 Coxeter 群的极限根"
date: 2020-06-01
tags:
  - Shadertoy
  - Coxeter groups
  - Limit roots
  - Hyperbolic geometry
categories:
  - [Shadertoy 作品]
url: "honeycombs-limit-set-and-limit-roots"
---

惊喜的发现我的博客又是半年多没更新了。比起折腾博客主题的次数来，我上传文章的频率未免太低了点。太容易的东西没意思不想写，有意思的东西写起来又太不容易。尤其还要白天上班晚上带娃，个人可以静下来独处的时间严重不足。我觉得钻研数学最好的地方是在象牙塔里，不满足这个条件的话就得要么单身，要么娶两个老婆。大老婆以为你在陪小老婆，小老婆以为你在陪大老婆，这样你就有时间做点数学了。

言归正传，下面是正文。


# 具有超理想顶点的双曲蜂巢


下图来自 Roice Nelson [^1]，我先不说话，大家欣赏下，看看能不能看懂它画的是什么？

<img style="margin:0px auto;display:block" src="/images/limitroots/373.png" width="500"/>

<!-- more -->

你可以看到图中出现了无数大小不一的 Poincaré 双曲圆盘，它们密密麻麻地铺在一个圆形区域内，但是还留下了一些空洞的部分没有被填充。这还是 Poincaré 双曲密铺吗？好像不太对哎？

其实这个图仍然描述的是一个双曲密铺，只不过这个密铺位于三维双曲空间中，空间的模型是 Poincaré 单位球
$$B_p = \{ (x,y,z)\in\mathbb{R}^3\, |\, x^2+y^2+z^2<1\},$$
密铺的类型是 Schläfli 记号 [^2] 下的双曲蜂巢 (3, 7, 3)，图中绘制的是在球面边界上发生的景象，此景象被球极投影到了 $z=0$ 平面上。

你可能要问了：球面在球极投影的结果不是应该铺满整个平面吗？怎么上图只有一个圆形区域呢？答案是，圆形区域的外部也是密铺的一部分，它对应的是基本胞腔与边界球面的无穷大交集 (Roice 的文章中叫做 *head*)，基本胞腔的所有面都染成了白色，所以虽然看起来好像投影后的区域只有一个圆形，实际不是的。

下图展示的是投影之前的景象：

<img style="margin:0px auto;display:block" src="/images/limitroots/373-ball.png" width=500 />

注意 (3, 7, 3) 这个密铺是非紧的 (non-compact)，其每个胞腔有一部分与无穷远边界相交。图中的每个空洞都来自一个对应的胞腔，特别地图中上半部分的最大的空洞属于基本胞腔。

下图从另一个角度展示了这一点：

<img style="margin:0px auto;display:block" src="/images/limitroots/373-catacomb.png"/>

这三张图展示的是同一个密铺，仅仅角度和场景不同。在第三张图中，每一个红色的小积木对应于双曲蜂巢中的一个胞腔，你可以把胞腔理解为双曲空间中的正多面体，但是这个多面体有无穷多个顶点和无穷多个面，图中只绘制了一个近似的形状。这些胞腔看起来有大有小，但是实际上它们在双曲空间中都是完全一样的，并且每个胞腔的体积是无穷大。特别地，观察者视角所在的空间也是一个胞腔的内部！场景中一共放置了五个胞腔，每个胞腔与理想平面的交是一个体积无限大的空洞，以及一组无限多个全等的正七边形。

图中每个双曲圆盘对应于密铺的一个顶点。这个顶点并不在上半空间中，甚至也不在理想平面上，实际上它位于双曲空间之外，是“虚拟的”，这样的顶点叫做**超理想顶点** (ultra-ideal)。由于 (3, 7, 3) 密铺的顶点配置 (vertex configure) 是 (7, 3)，所以任一顶点处有无穷多个胞腔与其相邻，这些胞腔构成一个 (7, 3) 类型的双曲密铺。圆盘中的每个正七边形是某个胞腔的“柱子”与理想平面的交，这个柱子在理想平面的另一侧汇聚到该顶点处。

以上内容在 Roice 的文章中都可以找到，我强烈建议读者去看看原文，里面有非常多精彩的图片。

不过等等，好像我们还漏掉了什么，注意到图中那些位于圆盘缝隙之间的点了吗？它们有什么含义吗？


# 双曲动力系统的极限集与无限 Coxeter 群的极限根


圆盘之间的缝隙是上面几张图中最有趣也是最神秘的部分，它有两种完全不同但是等价的描述：一方面它们是 (3, 7, 3) 的对称群 $W$ 作为 Kleinian 群作用在三维双曲空间 $\mathbb{H}_3$ 上的极限集 (limit set) $\Lambda(W)$，另一方面它们也是 $W$ 作为无限 Coxeter 群的极限根 (limit roots) $E(\Phi)$ (具体解释见后)。

$W$ 作为 Kleinian 群的极限集 $\Lambda(W)$ 有若干种不同的等价描述方式。

设 $x_0\in\mathbb{H}_3$ 是三维双曲空间中一点，$W(x_0)=\{w(x_0)\,|\, w\in W\}$ 为 $x_0$ 在 $W$ 作用下的轨道，则集合 $W(x_0)$ 的聚点都位于无穷远边界球面 $S^3$ 上。我们把 $W(x_0)$ 的所有聚点组成的集合叫做 $W$ 的*极限点*，把极限点的闭包叫做 $W$ 的*极限集*，记作 $\Lambda(W)$。可以证明 $\Lambda(W)$ 的定义不依赖于 $x_0$ 的选取，并且 $\Lambda(W)$ 是理想球面上在 $W$ 作用下不变的最小非空闭集。

而 $W$ 作为无限 Coxeter 群，其极限根的概念则是最近几年才提出。完整的描述极限根的概念需要颇为一番周折，我这里简单尝试介绍一下，恐怕不见得说得十分明白，读者最好还是参考论文如 [^3] [^4] 等。
 
首先我们知道 (3, 7, 3) 这个密铺的对称群 $W$ 是由 Coxeter 矩阵
$$\begin{pmatrix}1&3&2&2\\3&1&7&2\\2&7&1&3\\2&2&3&1\end{pmatrix}$$
确定的 Coxeter 群 $(W,\Delta)$，这里的 $\Delta$ 就是标准几何表示下的单根集。$W$ 的标准几何表示对应的双线性函数 $B(\cdot,\cdot)$ 的符号是 (3, 1)，因而等价于 $\mathbb{R}^4$ 上的 Minkowski 内积，$W$ 是此内积下的离散正交变换群。记 $q(v)=B(v,v)$ 是由 $B$ 决定的二次型，则在一组基 $\{e_i\}$ 下 $q$ 形如
$$q(v) = x_1^2+x_2^2+x_3^2-x_4^2,\quad v=\sum_{i=1}^4 x_ie_i.$$

分别记 $Q=\{v\, |\, q(v)=0\}$，$Q^-=\{v\, |\, q(v)<0\}$，则用超平面 $V_1=\{x_4=1\}$ 去截 $Q^-$ 得到的单位球
$$\{(x_1,x_2,x_3,x_4)\, |\, x_1^2+x_2^2+x_3^2<1,\ x_4=1\}$$
就是我们所熟悉的双曲几何的 Klein-Beltrami 模型。极限根的故事就发生在这个仿射单位球的边界 $S^3$ 上。

设 $\Delta = \{\alpha,\beta,\gamma,\delta\}$ 是 $W$ 的单根集，$\Phi$ 是 $(W,\Delta)$ 的根系，$\Phi^+$ 是其中的正根。

由于 $W$ 是无限群，$\Phi$ 也是无限的，而且 $\Phi$ 在 $\mathbb{R}^4$ 中是离散的，并不会有聚点。但是如果我们把 $\Phi^+$ 投影到超平面 $V_1$ 上去，即对每个正根 $\rho$，计算射线 $\mathbb{R}_{>0}\rho$ 与 $V_1$ 的交点得到点 $\hat{\rho}$ [^5]，并规定 $\pm\rho$ 在 $V_1$ 上的投影点为 $\hat{\rho}$，则奇妙的事情发生了，这些投影后的根 $\hat{\Phi} = \{\hat{\rho}, \rho\in\Phi^+\}$ 是有聚点的，记 $E(\Phi)$ 是 $\hat{\Phi}$ 的所有聚点组成的集合，$E(\Phi)$ 即为 $W$ 的极限根。则我们有如下定理：

{% blockquote %}
**定理 1**: 所有的极限根都落在迷向锥上，即 $E(\Phi)\subseteq Q\cap V_1$。
{% endblockquote %}

注意在三维双曲空间的情形，$Q\cap V_1$ 就是 Klein-Beltrami 模型下的理想球面 (这个球面位于仿射平面 $x_4=1$ 上)，所以极限根都落在球面 $S^3$ 上。

进一步 Hohlweg 等人证明了在 $W$ 是 Lorentzian 群的情形，极限根 $E(\Phi)$ 和 $\Lambda(W)$ 是相等的：

{% blockquote %}
**定理 2**: 若 $W$ 是 Lorentzian 群，即其几何表示对应的双线性型的符号为 $(n, 1)$，则 $E(\Phi) = \Lambda(W)$。
{% endblockquote %}

所以在 (3, 7, 3) 的情形，它既是一个 Kleinian 群，又是一个符号为 (3, 1) 的无限 Coxeter 群，所以图中的缝隙既可以理解为双曲动力系统的极限集，也可以理解为无限 Coxeter 群的根系在投影到某个超平面后的极限集。


# 前面的插图是怎么画出来的?


你可能想知道 Roice 是怎样画出这些漂亮的图形的，其实原理并不复杂。像 (3, 7, 3) 这种双曲反射群一律可以由四个关于球面的反演变换生成，只要把图像的每个像素对应到空间中的一点，然后将该点关于这四个球面反复作反演变换，如果经过一定次数的反演后该点落入基本区域，则根据反射的次数和最终得到的点的位置给最初的像素染色；否则就将该像素标记为极限集。

Roice 的代码[在这里](https://github.com/roice3/Honeycombs)，我正在考虑未来有时间用 C++ 把这个项目的精彩部分用 Coxeter 群的有限状态机的方法实现一遍。


# 彩蛋


好了，本文最精彩的部分来了：我写了一个 Shadertoy 小 demo 来演示极限集的形状，请欣赏：

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/WdGBz3?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

图中展示的是 (3, 3, 7) 的极限集。你可以使用鼠标旋转图案，或者点击窗口左上角的标题访问 Shadertoy 网站查看源码，并修改 PQR 的值来获得不同群对应的图案。(5, 4, 4) 看起来也是不错的：

<img style="margin:0px auto;display:block" width=600 src="/images/limitroots/544.png"/>

通过调整颜色和染色函数，可以获得更多不同的图案：

<img style="margin:0px auto;display:block" width=600 src="/images/limitroots/4-inf-4.png"/>


[^1]: [Visualizing Hyperbolic Honeycombs](https://arxiv.org/abs/1511.02851), Roice Nelson, Henry Segerman.
[^2]: [Schläfli symbol on wikipedia](https://en.wikipedia.org/wiki/Schl%C3%A4fli_symbol).
[^3]: [Asymptotical behaviour of roots of infinite Coxeter groups](https://arxiv.org/abs/1112.5415).
[^4]: [On the Limit Set of Root Systems of Coxeter Groups acting on Lorentzian spaces](https://arxiv.org/pdf/1305.0052.pdf).

[^5]: 这里需要证明每个正根 $\rho$ 所在的方向确实与 $V_1$ 有交点，见脚注 4 中的文献。
