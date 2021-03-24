---
title: "Coupling from the past 算法与 Markov 链的随机取样"
categories: [随机完美取样]
tags:
  - 算法
  - Coupling from the past
  - Perfectly random sampling
  - Lozenge tilings
date: 2016-07-02
url: "coupling-from-the-past"
---

本文是完美取样系列三部曲的最后一部，目的是介绍 Markov 链上的 coupling from the past 算法 (以下简称 *CFTP *)。之前的两部曲分别是多米诺洗牌算法和 Wilson 均匀生成树算法。

本文的代码在 [github](https://github.com/neozhaoliang/pywonderland/tree/master/src/CFTP) 上。

这三个算法的目的都是从某些很大很大的集合当中以给定的概率分布随机取样，区别在于它们针对的集合不同。多米诺洗牌算法是在 Aztec 钻石图的所有密铺中取样；Wilson 算法是在一个图的所有生成树中取样；而 CFTP 算法则是在一个 Markov 链的状态空间中按照其平稳分布取样。

我们先考虑一个看起来很初等的问题：

{% blockquote %}
**问题 1**：下图是一个边长分别为 $a,b,c$ 的平行六边形，其中 $a,b,c$ 都是正整数，内角均为 120 度：

<img style="margin:0px auto;display:block" width=300 src="/images/macmahon/hexagon.png">

请问：用边长为 1 的菱形密铺它，有多少种不同的方法？
{% endblockquote %}

<!-- more -->

比如下图就是一种密铺的示例：

<img style="margin:0px auto;display:block" width=300 src="/images/macmahon/planepartition.png"/>

图中三种不同摆放角度的菱形被染成了不同的颜色。

这个问题的答案很不容易猜到，叫做 Macmahon 公式：

{% blockquote %}
**Macmahon 公式**：记 $H(a,b,c)$ 为所求的六边形的不同菱形密铺的个数，则
$$H(a,b,c)=\prod_{i=1}^a\prod_{j=1}^b\prod_{k=1}^c\frac{i+j+k-1}{i+j+k-2}.$$
{% endblockquote %}

(多说一句，从这个表达式里你能看出它的结果是个整数吗？)

关于 Macmahon 公式的更多故事可以参见我的[另一篇文章](/macmahon-formula-plane-partitions/)，这里不再多介绍。但是不难看到 $H(a,b,c)$ 的值是指数级增长的，比如对 $a=b=c=10$ 这种比较小的情形 $H(a,b,c)\approx 9.265\times10^{33}$，已经是一个天文数字了。那好问题来了：

{% blockquote %}
**问题 2**：怎样在所有 $H(a,b,c)$ 种不同的密铺中完全随机地任选一种？(即按照均匀分布取样)
{% endblockquote %}

由于 $H(a,b,c)$ 很大所以我们不可能先把所有密铺列出来然后再挑选，所以得设计一个聪明点的方式，这就是 CFTP 算法大显身手的地方。


# Markov 链的随机取样


假设给定一个有限遍历的 Markov 链 $M$，其状态空间为 $S$，平稳分布为 $\pi$，我们希望以分布  $\pi$ 从 $S$ 中随机地取样，即对任何 $s\in S$，取样抽到 $s$ 的概率为 $\pi(s)$。通常的方法是任选一个初始状态 $s_0$ 然后从 $s_0$ 出发跑这个 Markov 链。可以证明只要运行的时间 $n$ 足够大，则其 $n$ 时刻的状态 $s_n$ 服从的分布就可以任意逼近平稳分布：
$$|\mathbb{P}(s_n=s) - \pi(s)| < \epsilon,\quad\forall s\in S,\ \forall\epsilon>0.$$
这个方法非常简单易行，但是它有两个缺陷：首先它只是一个近似算法，不管 $n$ 取得多么大，返回的 $s_n$ 的分布只是近似而非严格等于平稳分布 $\pi$；其次为了获得足够的精度采样所需的时间 $n$ (叫做 mixing time) 也不总是那么容易估计的。那么有没有什么办法可以给出 "精确地" 服从分布 $\pi$ 的采样呢？

Propp 和 Wilson 提出了如下的想法：既然从初始状态出发向未来 ($+\infty$ 方向) 跑 Markov 链只能无限接近平稳分布，我们何不从无穷远的过去 ($-\infty$ 方向) 向现在 (时刻 0) 跑呢？可以想象当这个链经过了无穷次迭代后，其 0 时刻的状态 $s_0$ 服从的分布就是平稳分布 $\pi$。当然我们没法做到真的从无穷远的过去出发，只可能是选择一个足够大的 $n$ 然后从时刻 $-n$ 时刻出发向时刻 0 跑，但是这样的话就和从 0 时刻向时刻 $n$ 跑没有什么区别了。Propp 和 Wilson 的观察的关键之处在于，只跑一个链是不行的，我们需要从每个 $s\in S$ 出发，同时跑 $M$ 的 $|S|$ 个不同的版本，并且需要它们在时刻 0 处耦合在一起 (coupled together)，即相遇到了相同的状态。这时输出的状态 $s_0$ 就恰好服从分布 $\pi$。如果没有相遇怎么办？那就从某个更久远的位置开始再来一遍，直到耦合出现为止，这就是 coupling from the past 的由来。

为了准确的描述 CFTP 算法，我们需要借助 Markov 链的随机映射表示 (random mapping representation)。


# Markov 链的随机映射表示


随机映射表示的目的是为了能够让我们用计算机程序模拟 Markov 链，它是一个由随机数流驱动的更新函数 $f: S\times [0, 1]\to S$。$f$ 本身是确定的，对任何状态 $s\in S$ 和 $u\in [0,1]$，$s'=f(s,u)$ 给出 Markov 链更新后的状态。特别地当 $u$ 来自某个服从 $[0, 1]$ 上的均匀分布的随机变量 $U$ 时，$\mathbb{P}(f(s, U)=s')=P_{s,s'}$。任何有限 Markov 链都存在随机映射表示，而且这个表示不是唯一的。最简单的构造方式是用一个阶梯函数：
$$f(s_i, u) = \begin{cases}\begin{array}{ll}s_1, &\text{for } u\in[0, P_{i,1}),\\s_2, &\text{for } u\in[P_{i,1}, P_{i,1}+P_{i,2}),\\\vdots &\vdots\\s_j, &\text{for } u\in\left[\sum_{k=1}^{j-1}P_{i,k}, \sum_{k=1}^jP_{i,k}\right),\\\vdots &\vdots\\s_n, &\text{for } u\in\left[\sum_{k=1}^{n-1}P_{i,k}, 1\right).\end{array}\end{cases}$$

假设有一个随机数发生器可以产生独立且服从 $[0,1]$ 上均匀分布的随机变量序列 $U_0,U_{-1},U_{-2},\ldots$，则我们可以由此来驱动 Markov 链 $M$ 从过去的某个时刻向现在运行：
$$s_{-n}\xrightarrow{f(s_{-n+1}, U_{-n+1})}s_{-n+1}\xrightarrow{f(s_{-n+2}, U_{-n+2})}\cdots\xrightarrow{f(s_0, U_0)}s_0.$$


# Coupling from the past 算法


现在我们可以来表述 coupling from the past 算法了。

设 $M$ 是一个有限遍历的 Markov 链，状态空间为 $S$，$f: S\times [0, 1]\to S$ 是其随机映射表示。$U_0,U_{-1},\ldots$ 是一列随机数，它们分别来自一列独立且服从 $[0, 1]$ 上均匀分布的随机变量。记 $(N_1,N_2,\ldots)=(1,2,4,8,\ldots)$，$-N_{m}$ 将作为我们第 $m$ 次重启的出发时间。

{% blockquote %}
**Coupling from the past 算法**：

1. 令 $m=1$。
2. 对每个 $s\in S$，以 $s$ 为初始状态，以 $-N_m$ 为初始时刻向时刻 0 的方向运行 Markov 链 $M$，所有 $|S|$ 个链使用的随机数均依次为 $U_{-N_m+1},\ldots,U_{-1},U_0$。
3. 如果步骤 2 中的 $|S|$ 个链在时刻 0 给出的状态相同，记此状态为 $s^\ast$，则输出 $s^\ast$ 并退出程序。否则将 $m$ 的值加 1 并重复步骤 2。

**断言**：如果上述步骤以概率 1 在有限时间内结束，则其返回值 $s^\ast$ 服从平稳分布 $\pi$:
$$\mathbb{P}(s^\ast = s) = \pi(s),\quad \forall s\in S.$$
{% endblockquote %}

注意这里的两个细节：第一是我们强调了前提**如果算法以概率 1 在有限时间内结束，则返回值服从平稳分布**。为了保证这个前提成立更新函数 $f$ 的选择就不能是任意的，特别地在后面的 monotone CFTP 中更新函数还要与 $S$ 上的偏序相容，更不能是任意的。第二是当第 $m$ 次执行步骤 2 时，使用的随机数为 $U_{-N_m+1},U_{-N_m+2},\ldots,U_{-1},U_0$，其中的后半部分 $U_{-N_{m-1}+1},U_{-N_{m-1}+2},\ldots,U_{-1},U_0$ 需要与上一次使用的相同，**即每一次都重复使用上一次的随机数作为后半段的随机源**，否则每次都重新生成一列新的随机数的话得到的最终状态未必服从平稳分布。

**证明**：任取 $s_i\in S$，我们只要证明对任何 $\epsilon > 0$ 都有
$$|\mathbb{P}(s^\ast=s_i) - \pi(s_i)|<\epsilon.$$
记 $A$ 为事件“算法在有限时间内结束”，则 $\mathbb{P}(A)=1$。又记 $A_i$ 为事件“算法不需要从早于 $-N_i$ 的时刻出发就可以结束”，则 $A_i\uparrow A$，$\mathbb{P}(A_i)\to\mathbb{P}(A)=1$。因此必然存在正整数 $K$ 使得对任何 $m\geq K$ 都有 $\mathbb{P}(A_m) \geq 1-\epsilon$。取定这样的 $K$，则在事件 $A_K$ 上，所有的链在时刻 0 具有相同的状态 $s^\ast$，算法返回的状态为 $s^\ast$。

此外我们以平稳分布 $\pi$ 选择一个初始状态，也从时刻 $-N_K$ 出发，也使用相同的随机数 $U_{-N_K+1},\ldots,U_0$ 运行链 $M$ 至时刻 0，并设这个链在时刻 0 的状态为 $Y$，则 $Y$ 服从平稳分布。

关键的来了：在事件 $A_K$ 上，算法的输出 $s^\ast$ 必然等于 $Y$ (因为所有 $|S|+1$ 条链使用的是同样的随机数序列，且所有的链都在时刻 0 耦合)，所以
$$\mathbb{P}(s^\ast=Y) \geq 1 - \epsilon.$$
从而对任何 $s_i\in S$，
$$\begin{align*}\mathbb{P}(s^\ast = s_i)-\pi(s_i)&= \mathbb{P}(s^\ast = s_i)-\mathbb{P}(Y = s_i)\\&\leq\mathbb{P}(s^\ast=s_i, Y\ne s_i)\\
&\leq\mathbb{P}(s^\ast\ne Y)\\&\leq\epsilon.\end{align*}$$
类似地
$$\begin{align*}\pi(s_i)-\mathbb{P}(s^\ast = s_i)&=\mathbb{P}(Y = s_i)-\mathbb{P}(s^\ast = s_i)\\&\leq\mathbb{P}(Y=s_i, s^\ast\ne s_i)\\
&\leq\mathbb{P}(s^\ast\ne Y)\\&\leq\epsilon.\end{align*}$$
由 $\epsilon$ 的任意性即得 $\mathbb{P}(s^\ast=s_i)=\pi(s_i)$，即 $s^\ast$ 服从平稳分布。


# 算法中的若干陷阱


CFTP 算法的证明看似不难，但其实微妙之处不少，值得细细品味。最主要的地方有三个：

{% blockquote %}
**问题 1**：为什么说更新函数 $f$ 的选择不能是任意的？

**问题 2**：既然 "coupling from the past" 可以，那 "coupling to the future" 可不可以？从时刻 0 开始从每个 $s\in S$ 出发跑 $|S|$ 个不同的链，直到它们在未来某个时刻 $n$ 耦合为止，然后输出第一次耦合时的状态不行吗？

**问题 3**：每次重启步骤 2 时需要复用之前的随机数，这一点在证明中哪里用到了？使用一列新的随机数为什么不可以？
{% endblockquote %}

我们用几个例子来说明这三个问题。

## 为什么更新函数不能是任意的

考虑含有两个状态 $S=\{s_1, s_2\}$ 的 Markov 链，其转移矩阵为 $P=\begin{bmatrix}0.5 & 0.5\\0.5 & 0.5\end{bmatrix}$，更新函数为 $$f(s_1, u) =\begin{cases}\begin{array}{ll}s_1 & \text{for } u \in [0, 0.5)\\s_2 & \text{for } u \in [0.5, 1]\end{array}\end{cases}$$ 和 $$f(s_2, u) =\begin{cases}\begin{array}{ll}s_2 & \text{for } u \in [0, 0.5)\\s_1 & \text{for } u \in [0.5, 1]\end{array}\end{cases}$$ 于是若从 $s_1,s_2$ 分别出发跑两个不同的链，但是每次使用相同的随机数，则它们要么保持不动，要么交换状态，永不耦合。

## Coupling to the future 为什么不行

仍然考虑含有两个状态 $S=\{s_1, s_2\}$ 的 Markov 链，其转移矩阵为 $P=\begin{bmatrix}0.5 & 0.5\\1 & 0\end{bmatrix}$，即从 $s_1$ 出发的话以 0.5 的概率待在原地，以 0.5 的概率跳到 $s_2$，从 $s_2$ 出发的话则总是跳到 $s_1$。

<img style="margin:0px auto;display:block" width="250" src="/images/cftp/counter_example.svg">

这个链的平稳分布为 $\pi=(\frac{2}{3},\frac{1}{3})$。现在假设从 $s_1,s_2$ 分别出发，从时刻 0 开始向 $+\infty$ 方向跑两个不同的链，$\tau$ 是它们首次耦合的时间，则 $\tau-1$ 时刻它俩必然一个位于 $s_1$，一个位于 $s_2$。但是位于 $s_2$ 的状态只能转移到 $s_1$，所以 $\tau$ 时刻的输出永远是 $s_1$，从而不满足平稳分布。

## 每次重新生成新的随机数为什么不行

在算法的证明当中，如果每次重启步骤 2 都使用新的随机数序列的话，则在第 $m$ 次重启时，由于生成的序列是全新的，有可能它实际上对很小的 $i$，从 $-N_i$ 出发就可以耦合，这个样本点不属于事件 $A_m$。

我们仍然用论证 coupling to the future 失败中使用的 Markov 链作为例子来说明。我们指定其更新函数 $f$ 为随机映射表示一节中给出的阶梯函数形式。假设算法每次都使用一列新的随机数，其最终输出为 $s^\ast$。定义随机变量 $\tau$ 为正整数 $m$ 使得算法中使用的最早的出发时间为 $-N_m$，则
$$\begin{align*}\mathbb{P}(s^\ast=s_1)&=\sum_{m=1}^\infty\mathbb{P}(s^\ast=s_1,\tau=m)\\&\geq\mathbb{P}(s^\ast=s_1,\tau=1)+\mathbb{P}(s^\ast=s_1,\tau=2)\\&=\mathbb{P}(\tau=1)\mathbb{P}(s^\ast=s_1|\tau=1)+\mathbb{P}(\tau=2)\mathbb{P}(s^\ast=s_1|\tau=2)\end{align*}$$
注意事件 $\{\tau=1\}$ 包含两种不同的演化路径：
$$\begin{align*}(1)\quad & s_1\to s_1,\quad s_2\to s_1.\\
(2)\quad & s_1\to s_2,\quad s_2\to s_1.\end{align*}$$
其中只有前者能成功耦合，所以 $\mathbb{P}(\tau=1)=\frac{1}{2}$，这时输出的状态只能是 $s_1$，所以$\mathbb{P}(s^\ast=s_1|\tau=1)=1$。

事件 $\{\tau=2\}$ 包含四种不同的演化路径：
$$\begin{align*}(1)\quad & s_1\to s_1\to s_1,\quad s_2\to s_1 \to s_1.\\
(2)\quad & s_1\to s_2\to s_1,\quad s_2\to s_1 \to s_1.\\
(3)\quad & s_1\to s_1\to s_2,\quad s_2\to s_1 \to s_2.\\
(4)\quad & s_1\to s_2\to s_1,\quad s_2\to s_1 \to s_2.\end{align*}$$
注意以下两种演化路径是非法的，因为每个时刻两个链使用的随机数一样，不可能在某个时刻同时出现一个链 $s_1\to s_2$，另一个 $s_1\to s_1$ 的情况：
$$\begin{array}{ll}
(*)\quad & s_1\to s_1\to s_2,\quad &s_2\to s_1 \to s_1.\\
(**)\quad & s_1\to s_1\to s_１,\quad &s_2\to s_1 \to s_２.\\
\end{array}$$
注意在我们现在这个错误的版本中，由于使用了全新的随机数流，四种路径都是合法的。这四个路径中前三种都成功耦合，两个耦合于 $s_1$ 一个耦合于 $s_2$，所以 $\mathbb{P}(s^\ast=s_1|\tau=2)=\frac{2}{3}$。

另一方面
$$\mathbb{P}(\tau=2)=\mathbb{P}(\tau\ne1)\cdot\mathbb{P}(\tau=2\ \text{时耦合})=\frac{1}{2}\cdot\frac{3}{4}=\frac{3}{8}.$$

所以
$$\begin{align*}\mathbb{P}(s^\ast=s_1)&\geq\mathbb{P}(\tau=1)\mathbb{P}(s^\ast=s_1|\tau=1)+\mathbb{P}(\tau=2)\mathbb{P}(s^\ast=s_1|\tau=2)\\&=\frac{1}{2}\cdot1 + \frac{3}{8}\cdot\frac{2}{3}\\&=\frac{3}{4}\ne \pi(s_1).\end{align*}$$


# Monotone coupling from the past


在 CFTP 算法中，我们需要同时跑 $|S|$ 个不同的链并要求它们在时刻 0 处耦合，可以想象当 $|S|$ 很大时所耗的时间和计算量都很不划算。但是如果 $S$ 是一个偏序集 $(S, \preceq)$，有最大最小元 $s_\max, s_\min$，并且更新函数 $f$ 与偏序 $\preceq$ 相容，即对任何 $s,s'\in S$，$u\in[0,1]$，
$$s\preceq s' \Rightarrow f(s, u) \preceq f(s', u),$$

