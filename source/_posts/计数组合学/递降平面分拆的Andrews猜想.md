---
title: "递降平面分拆的 Andrews 猜想"
date: 2015-08-30
tags:
  - Plane partitions
  - Descending plane partitions
  - Enumerative combinatorics
  - q- binomial theorem
  - Gessel-Viennot lemma
  - Alternating sign matrices
  - Andrews's conjecture
  - Non-intersecting path systems
  - Gauss lattice paths
categories: [计数组合学]
url: "descending-plane-partitions"
---

# 前言

你可能经常听到这样一句话：“做数学要大胆假设，小心求证”。我们今天要介绍的故事主角平面分拆中的 Andrews 猜想就完美地符合这一点。两个看似风马牛不相及的计数对象，因为有着相同的计数序列，冥冥中被联系在了一起，启发三位数学家 Mill, Robins 和 Rumsey 解决了一个困难的组合学猜想。整个过程并无高深的内容，但是其中的“信仰一跃”和“灵魂一猜”构成了故事的高潮，而那些繁琐的计算过程不过是小心求证的注脚而已。

本文来自我几年前读 David Bressoud 的

> Proofs and Confirmations: The Story of the Alternating Sign Matrix Conjecture

一书时的读书笔记，但是叙述与 Bressoud 的书不同：Bressoud 是把 DPP 的 Andrews 猜想和 CSPP 的 Macdonald 猜想统一用 $q-$ 超几何级数一起解决的，因此理论较为复杂。由于 Macdonald 猜想的证明似乎无法避免使用超几何级数的理论，而本人水平不足，没有看懂这一部分，所以这里只介绍 DPP 的 Andrews 猜想，并仅使用初等的 $q-$ 二项式定理作为工具，所以计算步骤会显得有些繁琐。

<!-- more -->

# 问题描述


**问题**：一个**严格错位平面分拆** (strict shifted plane partition) 是一个二维的正整数数组 $\pi$，其形状如下：
$$
\begin{matrix}
a_{11}&a_{12}&\cdots&\cdots&\cdots&a_{1,\lambda_1}\\
      &a_{22}&\cdots&\cdots&\cdots&a_{2,\lambda_2+1}\\
      &&\ddots&\cdots&\cdots&\cdots\\
      &&&a_{mm}&\cdots&a_{m,\lambda_m+m-1}
\end{matrix}
$$
其中 $\pi$ 满足如下限制条件：

1. 每一行与上一行相比都缩进 1 个位置，其非零元个数为 $\lambda_i$。
2. 每一行从左到右是弱递减的: $a_{ij}\geq a_{i,j+1}$。
3. 每一列从上到下是严格递减的：$a_{ij}>a_{i+1,j}$。

此外如果 $\pi$ 满足任何一行的长度严格小于该行第一个元素，并且大于等于下一行的第一个元素，即
$$
a_{11}>\lambda_1\geq a_{22}>\lambda_2\geq\cdots\geq a_{mm}>\lambda_m,
$$
就称 $\pi$ 是一个**递降平面分拆** (descending plane partition，本文以下简称为 DPP)。显然 DPP 是严格错位平面分拆的子集。

OK，我知道在一个定义里面一下子塞进去这么多定语会让人很晕，所以下面是一张插图：任何类型的平面分拆从“空间鸟瞰图”的角度去看都是在房间中按照一定的规则“堆方块”。例如 DPP 分拆
$$
\pi\ =\ \begin{matrix}
7&7&6&6&3&1\\&6&5&4&2\\&&3&3\\&&&2\end{matrix}
$$
对应的鸟瞰图如下图所示：

<img style="margin:0px auto;display:block" width="500" src="/images/dpp/dpp_example.png" />

你可以看到数组的每一行与方块的每一层一一对应。由于 $\pi$ 是严格错位平面分拆，所以每一层相对于下面一层在两个方向上分别缩进一个单位以后仍然可以被下面一层托住，从而不会出现“悬空”的方块。

我们记 $|\pi|=\sum_{i,j}a_{ij}$ 为 $\pi$ 的所有元素之和。

设 $\mathrm{dpp}(n)$ 为所有数字均不超过 $n$ 的 DPP 组成的集合，这样的 DPP 最多有 $n-1$ 行，每一行长度最多是 $n-1$，每个元素不大于 $n$，所以必然能装进一个大小为 $n\times n\times n$ 的空间 (当然不可能填满)。我们的目标是求出生成函数
$$
\sum_{\pi\in {\rm dpp}(n)} q^{|\pi|}.
$$

{% blockquote %}
**例子**：$\mathrm{dpp}(3)$ 总共包含 7 种不同的分拆 (空分拆也算一种)：
$$
\mathrm{dpp}(3)=\big\{
  \begin{array}{ccccccc}
  \emptyset,
  &\begin{matrix}3&3\\&2\end{matrix},
  &2,
  &\begin{matrix}3&3\end{matrix},
  &3,
  &\begin{matrix}3&2\end{matrix},
  &\begin{matrix}3&1\end{matrix}
  \end{array}
  \big\}.
$$
所以其 $q-$ 计数为
$$
\sum_{\pi\in {\rm dpp}(3)} q^{|\pi|}=1+q^2+q^3+q^4+q^5+q^6+q^8.
$$
{% endblockquote %}

