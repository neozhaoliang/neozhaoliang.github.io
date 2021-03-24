---
title: "Schur 多项式，Littlewood-Richardson rule 与 Hook 长度公式"
categories: ["计数组合学"]
tags:
  - Schur polynomial
  - Young tableaux
  - Hook length formula
  - Littlewood-Richardson rule
date: 2011-04-04
url: "schur-polynomials-and-hook-length-formula"
---

在数学中有那么一些问题，它们的表述简单而初等，但是解决起来却非常困难，往往需要相当的奇思妙想和深刻的工具，而且围绕这个问题许多不同领域的数学交织在一起，演绎出许多奇妙的故事来。

Young 表就是其中一个精彩的例子，组合数学，表示论，概率论在这里发生了奇妙的交汇。

我们先从两个有趣的问题开始：

{% blockquote %}
**问题 1**：$n$ 位选民要在一次选举中依次走到投票箱前给 $m$ 个候选人投票，每个选民只能投一票。已知第 $i$ 位候选人最终的得票数为 $\lambda_i$，这里 $\sum_{i=1}^m\lambda_i=n$ 且 $\lambda_1\geq\cdots\geq\lambda_m$。问题是：这 $n$ 个选民有多少种不同的投票顺序，使得在投票过程中的任一时刻，对任何的 $i<j$，第 $i$ 位候选人的得票数总不少于第 $j$ 位候选人的得票数？
{% endblockquote %}

{% blockquote %}
**问题 2**：在一个体积为 $a\times b\times c$ 的房间中堆箱子，堆放的方式要满足递降的条件：从墙角的那一摞开始，每一行从左到右，每一列从上到下，箱子的高度是弱递减的。问： 有多少种满足要求的方法？
<img style="margin:0px auto;display:block" width=400 src="/images/schur/planepartition.png"/>
{% endblockquote %}

这两个问题的表述很简单，但其实答案相当复杂，绝非一般的初等方法所能解决。对付它的最好方法是 Schur 多项式的理论，我接下来就来介绍它。

<!-- more -->

# Schur 多项式：组合定义


设 $\lambda=(\lambda_1,\lambda_2,\ldots)$ 是一个元素都是非负整数且只有有限多项非 0 的序列，如果有 $\lambda_1\geq \lambda_2\geq\cdots$ 成立，就称 $\lambda$ 是一个整数分拆，简称分拆，并记 $|\lambda|=\sum\limits_{i=1}^\infty \lambda_i$。$|\lambda|$ 总是一个有限的数，如果 $|\lambda|=n$ 就称 $\lambda$ 是整数 $n$ 的分拆，记作 $\lambda\vdash n$。此外用 $l(\lambda)$ 表示 $\lambda$ 中非零项的个数。

对每个分拆 $\lambda$，我们可以用一个图 $F_\lambda$ 来表示它：$F_\lambda$ 由 $n$ 个方格组成，第一行有 $\lambda_1$ 个方格，第二行有 $\lambda_2$ 个方格，. . . 以此类推，每一行都是左对齐的，总共有 $l(\lambda)$ 行。$F_\lambda$ 叫做 $\lambda$ 的 Ferrers 图。例如下图是分拆 $\lambda=(4, 2, 2, 1)$ 的 Ferrers 图。

|||||
|:-:|:-:|:-:|:-:|
|$\phantom{}$|$\phantom{}$|$\phantom{}$|$\phantom{}$|
|$\phantom{}$|$\phantom{}$|||
|$\phantom{}$|$\phantom{}$|||
|$\phantom{}$||||

将任何分拆 $\lambda$ 的 Ferres 图 $F^\lambda$ 转置 (第一行变第一列，第二行变第二列，等等) 后得到的也是一个 Ferres 图，其对应的分拆 $\lambda'$ 叫做 $\lambda$ 的共轭分拆，例如上图转置后得到的共轭分拆为 $\lambda'=(4, 3, 1, 1)$：

|   |   |   |   |
|:-:|:-:|:-:|:-:|
|$\phantom{}$|$\phantom{}$|$\phantom{}$|$\phantom{}$|
|$\phantom{}$|$\phantom{}$|$\phantom{}$||
|$\phantom{}$||||
|$\phantom{}$||||