则我们每次只要对 $s_\max, s_\min$ 这两个状态跑两个不同的链即可，当它们耦合时，所有其它的链也会被“挤压”到相同的状态。这就是前面六边形的菱形密铺取样所采取的方法。

每个密铺可以看做是在一个 $a\times b\times c$ 大小的房间的墙角“堆箱子”，每个箱子占据一个 $1\times1\times1$ 的正方体位置，总共有 $abc$ 个这样的位置。两个密铺 $t,t'$ 满足 $t\preceq t'$ 当且仅当 **$t'$ 的所有箱子占据的位置是 $t$ 的一个子集**。于是这个偏序下的最小元对应的密铺就是房间被所有箱子都填满，最大元对应的密铺就是“空”房间。这个定义看起来好像写反了：为什么箱子更多的反而在偏序下更小呢？这其实是因为密铺在程序中是用不相交的路径组表示的。

我们需要把所有密铺组成的集合看做一个 Markov 链的状态空间，并定义与此偏序相容的随机映射表示。这个 Markov 链是这样的：任选一个状态 $t$，这是一个密铺，任选房间中的一个位置，并尝试以 $\frac{1}{2}$ 的概率在该位置放置或者移走一个箱子。如果操作的结果仍然是一个密铺 $t'$，则状态转移为 $t\to t'$，否则保持 $t$ 不变。你可以验证这个链是有限的、可逆的、非周期的，所以其平稳分布就是均匀分布。此外上述操作步骤给出了一个与偏序相容的更新函数。