[George Andrews](https://en.wikipedia.org/wiki/George_Andrews_(mathematician)) 发现，这个生成函数可以表示为一个 $q-$ 行列式：
$$
\sum_{\pi\in {\rm dpp}(n)} q^{|\pi|}=
\det\left(
  \delta_{ij}+q^{i+1}
    \binom{i+j}{j-1}_q
    \right)_{1\leq i,j\leq n-1}.
$$
Andrews 会求 DPP 的计数序列 (即 $q=1$ 的情形)，但是不会算这个 $q-$ 行列式，事实上这个问题最难的地方就在求 $q-$ 行列式这一步上！不过 Andrews 猜出了这个行列式的表达式：

{% blockquote %}
**Andrews 猜想**：
$$
\det\left(
  \delta_{ij}+q^{i+1}
    \binom{i+j}{j-1}_q
    \right)_{1\leq i,j\leq n-1}=
\prod_{1\leq i,j\leq n}\frac{1-q^{n+i+j-1}}{1-q^{2i+j-1}}.
$$
{% endblockquote %}

这个猜想最终在 80 年代由 Mills, Robbins, Rumsey 三人解决 [^1]，整个证明过程可谓一波三折，既需要缜密细心的推理，也不乏大胆的猜测，本文接下来就来介绍他们的证明。


# 故事的开始


了解 DPP 背后的故事对理解证明是很有帮助的。对第一次接触递降平面分拆这个名词的读者来说，可能会纳闷：“数学家们为什么要考虑这种看起来很初等的计数问题呢？它似乎不像代数几何、数论中的问题那么有分量，而且还有一些不明所以的限制条件”。这是一种错觉，实际上平面分拆简单的外表背后有许多深刻而有趣的理论。DPP 最初是上世纪 70 年代 Andrews 在研究另一类平面分拆“循环对称平面分拆 (CSPP)”时得到的副产品，我们之前提到 Andrews 会算 DPP 计数序列在 $q=1$ 的情形，也猜出了 $q-$ 计数的正确答案，但是没有给出证明，不过那时 DPP 作为众多平面分拆猜想之一并不显得特别重要。

差不多在与 Andrews 研究 DPP 同样的时期，数学家 Mills, Robbins, Rumsey 三人正在为[交错符号矩阵](https://en.wikipedia.org/wiki/Alternating_sign_matrix) (Alternating Sign Matrix，以下简称 ASM) 猜想而苦苦挣扎，他们考虑的 $n$ 阶的交错符号矩阵是指满足如下条件的 $n\times n$ 矩阵：

1. 每个元素取值为 $1,-1,0$。
2. 矩阵的每一行和每一列的和都是 1。
3. 对每一行和每一列，其 $1$ 和 $-1$ 交替出现。

{% blockquote %}
**例子**：3 阶的交错符合矩阵共有 7 个，其中 6 个是置换矩阵，只有一个含有 -1：
$$
\begin{align*}
&\mathrm{ASM}(3)=
\Bigg\{
  \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},
  \begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
  \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},\\
  &\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
  \begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
  \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
  \begin{pmatrix}0&1&0\\1&-1&1\\0&1&0\end{pmatrix}
  \Bigg\}.
\end{align*}
$$
{% endblockquote %}

Mill 等人通过直观的杨辉三角法猜出了 ${\rm ASM}(n)$ 的计数序列，但是对怎样证明它毫无头绪，于是他们求助于 MIT 的组合学大师 Stanley，Stanley 告诉他们自己也不会做，但是 Mills 等人给出的 ASM 的计数序列**看起来**与 Andrews 得到的 DPP 的计数序列是相同的：
$$
|\mathrm{dpp}(n)|=|\mathrm{ASM}(n)|=\prod_{j=0}^{n-1}\frac{(3j+1)!}{(n+j+1)!}=1,2,7,42,429,\ldots
$$
于是 Mills 等人很自然地转而研究 DPP，希望从中找到解决 ASM 猜想的办法。有趣的是他们没能解决 ASM 猜想 (1995/96 年由 Zeilberger 和 Kuperberg 分别解决)，倒是解决了 DPP 的 Andrews 猜想以及 CSPP 的 Macdonald 猜想，这不能不说是“失之东隅，收之桑榆”。

Mills 等人的证明受到了 DPP 与 ASM **貌似**有相同的计数序列这个事情的启发。在一个 $n$ 阶 ASM 中，第一行必然有且只有一个 +1 (否则有 -1 的话这个 -1 所在的列不可能满足 +1 和 -1 交替出现且列和为 +1 )，这个 +1 所处的位置是一个重要的参数，根据这个 +1 所在的列 $k$ 可以把 $\mathrm{ASM}(n)$ 分成 $n$ 个子集 $\{A_{n,k},k=1,\ldots,n\}$，Mills 等人**猜测** $A_{n,k}$ 的大小为
$$
\left|A_{n,k}\right|=
  \begin{pmatrix}n+k-2\\k-1\end{pmatrix}
  \frac{(2n-k-1)!}{(n-k)!}
  \prod_{j=0}^{n-2}\frac{(3j+1)!}{(n+j)!}.
$$
既然 ${\rm dpp}(n)$ 和 ${\rm ASM}(n)$ **看起来**是一样大小的，那是不是意味着它也应该有一个参数，将 ${\rm dpp}(n)$ 对应地分为 $n$ 个不同的子集呢？

很自然地，Mills 等人猜测在一个 $\pi\in\mathrm{dpp}(n)$ 中数字 $n$ 出现的次数就是对应的参数，而且他们猜测恰好含有 $k-1(1\leq k\leq n)$ 个 $n$ 的 DPP 的个数等于 $|A_{n,k}|$，这个猜测在他们的证明中起着关键的作用。(注意 $n$ 出现的次数至多是 $n-1$，否则由于这些 $n$ 必然都在第一行，不满足 DPP 的行首严格大于该行长度的限制)

证明的第一步是把计数问题转化为行列式的求值，为此我们需要一些关于 Gauss 二项式系数的结论。


# 一点预备知识


本文需要的预备知识大致分为三点：

1. $q-$ 二项式定理。
2. Gauss 路径的 $q-$ 计数。
3. 格点图上不相交路径组计数的 Gessel-Viennot 引理。

其中 Gessel-Viennot 引理由于详细叙述起来比较占篇幅，这里就省略了，读者可以参考 Aigner 所著《Proofs from The Book》一书 [^2] 的 "Lattice paths and determinants" 一节。

Gauss 二项式系数的定义为
$$
\binom{n}{k}_q=\frac{(1-q^n)(1-q^{n-1})\cdots(1-q^{n-k+1})}{(1-q^k)(1-q^{k-1})\cdots(1-q)}.
$$
其中约定 $\binom{n}{0}_q=1$ 以及 $k<0$ 时 $\binom{n}{k}_q=0$。

关于 Gauss 二项式系数的两个基本结论是：

<div id="binom-theorem1">

{% blockquote %}
**定理 1**：
$$
\prod_{k=0}^{n-1}(1+xq^k)=\sum_{k=0}^nq^{\binom{k}{2}}\binom{n}{k}_qx^k.
$$
{% endblockquote %}
</div>

<div id="binom-theorem2">
{% blockquote %}

**定理 2**：
$$
\prod_{k=0}^{n}\frac{1}{1-xq^k}=\sum_{k=0}^\infty\binom{n+k}{k}_qx^k.
$$
{% endblockquote %}
</div>

Gauss 二项式系数有不少等价的描述方式，我们这里要用到的是它还等于 Gauss 路径的 $q-$ 计数。

考虑格点图 $\mathbb{Z}^2$，并设 $A=(0, m)$，$B=(n,0)$。一条从 $A$ 到 $B$ 的 Gauss 路径 $P$ 是一个从 $A$ 出发，每一步向右或者向下一个单位距离，经过 $m+n$ 步后到达 $B$ 的格点路径，如下图所示：

<img style="margin:0px auto;display:block" width="350" src="/images/dpp/gausspath.svg" />

熟知这样的 Gauss 路径一共有 $\binom{m+n}{n}$ 条，它们组成的集合记作 $\mathcal{G}(m,n)$。

我们规定路径 $P$ 的权重为 $q^{|P|}$，其中 $|P|$ 等于 $P$ 与坐标轴所围成的区域中包含的方格的个数，上图中用圆圈标出了这些方格，一共有 21 个，所以其权重为 $q^{21}$。

