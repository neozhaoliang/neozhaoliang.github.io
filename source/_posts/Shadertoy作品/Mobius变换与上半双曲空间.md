---
title: "Möbius 变换的分类与上半双曲空间的等距"
date: 2018-05-09
tags:
  - GLSL
  - Shader
  - Visual Complex Analysis
  - Hyperbolic space
  - Möbius transformation
  - Riemann sphere
  - Dupin cyclide
categories: [Shadertoy 作品]
url: "mobius-cn"
glsl: true
---

本文的想法源自 Roice Nelson 的 [shadertoy 项目](https://www.shadertoy.com/view/MstcWr)，我觉得他的创意很棒，就是效果有点糙，于是动手改进了一番，结果见[这里](https://www.shadertoy.com/view/4scfR2)。不懂的人看这个动画可能只是觉得好玩，其实它背后的数学并不简单。

这篇文章将用动画的形式从三个角度演示 Möbius 变换，这三个角度是密切相关的：

1. Möbius 变换作为扩充复平面 $\hat{\mathbb{C}}$ 到自身的全纯函数。
2. Möbius 变换作为 Riemann 球面 $S^2$ 到自身的全纯函数。
2. Möbius 变换作为上半双曲空间中的等距变换。

本文只做演示，并不介绍详细的数学证明。读者可以参考下面的两份资料：

> 1. [维基百科页面](https://en.wikipedia.org/wiki/M%C3%B6bius_transformation).
> 2. Visual complex analysis, Tristan Needham.

借助本文的动画你可以很容易地理解这两份资料中的内容。

文中的动画全部使用 shader 程序制作，需要你的浏览器支持 Webgl2.0，代码在 [github](https://github.com/neozhaoliang/pywonderland/tree/master/src/mobius) 上。

<!-- more -->

# 预备知识之正交圆族

设 $z_1,z_2$ 是复平面上的两个不同点，我们考虑两个不同的圆族 $\mathcal{C}_1$ 和 $\mathcal{C}_2$：

1. $\mathcal{C}_1$ 由所有同时过 $z_1$ 和 $z_2$ 的圆组成 (包含过 $z_1,z_2$ 的直线)。
2. $\mathcal{C}_2$ 由所有使得 $z_1$ 和 $z_2$ 关于 $C$ 互为反演点的圆 $C$ 组成 (包含线段 $[z_1,z_2]$ 的垂直平分线)。

则圆族 $\mathcal{C}_1$ 中的任何圆 $C_1$ 与 $\mathcal{C}_2$ 中的任何圆 $C_2$ 正交 (交点处的切线互相垂直)。

我们将考察当 $z_1,z_2$ 是一个 Möbius 变换 $M$ 的两个不动点时 $M$ 作用在 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 上的效果。


# Möbius 变换的共轭分类

一个 Möbius 变换 $M$ 是一个分式线性变换，它将扩充复平面 $\hat{\mathbb{C}}$ 一对一地映射为自身：
$$M(z) = \frac{az+b}{cz+d},\quad a,b,c,d\in\mathbb{C},ad-bc\ne0, z\in \hat{\mathbb{C}}.$$
所有的 Möbius 变换构成一个群 ${\rm PSL}_2(\mathbb{C})$。

可以证明在共轭的意义下，任何非恒等元的 Möbius 变换都属于下面 4 种基本类型之一：

1. $M$ 称作是抛物型的 (parabolic)，如果它共轭于一个纯平移：$z\to z+a$，其中 $a\ne0\in\mathbb{C}$，这时 $M$ 在 $\hat{\mathbb{C}}$ 上仅有一个不动点。
2. $M$ 称作是椭圆型的 (elliptic)，如果它共轭于一个纯旋转：$z\to e^{i\theta}z$，其中 $\theta\in\mathbb{R}$，这时 $M$ 在 $\hat{\mathbb{C}}$ 上有两个不动点。
3. $M$ 称作是双曲型的 (hyperbolic)，如果它共轭于一个纯缩放：$z\to\lambda z$，其中 $\lambda>0$ 是实数，这时 $M$ 在 $\hat{\mathbb{C}}$ 上有两个不动点。
4. $M$ 称作是斜航型的 (loxodromic)，如果它共轭于一个双曲缩放和一个椭圆旋转的复合：$z\to cz$，其中 $c\ne0\in\mathbb{C}$ 且 $c\notin\mathbb{R}$，这时 $M$ 在 $\hat{\mathbb{C}}$ 上有两个不动点。

{% blockquote %}
在研究每种类型的变换时，我们都先研究其共轭类中最简单的类型 $z\to z+a$, $z\to e^{i\theta}z$, $z\to\lambda z$, $z\to cz$ (它们都以无穷远点为一个不动点，除去抛物型之外的另一个不动点是原点)，这时的 Möbius 变换具有简单的表现形式，其在两个圆族上的作用也很容易分析，然后再推广到一般的情形。
{% endblockquote %}

## 1. 抛物型

我们先考察最简单的抛物型变换 $z\to z+a$。

这时唯一的不动点是无穷远点，圆族 $\mathcal{C}_1$ 由所有平行于 $x$ 轴的直线组成 (直线是半径无穷大的圆)，圆族 $\mathcal{C}_2$ 由所有垂直于 $x$ 轴的直线组成，圆族 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 是正交的，$M$ 保持 $\mathcal{C}_1$ 中的每条直线不变，把 $\mathcal{C}_2$ 中的每条直线变成同族中的另一条直线：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/parabolic-plane-inf.frag" width="480" height="320"></canvas>

你可以看到所有点都向着不动点无穷远点的方向“前进”。

对一般的抛物型变换 $M$ 且 $M$ 的唯一不动点 $z_0$ 是有限点的情形，结论仍然类似：它保持圆族 $\mathcal{C}_1$ 中的每个圆不变，这里 $\mathcal{C}_1$ 是一组在 $z_0$ 处相切的圆族，所有圆共用同一条切线。$M$ 同时把圆族 $\mathcal{C}_2$ 中的每个圆变为同族的另一个圆，这里 $\mathcal{C}_2$ 也是一组在 $z_0$ 处相切的圆族，所有圆也共用同一条切线，但是这条切线的方向与 $\mathcal{C}_1$ 的切线方向垂直：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/parabolic-plane.frag" width="480" height="320"></canvas>

由动画可见所有点都向着不动点 $z_0$ 的位置前进。事实上可以证明对任何 $z\in\mathbb{C}$ 都有 $\lim\limits_{n\to\infty}M^n(z)=z_0$，即任何点在 $M$ 反复作用下的轨迹都朝着 $z_0$ 的位置移动。

## 2. 椭圆型

我们先考察最简单的椭圆型变换 $z\to e^{i\theta}z$。

这时两个不动点是原点和无穷远点。注意它保持以原点为中心的同心圆族 $\mathcal{C}_1$ 不变，把原点和无穷远点连线组成的径向直线族 $\mathcal{C}_2$ 中的每一条直线变成同族中另一条直线，$\mathcal{C}_1$ 和 $\mathcal{C}_2$ 是正交的：


<canvas class="glslCanvas" data-fragment-url="/images/mobius/elliptic-plane-inf.frag" width="480" height="320"></canvas>

对一般的椭圆变换 $M$ 且 $M$ 的两个不动点 $z_1$ 和 $z_2$ 都有限的情形，仍然存在两个互相正交的圆族 $\mathcal{C}_1$ 和 $\mathcal{C}_2$，$M$ 保持 $\mathcal{C}_1$ 中的每个圆不变，把 $\mathcal{C}_2$ 中的每个圆变为同族中的另一个圆：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/elliptic-plane.frag" width="480" height="320"></canvas>

这里 $\mathcal{C}_1$ 由所有使得 $z_1$ 和 $z_2$ 关于 $K$ 互为反演点的圆 $K$ 组成，因此 $\mathcal{C}_1$ 中的圆的圆心都落在 $z_1$ 和 $z_2$ 两点间的连线上，但是位于线段 $[z_1,z_2]$ 的外部；圆族 $\mathcal{C}_2$ 由所有过 $z_1$ 和 $z_2$ 的圆组成，因此 $\mathcal{C}_2$ 中的圆的圆心都落在线段 $[z_1,z_2]$ 的垂直平分线上。

## 3. 双曲型

与椭圆变换 $z\to e^{i\theta}z$ 的情形类似，$z\to\lambda z$ 也以原点和无穷远点为不动点，但是圆族 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 的角色发生了互换：它保持由原点与无穷远点连线组成的直线族 $\mathcal{C}_2$ 不变，把由以原点为中心的同心圆族 $\mathcal{C}_1$ 中的每个圆变为同族中的另一个圆：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/hyperbolic-plane-inf.frag" width="480" height="320"></canvas>

对一般的双曲变换 $M$ 且 $M$ 的两个不动点 $z_1$ 和 $z_2$ 都有限的情形，仍然与椭圆变换的情形类似，圆族 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 的角色发生了互换：所有过 $z_1$ 和 $z_2$ 的圆组成的圆族 $\mathcal{C}_2$ 保持不变；所有反演圆组成的圆族 $\mathcal{C}_1$ 被变为同族中的另一个圆：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/hyperbolic-plane.frag" width="480" height="320"></canvas>

这时在 $M$ 的作用下 $z_1$ 和 $z_2$ 一个是“源点”，另一个是“汇点”，轨迹从源点源源不竭地发出，汇聚到汇点中。

## 4. 斜航型

仍然先看 $z\to cz$ 的情形。

这时不动点是原点和无穷远点，显然 $M$ 把圆族 $\mathcal{C}_1$ 中的每个圆变为同族中的另一个圆，同样地也把圆族 $\mathcal{C}_2$ 中的每个圆变为同族中的另一个圆：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-plane-inf.frag" width="480" height="320"></canvas>

这时点 $z$ 在 $M$ 的反复作用下的轨迹是一条曲线，其形如 $\gamma(t)=c^tz$，这是一条对数螺线，其与 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 的夹角都是常数。

这个结论对一般的斜航型变换也成立：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-plane.frag" width="480" height="320"></canvas>

由于斜航型变换包含双曲变换作为组成成分，因此看起来它也有一个源点和一个汇点。这时任意点 $z$ 在 $M$ 的反复作用下的轨迹是一条双螺线 (double spiral)，其与 $\mathcal{C}_1$ 和 $\mathcal{C}_2$ 的夹角仍然都是常数 (Möbius 变换是保角的)。

判断 Möbius 变换 $M$ 具体属于哪一类可以根据其迹的平方 $\mu=(a+d)^2$ 来判断 (这是一个共轭不变量)：

1. $M$ 是抛物型的当且仅当 $\mu=4$。
2. $M$ 是椭圆型的当且仅当 $0\leq\mu<4$。
3. $M$ 是双曲型的当且仅当 $\mu>4$。
4. $M$ 是斜航型的当且仅当 $\mu<0$ 或者 $\mu\notin\mathbb{R}$。


## 斜航 (loxodromic) 是什么意思？

斜航这个词听起来好像和船的航行有关，怎么就用来给 Möbius 变换分类了呢？这里面肯定有故事，值得扒一扒。

斜航线 (loxodrome) 指的是地球上的一条航行路径，其在每个点处的切线与过该点的经线的夹角为定值。比如说，如果船始终朝着东北方向 30 度行驶，走过的轨迹就是一条斜航线。Loxodrome 最初是一个希腊词，loxos 的意思是 oblique，即倾斜的，dromos 意为 bearing，方位的意思，后来拉丁化以后成为现在的样子。葡萄牙数学家 Pedro Nunes (1492-1577) 第一个认识到斜航线并非两点之间最短路径，而且它无限接近但永不可能到达极点。

在大航海的时代，没有卫星导航，只能靠罗盘或者星座来标识船的航向，而星座的方法在遇到恶劣天气的时候又不能使用，只有罗盘是最可靠的方法。理论上地球表面两点之间的最短路径是过球心的大圆，但罗盘只能定出经线的方向 (原理是地球的磁极和南北极近似重合)，这二者的夹角不是固定的，要保持沿着大圆的弧走就必须不停调整船的航向，但现实中的船不可能一直有人守在船舵处调整方向，一般是事先定好航向以后接下来的若干天都沿着这个方向走，所以在一定路程内船实际上走的是斜航线。

荷兰地图学家墨卡托 (Mercator) 据此于 1569 年提出了墨卡托地图，将地球投影至墨卡托地图是一个保角变换，即曲线的夹角保持不变。所以要从地球上的 $A$ 点航向到 $B$ 点，只要找到它们在墨卡托地图上的对应点 $A',B'$，算出地图上的直线 $A'B'$ 与经线的夹角 $\theta$，则航行时只要让罗盘与经线一直保持角度为 $\theta$ 就可以从 $A$ 航行到 $B$ 了。这个路径虽不是最短，但是好在不容易迷失航向。

那这和 Möbius 变换有什么关系呢？

# Möbius 变换在 Riemann 球面上的作用

由于 Möbius 变换都是扩充复平面 $\hat{\mathbb{C}}$ 到 $\hat{\mathbb{C}}$ 的自同构，而 $\hat{\mathbb{C}}$ 在球极投影下等同于 Riemann 球面 $S^2$，所以 Möbius 变换也都是 Riemann 球面的自同构。我们来看看 Möbius 变换作用在 Riemann 球面上是什么样子的。

这是一个作用在 Riemann 球上的斜航型变换：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-sphere.frag" width="480" height="320"></canvas>

我来解释一下这个动画的含义：从动画可见 Riemann 球面上有一对源点和汇点，它们在球极投影下对应于 $M$ 在扩充复平面上的两个不动点。这对源点和汇点可以理解为球面的“北极”和“南极” (当扩充复平面上的两个不动点分别是原点和无穷远时，这两个极点就是通常意义下的北极和南极)，这时球面上的“经线”是所有过两个极点的大圆，在球极投影下它们对应于同时过两个不动点的圆族 $\mathcal{C}_1$；球面上的纬线是所有与经线正交的圆，在球极投影下它们对应于反演圆族 $\mathcal{C}_2$，球面上每个点的轨迹是对数螺线轨迹在逆球极投影下在球面上的对应曲线，这条曲线与经线纬线的夹角都是常数 (因为球极投影是保角的)，从而是一条斜航线！

{% blockquote %}
**练习**：解释下面这个动画的含义：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/parabolic-sphere.frag" width="480" height="320"></canvas>

提示：这是一个抛物型变换。
{% endblockquote %}


# Möbius 变换作为上半双曲空间的等距

上半双曲空间 $H_3$ 的定义为
$$H_3 = \{(x,y,z)\in\mathbb{R}^3\ |\ z>0\}.$$
这个空间中的度量是双曲度量，其定义非常类似双曲几何的上半平面模型：对 $H_3$ 中的两点 $A,B$，作平面 $P$ 过 $A,B$ 且垂直于 $xy$ 平面，则 $A,B$ 在 $P$ 作为上半平面模型中的双曲距离即为它们在 $H_3$ 中的双曲距离。这个定义与 $P$ 的选取是无关的。

换言之，这个双曲空间中的测地线都是与 $xy$ 平面正交的圆的弧。

注意 $xy$ 平面不属于 $H_3$，它是 $H_3$ 的“无穷远边界”：$H_3$ 中任何一点到 $xy$ 平面的距离是无穷大！

一个教材中不太常讲到的事实是：**任何 Möbius 变换都可以唯一地扩展为 $H_3$ 的一个等距变换 $\overline{M}$**。这个扩展用四元数来描述的话很简单：设
$$M: z\to\frac{az+b}{cz+d}$$
是任一 Möbius 变换，$p=(x,y,z)\in\mathbb{H}^3$，则令 $q=xi+yj+zk$ 为纯虚四元数，定义
$$\overline{M}(p) = \frac{aq+b}{cq+d}.$$
这里的运算都是在四元数体中进行。

我们还能像上面那样用动画演示 Möbius 变换 $\overline{M}$ 在 $H_3$ 上的作用吗？可以！比如下图是一个形如 $z\to cz$ 的斜航型变换扩展到 $H_3$ 后作用在一个**圆柱**体上的效果：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-cone.frag" width="480" height="320"></canvas>

你可能要问了：这明明是个圆锥体，你怎么说它是圆柱体呢？是不是笔误了啊？

其实是因为我们现在是在双曲空间里看待它，在双曲度量下，锥面上所有点到旋转轴的距离都是一样的，所以虽然在欧式空间 $\mathbb{R}^3$ 中看它是一个锥体，但是在 $H_3$ 中它其实是圆柱体。

你可以看到这时 $\overline{M}$ 有两个不动点，都位于无穷远处，这样的点叫做“理想点”。两个不动点之间的连线构成圆柱的轴。两个不动点一个是源点，一个是汇点，空间中的点在变换的作用下“远离”源点，“趋向”汇点。

对于一般的斜航型变换 $M$，且其两个不动点都是扩充复平面上的有限点时，$M$ 在 $H_3$ 上的扩展 $\overline{M}$ 仍然保持一个 $H_3$ 中的圆柱体不变：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-cyclide.frag" width="480" height="320"></canvas>

这个曲面在欧式空间中叫做 [Dupin cyclide](https://www.maths.ox.ac.uk/about-us/departmental-art/dupin-cyclides)，它的两个端点恰好是 $M$ 的两个不动点。但在双曲空间中它其实是一个圆柱体，由于其两端落在无穷远平面上，因此也是无限长的。圆柱体的轴是连接两个端点的测地线。如果是 $M$ 是椭圆型的话，那么 $\overline{M}$ 将该圆柱绕着轴旋转：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/elliptic-cyclide.frag" width="480" height="320"></canvas>


# 这些动画是怎么生成的？

动画使用的是 glsl 语言和 raymarching 的技术。我在 Roice 的代码基础上作了许多优化，但肯定还可以更精炼。限于我写 shader 的能力不足，做出更美轮美奂的效果就不指望了 ...

严格讲，这些动画其实还是尝试在欧式空间中去观察双曲空间中的对象，因为 raymarching 技术假定的是光走直线，但在双曲空间中光一般不走直线，所以我们这里看到的效果与真实的生活在双曲空间中的“外星人”所看到的还是有差别的。


# 更多的故事

说到动画演示 Möbius 变换，很难不提到 [Möbius Transformations Revealed](http://www-users.math.umn.edu/~arnold//moebius/) 这部视频，这个视频揭示的是 Möbius 变换的另一种刻画方式：它们可以由 Riemann 球面 $S^2$ 在 $\mathbb{R}^3$ 中的刚体运动得到！即你可以把扩充复平面通过逆球极投影映射到 $S^2$ 上，然后将 $S^2$ 在 $\mathbb{R}^3$ 中作刚体运动 (旋转加平移)，但要保持北极点位于上半空间内，然后再球极投影回扩充复平面，这个复合变换就是一个  Möbius 变换，并且所有的 Möbius 变换都可以用此方式得到。


# 演示斜航线与双螺线的另一个动画

下面是项目里面的另一个 shader 动画，可以更清楚地看到 Riemann 球面上的斜航线在球极投影下与  Möbius 变换的不动点之间的双螺线之间的对应关系：

<canvas class="glslCanvas" data-fragment-url="/images/mobius/loxodromic-shadow.frag" data-textures="/images/mobius/wood.jpg" width="480" height="320"></canvas>

我很喜欢这个动画的阴影效果。