在 Ferrers 图的每个方格中填入正整数，使得**每一行从左到右是弱递增的**，**每一列从上到下是严格递增的**，这样得到的表格叫做半标准 Young 表 (SSYT)；如果一个形状为 $\lambda\vdash n$ 的半标准的 Young 表包含的数字恰好为集合 $\{1,2,\ldots,n\}$，则称其为一个标准 Young 表 (SYT)。标准 Young 表由于其中的数字互不相同所以也是行严格递增的。例如下图分别显示的是形状为 $\lambda=(4, 3, 2,1)$ 的一个半标准和一个标准 Young 表。

|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 1  | 1  | 2  | 2  |
| 3  | 3  | 8  ||
| 4  | 6  |||
| 5  ||||


|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 1  | 3  | 6  | 10  |
| 2  | 5  | 7
| 4  | 9
| 8

文章开头的投票序列问题本质上是计算给定形状为 $\lambda=(\lambda_1,\ldots,\lambda_m)$，且填入的数字为集合 $\{1,\ldots,n\}$ 的标准 Young 表的个数 (这是个思考题，想一想，为什么？)。怎么办呢？方法是我们都熟悉的生成函数方法：给每个半标准的 Young 表赋以一个权值，这个权值是一个含有不定元的单项式，把它们的权值加起来，得到一个多变元多项式，这个多项式也叫做权函数。如果我们能找到权函数满足的递推关系并把它解出来，自然就求出了半标准 Young 表的个数。

把上面的想法付诸实践：设 $T$ 是一个半标准 Young 表，记向量 $w(T)=(w_1,w_2,\ldots)$，其中 $w_k$ 是 $T$ 中数字 $k$ 的个数。向量 $w(T)$ 叫做 $T$ 的权。我们采用这样的约定：如果 $\alpha=(\alpha_1,\alpha_2,\ldots)$ 是一个元素都是非负整数的序列，且只有有限多项非 0，则记
$$X^\alpha = x_1^{\alpha_1}x_2^{\alpha_2}\cdots.$$
显然 $X^\alpha$ 是一个次数有限的单项式。

例如上面的半标准 Young 表


|   |   |   |   |
|:-:|:-:|:-:|:-:|
| 1  | 1  | 2  | 2  |
| 3  | 3  | 8
| 4  | 6
| 5

的权向量为 $(2, 2, 2, 1, 1, 1, 0, 1, 0, \ldots)$ (后面都是 0)，其对应的单项式为
$$X^{w(T)} = x_1^2x_2^2x_3^2x_4x_5x_6x_8.$$

{% blockquote %}
**Schur 多项式的组合定义**：设 $\lambda$ 是一个分拆，定义关于无穷多个变元 $\{x_n\}_{n=1}^\infty$ 的多项式
$$s_\lambda(x_1,\ldots,x_n,\ldots)=\sum_{T}X^{w(T)}.$$
这里 $T$ 跑遍所有将正整数集填入 $F_\lambda$ 得到的半标准 Young 表。
{% endblockquote %}

注意这里定义的 Schur 多项式包含无穷多个单项式，每个单项式的次数都是 $|\lambda|$，每个单项式前面的系数都是有限的。

在计算具体问题时，往往对填入 Young 表的数字有所限制，比如只允许填入 $\{1,2,\ldots,n\}$ 中的数字。由于填法只有有限多种，所以这时得到的 Schur 多项式是一个关于 $x_1,\ldots,x_n$ 的多元多项式。

Schur 多项式的组合定义是最容易被理解和接受的，但我们对它具体是个什么东西还完全没有概念，为此我们需要找到 Schur 多项式的其它表现形式。首先我们将证明 Schur 多项式总是对称多项式。


# Bender-Knuth 对合


这一节我们来证明 Schur 多项式是对称多项式，为此只要证明对任意的 $i$，$s_\lambda$ 在交换 $x_i$ 和 $x_{i+1}$ 后保持不变即可，而这又只要说明权为 $(\ldots,w_i,w_{i+1},\ldots)$ 的半标准 Young 表与权为 $(\ldots,w_{i+1},w_i,\ldots)$ 的半标准 Young 表一一对应即可。为此只要对每个形状为 $\lambda$ 的 Young 表，把其中的数字 $i$ 全换成 $i+1$，同时把 $i+1$ 全换成 $i$ 就可以了，是吗？