关于 Gauss 路径的一个基本结论是，所有 $\mathcal{G}(m,n)$ 中路径的权重之和等于 Gauss 二项式系数 $\binom{m+n}{n}_q$：
$$
\sum_{P\in\mathcal{G}(m,n)}q^{|P|} = \binom{m+n}{n}_q.
$$


# 将问题转化为行列式求值


设 $\pi\in\mathrm{dpp}(n)$ 的行首**从下到上**分别为 $2\leq a_1 <\cdots < a_m\leq n$，注意 $a_1$ 是必须大于 1 的 (否则与每一行的第一个元素必须大于该行的长度矛盾)。我们的策略是在假定这些行首已知的前提下，求出行首恰好为集合 $\{a_1,\ldots,a_m\}$ 的那些 DPP 的生成函数，然后再对 $\{a_1,\ldots,a_m\}$ 的所有可能求和。

> 注意我们这里对 $a_1,\ldots,a_m$ 的标记顺序与前面 DPP 定义中的行的顺序是反着来的，$a_1$ 是第 $m$ 行的行首，$a_2$ 是第 $m-1$ 行的行首，以此类推，$a_m$ 是第一行的行首。这样做看起来有些奇怪，其实是为了后面记号方便，下面很快就会看到原因。

既然这些行首 $\{a_1,\ldots,a_m\}$ 已经固定，我们就可以把这 $\sum_{i=1}^m a_i$ 个箱子移走 (后面补上 $q^{\sum_{i=1}^ma_i}$ 的因子即可)。由于递降平面分拆中每一行的行首严格大于该行的长度，所以删去 $a_i$ 以后其所在行剩下的部分是一个长度 $\leq a_i-2$，最大元素 $\leq a_i$ 的序列，这样的序列与从 $(0, a_i)$ 出发，每一步向右或者向下，到达 $(a_i-2,0)$ 的 Gauss 路径 $P_i\in\mathcal{G}(a_i,a_i-2)$ 一一对应，所有 $P_i$ 构成一个**不相交的格点路径组** $\mathcal{P}=\{P_1,\ldots,P_m\}$，其起点集合为 $\{A_i=(0, a_i)\}$，终点集合为 $\{B_j=(a_j-2, 0)\}$，如下面的动画所示：

<video src="/images/dpp/dpp-path.mp4" width="500" controls></video>

将这些路径投影到地面上就得到如下的示意图：

<img style="margin:0px auto;display:block" width="400" src="/images/dpp/dpp-path.svg" />

我们费点笔墨解释下为什么这些路径之间是没有交点的。

注意 $P_i$ 在 $x$ 轴上的终点是 $(a_i-2,0)$，而它上方的路径 $P_{i+1}$ 必然经过 $x$ 轴上的 $(\lambda_{i-1}-1,0)$ 这个点 (注意我们对路径的标号和原本 $\pi$ 的行号是反着来的，下标越大对应的行越往上)，要使得 $P_i,P_{i+1}$ 不相交就必须有 $\lambda_{i-1} - 1 > a_i - 2$，即 $\lambda_{i-1}\geq a_i$，这就是为什么在 DPP 的定义中要求每一行的长度大于等于下一行的行首元素。

那为什么 $P_i,P_{i+1}$ 也不会在 $x$ 轴上方相交呢？这是因为假设它们有交点 $v$，设 $v$ 的 $y$ 坐标为 $h$，则 $P_i$ 在到达 $v$ 之前的最后一条水平边的高度 $h'\geq h$，$P_{i+1}$ 在从 $v$ 继续出发接下来的第一条水平边的高度 $h''\leq h$，从而 $h'\geq h''$，这与 $\pi$ 的列是严格递降的矛盾。

反之给定这样的一个不相交路径组 $\mathcal{P}$，我们也可以还原出对应的 DPP 来，于是根据 Gessel-Viennot 引理，以 $\{a_1,\ldots,a_m\}$ 为行首的 DPP 的个数为
$$
\det\left(\binom{a_i+a_j-2}{a_j-2}\right)_{1\leq i,j\leq m}.
$$
其中矩阵的 $(i,j)$ 位置的元素为从 $A_i=(0,a_i)$ 到 $B_j=(a_j-2,0)$ 的 Gauss 路径的个数，这当然是 $\binom{a_i+a_j-2}{a_j-2}$。

对所有的 $2\leq a_1 <\cdots < a_m\leq n$ 求和即为 ${\rm dpp}(n)$ 的个数：
$$
|{\rm dpp}(n)|=\sum_{2\leq a_1<\cdots< a_m\leq n}\det\left(\binom{a_i+a_j-2}{a_j-2}\right)_{1\leq i,j\leq m}.
$$
为了把这个表达式化简，我们用 $a_i-1$ 代替每个 $a_i$，于是
$$
|{\rm dpp}(n)|=\sum_{1\leq a_1<\cdots< a_m\leq n-1}\det\left(\binom{a_i+a_j}{a_j-1}\right).
$$
现在我们只需要一个线性代数的引理：

<div id="linalg1">
{% blockquote %}

**引理 1**：设 $A$ 是一个 $r\times r$ 矩阵，则 $\det(I_r+A)$ 等于对 $A$ 的所有主子式求和，即 $$\det(I_r+A)=\sum_{1\leq a_1<\cdots< a_m\leq r}\det A[a_1a_2\cdots a_m].
$$
其中 $A[a_1a_2\cdots a_m]$ 是由 $A$ 的第 $a_1,\ldots,a_m$ 行和同样下标的列组成的 $m$ 阶子矩阵。
{% endblockquote %}
</div>

由此我们得到 $$|{\rm dpp}(n)|=\det\left(\delta_{ij}+\binom{i+j}{j-1}\right)_{1\leq i,j\leq n-1}.
$$
至此我们就得到了 $q=1$ 时 ${\rm dpp}(n)$ 的计数序列的行列式形式。

求 $q-$ 计数的行列式表达式的话需要多做一点微小的工作：由于 Gauss 路径 $P_i$ 的权重等于 $q^{|P_i|}$，其中 $|P_i|$ 是位于它下方的方格的总数，这个数目正是在递减平面分拆中，在移走行首 $a_i$ 后，第 $i$ 层中剩下的方块个数。我们需要说明所有路径权重的乘积在 Gessel-Viennot 引理中交换路径的操作后仍然保持不变，否则无法直接使用 G-V 引理。(Bressoud 的书插图 3.4 给出了针对通常平面分拆的一个反例)

