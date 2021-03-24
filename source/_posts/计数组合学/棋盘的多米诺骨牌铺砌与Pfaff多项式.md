---
title: 棋盘的多米诺骨牌密铺
date: 2009-05-08
tags:
  - Pfaffian
  - Perfect matching
  - Kasteleyn orientation
categories: [计数组合学]
url: "Pfaffian-and-chessboard-tiling"
---

下面的问题与统计物理中的 Dimer 格点模型有关：

{% blockquote %}
**问题**：一张 $8\times8$ 的国际象棋棋盘，用 $1\times2$ 的多米诺骨牌密铺，有多少种不同的方法？
{% endblockquote %}

下图是其中一种 (图片来自 wiki 百科)：

<img style="margin:0px auto;display:block" src="/images/pfaff/chessboard.png"/>

答案是 12988816，非常大的一个数字，绝对不是一个一个数出来的。1961 年德国物理学家 Kasteleyn 借助于线性代数中的一个结论首先解决了这个问题，接下来就介绍他的方法。

<!-- more -->

# 反对称矩阵的 Pfaffian


我们从一个线性代数的结论说起，先看一个 4 阶反对称矩阵的例子：

$$\det\begin{pmatrix}0&a_{12}&a_{13}&a_{14}\\-a_{12}&0&a_{23}&a_{24}\\-a_{13}&-a_{23}&0&a_{34}\\-a_{14}&-a_{24}&-a_{34}&0\end{pmatrix}=(a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23})^2.$$
你发现了什么？这个反对称矩阵的行列式是一个多项式的平方，而且观察右边每个单项式的下标你发现，它们分别是 $\{(12),(34)\}$，$\{(14),(23)\}$，$\{(13),(24)\}$，恰好跑遍集合 $\{1,2,3,4\}$ 的所有匹配！

这个结论不是偶然的，实际上任何偶数阶反对称矩阵的行列式都可以表示为一个多项式的平方，这个多项式叫做 Pfaffian 多项式。

那么奇数阶反对称矩阵呢？它们的行列式都是 0，所以不考虑它们。

设 $A$ 是一个给定的 $2n$ 阶的反对称矩阵，下面来定义 $A$ 的 Pfaffian 多项式 $\text{pf}(A)$，你会看到 $\text{pf}(A)$ 总是一个 $n$ 次的齐次多项式。

记 $[2n]=\{1,2,\ldots,2n\}$，考虑一种把 $[2n]$ 两两配对 (从而分成 $n$ 对) 的方式：
$$\pi = (i_1,j_1)(i_2,j_2)\cdots(i_n,j_n).$$
$\pi$ 叫做集合 $[2n]$ 的一个匹配，它可以用一个置换来表示 (仍然记作 $\pi$)：
$$\pi=\begin{pmatrix}1&2&3&4&\cdots&2n-1&2n\\i_1&j_1&i_2&j_2&\cdots&i_n&j_n\end{pmatrix}.$$
定义 $\pi$ 的权为
$$\mathrm{wt}(\pi)=\text{sgn}(\pi)\cdot a_\pi.$$
其中 $\text{sgn}(\pi)$ 就是置换 $\pi$ 的符号 (偶置换时为 $+1$，奇置换时为 $-1$)，
$$a_\pi=a_{i_1j_1}a_{i_2j_2}\cdots a_{i_nj_n}.$$
于是 $\mathrm{wt}(\pi)$ 是一个次数为 $n$ 的单项式。

注意一个匹配 $\pi$ 可以有多种不同的置换表示：你可以按任意的顺序排列这些 $(i_k,j_k)$ 对，或是交换某一对中 $i_k$ 和 $j_k$ 的位置。不同的置换表示给出的 $\text{sgn}(\pi)$ 和 $a_\pi$ 的值可能不同，但是二者的乘积 $\mathrm{wt}(\pi)$ 的值都是一样的。比如你把某个 $(i_k,j_k)$ 改写成 $(j_k,i_k)$，那么 $\text{sgn}(\pi)$ 和 $a_\pi$ 都同时变号，乘积保持不变。总之 $\mathrm{wt}(\pi)$ 的定义只与匹配 $\pi$ 有关，并不依赖于具体置换的选择。

设 $\mathcal{M}_{2n}$ 为 $[2n]$ 的所有匹配组成的集合，矩阵 $A$ 的 Pfaffian 多项式 $\text{pf}(A)$ 就定义为
$$\text{pf}(A) =\sum_{\pi\in\mathcal{M}_{2n}} \mathrm{wt}(\pi).$$