问题出在这样得到的未必还是一个半标准的 Young 表。如果某个 $i$ 的下方恰好是 $i+1$，就称这样的 $i$ 和 $i+1$ 是匹配了的。而那些下方没有 $i+1$ 的 $i$ 或者上方没有 $i$ 的 $i+1$ 统称为未匹配的。下面的事实不难验证：

> 在 $T$ 的任意一行中，设 $x,y\in\{i,i+1\}$ 是两个未匹配的元素，则它们中间不可能有匹配的元素。即在一行中，未匹配的元素总是构成一段连续的序列。

下图中演示了 $i=2$ 的例子，绿色显示了匹配的元素，红色显示了未匹配的元素。

|   |   |   |   |  | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1  | 1  | 1  | 1 | 1  | 1 | <font color="green">2</font> |
|<font color="green">2</font>| <font color="red">2</font>  | <font color="red">2</font>  | <font color="red">2</font> | <font color="red">3</font>  | <font color="red">3</font> | <font color="green">3</font> |
| <font color="green">3</font>  | 4  | 4 |
| 4|


设在一行中，未匹配的元素是 $r$ 个 $i$ 后面接着 $s$ 个 $i+1$，我们把这段序列替换为 $s$ 个 $i$ 后面接上 $r$ 个 $i+1$，对 $T$ 的每一行都进行这个操作而保持 $T$ 的其它数字不动。在这个变换下 $T$ 变成 $T^\ast$，$T^\ast$ 仍然是半标准的：上图 $T$ 是 3 个 2 后面跟了 2 个 3，变换后在 $T^\ast$ 中变成了 2 个 2 后面跟了 3 个 3：

|   |   |   |   |  | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1  | 1  | 1  | 1 | 1  | 1 | <font color="green">2</font> |
|<font color="green">2</font>| <font color="red">2</font>  | <font color="red">2</font>  | <font color="red">3</font> | <font color="red">3</font>  | <font color="red">3</font> | <font color="green">3</font> |
| <font color="green">3</font>  | 4  | 4 |
| 4 |

容易验证若 $T$ 的权为 $(\ldots,w_i,w_{i+1},\ldots)$，则 $T^\ast$ 的权为 $(\ldots,w_{i+1},w_i,\ldots)$。这个变换显然是个对合：$(T^\ast)^\ast=T$，这就证明了 Schur 多项式是对称的。


# Jacobi-Trudi 恒等式


定义 $h_k(x_1,\ldots,x_n,\ldots)$ 为所有 $k$ 次单项式的和：
$$h_k(x_1,\ldots,x_n,\ldots)=\sum_{\begin{subarray}{c}\alpha_1+\alpha_2+\cdots=k\\\alpha_i\in\mathbb{Z}_{\geq0}\end{subarray}} x_1^{\alpha_1}x_2^{\alpha_2}\cdots.$$

这里约定 $h_0=1$，$k<0$ 时 $h_{k}=0$。显然每个 $h_k$ 是齐次的对称多项式。

{% blockquote %}
**定理**：设 $\lambda=(\lambda_1,\ldots,\lambda_n)\in\mathbb{Z}^n_{\geq0}$ 为一个分拆，则
$$s_\lambda=\det\left( h_{\lambda_i-i+j}\right)_{1\leq i,j\leq n}.$$
{% endblockquote %}

这里的证明采用 Gessel-Viennot 的不相交格点路径组方法，思路一目了然，论证简单直接。关于这个方法你可以参考我之前的[一篇博文](/macmahon-formula-plane-partitions)。当然，《Proofs from The Book》一书中的格点路径组一章也是极好的介绍。

关键是要**把每个半标准 Young 表对应到一个不相交的路径组**，如果你熟悉格点路径组方法的话，这个构造过程是很自然的。

下面的动图显示了 $\lambda=(5,4,3,2)$ 时的一个形状为 $\lambda$ 的 Young 表


|   |   |   |   | |
|:-:|:-:|:-:|:-:|:-:|
| 1  | 1  | 1  | 1  | 2  |
| 2  | 2  | 3  | 3  |
| 3  | 4  | 4  |
| 4  | 5  |

与其不相交路径组的对应关系：

<img style="margin:0px auto;display:block" width="600" src="/images/schur/jacobi-trudi.gif"/>


设 $T$ 是一个形状为 $\lambda$ 的半标准 Young 表，则 $T$ 的第 $i$ 行是一个长度为 $\lambda_i$ 的弱递增的数列，这样一个数列很自然地对应于一条从点 $(0,1)$ 到点 $(\lambda_i,+\infty)$ 的 Gauss 路径，这个路径即为这一行的“高度图”。