注意到一个长度为 $l$ 的 Gauss 路径可以用一个长度为 $l$ 的 0-1 序列 $\sigma$ 来表示，0 表示垂直向下的一步，1 表示水平向右的一步，路径下方所含的方格个数与序列 $\sigma$ 的“逆序数” $\mathrm{inv}(\sigma)$ 相同，这里
$$
\mathrm{inv}(\sigma) = \#\{(i,j)\, |\, i < j, 1=\sigma(i) >\sigma(j)=0\}.
$$
这个方格个数与逆序对的对应很容易从下图看出来：

<img style="margin:0px auto;display:block" width="350" src="/images/dpp/path-weight.svg" />

上图中 $\sigma=1110011000$。

设 $P$ 和 $Q$ 是两个 Gauss 路径，其对应的 0,1 序列分别为 $\sigma_1$ 和 $\sigma_2$，$P$ 和 $Q$ 有一个公共的交点 $v$。交换 $P$ 和 $Q$ 在 $v$ 之后的部分得到的路径记作 $P'$ 和 $Q'$，对应的 0,1 序列分别为 $\sigma_1'$ 和 $\sigma_2'$，则不难验证有
$$
\begin{align*}
|P'|+|Q'|-|P|-|Q|&=\mathrm{inv}(\sigma_1')+\mathrm{inv}(\sigma_2')-\mathrm{inv}(\sigma_1)-\mathrm{inv}(\sigma_2)\\
&=(p_0-q_0)(p_1-q_1).
\end{align*}
$$
这里 $p_0,q_0$ 分别表示 $P,Q$ 在交点 $v$ **之后**的部分所含的 0 的个数，$p_1,q_1$ 分别表示 $P,Q$ 在交点 $v$ **之前**的部分所含的 1 的个数。

在 DPP 的情形，由于每条路径的出发点都在 $y$ 轴上，终点都在 $x$ 轴上，因此 $P,Q$ 在到达它们的交点处 (如果有的话) 各自横向移动的步数相同，从交点到终点各自纵向移动的步数也相同，所以 $p_0=q_0$，$p_1=q_1$，从而 $|P'|+|Q'|=|P|-|Q|$，因此路径权重的乘积 $q^{|P|}\cdot q^{|Q|}=q^{|P'|}\cdot q^{|Q'|}$ 保持不变，从而 Gessel-Viennot 引理仍然可用。