下图显示的是一个 $a=b=c=50$ 时的随机密铺：

<img style="margin:0px auto;display:block" width="400" src="/images/cftp/cftp.png">

你有没有发现图形中出现了一个内切的近似椭圆的形状？当六边形足够大时，会出现某个极限区域，密铺在区域内部表现得杂乱无序，而在区域外部则呈现某种“冻结”的形状。这种随机的密铺在大标度下表现出某种确定性行为是一个非常有意思的研究方向。


# CFTP 的直观解释


CFTP 算法可以形象的理解为在一大团线束中寻找特殊的一根：设随机数序列 $U_0,U_{-1},\ldots$ 已经给定，我们对每个状态 $s\in S$ 和每个 $k=-1,-2,\ldots$，从 $s_i$ 出发，以初始时刻为 $k$ 运行 Markov 链 $M$ 至时刻 0，则得到了一条颜色为 $s$，长度为 $k$ 的轨迹 $\mathcal{T}_{s,k}$。所有的轨迹 $\{\mathcal{T}_{s,k}\}$ 合在一起构成了一个巨大的线束，这个线束汇聚在时刻 0 处。我们要在这个巨大的线束中寻找“神奇”的那一根，即它由 $|S|$ 根不同颜色但是具有相同长度的线束在某处汇聚而成。一旦找到了它，则一个从无穷远的过去运行到现在的 Markov 链，不论其初始状态是什么，其最后的部分必然与此线束重合，从而该线束的端点就是一个服从平稳分布的状态。为此我们一段一段地向过去捋这个线束，依次检查长度为 $N_m=1,2,4,8,\ldots,$ 的部分，不满足要求就加大距离继续向前捋。


# 参考文献


1. Finite Markov chains and algorithmic applications, Olle Häggström.
2. [Markov chains and mixing times](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf), Yuval Peres, Elizabeth L. Wilmer, David A. Levin.