但是半标准 Young 表的列是严格递增的，这个递减关系反映在 Gauss 路径上，就是 $T$ 的第二行对应的路径应该整体位于第一行对应路径的上方，第三行对应的路径整体位于第二行对应的路径的上方，...，两条路径之间可以有垂直的公共边，但是不能有水平的公共边。

现在把第 $i$ 条路径水平地向左平移 $i$ 个单位，变成一条从 $(-i,1)$ 到 $(-i+\lambda_i,+\infty)$ 的路径，则这样得到的 $n$ 条路径两两之间没有公共点，即构成一个不相交的路径组。

反过来对每一个这样的不相交的路径组，也很容易得出其对应的半标准 Young 表来。

令水平线 $y=k$ 的权值为 $x_k$，垂直边的权值一律为 1，应用带权的 Gessel-Viennot 引理并注意任何两点之间的路径由于其横向长度是固定的所以其次数是固定的，而高度序列则可以任意变化，从而当路径变化时其权重之和是个齐次对称多项式 $h_k$，得到
$$s_\lambda=\det\left(h_{\lambda_i-i+j}\right)_{1\leq i,j\leq n}.$$
这就证明了 Jacobi-Trudi 恒等式。


# Bi-alternant 公式


在这一小节我们考虑的分拆 $\lambda=(\lambda_1,\ldots,\lambda_n),\mu=(\mu_1,\ldots,\mu_n)$ 以及 Young 表的权 $w(T)$ 都是 $\mathbb{Z}^n_{\geq0}$ 中的向量。

设 $T$ 是一个形状为 $\mu$ 的半标准 Young 表，用记号 $T_{\geq j}$ 表示由 $T$ 的第 $j,j+1,\ldots$ 列组成的半标准 Young 表，同理记号 $T_{>j}$ 和 $T_{<j}$ 的含义都是不言自明的。如果对任何 $j$，向量 $\lambda+w(T_{\geq j})$ 都是一个分拆，就称 $T$ 是一个“好” Young 表，否则就称 $T$ 是一个“坏” Young 表。

定义 Weyl 向量 $\rho=(n-1,n-2,\ldots,1,0)\in\mathbb{Z}^n_{\geq0}$。

定义如下的 $n$ 阶行列式：

$$a_\lambda=\det(x_i^{\lambda_j})=\sum_{\sigma\in S_n}\text{sgn}(\sigma)X^{\sigma(\lambda)}.$$

{% blockquote %}
**定理**：
$$a_{\lambda+\rho}s_{\mu}=\sum_{T}a_{\lambda+w(T)+\rho}.$$
这里求和跑遍那些形状为 $\mu$ 的好 Young 表。
{% endblockquote %}

注意两边都是关于 $n$ 个变元 $x_1,\ldots,x_n$ 的多项式。


这个定理乍看起来从叙述到证明都很不直观，不过它的结论却非常重要，这就是 Littlewood - Richardson 定律。下面这个证明有很深刻的来源 (李代数的晶体图)。见

> A Concise Proof of the Littlewood-Richardson Rule, by John R. Stembridge,

证明：由于 $s_\mu$ 是 $n$ 变元的对称多项式，因此利用定义不难验证

$$a_{\lambda+\rho}s_\mu =\sum_{T}a_{\lambda+w(T)+\rho},$$

这里 $T$ 跑遍所有形状为 $\mu$ 的半标准 Young 表。这里的关键之处在于，借助 Bender-Knuth 对合，我们可以把求和项中坏的 Young 表两两配对抵消掉，从而剩下的和项都是好 Young 表。

设 $T$ 是一个 坏 Young 表，则存在 $j$ 使得 $\lambda+w(T_{\geq j})$ 不是一个分拆，在所有这样的 $j$ 中，选取最大的那个。选好 $j$ 以后，由于 $\lambda+w(T_{\geq j})$ 不是分拆，因此存在 $k$ 使得
$$\lambda_k+w_k(T_{\geq j}) < \lambda_{k+1}+w_{k+1}(T_{\geq j}).$$
在所有这样的 $k$ 中，选取最小的那个。