现在顶点集合 $\{A_i=(0,a_i)\}$，$\{B_j=(a_j-2,0)\}$，而从 $A_i$ 到 $B_j$ 的 Gauss 路径的 $q-$ 计数为 $\binom{a_i+a_j-2}{a_j-2}_q$，于是行首分别为 $\{a_1,\ldots,a_m\}$ 的 DPP 的 $q-$ 计数为
$$
q^{\sum_{i=1}^m a_i}\cdot\det\left(\binom{a_i+a_j-2}{a_j-2}_q\right)_{1\leq i,j\leq m}=
\det\left(q^{a_i}\binom{a_i+a_j-2}{a_j-2}_q\right)_{1\leq i,j\leq m}.
$$
通过用 $a_i-1$ 代替 $a_i$ 并使用前面的[引理](#linalg1)，我们得到

{% blockquote %}
**定理 3**：${\rm dpp}(n)$ 的 $q-$ 计数为
$$
\det\left(\delta_{ij}+q^{i+1}\binom{i+j}{j-1}_q\right)_{1\leq i,j\leq n-1}.
$$
{% endblockquote %}

现在剩下的任务就是求这个行列式的值了，而这才是整个故事中最困难的部分，到目前为止我们的路才走了一小半呢。


# 用关键参数将行列式分解


在上一节中，我们已经把 ${\rm dpp}(n)$ 的 $q-$ 计数归结为求行列式 $\det(I_{n-1}+H_{n-1})$ 的值，其中 $H_{n-1}=\left(q^{i+1}\binom{i+j}{j-1}_q\right)_{1\leq i,j\leq n-1}$。这里你需要小心 ${\rm dpp}(n)$ 对应的是一个 $n-1$ 阶矩阵，这在记号上确实会带来一些困扰。

Mills 等人认为，在一个 $\pi\in{\rm dpp}(n)$ 中，$n$ 出现的次数是一个重要的参数，根据 $n$ 出现的次数 $k$ 可以把 ${\rm dpp}(n)$ 分成 $n$ 个子集 $\{S_k,k=0,\ldots,n-1\}$，解决问题的关键在于分别求出每个 $S_k$ 的 $q-$ 计数对应的行列式表示，并将这些行列式的值看作序列计算其满足的递推关系。

<div id="theorem-Hkn">
{% blockquote %}

**定理 4**： $S_k$ 的 $q-$ 计数为 $\det H_{k,n-1}$，其中矩阵 $H_{k,n-1}$ 在 $k=0$ 时是把 $I_{n-1}+H_{n-1}$ 的最后一行用 $(0,\ldots,0,1)$ 替换得到的矩阵，而在 $k>0$ 时则是把 $I_{n-1}+H_{n-1}$ 的最后一行用向量
$$
q^{kn}
\left(\binom{n+0-k}{1-k}_q,\binom{n+1-k}{2-k}_q,\cdots,\binom{n+n-2-k}{n-1-k}_q\right)
$$
替换得到的矩阵。

这里我们规定当 $m<0$ 时有 $\binom{a}{m}_q=0$。
{% endblockquote %}
</div>

**证明**：$k=0$ 的情形其实就是 ${\rm dpp}(n-1)$ 的 $q-$ 计数，它等于 $I_{n-2}+H_{n-2}$，正好是 $I_{n-1}+H_{n-1}$ 的左上角 $n-2$ 阶子矩阵，所以这个情形很简单，下面考虑 $k>0$ 的情形。

我们还是先**从下到上**固定每一行的行首 $\{a_1,\ldots,a_m\}$，求出行首固定时的生成函数，再对所有可能的行首相加。

办法和以前一样：现在除了行首 $\{a_1,\ldots,a_m\}$ 是已知的，我们知道第一行还有 $k-1$ 个 $n$ 出现，并且它们的位置必然是紧跟在行首的 $n$ 后面。我们把这些已知的 $\sum_{i=1}^{m-1}a_i+kn$ 个箱子移走，将剩下的部分对应到一个不相交的路径组，用 Gessel-Viennot 引理得出其生成函数，最后再补上因子 $q^{\sum_{i=1}^{m-1}a_i+kn}$ 即可。

这个到路径组的对应方法和以前类似，只不过我们截掉 $\pi$ 的第一行路径中已知的部分，以之前的插图为例子并取 $n=7$：

<img style="margin:0px auto;display:block" width="400" src="/images/dpp/dpp-path2.svg" />

这里 $\pi$ 的第一行必然首先从 $(0,n)$ 出发，向右走 $k-1$ 步到达 $(k-1,n)$，然后向下走到 $(k-1,n-1)$。我们把这部分截去，只保留剩下的部分，这相当于把起点 $A_m=(0, n)$ 换成了 $(k-1,n-1)$，其余的起点和终点保持不变，则新顶点集 $\{A_i\}$ 和 $\{B_j\}$ 之间的不相交的路径组的 $q-$ 计数为 (注意由于终点都在 $x$ 轴上因此 Gesssel-Viennot 引理仍可用, important!) $\det X$，其中
$$x_{ij}=\begin{cases}
\binom{a_i+a_j-2}{a_j-2}_q, & i < m\\
\binom{n+a_j-k-2}{a_j-k-1}_q, & i=m.
\end{cases}
$$
把因子 $q^{\sum_{i=1}^{m-1}a_i+kn}$ 补回去，其中 $q^{a_i}$ 补在第 $i$ 行上，$kn$ 补在第 $m$ 行，我们就得到行首为 $\{a_1,\ldots,a_m\}$ 且恰好含有 $k$ 个 $n$ 的 DPP 的 $q-$ 计数为 $\det Y$，其中
$$y_{ij}=
\begin{cases}
  q^{a_i}\binom{a_i+a_j-2}{a_j-2}_q, & i < m\\
  q^{kn}\binom{n+a_j-k-2}{a_j-k-1}_q, & i=m.
\end{cases}
$$
对每个 $1\leq i\leq m$ 用 $a_i-1$ 代替 $a_i$ 得到 $Y$ 为
$$
y_{ij}=
\begin{cases}
  q^{a_i+1}\binom{a_i+a_j}{a_j-1}_q, & i < m\\
  q^{kn}\binom{a_m+a_j-k}{a_j-k}_q, & i=m
\end{cases}
$$
这时 $1\leq a_1<\cdots< a_{m-1}< a_m=n-1$，从而 $Y$ 的左上角 $m-1$ 阶矩阵来自 $H_{n-1}$ 的左上角 $n-2$ 阶子矩阵的主子式，$Y$ 的最后一行和最后一列分别来自固定的向量，因此要说明对所有 $\det Y$ 求和等于 $\det H_{k,n-1}$，我们只需要一个与之前稍有不同的线性代数结论：

{% blockquote %}

**引理 2**：设 $A$ 是一个 $n-1$ 阶方阵，$D_{n-1}$ 是前 $n-2$ 个对角元为 1，其余元素均为 0 的 $n$ 阶对角矩阵，则
$$
\det(D_{n-1}+A)=\sum_{1\leq a_1<\cdots< a_{m-1}\leq n-2}\det A[a_1\cdots a_{m-1}|n-1],
$$ 这里求和项跑遍由 $A$ 的第 $\{a_1,\ldots,a_{m-1},n-1\}$ 行和同样下标的列组成的 $m$ 阶主子式。
{% endblockquote %}

这就完成了定理的证明。


# Mills, Robbins, Rumsey 的巧妙想法


记 $h_n=\det(I_n+H_n)$ 为 ${\rm dpp}(n+1)$ 的 $q-$ 计数，$h_{kn}=\det H_{kn}$ 是其中 $n+1$ 恰好出现 $k(0\leq k\leq n)$ 次的 $q-$ 计数，则 $\sum_{k=0}^n h_{kn}=h_n$。特别地 $h_{0n}$ 是 $n+1$ 出现 0 次的 $q-$ 计数，因而等于 ${\rm dpp}(n)$ 的 $q-$ 计数，即 $h_{0n}=h_{n-1}$。总之我们有一个三角形的二维数组，其每一行的和等于下一行的首元素。

| ${\rm dpp}(n+1)$ | $h_n$ | $h_{0n}$ | $h_{1n}$ |$h_{2n}$ |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| $n=0$ | $h_0$ | $1$ |$\phantom{}$|$\phantom{}$ |
| $n=1$ | $h_1$ | $1$| $q^2$ | $\phantom{}$|
| $n=2$ | $h_2$ | $1+q^2$ | $q^3+q^4+q^5$ | $q^6+q^8$|

> 注意 $H_{kn}$，$h_{kn}$ 这些记号来自 $n$ 阶矩阵，但它们对应的都是 ${\rm dpp}(n+1)$ 中的分拆。

由于 $I_n+H_n$ 和所有的 $\{H_{kn},k=0,\ldots,n\}$ 的前 $n-1$ 行都相同，仅最后一行不同，所以它们最后一行有共同的代数余子式，设列向量 $C=(c_1,\ldots,c_n)^{T}$ 为它们最后一行元素对应的代数余子式，$R_k$ 是 $H_{kn}$ 的最后一行，则 $R_k\cdot C=\det H_{kn}=h_{kn}$。于是设 $R$ 是由 $R_1,\ldots,R_n$ 为行向量排成的 $n\times n$ 矩阵 (不含 $k=0$)，则
$$
RC = \begin{pmatrix}h_{1n}\\h_{2n}\\\vdots\\h_{nn}\end{pmatrix}.
$$
**注意到 $R$ 是一个对角线上都是 1 的上三角矩阵** (在[前面定理](#theorem-Hkn)中对 $n+1$ 的情形依次令 $k=1,\ldots,n$)，所以 $R$ 是可逆的，从而
$$
C = R^{-1}\begin{pmatrix}h_{1n}\\h_{2n}\\\vdots\\h_{nn}\end{pmatrix}.
$$
另一方面对矩阵 $H_{0n}$，其最后一行 $R_0$ 满足 $R_0\cdot C=\det H_{0n}=h_{0n}$，而其它的任何行与 $C$ 的内积是 0，所以
$$
H_{0n}C=\begin{pmatrix}0\\0\\\vdots\\h_{0n}\end{pmatrix}=
h_{0n}\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}.
$$
于是
$$
RH_{0n}R^{-1}\begin{pmatrix}h_{1n}\\h_{2n}\\\vdots\\h_{nn}\end{pmatrix}=
RH_{0n}C=
h_{0n}R\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}.
$$
记 $A_n=RH_{0n}R^{-1}$，
$$
V_n=R\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix},
$$
则我们有
$$
\begin{equation}
A_n\begin{pmatrix}h_{1n}\\h_{2n}\\\vdots\\h_{nn}\end{pmatrix}=h_{0n}V_n.
\end{equation}
$$

到目前为止这些都是寻常的线性代数操作，并无出彩之处。Mills 等人的第一个想法是：上式中给出的递推关系，加上我们已知的初始条件 $h_1=1+q^2$，是否能够唯一确定序列 $\{h_{kn}\}$？这就是下面的引理：

<div id="lemma3">
{% blockquote %}

**引理 3**：如果序列 $\{b_{kn},n\geq1,0\leq k\leq n\}$ 满足

