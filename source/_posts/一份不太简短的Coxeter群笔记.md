---
title: "Coxeter 群基础知识提要"
categories: [代数]
date: 2013-04-02
tags:
  - Cartan matrix
  - Coxeter matrix
  - Coxeter groups
  - Gallery
  - Reduced word
  - Reflection
  - Standard geometric realization
  - Tits cone
  - Simple root
  - Root system
url: "introduction-to-coxeter-groups"
---

本文整理自我读研时的笔记，目的是介绍 Coxeter 群的一些基本知识。根据我个人的体会，理解 Coxeter 群一定要联系几何直观，弄清楚每一个结论它对应的几何解释是什么。我从 [Casselman](https://www.math.ubc.ca/~cass) 的讲义中受益很多，许多插图也是受到了他的启发所作，特别致谢。


<!-- more -->

# 抽象 Coxeter 群


设 $S$ 是一个集合，一个基于 $S$ 的 Coxeter 矩阵 $M=(m_{s,t})_{s,t\in S}$ 是一个对称矩阵，其对角线上都是 1，非对角线元素取值范围为 $\{2,3,\ldots,\infty\}$。

$S$ 的基数 $|S|$ 叫做 $M$ 的秩 (rank)，在本文中我们只考虑 $M$ 的秩为有限的情形，即 $|S|<\infty$ 的情形。

Coxeter 矩阵也可以用直观的方式展示出来，即其 Coxeter 图：Coxeter 图是一个带标记的无向图，其顶点集为 $S$，两个顶点 $s\ne t$ 之间有边相连当且仅当 $m_{s,t}\geq3$，且这条边被标记为 $m_{s,t}$，只不过在 $m_{s,t}=3$ 时我们通常省略其标记。

例如 Coxeter 矩阵
$$\begin{bmatrix}1&3&3\\3&1&4\\3&4&1\end{bmatrix}$$
对应的 Coxeter 图为

<img style="margin:0px auto;display:block" width=150 src="/images/coxeter/diagram334.svg"/>

对给定的 Coxeter 矩阵 $M$，$M$ 确定了一个有限表现群 $W$，$W$ 叫做抽象 Coxeter 群，其生成元是集合 $S$，生成关系由所有的 $(st)^{m_{s,t}}=1$ 组成：
$$W = \langle s\in S\ |\ (st)^{m_{s,t}}=1\ {\rm if}\ m_{s,t}<\infty\rangle.$$

注意 $(st)^\infty=1$ 可以理解为 $s$ 和 $t$ 之间没有约束关系，所以它们不出现在群表现中。

总之 $S$ 作为 $W$ 的生成元满足如下的生成关系：

1. 对任何 $s\in S$ 有 $s^2=1$。
2. 对任何 $s\ne t, m_{s,t}<\infty$ 有辫关系 $\overbrace{sts\cdots}^{m_{s,t}}=\overbrace{tst\cdots}^{m_{s,t}}$ 成立。

我们把 $(W, S)$ 叫做一个 Coxeter 系。

对 $W$ 中的任一元素 $w$，它可能有许多种不同的方式表示为 $S$ 中生成元的乘积。在 $w$ 的所有表示中，长度最短的表示叫做 $w$ 的既约表示：即若 $w=s_{i_1}s_{i_2}\cdots s_{i_k}$ 是一个将 $w$ 表示为 $k$ 个生成元的乘积，且 $w$ 不存在任何长度小于 $k$ 的这样的表示，就称 $s_{i_1}s_{i_2}\cdots s_{i_k}$ 是 $w$ 的一个既约表示。$w$ 的既约表示可能不唯一，但它们必然都具有相同的长度。$w$ 的长度 $l(w)$ 就定义为 $w$ 的任意一个既约表示的长度。

$l(w)$ 具有如下的性质：

1. $l(xy)\leq l(x) + l(y)$。
2. $l(w) = l(w^{-1})$。
3. $l(w)=0$ 当且仅当 $w$ 是恒等元。
4. $l(ws)$ = $l(w)\pm 1$，其中 $w\in W, s\in S$。

前三点都是显然的，只有 4 需要论证。显然 $|l(ws)-l(w)|\leq 1$，所以只要说明 $l(ws)$ 和 $l(s)$ 不相等即可。

设 $F$ 是由集合 $S$ 生成的自由群，定义群同态 ${\rm sgn}: F\to\{\pm1\}$ 如下：对自由群 $F$ 的每个生成元 $s\in S$ 定义映射 ${\rm sgn}(s)=-1$，然后将此映射扩充为 $F$ 到 $\{\pm1\}$ 的群同态。容易验证 $(W,S)$ 的所有生成关系都属于这个同态的核 (注意它们的长度都是偶数！)，因此 ${\rm sgn}$ 诱导了一个从 $(W,S)$ 到 $\{\pm1\}$ 的群同态。在此同态下，若 $w=s_{i_1}s_{i_2}\cdots s_{i_k}$ 是 $w$ 的任一既约表示，则
$${\rm sgn}(w)={\rm sgn}(s_{i_1}){\rm sgn}(s_{i_2})\cdots{\rm sgn}(s_{i_k})=(-1)^k=(-1)^{l(w)}.$$
从而 ${\rm sgn}(ws)={\rm sgn}(w){\rm sgn}(s)=-{\rm sgn}(w)$ 说明 $l(ws)\ne l(w)$。

长度函数 $l(\cdot)$ 是研究 Coxeter 群结构的基本工具。注意 $l(\cdot)$ 的定义依赖于生成元集 $S$ 的选择：对一个 Coxeter 群 $(W,S)$，完全可能选择其另一组不同的生成元 $S'\ne S$ 使得它们生成的群都是 $W$，但这时 $W$ 上的长度函数，根系，Bruhat 序等都可能随之改变。这就是为什么在描述一个 Coxeter 群 $(W,S)$ 时要指明 $S$ 的原因。


# 作为反射群的 Coxeter 群


反射群，顾名思义就是由空间中的反射变换生成的群。Coxeter 群都是反射群，即对任何抽象 Coxeter 群 $(W,S)$，我们都可以通过在 $\mathbb{R}^n\,(n=|S|)$ 中“精心摆放” $n$ 个反射镜面，使得关于这些镜面的反射生成的反射群同构于 $W$，这样就可以通过研究 $W$ 在空间中的作用来分析其结构，即用几何的方式来研究代数结构。将抽象 Coxeter 群实现为反射群的方式不唯一，其中最常用的是所谓的**标准几何实现**。这里最关键之处在于要弄清楚镜子的摆放方式对生成的反射群的结构有何影响。本文后面会看到，理解标准几何实现可以“庖丁解牛”地归结为理解一对反射变换 $s,t$ 生成的反射群的结构。


## 单个反射变换

{% blockquote %}
**定义**：设 $V$ 是一个 $n$ 维实向量空间，$\alpha\in V^\ast$ 是对偶空间中的线性泛函，$\alpha^\vee\in V$ 满足 $(\alpha,\alpha^\vee)=2$，则线性变换
$$s:V\to V,\quad s(v) =v-(\alpha, v)\alpha^\vee$$
满足

1. $s(\alpha^\vee)=-\alpha^\vee$。
2. $s$ 保持超平面 $\alpha=0$ 上的点不动。
3. $s^2=1$。

我们称 $s$ 是一个关于超平面 $\alpha=0$ 的反射变换。
{% endblockquote %}

即反射变换保持某个 $n-1$ 维超平面 $H$ 不动，同时把某个 $x\notin H$ 变为 $-x$。

<img style="margin:0px auto;display:block" width=300 src="/images/coxeter/reflection.svg"/>

注意你可以给 $\alpha$ 乘以任何非零实数 $c$，同时给 $\alpha^\vee$ 乘以 $1/c$，得到的反射变换仍然是 $s$。

在反射变换的定义中并不涉及内积的概念，当 $V$ 上有一个内积 $(\bullet)$ 时，对任何非迷向向量 $\alpha^\vee\in V$，反射变换
$$s(v) = v - 2\frac{(v\bullet\alpha^\vee)}{(\alpha^\vee\bullet\alpha^\vee)}\alpha^\vee$$
保持内积 $(\bullet)$ 不变，所以是一个正交变换，这时线性泛函 $\alpha$ 由 $u=\dfrac{2\alpha^\vee}{(\alpha^\vee,\alpha^\vee)}$ 给出：$v\to(v\bullet u)$。


## 两个反射变换


理解两个反射变换生成的反射群的结构非常重要，由此才能真正理解后面许多处理为什么要这样做。


设 $s$ 和 $t$ 分别是由 $(\alpha,\alpha^\vee)$ 和 $(\beta,\beta^\vee)$ 给出的两个反射变换，**在本节中我们只考虑两个线性泛函 $\alpha$ 和 $\beta$ 线性无关的情形**。我们想弄清楚 $s,t$ 生成的反射群 $G_{s,t}$ 的结构，以及它是怎样作用在空间 $V$ 上的。特别地我们想知道何时 $G_{s,t}$ “离散地”作用在 $V$ 上 (act discretely on $V$)，这里一个群 $G\subset GL(V)$ “离散地”作用在 $V$ 上的含义是，存在一个开区域 $\mathcal{D}\subset V$，使得对任何 $g\in G,g\ne1$ 都有 $g\mathcal{D}\cap\mathcal{D}=\emptyset$。

为什么要关心离散作用呢？不离散的作用会有什么问题吗？**答案是，只有在反射群离散地作用在 $V$ 上时，我们才可以打包票说整个反射群的结构可以由基本反射 $s\in S$ 之间两两的关系决定，而这归结为对每一对 $s,t\in S$，其生成的反射群 $G_{s,t}$ 离散地作用在 $V$ 上**。

不离散作用的典型例子是星状多面体，详情可以参考我的[这篇博客文章](/Todd-Coxeter-and-uniform-polytopes)。

记 $c_{s,t}=(\alpha,\beta^\vee), c_{t,s}=(\beta,\alpha^\vee)$，$G_{s,t}$ 的 Cartan 矩阵为
$$
\begin{bmatrix}(\alpha, \alpha^\vee) & (\alpha, \beta^\vee)\\
(\beta,\alpha^\vee) & (\beta,\beta^\vee)
\end{bmatrix} = \begin{bmatrix}2 & c_{s,t}\\
c_{t,s} & 2
\end{bmatrix}.
$$
给 $\alpha$ 乘以一个非零常数 $c$ 同时给 $\alpha^\vee$ 乘以 $1/c$ 不改变反射 $s$，这相当于给 $c_{s,t}$ 乘以 $c$ 同时给 $c_{t,s}$ 乘以 $1/c$，但是乘积 $n_{s,t}=c_{s,t}c_{t,s}$ 不变。我们会看到 $n_{s,t}$ 很大程度上决定了 $G_{s,t}$ 作用在 $V$ 上的方式。

由于我们假定了 $\alpha,\beta$ 是线性无关的，所以 $M=\{\alpha=0\}\cap\{\beta=0\}$ 是一个 $n-2$ 维的超平面。

一个简单的观察：

{% blockquote %}
**引理**：

1. 若 $\alpha^\vee$ 和 $\beta^\vee$ 线性相关则 $n_{s,t}=4$。
2. 若 $n_{s,t}\ne 4$ 则 $\alpha^\vee,\beta^\vee$ 线性无关且构成二维商空间 $V/M$ 的一组基。
{% endblockquote %}

**证明**：若 $\alpha^\vee$ 和 $\beta^\vee$ 线性相关，不妨设 $\alpha^\vee = c\beta^\vee$，则
$$\begin{align*}
c_{s,t}&=(\alpha,\beta^\vee)=(\alpha,\alpha^\vee/c)=2/c,\\
c_{t,s}&=(\beta,\alpha^\vee)=(\beta,c\beta^\vee) = 2c.
\end{align*}$$
从而 $n_{s,t}=4$。

反之若 $n_{s,t}\ne4$，则 Cartan 矩阵
$$\begin{bmatrix}2 & c_{s,t}\\c_{t,s} & 2\end{bmatrix}.$$
是非奇异的。若 $\alpha^\vee,\beta^\vee$ 不构成 $V/M$ 的一组基，则存在不全为 0 的 $c_1,c_2$ 使得
$$c_1\alpha^\vee + c_2\beta^\vee \in M.$$
从而
$$\begin{align*}
c_1(\alpha,\alpha^\vee) + c_2(\alpha, \beta^\vee)&=0,\\
c_1(\beta, \alpha^\vee) + c_2(\beta,  \beta^\vee)&=0.\\
\end{align*}
$$
这与 Cartan 矩阵非奇异矛盾。

所以在 $n_{s,t}\ne4$ 时，我们可以简化为讨论 $\alpha^\vee,\beta^\vee$ 生成的二维空间 $U$。

{% blockquote %}
**定理 1**：当 $n_{s,t}\ne 0,4$ 时 $U$ 上存在一个 $G_{s,t}-$ 不变的内积 $(\bullet)$，这个内积是正定的当且仅当 $0<n_{s,t}<4$。
{% endblockquote %}

分析一下：如果 $(\bullet)$ 是 $U$ 上的 $G_{s,t}-$ 不变的内积，则 $s$ 和 $t$ 都是此内积下的正交变换，这当且仅当 $\alpha^\vee$ 在此内积下正交于 $\{\alpha=0\}$，以及 $\beta^\vee$ 在此内积下正交于 $\{\beta=0\}$。注意到 $c_{s,t}\alpha^\vee - 2\beta^\vee\in\{\alpha=0\}$ 以及 $c_{t,s}\beta^\vee - 2\alpha^\vee\in\{\beta=0\}$，所以
$$\begin{align*}
(c_{s,t}\alpha^\vee - 2\beta^\vee) \bullet \alpha^\vee &= 0,\\
(c_{t,s}\beta^\vee - 2\alpha^\vee) \bullet \beta^\vee &= 0.
\end{align*}$$
即
$$\begin{align*}
c_{s,t}(\alpha^\vee\bullet\alpha^\vee) &= 2(\beta^\vee\bullet\alpha^\vee),\\
c_{t,s}(\beta^\vee\bullet\beta^\vee) &= 2(\alpha^\vee \bullet \beta^\vee).
\end{align*}$$
由于 $n_{s,t}\ne0$ 所以 $c_{s,t},c_{t,s}$ 都不是 0，从而内积在 $U$ 上的值由 $(\alpha^\vee\bullet\beta^\vee)$ 完全决定。即只要指定了 $(\alpha^\vee\bullet\beta^\vee)$ 的值，我们就得到了 $U$ 上的一个 $G_{s,t}-$ 不变内积。

内积 $(\bullet)$ 在 $U$ 上的 Gram 矩阵为
$$
\begin{bmatrix}
(\alpha^\vee\bullet\alpha^\vee) & (\alpha^\vee \bullet \beta^\vee)\\
(\alpha^\vee\bullet\beta^\vee)  & (\beta^\vee\bullet\beta^\vee)
\end{bmatrix} = (\alpha^\vee \bullet \beta^\vee)^2
\begin{bmatrix}2/c_{s,t} & 1\\1& 2/c_{t,s}\end{bmatrix}.
$$
Gram 矩阵是正定的当且仅当 $c_{t,s},c_{s,t}$ 同号且其行列式大于 0，即 $0<n_{s,t}<4$，得证。

### $0<n_{s,t}<4$

我们已经看到这时 $U$ 上的 $G_{s,t}-$ 不变内积是正定的，$s,t$ 是两个二维的欧式反射，所以 $st$ 是一个欧式旋转，设其旋转角为 $\theta$，则要使得 $G_{s,t}$ 离散地作用在 $U$ 上 $G_{s,t}$ 必须是有限群，即 $st$ 的阶有限，也即 $\theta$ 为有理数。


<img style="margin:0px auto;display:block" width=500 src="/images/coxeter/affine2d.svg"/>

<img style="margin:0px auto;display:block" width=400 src="/images/coxeter/finite2d.svg"/>

<img style="margin:0px auto;display:block" width=400 src="/images/coxeter/hyperbolic2d.svg"/>


## Coxeter 群的标准几何实现


# 根系


# Tits 锥


# 有限 Coxeter 群的分类





[^1]: James Humphreys, Reflection groups and Coxeter groups, Cambridge Press, 1990.

[^2]: V. Kac, Infinite dimensional Lie algebras, Cambridge University Press.

[^3]: [E. B. Vinberg, Discrete linear groups generated by reflections, Math. U. S. S. R. Izvestia 5 (1971)](/papers/Vinberg.pdf).

[^4]: [A. M. MacBeath, Groups of homeomorphisms of a simply connected space, Annals of Mathematics 79 (1964)](/papers/Macbeath.pdf).

[^5]: Notes and papers by [Casselman](https://www.math.ubc.ca/~cass/).