{% blockquote %}
**断言**：在 $T_{>j}$ 中 $k$ 和 $k+1$ 的个数相同，且 $T$ 的第 $j$ 列有一个 $k+1$ 但是没有 $k$。
{% endblockquote %}

这里仔细解释一下：事情乍看起来有点复杂但是实际上很简单。为了让你理解清楚怎么回事，考虑这样的场景：$A,B$ 两人玩游戏，每局获胜的一方可得 1 元，输的一方得 0 元，打平则各得 1 元。初始时刻 $A$ 有 $\lambda_k$ 元，$B$ 有 $\lambda_{k+1}$ 元，这里 $\lambda_k\geq\lambda_{k+1}$。已知第 $m$ 局结束后 $B$ 的资金首次大于 $A$ 的资金，你能推断出什么？

很显然，第 $m$ 局的结果必然是 $B$ 获胜了；不仅如此，前 $m-1$ 局结束的时候 $B$ 的资金也应该恰好追平了 $A$。很简单的推理，对不对？这些就足够了。

现在回到我们的“坏伙计” $T$：我们知道一个 Young 表的每一列至多有一个 $k$ (也至多有一个 $k+1$)，我们把每一列包含的关于 $k$ 和 $k+1$ 的个数看做一局游戏的结果：设 $T$ 有 $m$ 列，最右端的一列描述了 $A,B$ 第一局的结果：如果有 $k$ 无 $k+1$，则 $A$ 得 1 元；既有 $k$ 又有 $k+1$ 则 $A,B$ 各得 1 元；无 $k$ 有 $k+1$ 则 $B$ 得 1 元，以此类推。这样从右向左到第 $j+1$ 列时，根据 $j$ 的选取规则，$A$ 的资金仍然不少于 $B$，但是到第 $j$ 列时 $A$ 的资金被 $B$ 超过。根据我们前面的分析，这说明 $T$ 的第 $j$ 列有一个 $k+1$ 但是没有 $k$，而且
$$\lambda_k+w_k(T_{>j})=\lambda_{k+1}+w_{k+1}(T_{>j}).$$
这就印证了之前的断言。

现在考虑对 $T$ 进行如下的变换：保持 $T_{\geq j}$ 的部分不动，把 $T_{<j}$ 的部分对数字 $k$ 和 $k+1$ 进行 Bender-Knuth 变换，得到一个 Young 表 $T^\ast$ (不排除 $T=T^\ast$ 的可能)。不难验证 $T^\ast$ 也是半标准的 (利用 $T$ 的第 $j$ 列不含 $k$ 这一点)，$T^\ast$ 也是一个坏 Young 表且 $(T^\ast)^\ast =T$ (因为 $T^\ast_{\geq j}$ 和 $T_{\geq j}$ 完全一样)。容易验证对换 $s_k=(k,k+1)$ 交换 $w(T_{< j})$ 和 $w(T^\ast_{< j})$ 的 $k$ 和 $k+1$ 位置：
$$s_kw(T_{< j}) = w(T^\ast_{< j}).$$
结合等式
$$\lambda_k+w_k(T_{>j})=\lambda_{k+1}+w_{k+1}(T_{>j})$$
以及 $T$ 的第 $j$ 列有一个 $k+1$ 但是没有 $k$ 可知
$$s_k(\lambda+w(T)+\rho)=\lambda+w(T^\ast)+\rho,$$
所以两个行列式 $a_{\lambda+w(T)+\rho}$ 和 $a_{\lambda+w(T^\ast)+\rho}$ 是反号的 (矩阵相差两列的交换)。(在 $T=T^\ast$ 的情形，矩阵有两列是相同的，行列式自然是 0)

{% blockquote %}
**推论 [bi-alternant formula]**：
$$s_{\mu}=\frac{a_{\mu+\rho}}{a_\rho}.$$
{% endblockquote %}

证明：在定理中令 $\lambda=0$，则只有唯一的一个形状为 $\mu$ 的好 Young 表 $T$，使得 $w(T_{\geq j})$ 对任何 $j$ 都是一个分拆，这个表必须是第一行都填 1，第二行都填 2，...， 以此类推，从而 $w(T)=\mu$，因此得证。


# Jacobi-Trudi 恒等式的应用：Hook 长度公式

这一节来介绍并证明著名的 hook 长度公式。Hook 公式的表述简单优美，结论出人意料，让人第一眼看到它就会被它所吸引。