1. 初始条件 $b_1=h_1$。
2. 每一行的和等于下一行的首元素，即对任何 $n\geq1$ 有 $\sum_{k=0}^nb_{kn}=b_n=b_{0,n+1}$ 成立。
3. 设 $A_n,V_n$ 如前，且
$$A_n\begin{pmatrix}b_{1n}\\b_{2n}\\\vdots\\b_{nn}\end{pmatrix}=b_{0n}V_n.$$

则对任何 $k,n$ 都有 $b_{kn}=h_{kn}$ 成立。
{% endblockquote %}
</div>

**证明**：对 $n$ 归纳，$b_1=h_1$ 是已知的，设 $b_i=h_i$ 对所有 $i<n$ 成立，则 $b_{0n}=h_{0n}$，于是 $(b_{1n},\ldots,b_{nn})^T$ 和 $(h_{1n},\ldots,h_{nn})^T$ 都是线性方程组 $A_nX=h_{0n}V_n$的解，由于 $A_n$ 是可逆矩阵，此方程组有唯一解，从而 $b_{kn}=h_{kn}$ 对任何 $k,n$ 成立。

所以如果我们能构造出一个满足引理中三个条件的序列来，那么它必然就是我们要求的 $\{h_{kn}\}$。怎么构造好呢？看起来 $b_{0n}$ 孤零零地放在右边，这不美观啊？可不可以把它和 $b_{1n},\ldots,b_{nn}$ 放在一起呢？这就是 Mills 等人接下来的精彩操作了：记
$$
K_n=\begin{pmatrix}\ast&\ast\\V_n&I_n-A_n\end{pmatrix}.
$$
注意 $K_n$ 是一个 $n+1$ 阶的矩阵，$\ast$ 位置是 $K_n$ 的第一行，暂时不确定是什么，但是不管 $\ast$ 是什么，$K_n$ 都满足
$$K_n\begin{pmatrix}h_{0n}\\h_{1n}\\\vdots\\h_{nn}\end{pmatrix}=
  \begin{pmatrix}\ast\\h_{1n}\\\vdots\\h_{nn}\end{pmatrix}.