现在我们可以叙述本节的主要结论了：

{% blockquote %}
**定理 1**：设 $A$ 是 $2n$ 阶反对称矩阵，则 $\det A=[\text{pf}(A)]^2$。
{% endblockquote %}

**证明**：根据行列式的定义，
$$\det A=\sum_{\sigma}\text{sgn}(\sigma)a_{\sigma}=\sum_{\sigma}\text{sgn}(\sigma) a_{1\sigma(1)}a_{2\sigma(2)}\cdots .$$
这里 $\sigma$ 跑遍置换群 $S_{2n}$。

回忆任何置换 $\sigma$ 都可以表示为若干不相交的轮换的乘积：
$$\sigma = (i_1i_2\cdots i_k)(j_1j_2\cdots j_l)\cdots.$$
其中 $k,l,\ldots$ 为对应的轮换的长度。设 $\mathcal{E}_{2n}$ 为轮换长度都是偶数的那些置换组成的集合，我们要证明在上述行列式的求和中，$\sigma$ 只跑遍 $\mathcal{E}_{2n}$，即不属于 $\mathcal{E}_{2n}$ 的那些置换整体对行列式的贡献为 0。

分两种情况：

1. 如果 $\sigma$ 包含一个不动点：$\sigma(i)=i$，则由于 $a_{i\sigma(i)}=0$ 从而 $\sigma$ 对行列式的贡献为 0。
2. 如果 $\sigma$ 没有不动点，但是包含长度为奇数的轮换，选择其中含有最小元素的那个，设为 $C=(i_1i_2\cdots i_k)$，这里 $k$ 为奇数且大于等于 3。定义置换 $\sigma'$ 如下：$\sigma'$ 的其它轮换与 $\sigma$ 完全相同，只是把 $C$ 改成 $(i_k\cdots i_2i_1)$。举个例子，比如 $n=10$，$\sigma=(13)(246)(578)(9,10)$，则 $\sigma$ 有 2 个长度为奇数的轮换 $(246)$ 和 $(578)$，这两个轮换中最小的元素是 $2$，它出现在 $(246)$ 中，所以 $\sigma'=(13)(642)(578)(9,10)$。显然 $\sigma'$ 对应的和项与 $\sigma$ 抵消，而且如果对 $\sigma'$ 执行此操作又会回到 $\sigma$。于是所有没有不动点，而且包含长度是奇数的轮换的置换可以两两配对抵消。

这就证明了在行列式的求和中，我们只需要考虑那些轮换分解长度都是偶数的置换。