首先来定义什么是 hook 长度：设 $\lambda\vdash n$, $F_\lambda$ 是对应的 Ferrers 图，用 $v=(i,j)$ 来表示 $F_\lambda$ 中第 $i$ 行第 $j$ 列位置的方格 (只考虑那些有方格的位置)。数数与 $v$ 同行但是位置在 $v$ 的右边，以及与 $v$ 同列但是位置在 $v$ 的下方的方格的总数，$v$ 自己也算一个但是只算一次。这个数字称作 $v$ 的 hook 长度，记作 $h_v$。

例如下图显示的是 $\lambda=(5, 4, 3, 2, 1)$ 对应的 Ferrers 图中，计算 $v=(1, 1)$ 方格的 Hook 长度时包含的方格，于是 $h_v=5$。

|   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|
| $\phantom{}$ | $\phantom{}$  | $\phantom{}$  |  $\phantom{}$ | $\phantom{\bullet}$  |
| $\phantom{\bullet}$   | $\bullet$  | $\bullet$  | $\bullet$
|$\phantom{\bullet}$  | $\bullet$  |
| $\phantom{\bullet}$  | $\bullet$
| $\phantom{\bullet}$

{% blockquote %}
**定理 [hook 公式]**：形状为 $\lambda$ 的标准 Young 表的个数为
$$f_\lambda=\frac{n!}{\prod_{v\in F_\lambda}h_v}.$$
这里 $n=|\lambda|$。
{% endblockquote %}

Hook 公式的表达式虽然很形象，但是这个表达式真要用起来并不顺手。我们需要一个看起来不那么直观，但是用起来趁手的表达式，这就是下面的关键引理：

{% blockquote %}
**引理**：设 $\mu_i=\lambda_i+r-i$，这里 $r=l(\lambda),1\leq i\leq r$，则
$$\prod_{v\in F_\lambda} h_v =\frac{\prod_{i=1}^r \mu_i!}{\prod_{i<j}(\mu_i-\mu_j)}.$$
{% endblockquote %}

引理的证明：这里的表述来自

> Symmetric Functions and Hall Polynomials, by I. G. Macdonald.