$$
哎呦，这不很像一个特征值是 1 的特征向量嘛？所以如果我们能在 $K_n$ 中适当填入 $\ast$ 位置的元素，并找到 $K_n$ 的**任何一个**特征值是 1 的特征向量 $v_n=(v_{0n},\ldots,v_{nn})^T$，则
$$
\begin{pmatrix}v_{0n}\\v_{1n}\\\vdots\\v_{nn}\end{pmatrix}=
K_n\begin{pmatrix}v_{0n}\\v_{1n}\\\vdots\\v_{nn}\end{pmatrix}=
\begin{pmatrix}
v_{0n}\\v_{0n}V_n+(I_n-A_n)\begin{pmatrix}v_{1n}\\\vdots\\v_{nn}\end{pmatrix}
\end{pmatrix}.
$$
即
$$
A_n\begin{pmatrix}v_{1n}\\\vdots\\v_{nn}\end{pmatrix}=v_{0n}V_n.
$$
从而取 $b_1=h_1=1+q^2$，$b_{01}=h_{01}=1$，$b_{11}=h_{11}=q^2$，并假设对任何 $i<n$ 已经得到了 $b_i$ 和 $b_{ki}(0\leq k\leq i)$ 的值，定义 $b_{kn}=\dfrac{b_{n-1}}{v_{0n}}v_{kn}$ 和 $b_n=\sum_{k=0}^nb_{kn}$，则不难验证 $\{b_{kn}\}$ 满足[引理 3](#lemma3) 的条件，从而必然等于 $\{h_{kn}\}$，这样就得到了 DPP 的 $q-$ 计数。

Mills 等人算出了 $I_n-A_n$ 和 $V_n$：
$$
\begin{align*}
I_n-A_n&=\left((-1)^{j}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\binom{2n-i}{n-i-j}_q\right)_{1\leq i,j\leq n},\\
V_n&=\left(q^{k(n+1)}\binom{2n-k}{n-k}_q\right)^T_{1\leq k\leq n}.
\end{align*}
$$
如果要把 $I_n-A_n$ 填入 $K_n$ 的右下角 $n\times n$ 的位置，那么 $K_n$ 的其它位置应该是什么呢？注意到如果在 $I_n-A_n$ 的表达式中令下标 $j=0$，则得到的列向量正是 $V_n$，那 $K_n$ 是什么已经呼之欲出了：它应该是把 $I_n-A_n$ 中的 $i,j$ 下标各自扩展到 0 后得到的 $n+1$ 阶方阵，即
$$
K_n=\left((-1)^{j}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\binom{2n-i}{n-i-j}_q\right)_{0\leq i,j\leq n}.
$$
于是 $V_n$ 正好位于 $K_n$ 的左下方，$I_n-A_n$ 正好位于 $K_n$ 的右下方。

**这一步即为 Mills 等人的“信仰一跃”**。

然而看到 $K_n$ 的表达式还是不免让人倒吸一口凉气，这么复杂的矩阵，Mills 等人是怎么猜出它的特征值是 1 的特征向量来的呢？

我们之前说过，Mills 等人研究 DPP 的目的是为了解决 ASM 的计数。他们正确的猜出了 ${\rm ASM}(n)$ 中第一行的 1 恰好出现在第 $1\leq k\leq n$ 列的 ASM 个数为
$$
|A_{n,k}|=\binom{n+k-2}{k-1}\frac{(2n-k-1)!}{(n-k)!}\prod_{j=0}^{n-2}\frac{(3j+1)!}{(n+j)!}.
$$
而且他们直觉认为这就是 ${\rm dpp}(n)$ 中恰好含有 $k-1$ 个 $n$ 的 DPP 的个数，即 $h_{k-1,n-1}$，所以他们猜测特征向量 $v_n$ 的第 $k$ 个分量 $v_{kn}$ 应该形如
$$
q^{\text{some power}}\times\binom{n+k}{k}_q\binom{2n-k}{n-k}_q.
$$
经过试验以后他们发现取
$$
v_{kn}=q^{k(n+1)}\binom{n+k}{k}_q\binom{2n-k}{n-k}_q
$$
即可。**这一步即为 Mills 等人的“灵魂一猜”**。

不难验证 $v_{0n}=\binom{2n}{n}_q$ 和 $\sum_{k=0}^nv_{kn}=\binom{3n+1}{n}_q$，所以如前所述记 $b_{kn}=b_{n-1}\dfrac{v_{0n}}{v_{kn}}$，则
$$
b_n=\sum_{k=0}^nb_{kn}=b_{n-1}\frac{\sum_{k=0}^nv_{kn}}{v_{0n}}=b_{n-1}\frac{\binom{3n+1}{n}_q}{\binom{2n}{n}_q}.
$$
此即为序列 $\{b_n\}$ 满足的递推关系。再结合
$$
b_1=h_1=1+q^2=\frac{1-q^4}{1-q^2}=\frac{\binom{3+1}{1}_q}{\binom{2}{1}_q},
$$ 我们就算出了 ${\rm dpp}(n+1)$ 的 $q-$ 计数为
$$
h_n=b_n=\prod_{k=1}^n\frac{\binom{3k+1}{k}_q}{\binom{2k}{k}_q}=\prod_{1\leq i\leq j\leq n+1}\frac{1-q^{n+i+j}}{1-q^{2i+j-1}}.
$$

{% blockquote %}
**注**：我们来验证一下连乘积 $\prod\limits_{k=1}^n\dfrac{\binom{3k+1}{k}_q}{\binom{2k}{k}_q}$ 确实等于 Andrews 猜想中给出的表达式
$$\prod\limits_{1\leq i\leq j\leq n+1}\frac{1-q^{n+i+j}}{1-q^{2i+j-1}}.$$
过程并不复杂，只是一些下标的变换而已。记
$$
\prod_{1\leq i\leq j\leq n+1}\frac{1-q^{n+i+j}}{1-q^{2i+j-1}} = \frac{x_{n+1}}{y_{n+1}},
$$
则 $y_{n+1}=y_n\prod\limits_{i=1}^{n+1}(1-q^{2i+n})$，分离分子中 $j=n+1$ 的部分有
$$
\begin{align*}
x_{n+1}&=\prod_{i=1}^n\prod_{j=i}^n(1-q^{n+i+j})\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\\
&=\prod_{i=1}^{n-1}\prod_{j=i}^n(1-q^{n+i+j})\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\cdot (1-q^{3n})\\
&=\prod_{i=2}^n\prod_{j=i-1}^n(1-q^{n+i+j-1})\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\cdot (1-q^{3n})\\
&=\prod_{i=2}^n\prod_{j=i}^n(1-q^{n+i+j-1})\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\prod_{i=2}^n(1-q^{n+2i-2})\cdot (1-q^{3n})\\
&=\prod_{i=2}^n\prod_{j=i}^n(1-q^{n+i+j-1})\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\prod_{i=1}^{n}(1-q^{n+2i})\\
&=x_n\cdot \prod_{i=1}^{n+1}(1-q^{2n+i+1})\prod_{i=1}^{n}(1-q^{n+2i})/\prod_{j=1}^n(1-q^{n+j}).
\end{align*}
$$
所以
$$
\frac{x_{n+1}}{y_{n+1}}=\frac{x_n}{y_n}\cdot\frac{\prod_{i=1}^{n+1}(1-q^{2n+i+1})\prod_{i=1}^{n}(1-q^{n+2i})}{\prod_{j=1}^n(1-q^{n+j})\prod_{i=1}^{n+1}(1-q^{2i+n})}=\frac{\binom{3n+1}{n}_q}{\binom{2n}{n}_q}.
$$
{% endblockquote %}


# 详细计算步骤


下面进入“小心求证”的部分，这里主要的工具是前面的 Gauss 二项式[定理 1](binom-theorem1) 和[定理 2](binom-theorem2)。我们要计算 $I_n-A_n=I_n-RH_{0n}R^{-1}$，为此需要先计算 $R^{-1}$。

## 计算 $R^{-1}$

从[定理 4](#theorem-Hkn) 可知
$$
R=\left(q^{i(n+1)}\binom{n+j-i}{j-i}_q\right)_{1\leq i,j\leq n}.
$$
利用 $\prod_{k=0}^n(1-xq^k)\cdot\prod_{k=0}^n\dfrac{1}{(1-xq^k)}=1$ 得到 $$
\left(\sum_{k=0}^{n+1}(-1)^kq^{\binom{k}{2}}\binom{n+1}{k}_qx^k\right)
\left(\sum_{l=0}^\infty\binom{n+l}{l}_qx^l\right)=1.
$$
对 $1\leq i,j\leq n$，比较两边 $x^{j-i}$ 项的系数，右边显然是 $\delta_{ij}$，左边取第一个因子的 $x^{k-i}$ 项系数，取第二个因子的 $x^{j-k}$ 项系数并对 $k$ 求和，有
$$
\sum_{i\leq k\leq j}(-1)^{k-i}q^{\binom{k-i}{2}}\binom{n+1}{k-i}_q
\binom{n+j-k}{j-k}_q =\delta_{ij}.
$$
采用之前 $\binom{a}{-m}_q=0$ 的约定的话，上式可以写成
$$
\sum_{1\leq k\leq n}(-1)^{k-i}q^{\binom{k-i}{2}}\binom{n+1}{k-i}_q
\binom{n+j-k}{j-k}_q=\delta_{ij}.
$$
这说明 $\left((-1)^{j-i}q^{\binom{j-i}{2}}\binom{n+1}{j-i}_q\right)_{1\leq i,j\leq n}$ 和 $\left(\binom{n+j-i}{j-i}_q\right)_{1\leq i,j\leq n}$ 互为逆矩阵。而后者与 $R$ 的第 $i$ 行相差 $q^{i(n+1)}$ 的因子，所以给前者的第 $j$ 列补上 $q^{-j(n+1)}$ 的因子便可得到
$$
R^{-1}=\left((-1)^{j-i}q^{\binom{j-i}{2}}q^{-j(n+1)}\binom{n+1}{j-i}_q\right)_{1\leq i,j\leq n}.
$$

## 计算 $RH_{0n}R^{-1}$

记 $H_n^\ast$ 是与 $H_n$ 的前 $n-1$ 行全相同，但是最后一行全是 0 的矩阵，则 $H_{0n}=I_n+H_n^\ast$，于是 $RH_{0n}R^{-1}=I_n+RH_n^\ast R^{-1}$，所以只要计算 $RH_n^\ast R^{-1}$ 即可。

首先由于 $H_n^\ast$ 的最后一行是 0，所以 $H_n^\ast R^{-1}$ 的最后一行也是 0，其它行的 $(i,j)$ 分量为当 $i<n$ 时为
$$
\sum_{k=1}^n(H_n^*)_{ik}(R^{-1})_{kj}=
q^{i+1-j(n+1)}\sum_{k=1}^n(-1)^{j-k}q^{\binom{j-k}{2}}\binom{i+k}{k-1}_q\binom{n+1}{j-k}_q.
$$
用 Gauss 二项式定理展开
$$\prod_{l=0}^n(1-xq^l)\cdot\prod_{l=0}^{i+1}\frac{1}{1-xq^l}=\prod_{l=i+2}^n(1-xq^l)$$
左边第一个因子的 $x^{j-k}$ 项系数为 $(-1)^{j-k}q^{\binom{j-k}{2}}\binom{n+1}{j-k}_q$，第二个因子中 $x^{k-1}$ 项系数为 $\binom{i+k}{k-1}_q$，相乘并对 $k$ 求和后是右边 $x^{j-1}$ 项系数，利用代换 $z=xq^{i+2}$ 不难得出此系数为
$$
(-1)^{j-1}q^{(i+2)(j-1)}q^{\binom{j-1}{2}}\binom{n-i-1}{j-1}_q.
$$
于是
$$
\begin{align*}
\sum_{k=1}^n(H_n^*)_{ik}(R^{-1})_{kj}&=q^{i+1-j(n+1)}q^{(i+2)(j-1)}(-1)^{j-1}q^{\binom{j-1}{2}}\binom{n-i-1}{j-1}_q\\
&=q^{ij-jn}(-1)^{j-1}q^{\binom{j}{2}}\binom{n-i-1}{j-1}_q.
\end{align*}
$$
即
$$
H_n^*R^{-1}=\left(
  q^{ij-jn}(-1)^{j-1}q^{\binom{j}{2}}\binom{n-i-1}{j-1}_q
  \right)_{1\leq i,j\leq n}.
$$
如果约定 $\binom{-a}{m}_q=0$ 的话我们可以把 $H_n^*R^{-1}$ 最后一行都是 0 也统一到上面的表达式中。

继续
$$\sum_{k=1}^n(R)_{ik}(H_n^*R^{-1})_{kj}=\sum_{k=1}^nq^{i(n+1)}
\binom{n+k-i}{k-i}_qq^{kj-jn}(-1)^{j-1}q^{\binom{j}{2}}\binom{n-k-1}{j-1}_q.$$
把右边与 $k$ 无关的项提出来，得到其等于 $$(-1)^{j-1}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\sum_{k=1}^n q^{(k-i)j}
\binom{n+k-i}{k-i}_q\binom{n-k-1}{j-1}_q.
$$
把 $\binom{n-k-1}{j-1}_q$ 改写为 $\binom{j-1+(n-k-j)}{n-k-j}_q$，可以将其进一步化为
$$
(-1)^{j-1}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\sum_{k=1}^n q^{(k-i)j}
\binom{n+k-i}{k-i}_q\binom{j-1+(n-k-j)}{n-k-j}_q.
$$
注意 $\binom{j-1+(n-k-j)}{n-k-j}_q$ 是 $\prod\limits_{l=0}^{j-1}\frac{1}{1-xq^l}$ 中 $x^{n-k-j}$ 项的系数，$q^{(k-i)j}\binom{n+k-i}{k-i}_q$ 是 $\prod\limits_{l=j}^{n+j}\frac{1}{1-xq^l}$ 中 $x^{k-i}$ 项的系数，二者相乘并对 $k$ 求和得到的是 $\prod\limits_{l=0}^{n+j}\frac{1}{1-xq^l}$ 中 $x^{n-i-j}$ 项的系数，即 $\binom{2n-i}{n-i-j}_q$，于是
$$
RH_n^*R^{-1}=\left(
  (-1)^{j-1}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\binom{2n-i}{n-i-j}_q
  \right)_{1\leq i,j\leq n}.
$$
从而
$$
I_n-A_n=-RH_n^*R^{-1}=\left(
  (-1)^{j}q^{(i-j)(n+1)+ij}q^{\binom{j+1}{2}}\binom{2n-i}{n-i-j}_q
  \right)_{1\leq i,j\leq n}.
$$

## 得到 $V_n$

列向量 $V_n$ 比较好求，它就是 $R$ 的最后一列，也就是分别取出 $H_{1n},\ldots,H_{nn}$ 最右下角元素后排成的列向量，即
$$
V_n=\left(q^{k(n+1)}\binom{2n-k}{n-k}_q\right)^T_{1\leq k\leq n}.
$$

## 验证 $v_n$ 是 $K_n$ 的特征向量

我们来验证 $\left(q^{k(n+1)}\binom{n+k}{k}_q\binom{2n-k}{n-k}_q\right)_{0\leq k\leq n}$ 是 $K_n$ 的特征向量。
$$
\sum_{k=0}^n(K_n)_{ik}v_{kn}=\sum_{k=0}^n(-1)^{k}q^{i(n+1)+ik}q^{\binom{k+1}{2}}
\binom{2n-i}{n-i-k}_q
\binom{n+k}{k}_q
\binom{2n-k}{n-k}_q.
$$
利用 Gauss 二项式的定义不难验证
$$
\binom{2n-i}{n-i-k}_q\binom{n+k}{k}_q=\binom{2n-i}{n-i}_q\binom{n-i}{k}_q.
$$
所以
$$
\sum_{k=0}^n(K_n)_{ik}v_{kn}=q^{i(n+1)}\binom{2n-i}{n-i}_q
\sum_{k=0}^n(-1)^{k}q^{ik}q^{\binom{k+1}{2}}\binom{n-i}{k}_q\binom{2n-k}{n-k}_q.
$$
所以要证明 $\sum_{k=0}^n(K_n)_{ik}v_{kn}=v_{in}$，只要再证明
$$
\sum_{k=0}^n(-1)^{k}q^{ik}q^{\binom{k+1}{2}}\binom{n-i}{k}_q
\binom{2n-k}{n-k}_q=\binom{n+i}{i}_q.
$$
实际上右边是 $\prod\limits_{l=0}^i\dfrac{1}{1-xq^l}$ 中 $x^n$ 项的系数，而
$$
\prod\limits_{l=0}^i\dfrac{1}{1-xq^l} =\left(
\prod\limits_{l=i+1}^n(1-xq^l)
\right) \left(\prod\limits_{l=0}^n\dfrac{1}{1-xq^l}\right).
$$
取第一个因子的 $x^k$ 项系数，第二个因子的 $x^{n-k}$ 项系数相乘并对 $k$ 求和即为所求等式。

## 验证 $\sum\limits_{k=0}^nv_{kn}=\binom{3n+1}{n}_q$

最后我们来验证
$$
\sum\limits_{k=0}^nv_{kn}=\sum\limits_{k=0}^nq^{k(n+1)}\binom{n+k}{k}_q\binom{2n-k}{n-k}_q=\binom{3n+1}{n}_q.
$$
只要比较
$$
\left(\prod_{l=0}^n\frac{1}{1-xq^l}\right)\left(\prod_{l=n+1}^{2n+1}\frac{1}{1-xq^l}\right)=\left(\prod_{l=0}^{2n+1}\frac{1}{1-xq^l}\right)
$$
两边 $x^n$ 项的系数，取左边第一个因子的 $x^k$ 项系数，第二个因子的 $x^{n-k}$ 系数并对 $k$ 求和即得。


[^1]: W. H. Mills, D. H. Robbins and H. Rumsey, Alternating sign matrices and descending plane partitions, J. Combin. Theory Ser. A34(1983), 340–359.

[^2]: Aigner, Martin; Ziegler, Günter (2009). Proofs from THE BOOK (4th ed.). Berlin, New York: Springer-Verlag.