我们想要建立一个双射
$$\mathcal{M}_{2n}\times \mathcal{M}_{2n}\rightarrow \mathcal{E}_{2n}:\quad (\pi,\pi')\rightarrow \sigma,$$
而且这个双射还保持权的相等，即
$$\mathrm{wt}(\pi)\cdot \mathrm{wt}(\pi')=\text{sgn}(\sigma)a_{\sigma},$$
这样就证明了定理。

对任何两个匹配 $(\pi,\pi')\in\mathcal{M}_{2n}\times\mathcal{M}_{2n}$，我们把它俩画在同一张图上，图的顶点集合就是 $[2n]$，两个顶点如果在 $\pi$ 中配成一对就在它们之间连一条红色边，两个顶点如果在 $\pi'$ 中配成一对就在它们之间连一条蓝色边。这样我们得到的是一个顶点度数都是 2 的正则图：每个顶点恰好有一条红边和一条蓝边与之相连，从而这个图可以表示为若干条不相交的回路的并 (想一想，为什么？提示：从任一顶点 $x$ 出发沿着红边到达顶点 $y$，再从 $y$ 出发沿着蓝边到达顶点 $z$，再从 $z$ 出发沿着红边到达顶点 $w$，这样一直继续下去肯定会回到起点 $x$)，在一个回路中，红边和蓝边是交错出现的，因此每个回路的长度都是偶数。

设 $C$ 是这样的一条回路，$i_1$ 是 $C$ 中最小的元素，从 $i_1$ 出发，沿着红色的边 (匹配 $\pi$ 的方向) 绕 $C$ 一圈：
$$i_1\color{red}{\xrightarrow{\pi}}i_2\color{blue}{\xrightarrow{\pi'}}i_3\color{red}{\xrightarrow{\pi}}\cdots\color{blue}{\xrightarrow{\pi'}}i_1.$$
这自然就得到了一个轮换 $(i_1i_2\cdots i_k)$，与 $(\pi,\pi')$ 对应的置换 $\sigma$ 就定义为所有回路对应的轮换的乘积。

逆映射也很显然，对任何 $\sigma\in\mathcal{E}_{2n}$，在 $\sigma$ 的每个轮换 $C$ 中，找到最小的 $i_1\in C$，设 $C=(i_1i_2\cdots i_k)$，那么依次规定
$$i_1\color{red}{\xrightarrow{\pi}}i_2\color{blue}{\xrightarrow{\pi'}}i_3\color{red}{\xrightarrow{\pi}}\cdots\color{blue}{\xrightarrow{\pi'}}i_1$$
即可。

还需要说明这个对应保持权的相等，这很容易：设 $\sigma$ 的轮换分解式为
$$\sigma=(i_1i_2\cdots i_{2k-1}i_{2k})(j_1j_2\cdots j_{2l-1}j_{2l})\cdots,$$
其中 $i_1,j_1,\ldots$ 是每个轮换中最小的元素，于是 $\pi=(i_1,i_2)\cdots(i_{2k-1},i_{2k})\cdots$，其置换表示为
$$\pi=\begin{pmatrix}1&2&\cdots&2k-1&2k&\cdots\\i_1&i_2&\cdots&i_{2k-1}&i_{2k}&\cdots\end{pmatrix}.$$
同理 $\pi'=(i_2,i_3)\cdots(i_{2k},i_1)\cdots$，其置换表示为
$$\pi'=\begin{pmatrix}1&2&\cdots&2k-1&2k&\cdots\\i_2&i_3&\cdots&i_{2k}&i_{1}&\cdots\end{pmatrix}.$$
容易验证 $a_\pi a_{\pi'}=a_\sigma$ 以及 $\pi'=\sigma\cdot\pi$，从而结论得证。


# 平面图的 Pfaffian 定向


Pfaffian 多项式的结论启发我们可以用它来计算一个图 $G$ 的所有匹配的个数。

设 $G$ 有 $2n$ 个顶点。首先给 $G$ 的边任意定向，得到一个简单有向图 $\overrightarrow{G}$。写出 $\overrightarrow{G}$ 的邻接矩阵 $A=(a_{ij})$：

$$a_{ij}=\begin{cases}1& i\rightarrow j,\\-1& j\rightarrow i,\\ 0&\text{else}.\end{cases}$$

则 $A$ 是一个反对称矩阵且

$$\det A=\left(\sum_{\pi\in\mathcal{M}_{2n}}\mathrm{wt}(\pi)\right)^2.$$

这里 $\pi$ 跑遍集合 $[2n]$ 的所有匹配。注意每一项 $\mathrm{wt}(\pi)$ 的值为 1，-1 或者 0，且 $\mathrm{wt}(\pi)$ 不为 0 当且仅当 $\pi$ 给出图 $\overrightarrow{G}$ 的一个完美匹配，所以图 $G$ 的所有匹配都和 Pfaffian 多项式中的所有非零项一一对应。不幸的是，这些非零项有 +1 有 -1，你把它们直接加起来得到的可不是图 $G$ 的所有匹配的个数。但是我们可以这样想： 能否通过适当的定向 $G$，即适当给 $a_{ij}$ 赋以 +1 或者 -1，使得每一个非零的 $\mathrm{wt}(\pi)$ 都同为 +1 或者同为 -1？如果可以，那么$\sqrt{|\det A|}$ 就是要求的匹配的个数。

回忆在证明 Pfaffian 多项式定理时，我们有结论
$$\mathrm{wt}(\pi)\cdot \mathrm{wt}(\pi')=\text{sgn}(\sigma)a_{\sigma},$$
为了让所有 $\mathrm{wt}(\pi)$ 都同为 +1 或者同为 -1，只要让每一个 $\text{sgn}(\sigma)a_{\sigma}=1$ 即可。设 $\sigma$ 的轮换分解为 $\sigma=C_1\cdots C_l$，则 $\text{sgn}(\sigma)=(-1)^l, a_\sigma=a_{C_1}\cdots a_{C_l}$，所以只要让每一个 $a_{C_i}=-1$ 即可。其中若轮换 $C=(i_1i_2\cdots i_k)$ 则 $a_C=a_{i_1i_2}\cdots a_{i_ki_1}$。注意每个 $C_i$ 都是长度为偶数的回路，即 $k$ 是偶数，因此只要 $\{a_{i_1i_2},\ldots,a_{i_ki_1}\}$ 中有奇数个是 -1 即可。换句话说，当沿着回路
$$i_1\rightarrow i_2\rightarrow \cdots \rightarrow i_k\rightarrow i_1$$
绕 $C$ 一圈时，有奇数条边的定向与行走方向一致即可 (当然也就有奇数条边与行走方向相反)。

{% blockquote %}
**定义**：在一个有向图 $G$ 中，如果一条回路的 $C$ 的长度是偶数，且删除 $C$ 后剩下的部分仍然存在完美匹配，就称 $C$ 是一个好的回路。如果 $G$ 的一个定向使得 $G$ 的所有好的回路都是奇定向的 (即沿着回路的任一方向行走都有奇数条边的定向与行走方向一致)，就称这个定向是 $G$ 的一个 Pfaffian 定向。
{% endblockquote %}

对一般的图，找到其 Pfaffian 定向是困难的事，但是对平面图却很简单。这就是下面的定理：

{% blockquote %}
**Kasteleyn 定理**：设 $G$ 是一个简单平面图，则可以给 $G$ 的边适当定向，使得当逆时针沿着 $G$ 的每个面行走时 (外部的无穷区域不算)，都有奇数条边与行走方向一致，这种定向就是 $G$ 的 Pfaffian 定向。
{% endblockquote %}

**证明**：首先说明存在这样的定向，使得 $G$ 的每个面都是奇定向的。对面的个数归纳：$f=0$，则 $G$ 是一个树，任何定向都是 Pfaffian 定向。设结论对有 $f-1$ 个面的简单有向图成立，对有 $f>1$ 个面的图 $G$，找到一条内部面与外部区域相邻的边 $e$，删去 $e$ 得到的是一个有 $f-1$ 个面的有向图，因此由归纳假设，可以让每个面都是奇定向，然后把 $e$ 补回去，适当给 $e$ 定向使得最后这个面也是奇定向的即可。

接下来说明这样的定向是 Pfaffian 定向。为此需要说明对 $G$ 中任意好的回路 $C$，当绕着 $C$ 的内部逆时针 (或者顺时针也行) 行走一圈时，有奇数条边的定向与行走方向一致。

设 $C$ 长度为 $l$，$C$ 内部有 $p$ 个顶点，$q$ 条边，$r$ 个面，$C$ 上逆时针定向的边的个数为 $c$，内部的第 $i$ 个面 ($1\leq i\leq r$) 上逆时针定向的边的个数为 $c_i$。

绕着所有面都逆时针走一圈，遇到的与行走方向定向相同的边的个数是 $\sum\limits_{i=1}^rc_i=c+q$，这是因为 $C$ 内部的每条边 (一共有 $q$ 条) 都被走了两次，一次逆时针，一次顺时针，因此都被计算了一次；而 $C$ 上的边只有逆时针定向的那些边 (一共有 $c$ 条) 被计算了一次。

由于每个 $c_i$ 都是奇数，因此
$$r\equiv c+q\ (\text{mod}\ 2).$$

另一方面对 $C$ 包含的区域用 Euler 定理，得到
$$(p+l)-(q+l)+r=1.$$
从而 $p$ 与 $c$ 奇偶性相反，但是 $p$ 是偶数 (因为删去 $C$ 以后仍然存在匹配说明 $C$ 的内部和外部各有偶数个顶点)，因此 $c$ 是奇数，这就证明了定理。


# 棋盘的多米诺骨牌密铺的计数


回到文章开始的问题。

设棋盘的大小为 $m\times n$，$m$ 是行数。这里 $m,n$ 必须至少有一个是偶数，我们这里假定列数 $n$ 是偶数。

把棋盘的每个方格看作图 $G$ 的顶点，两个方格对应的顶点 $u,v$ 在 $G$ 中相邻当且仅当它们有公共的边，这样就得到一个有 $mn$ 个顶点的平面图。棋盘的多米诺密铺与 $G$ 的完美匹配是一一对应的 (密铺中的每个骨牌恰好盖住两个相邻的方格，这两个方格匹配在了一起)。

为了求出 $G$ 的完美匹配个数，只要标记出 $G$ 的一个 Pfaffian 定向，写出对应的邻接矩阵，然后求出行列式，再开平方即可。

Pfaffian 定向是很容易找的，如下图所示：

<img style="margin:0px auto;display:block" src="/images/pfaff/pfaffian.png"/>

下一步是写出这个定向图的邻接矩阵来 (顶点标号的顺序就是第一行从左到右，然后是第二行从左到右，以此类推)。设
$$B_n=\begin{pmatrix}0&1&0&&\\-1&0&1&&\\&-1&0&1&\\&&&\ddots&1\\&&&-1&0\end{pmatrix}_{n\times n}.$$
则邻接矩阵为
$$L(m,n)=\begin{pmatrix}B_n&I_n&&&\\-I_n&-B_n&I_n&&\\&-I_n&B_n&&\\&&&\ddots&I_n\\&&&-I_n&(-1)^{m-1}B_n\end{pmatrix}_{m\times m}.$$

我把求邻接矩阵的详细过程放在后面的附录中，先来求 $L(m,n)$ 的行列式。

适当给 $L(m,n)$ 的行列变号，可以得到
$$\begin{align*}
\det L(m,n)&=\det\begin{pmatrix}B_n&-I_n&&&\\-I_n&B_n&-I_n&&\\&-I_n&B_n&&\\&&&\ddots&-I_n\\&&&-I_n&B_n\end{pmatrix}\\&=\det(B_n\otimes I_m-I_n\otimes C_m).\end{align*}$$
其中
$$C_m=\begin{pmatrix}0&1&0&&\\1&0&1&&\\&1&0&1&\\&&&\ddots&1\\&&&1&0\end{pmatrix}.$$
其实这个变号步骤并不显然，你可以对 $m=8$ 的情形试一试。

剩下的就是线性代数中求特征值的部分，需要一些关于矩阵张量积的知识，这里就不展开写了，大致逻辑是这样的：设 $B_n$ 的特征值为 $\lambda_1,\ldots,\lambda_n$，$C_m$ 的特征值为 $\mu_1,\ldots,\mu_m$，则 $B_n\otimes I_m- I_n\otimes C_m$ 的 $mn$ 个特征值为 $\{\lambda_i-\mu_j, 1\leq i\leq n, 1\leq j\leq m\}$，所以
$$\det(B_n\otimes I_m- I_n\otimes C_m) = \prod_{i=1}^n\prod_{j=1}^m(\lambda_i-\mu_j).$$
$B_n$ 和 $C_m$ 的特征值的计算应该是线性代数课程中行列式部分的常见的习题，我把具体的计算步骤放在附录中，最终结果是
$$\sqrt{|\det L(m,n)|} =\prod_{k=1}^m\prod_{l=1}^n(4\cos^2\frac{k\pi}{m+1}+4\cos^2\frac{l\pi}{n+1})^{\frac{1}{4}}.$$
此即为要求的完美匹配的个数。


# 未尽的讨论


我们已经得到了一个关于 $m\times n$ 棋盘的多米诺骨牌密铺的漂亮的表达式，事情可以结束了吗？其实还没有，这个表达式虽然很漂亮，但是我们没法用它来具体计算匹配个数的值 (一堆三角函数的乘积怎么算？)。那应该怎么办呢？这里需要一些关于多项式的结式的知识，本文就不写了，有兴趣的读者可以参考 Martin Aigner 的《A Course in Enumeration》一书 10.1 小节。


# 附录


## 求邻接矩阵 $L(m,n)$ 的具体步骤


考虑从 $G$ 中取出红色箭头标记的一行后得到的图：

<img style="margin:0px auto;display:block" src="/images/pfaff/row.png"/>

这个图有 $n$ 个顶点 (顺序从左到右)，其邻接矩阵为
$$B_n=(b_{ij})=\begin{pmatrix}0&1&0&&\\-1&0&1&&\\&-1&0&1&\\&&&\ddots&1\\&&&-1&0\end{pmatrix}_{n\times n}.$$

同理 $G$ 的绿色箭头标记的行对应的图的邻接矩阵是 $-B_n$：

<img style="margin:0px auto;display:block" src="/images/pfaff/rowback.png"/>

以及 $G$ 的任何一列对应的图 (包含 $m$ 个顶点) 的邻接矩阵是 $A_m$：

<img style="margin:0px auto;display:block" src="/images/pfaff/col.png"/>
 
$$A_m=(a_{ij})=\begin{pmatrix}0&1&0&&\\-1&0&1&&\\&-1&0&1&\\&&&\ddots&1\\&&&-1&0\end{pmatrix}_{m\times m}.$$

我们把网格图 $G$ 的顶点标记如下：

$$\begin{matrix}(1,1)&(1,2)&\cdots&(1, n)\\(2,1)&(2,2)&\cdots&(2,n)\\\vdots&\vdots&\ddots&\vdots\\(m, 1)&(m,2)&\cdots&(m, n)\end{matrix}$$

为了写出 $G$ 的邻接矩阵，我们要先把这些顶点排序，排序规则就是先第一行从左到右，然后是第二行从左到右，以此类推，最后是第 $m$ 行从左到右。在这个顺序下 $G$ 的邻接矩阵是一个 $m\times m$ 的分块矩阵，其每一个子块都是 $n\times n$ 的矩阵，其中位于 $(i, i')$ 位置处的子块的 $(j,j')$ 位置处的元素是顶点 $(i,j)$ 和顶点 $(i',j')$ 之间的边的权值。参考下面的示意图：

$$\begin{array}{c|c|c}&(i',1), \cdots, (i',j'),\cdots, (i',n)&\\ &\hline&\qquad\\(i, 1)&&\\\vdots&&\\(i,j)&\ast&\\\vdots&&\\(i,n)&&\\ &\hline&\qquad\\ &&\end{array}$$

设 $(i, j)$ 和 $(i',j')$ 是两个不同的顶点，则有三种情况：

1. $i\ne i'$ 且 $j\ne j'$，即 $(i, j)$ 和 $(i',j')$ 既不同行也不同列，它们之间没有边连接，所以权值是 0。
2. $i = i'$，这时 $(i, j)$ 和 $(i',j')$ 都位于第 $i$ 行，若 $i$ 是奇数则它们之间的边的权值是 $b_{jj'}$，若 $i$ 是偶数则它们之间的边的权值是 $-b_{jj'}$。
3. $j=j'$，这时 $(i, j)$ 和 $(i',j')$ 都位于第 $j$ 列，它们之间的权值是 $a_{ii'}$。

总之 $(i, j)$ 和 $(i',j')$ 之间的边的权值可以表示为

$$\begin{cases}\delta_{ii'}b_{jj'}+a_{ii'}\delta_{jj'}& \text{$i$ odd},\\-\delta_{ii'}b_{jj'}+a_{ii'}\delta_{jj'}& \text{$i$ even}.\end{cases}$$

考虑 $m\times m$ 的分块矩阵

$$I_n\otimes A_m=\begin{pmatrix}0&I_n&0&&\\-I_n&0&I_n&&\\&-I_n&0&I_n&\\&&&\ddots&I_n\\&&&-I_n&0\end{pmatrix}_{m\times m}.$$

此矩阵的第 $(i, i')$ 个子块 $I_na_{ii'}$ 的 $(j,j')$ 位置处的元素是 $a_{ii'}\delta_{jj'}$。

类似地 $m\times m$ 的对角分块矩阵

$$\begin{pmatrix}B_n&&&\\&-B_n&&\\&&\ddots&\\&&&(-1)^{m-1}B_n\end{pmatrix}$$

的第 $(i,i')$ 个子块 $\delta_{ii'}(-1)^{i-1}B_n$ 的 $(j,j')$ 位置处的元素是

$$\begin{cases}\delta_{ii'}b_{jj'}& \text{$i$ odd},\\-\delta_{ii'}b_{jj'}& \text{$i$ even}.\end{cases}$$

于是二者之和就是 $G$ 的邻接矩阵。


## 求 $B_n$ 和 $C_m$ 的特征值

我们以
$$C_m=\begin{pmatrix}0&1&0&&\\1&0&1&&\\&1&0&1&\\&&&\ddots&1\\&&&1&0\end{pmatrix}.$$
为例来说明怎样求它的特征值，$B_n$ 的求解是类似的。

我们需要求出其特征多项式

$$f_n(\lambda) = \det\begin{pmatrix}\lambda&-1&0&&\\-1&\lambda&-1&&\\&-1&\lambda&-1&\\&&&\ddots&-1\\&&&-1&\lambda\end{pmatrix}.$$

按第一行展开可得递推关系

$$f_m = \lambda f_{m-1} - f_{m-2},$$

结合初始条件 $f_0=1, f_1=\lambda$ (初始条件可以从 $m=2$ 的情形展开确定) 可得

$$f_m(\lambda) = \frac{1}{\sqrt{\lambda^2-4}}\left[\left(\frac{\lambda+\sqrt{\lambda^2-4}}{2}\right)^{m+1}-\left(\frac{\lambda-\sqrt{\lambda^2-4}}{2}\right)^{m+1}\right].$$

由此不难确定 $C_m$ 的 $m$ 个特征值为 $2\cos\dfrac{k\pi}{m+1},k=1,\ldots,m$。