一书。记 $\lambda'=(\lambda_1',\lambda_2',\ldots)$ 为 $\lambda$ 的共轭分拆，任取正整数 $m\geq\lambda_1,n\geq\lambda'_1$，则 $\lambda$ 的 Ferrers 图可以放在一个 $m\times n$ 的矩形当中，它的边界是一条从 $(0,0)$ 到 $(m,n)$ 的 Gauss 路径。从左下角开始给路径上的边依次标号为 $0,1,\ldots,m+n-1$，可以很容易看出垂直的边 (也就是每行末端的垂直边界) 的标号为 $\{\lambda_i+n-i,1\leq i\leq n\}$，水平的边的标号为 $\{n-1+j-\lambda'_j,1\leq j\leq m\}$。于是我们得到下面的结论：

{% blockquote %}
集合 $\{\lambda_i+n-i,1\leq i\leq n\}$ 和 $\{n-1+j-\lambda'_j,1\leq j\leq m\}$ 合起来构成 $\{0,1,\ldots,m+n-1\}$ 的一个置换。
{% endblockquote %}

注意集合 $\{\lambda_i+n-i,1\leq i\leq n\}$ 在 $n=\lambda'_1$ 时恰好是 $F_\lambda$ 的第一列的 hook 长度。如果我们想要得到第一行的 hook 长度，只要把这个结论应用在 $F_\lambda$ 的共轭图 $F_{\lambda'}$ 上，即 (交换 $\lambda$ 和 $\lambda'$ 的地位)

{% blockquote %}
集合 $\{\lambda'_j+m-j,1\leq j\leq m\}$ 和 $\{m-1+i-\lambda_i,1\leq i\leq n\}$ 合起来构成 $\{0,1,\ldots,m+n-1\}$ 的一个置换。
{% endblockquote %}

这才是我们想要的：令 $m=\lambda_1$，$n=\lambda_1'=r$ 为 $F_\lambda$ 的行数，则集合 $\{\lambda'_j+m-j,1\leq j\leq m\}$ 正好就是 $F_\lambda$ 的第一行的方格的 hook 长度，而集合 $\{m-1+i-\lambda_i,1\leq i\leq n\}$ 正好就是 $\{\mu_1-\mu_j,1\leq j\leq r\}$，它们合起来构成集合 $\{0,1,\ldots,\mu_1\}$ 的一个置换，因此 $F_\lambda$ 的第一行的所有方格的 hook 长度的乘积恰好等于

$$\frac{\mu_1!}{\prod_{i=2}^r(\mu_1-\mu_i)}.$$

然后擦去 $F_\lambda$ 的第一行，对第二行采用同样的论证道理，第二行所有方格的 hook 长度乘积为
$$\frac{\mu_2!}{\prod_{i=3}^r (\mu_2-\mu_i)}.$$

这样一直下去就得到了引理的证明。

回到 hook 公式的证明： 这里的技巧可以概括为 "think out of the box"， 考虑无穷多个变元的对称多项式环 $\Lambda[x_1,\ldots,x_n,\ldots]$，这个环到单变元形式幂级数环有一个同态 $\theta$：
$$\theta(f) = \sum_{k=0}^n f_k \frac{t^k}{k!}.$$
其中 $f_k$ 是 $f$ 中单项式 $x_1x_2\cdots x_k$ 的系数 (留给你验证这确实是一个同态)。特别地 $\theta(h_k)=\frac{t^k}{k!}$。在 Jacobi-Trudi 恒等式两边同时用 $\theta$ 作用，得到
$$f_\lambda \frac{t^n}{n!}=\det\left( \frac{t^{\lambda_i-i+j}}{(\lambda_i-i+j)!} \right).$$
这里左边是因为要想不重复不遗漏地填入 $x_1,\ldots,x_n$ 得到半标准 Young 表，必然有 $n=|\lambda|$ 且得到的是标准 Young 表。
然后在两边令 $t=1$ 就得到
$$f_\lambda = n!\cdot \det\left(\frac{1}{(\lambda_i-i+j)!}\right).$$

留给你验证右边等于引理中的表达式，这就完成了 hook 公式的证明。


# Bi-alternant 公式的应用：平面分拆的 Macmahon 公式

文章开头的堆箱子问题可以表述为

{% blockquote %}
**问题**：给定 3 个正整数 $a,b,c$，有多少满足如下条件的 $a\times b$ 矩阵？

1. 矩阵的元素都是非负整数，且每一行从左到右，每一列从上到下都是弱递减的。
2. 矩阵的元素均不超过 $c$。
{% endblockquote %}

这个问题又叫做受限制的平面分拆，最早由 Macmahon 在 1903 年解决。答案是非常难猜到的：

$$\prod_{i=1}^a\prod_{j=1}^b\prod_{k=1}^c \frac{a+b+c-1}{a+b+c-2}.$$

这就是有名的 Macmahon 公式。这个问题有很多解法，下面的解法利用了 Schur 多项式。

设使用 $n$ 个箱子的平面分拆的个数为 $a_n$，我们要计算生成函数

$$F(q)=\sum_{n=0}^{abc} a_nq^n.$$

特别令 $q=1$ 就是所有满足限制的平面分拆的总数。

设 $\lambda=(a,\ldots,a,0,\ldots,0)$，总共有 $b$ 个 $a$，$c$ 个 $0$。则 $s_\lambda(q^{b+c},\ldots,q)$ 就是列严格递减，行弱递减，最大元素不超过 $b+c$，元素都是正整数的矩阵的生成函数。这样的一个矩阵与受限制的平面分拆一一对应：

只要给第一行同时减去 $b$，第二行同时减去 $b-1$，$\ldots$，第 $b$ 行同时减去 1，则得到的就是行列都弱递降，最大元素不超过 $c$，元素都是非负整数的矩阵的生成函数，即

$$s_\lambda(q^{b+c},\cdots,q)= q^{ab(b+1)/2} F(q).$$

为了求出左边的表达式，只要利用 Schur 多项式的 bi-alternant 公式：

$$s_\lambda(q^{b+c},\cdots,q)=\frac{\det(q^{(b+c+1-i)(b+c-j+\lambda_j)})}{\det(q^{(b+c+1-i)(b+c-j)})}.$$

这个行列式的计算没有什么难度：(利用 Vandermonde 行列式)
$$F(q)=\prod_{i=1}^a\prod_{j=1}^b\prod_{k=1}^c\frac{1-q^{a+b+c-1}}{1-q^{a+b+c-2}}.$$
特别令 $q\to1$ 即得 Macmahon 公式。