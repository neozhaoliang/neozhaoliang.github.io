---
title: "Coxeter 群笔记（二）：根系"
categories: [Coxeter Groups]
date: 2021-12-05
url: "coxeter-groups-root-system"
---

\newcommand{\lfun}[2]{\langle #1,\,#2\rangle}
\newcommand{\fd}{\mathcal{D}}
\newcommand{\tc}{\mathcal{C}}
\newcommand{\stab}[1]{\mathrm{Stab}(#1)}
\newcommand{\negf}[1]{\mathrm{Neg}(#1)}
\newcommand{\barfd}{\overline{\mathcal{D}}}
\newcommand{\plc}[1]{\mathrm{PLC}(#1)}
\newcommand{\barc}{\overline{C}}
\newcommand{\bartc}{\overline{\tc}}
\newcommand{\sthe}[1]{\dfrac{\sin #1\theta}{\sin\theta}}
\newcommand{\shthe}[1]{\dfrac{\sinh #1\theta}{\sinh\theta}}
\newcommand{\inn}{(\cdot,\cdot)}
\newcommand{\gl}{\mathrm{GL}}
\newcommand{\R}{\mathbb{R}}

我们先简要回顾 [第一篇笔记](/coxeter-groups/geometric-realization/) 的核心内容。

设 $(W,S)$ 是一个 Coxeter 系。我们在该文中将其实现为一个实向量空间 $V$ 上的正交反射群，方式如下：

1. 取 $n=|S|$ 维实向量空间 $V$，并设其一组基为 $\{\alpha_s\mid s\in S\}$；
2. 定义 $V$ 上的内积 $\inn$；
2. 对每个生成元 $s\in S$ 在 $V$ 上的作用是以 $\alpha_s$ 为法向量的反射 $\rho_s$；
3. 最后，我们证明了 $\rho\,\colon\ W\to\mathrm{O}(V)$ 是群同态。

但是我们还有一个未完成的工作：证明 $\rho$ 是同构。本文会完成它。此外我还会介绍一些关于根系的知识。如果你直接翻到本文后面，会看到我罗列了很多关于根系的推论。这并不是我在故意掉书袋，这些推论每一条后面都会用到。不过读者初次阅读时只要大致浏览它们即可，等后面用到时再跳转过来查看细节。

<!--more-->

# 根系

:::{.definition}
我们称集合
$$\Phi=W\cdot\Delta=\{w\alpha_s\mid w\in W, \, \alpha_s\in\Delta\}$$
为 $(W, S)$ 的**根系**，任何 $\lambda\in\Phi$ 叫做根向量，简称为**根**。$\Delta$ 叫做 **单根系**，$\Delta$ 中的元素叫做**单根**。
:::

我们可以立刻观察到以下几点：

+ 每个根 $\lambda=w\alpha_s$ 都是内积 $\inn$ 下的单位向量，因为群 $W$ 的作用保持内积；
+ 若 $\alpha, \beta \in \Phi$ 共线，则 $\alpha = \pm \beta$。这是因为它们都是单位向量，$\alpha = k\beta\Rightarrow k^2 = 1$。

由于 $\Delta$ 构成 $V$ 的一组基，所以每个根 $\Phi\in\lambda$ 都是单根的线性组合：
$$\lambda = \sum_{s\in S}c_s\alpha_s,\quad c_s\in\mathbb{R}.$$
如果上面的所有系数 $c_s$ 都非负，就称 $\lambda$ 是**正根**；若所有系数 $c_s$ 都非正，就称 $\lambda$ 是**负根**。正根和负根组成的集合分别记作 $\Phi^+$ 和 $\Phi^-$。显然 $\Phi^+\cap\Phi^-=\emptyset$。

这就引出了一个问题：每个根都必然是正根或者负根吗？即是否有 $\Phi=\Phi^+\cup\Phi^-$ 成立？虽然答案是肯定的，但这并不显然。为此我们需要一个关键引理。这个引理的证明有点长，但是它非常重要，Coxeter 群的几乎所有性质的证明多少都会用到它。在引入它之前，我们需要做一点小小的准备。

设 $I\subseteq S$，$I$ 中的生成元在 $(W,S)$ 中生成一个子群 $W_I \leqslant (W,S)$，$W_I$ 叫做**标准椭圆子群**。记 $l_I(\cdot)$ 是 $W_I$ 上的长度函数，则显然对任何 $w\in W_I$ 有 $l(w)\leq l_I(w)$ 成立（因为 $W_I$ 中的既约表示放到 $W$ 中可能不是既约的）。我们后面会证明其实有 $l_I=l\mid_{W_I}$。

现在请出我们的重要引理：

::: {.lemma #key-lemma}

设 $s\in S,\, w\in W$，则

1. $l(ws) > l(w)$ 当且仅当 $w\alpha_s\in\Phi^+$。
2. $l(ws) < l(w)$ 当且仅当 $w\alpha_s\in\Phi^-$。
:::

**证明**：这里 1 和 2 是等价的：如果 1 成立，则

$$
\begin{align*}
l(ws)<l(w)&\Leftrightarrow l((ws)s) > l(ws)\\
&\Leftrightarrow ws(\alpha_s)\in\Phi^+\\
&\Leftrightarrow w(-\alpha_s)\in\Phi^+\\
&\Leftrightarrow w\alpha_s\in\Phi^-.
\end{align*}
$$

所以只需要证明 1 即可。

我们先证明充分性：若 $l(ws)>l(w)$ 则 $w\alpha_s\in\Phi^+$。

对 $l(w)$ 归纳：$l(w)=0$ 时 $w=1$，结论显然成立。下面设结论对所有长度小于 $l(w)$ 的元素成立。

我们总是可以取 $t\in S$ 使得 $l(wt)<l(w)$，比如 $t$ 取为 $w$ 的某个既约表达式的最后一项。由于 $l(ws)>l(w)$，故 $t\ne s$。令 $I=\{s,t\}$，定义集合
$$A = \{(x,x_I)\in W\times W_I\mid w=xx_I,\,l(w)=l(x)+l_I(x_I)\}.$$
由于 $(wt,t)\in A$ 所以 $A$ 非空。取 $(v,v_I)\in A$ 使得 $l(v)$ 是最小的，则
$$l(v)\leq l(wt)=l(w)-1.$$
我们断言对任何 $u\in I$ 都有 $l(vu)>l(v)$。若不然，则 $l(vu)=l(v)-1$，于是
$$\begin{align*}
l(w)&=l(vu\cdot uv_I)\leq l(vu) + l(uv_I) = (l(v) -1) + l(uv_I)\\
&\leq (l(v) -1) + l_I(uv_I)\\
&\leq (l(v) -1) + (l_I(v_I) + 1)\\
& = l(v) + l_I(v_I)=l(w).
\end{align*}$$
于是所有的不等号都是等式，从而 $(vu,uv_I)\in A$，但这与 $(v,v_I)$ 的选择矛盾。所以不论 $u=s$ 或是 $u=t$ 都有 $l(vu)>l(v)$。

由于 $l(v)\leq l(w)-1$ 所以根据归纳假设 $v\alpha_s,\,v\alpha_t$ 都是正根。如果我们能够证明 $v_I\alpha_s$ 是 $\alpha_s$ 和 $\alpha_t$ 的非负线性组合：$$v_I\alpha_s = a\alpha_s + b\alpha_t,\quad a,\,b\geq0.$$
则
$$w\alpha_s=vv_I\alpha_s=v(a\alpha_s + b\alpha_t)=av\alpha_s + bv\alpha_t\in\Phi^+.$$
这就证明了结论。

注意到 $v_I\in W_I$ 的任何既约表示都是 $s,t$ 的交错乘积，而且不能以 $s$ 结尾，否则 $l_I(v_Is)=l_I(v_I)-1$，从而
$$l(ws)=l(vv_Is)\leq l(v) + l(v_Is)\leq l(v)+l_I(v_Is)=l(v)+l_I(v_I)-1=l(w)-1.$$
这与 $l(ws) > l(w)$ 矛盾！

于是 $v_I$ 形如 $v_I=st\cdots t$ 或者 $v_I=ts\cdots t$，问题归结为分析这样的 $v_I$ 在 $\alpha_s$ 上的作用。我们在 [前文](/coxeter-groups/geometric-realization#rank2-roots) 中已经有过计算：

1. $m=m_{s,t}<\infty$ 时，$W_I$ 是有限二面体群 $D_m$。$W_I$ 中所有长度 $\leq m-1$ 且以 $t$ 结尾的元素罗列如下（包含恒等元）：
$$1,\ t,\ st,\ \ldots,\ \overbrace{\ast\cdots st}^{m-1}.$$
它们作用在 $\alpha_s$ 上给出如下链条的前 $m$ 项：
$$\alpha_s\xrightarrow{\ t\ }\sthe{}\alpha_s+\sthe{2}\alpha_t\xrightarrow{\ s\ }\sthe{3}\alpha_s+\sthe{2}\alpha_t\xrightarrow{\ t\ }\cdots$$
其中 $\theta=\pi/m$。这 $m$ 项都是 $\alpha_s,\alpha_t$ 的非负线性组合。

:::{.example}
以 $m=5$ 为例，所有 $m$ 个正根都位于 $\alpha_s,\alpha_t$ 张成的楔形区域内：

![$m=5$ 的例子](/images/coxeter/finite2d.svg){ width=400}

从 $\alpha_s$ 一侧开始，这些正根形如 $$\sthe{k}\alpha_s+\sthe{(k-1)}\alpha_t,\quad k=1,2,\ldots,m.$$
从 $\alpha_t$ 一侧开始，它们形如
$$\sthe{(k-1)}\alpha_s+\sthe{k}\alpha_t,\quad k=1,2,\ldots,m.$$
当 $k$ 跑遍 $1,\ldots,m$ 时，第一个序列从 $\alpha_s$ 开始过渡到 $\alpha_t$，第二个序列从 $\alpha_t$ 开始过渡到 $\alpha_s$。它们最接近的位置是在 $k=\lfloor(m+1)/2\rfloor$ 处（$m$ 为奇数时重合）。这两个序列的前 $\lfloor(m+1)/2\rfloor$ 项合起来正好给出全部 $m$ 个正根。这 $m$ 个正根可以通过将 $1,t,st,\ldots,\overbrace{\ast\cdots st}^{m-1}$ 这 $m$ 个元素作用在 $\alpha_s$ 上得到。
:::

2. $m=m_{s,t}=\infty$ 时，记 $\cosh\theta=a_{s,t}\,(\theta\geq0)$，则
$$\alpha_s\xrightarrow{\ t\ }\shthe{}\alpha_s+\shthe{2}\alpha_t\xrightarrow{\ s\ }\shthe{3}\alpha_s+\shthe{2}\alpha_t\xrightarrow{\ t\ }\cdots$$
每一项都是 $\alpha_s,\alpha_t$ 的非负线性组合。

:::{.example}
当 $\theta=0$ 时，$W_I$ 是一维直线上两个平行镜面生成的（仿射）反射群（包含了平移），它可以处理成二维平面上的线性反射群：

![](/images/coxeter/affine2d.svg){.fig width=500}

当 $\theta>0$ 时，$W_I$ 是双曲空间中两个超平行的镜面生成的双曲反射群，它也可以处理成二维平面上的线性反射群：

![](/images/coxeter/hyperbolic2d.svg){.fig width=400}
:::

必要性的证明：

我们要证明若 $w\alpha_s\in\Phi^+$ 则 $l(ws)>l(w)$。若不然，则 $l(w)=l(wss)>l(ws)$，从而由充分性的证明知道 $ws\alpha_s\in\Phi^+$，即 $w\alpha_s\in\Phi^-$，矛盾！至此关键引理得证。$\blacksquare$

从 @Pre:key-lemma 出发我们可以得到许多重要推论：

:::{.corollary #faithful}
如果 $w\in W$ 满足对任何 $v\in V$ 都有 $wv=v$，则 $w$ 必然是恒等元。换言之，表示 $\rho: W\to{\rm O}(V)$ 是忠实的。
:::

**证明**：若 $w\ne 1$，则存在 $s\in S$ 使得 $l(ws)<l(w)$，从而 $w\alpha_s\in\Phi^-$，这与 $w\alpha_s=\alpha_s$ 矛盾。$\blacksquare$

::: {.corollary #pos-neg}
每个根不是正根就是负根，即 $\Phi=\Phi^+\cup\Phi^-$。
:::

**证明**：任取 $\lambda \in \Phi$，则存在 $w \in W$ 与 $s \in S$ 使得 $\lambda = w\alpha_s$。若 $l(ws) > l(w)$，则 $\lambda \in \Phi^+$，否则 $\lambda \in \Phi^-$。$\blacksquare$

:::{.corollary #simple-ref}
任何单反射 $s$ 置换 $\Phi^+\setminus\{\alpha_s\}$ 中的正根，同时将 $\alpha_s$ 变为 $-\alpha_s$。
:::

**证明**：对任一正根 $\lambda\ne\alpha_s\in\Phi^+$，$\lambda$ 不可能与 $\alpha_s$ 共线，所以其作为单根的线性组合 $\lambda=\sum_{t\in S}c_t\alpha_t$ 中必有某个 $t\ne s$ 使得 $c_t>0$，于是 $s\lambda=\lambda-2(\lambda,\alpha_s)\alpha_s$ 的 $\alpha_t$ 分量保持不动仍然为正，于是根据 @Pre:pos-neg $s\lambda$ 仍然是正根。$\blacksquare$

:::{.corollary #lw-nw}
对 $w\in W$，定义 $N(w)$ 为被 $w$ 变成负根的那些正根组成的集合：
$$N(w)=\{\lambda\in\Phi^+\mid w\lambda\in\Phi^-\}.$$
则 $|N(w)|=l(w)$。
:::

**证明**：对 $l(w)$ 归纳。$l(w)=0$ 时 $w=1$，结论成立。若 $l(w)>0$，取 $s\in S$ 使得 $w=w's$ 且 $l(w')<l(w)$。由 @Pre:key-lemma，$\alpha_s\in N(w)$ 但是 $\alpha_s\notin N(w')$。

对任何正根 $\lambda\ne\alpha_s$，$s\lambda$ 仍然是正根。由恒等式
$$w'\lambda\in\Phi^- \Leftrightarrow w(s\lambda)\in\Phi^-$$
可得 $\lambda\leftrightarrow s\lambda$ 给出了 $N(w')$ 和 $N(w)\setminus\{\alpha_s\}$ 之间的一一对应，即
$$N(w)=s\cdot N(w')\cup\{\alpha_s\}.$$
从而由归纳假设
$$|N(w)|=|N(w')|+1=l(w')+1=l(w).$$
$\blacksquare$

:::{.corollary #nw-zero-means-identity}
若 $w\in W$ 满足 $w(\Phi^+)\subseteq\Phi^+$，则 $w=1$。
:::

**证明**：根据 @Pre:lw-nw 有 $l(w)=|N(w)|=0$，从而 $w=1$。$\blacksquare$

:::{.corollary #w-phi-both-finite-infinite}
$|W|<\infty$ 当且仅当 $|\Phi|<\infty$。
:::

**证明**：如果 $W$ 是有限群，由于 $\Phi=W\cdot \Delta$，$|\Phi|\leq |W|\cdot |\Delta|$ 也是有限的。

反之若 $|\Phi|<\infty$，由于 $W$ 保持 $\Phi$ 不变，所以 $W$ 置换地作用在 $\Phi$ 上，即有 $W$ 到置换群 $S_{|\Phi|}$ 的同态 $W\xrightarrow{\varphi} S_{|\Phi|}$。@Pre:nw-zero-means-identity 说明 $\varphi$ 是嵌入，从而 $W$ 也是有限的。$\blacksquare$

:::{.corollary #longest}
若 $W$ 是一个有限群，则存在唯一的元素 $w_0$，$w_0$ 是 $W$ 中长度最大者，它交换 $\Phi^+$ 和 $\Phi^-$：$w_0(\Phi^+)=\Phi^-$，且 $w_0$ 是一个对合：$w_0^2=1$。
:::

**证明**：由于 $W$ 有限所以存在一个长度最大的元素 $w_0$，对任何 $s\in S$ 只能有 $l(w_0s)<l(w)$，从而 $w_0\alpha_s\in\Phi^-$，从而 $w_0$ 把 $\Phi^+$ 变为 $\Phi^-$。

进一步 $w_0^2$ 仍然把 $\Phi^+$ 映射为 $\Phi^+$，所以由 @Pre:nw-zero-means-identity $w_0^2=1$，因此 $w_0$ 是一个对合。

如果存在 $w_1\ne w_0$ 使得 $l(w_1)=l(w_0)$ 的话，则 $w_1$ 也满足 $w_1(\Phi^+)=\Phi^-$，从而 $w_0^{-1}w_1$ 保持 $\Phi^+$ 不变，根据 @Pre:nw-zero-means-identity 有 $w_0^{-1}w_1=1$，即 $w_0=w_1$。所以这样的 $w_0$ 是唯一的。$\blacksquare$

:::{.corollary #remain-positive-root}
设 $I\subsetneqq S$ 是真子集，$\lambda\in \Phi^+\setminus\Phi^+_I$ 是正根，则对任何 $w\in W_I$，$w\lambda$ 仍然是正根。
:::

**证明**：$w\lambda$ 是 $\lambda$ 和 $\{\alpha_t\mid t\in I\}$ 中向量的线性组合：
$$w\lambda=\lambda + \sum_{t\in I}c_t\alpha_t.$$
$\lambda\in\Phi^+\setminus\Phi^+_I$ 说明将 $\lambda$ 表示为单根的线性组合时，其至少有一项 $\alpha_s\,(s\notin I)$ 的系数大于 0，从而 $w\lambda$ 的 $\alpha_s$ 项的系数也大于 0，所以 $w\lambda$ 必然是正根。$\blacksquare$

::: {.corollary #lI-equals-l}
设 $w\in W_I$，则其任何既约表示 $w=s_1\cdots s_k$ 中，每个 $s_i\in I$，特别地 $l_I(w)=l(w)$。
:::

**证明**：从右到左依次验证 $s_k,\ldots,s_1\in I$。记 $s=s_k$。由于 $w\in W_I$ 所以 $w\alpha_s$ 是 $\alpha_s$ 和一些 $\{\alpha_t\mid t\in I\}$ 的线性组合：
$$w\alpha_s=\alpha_s+\sum_{t\in I} c_t\alpha_t.$$
由于 $w\alpha_s\in\Phi^-$ 所以必然有某个 $t\in I$ 使得 $s=t$，即 $s\in I$。对 $ws=s_1\cdots s_{k-1}\in W_I$ 重复此论证即得每个 $s_i\in I$。$\blacksquare$