---
title: "Todd Kemp 概率论课程笔记"
date: 2021-03-01
url: todd-kemp
---
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\N}{\mathcal{N}}
\newcommand{\O}{\Omega}
\newcommand{\P}{\mathbb{P}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\S}{\mathcal{S}}
\newcommand{\L}{\mathcal{L}}
\newcommand{\H}{\mathbb{H}}
\newcommand{\M}{\mathbb{M}}
\newcommand{\dtv}{\mathrm{d_{TV}}}
\newcommand{\io}{\mathrm{i.o.}}
\newcommand{\ae}{\mathrm{a.e.}}
\newcommand{\iid}{\mathrm{i.i.d}}

\newcommand{\du}{\,\mathrm{d}\mu}
\newcommand{\dun}{\,\mathrm{d}\mu_n}
\newcommand{\dv}{\,\mathrm{d}\nu}
\newcommand{\da}{\,\mathrm{d}\alpha}
\newcommand{\dx}{\,\mathrm{d}x}
\newcommand{\dy}{\,\mathrm{d}y}
\newcommand{\dz}{\,\mathrm{d}z}
\newcommand{\dt}{\,\mathrm{d}t}
\newcommand{\dp}{\,\mathrm{d}\mathbb{P}}
\newcommand{\dxi}{\,\mathrm{d}\xi}

\newcommand{\triple}{(\Omega,\mathcal{F},\mathbb{P})}
\newcommand{\Lone}{L^1(\Omega,\mathcal{F},\mathbb{P})}

\newcommand{\ind}{\mathbb{1}}

\newcommand{\ud}[1]{\mu(\mathrm{d}#1)}
\newcommand{\vd}[1]{\nu(\mathrm{d}#1)}
\newcommand{\uxuy}{\mu_X\otimes\mu_Y}
\newcommand{\uxvy}{\mu_X\otimes\nu_Y}
\newcommand{\sgn}{\mathrm{sgn}}
\renewcommand{\Re}{\mathrm{Re}\,}
\newcommand{\span}{\mathrm{span}}
\DeclareMathOperator{\supp}{supp}

# ✅ 0 Banach Tarski

:::{.example}
**不可测集的例子** 记单位圆 $S^1=\{e^{it},\,t\in\R\}$，子群 $H=\{e^{iq},\,q\in\Q\}$，在每个左陪集 $S^1/H$ 中选择一个代表元组成集合 $E$，则 $E$ 是不可测集合。这是因为 $S^1 = \bigcup_{q\in\Q}Ee^{iq}$ 是可数多个互不相交的集合的并，这些集合两两之间只差乘以一个单位复数，即差一个旋转，所以测度均相等，于是
$$1 = \sum_{q\in\Q}\mu(E) = \infty\cdot \mu(E)\Rightarrow E\text{ not measuabe.}$$
:::

# ✅ 1.1 Probability Motivation

无要点

# ✅ 1.2 $\sigma$- Fields

介绍了 $\sigma$- 域的概念，以及最重要的 $\sigma$- 域的例子：拓扑空间中开集生成的 Borel 域。

# ✅ 2.1 Measures Definition and Examples

介绍了可测空间，以及测度的定义和基本性质。

:::{.definition .unnumbered}
设 $\F$ 是一个 $\sigma$- 域，称 $\mu:\ \F\to[0,\infty]$ 是测度，如果对任何可数多个不交并有 $\mu(\uplus_{n=1}^\infty E_n)=\sum_{n=1}^\infty\mu(E_n)$ 成立。
:::

测度的三个基本性质：

+ 单调性：$A\subseteq B\Rightarrow \mu(A)\leq\mu(B)$。
+ 加法等式 $\mu(A\cup B) + \mu(A\cap B) = \mu(A) + \mu(B)$。
+ 次可数可加：$\mu(\cup_{n=1}^\infty E_n)\leq\sum_{n=1}^\infty\mu(E_n)$。

此外如果 $\{\mu_n\}_{n=1}^\infty$ 是一列测度，则它们的和 $\mu=\sum\limits_{n=1}^\infty\mu_n$ 也是测度。

预告了接下来构造测度的过程：有限可加测度 $\Rightarrow$ 预测度 $\Rightarrow$ ·测度。

# ✅ 2.2 Finitely Additive Measures

这一讲介绍了**有限可加测度**，**预测度 (pre-measure，即域上的可数可加测度)**，**半代数 (semi-algebra)** 等概念。

:::{.definition .unnumnered}
1. 域上的可数可加测度叫做 **预测度**。
2. 域上的有限可加测度叫做 **有限可加测度**。
:::

> **核心思想**：半代数 $\mathcal{S}$ 上的有限可加测度 $\Rightarrow$ 代数 $\mathcal{A}$ 上的有限可加测度 $\Rightarrow$ 代数 $\mathcal{A}$ 上的可数可加测度 $\Rightarrow$ $\sigma$- 域上的可数可加测度。

域 $\mathcal{A}$ 上的有限可加测度的基本性质：

+ 单调性、加法等式同可数可加的情形。
+ **超可数可加**：如果 $\{E_n\}_{n=1}^{\infty}$ 是一列不相交的集合，每个 $E_n\in\mathcal{A}$ 并且 $\mu(\uplus_{n=1}^\infty E_n)\in\mathcal{A}$。则 $\mu(\uplus_{n=1}^\infty E_n)\geq\sum_{n=1}^\infty\mu(E_n)$。这是由于单调性左边始终是右边部分和的上界。


:::{.definition}
一个半代数 $\mathcal{S}$ 是指满足如下条件的集合族：

1. $\emptyset\in\mathcal{S}$。
2. 若 $A,\,B\in\mathcal{S}$ 则 $A\cap B\in\mathcal{S}$。
3. 若 $A\in\mathcal{S}$ 则 $A^c$ 可以表示为 $\mathcal{S}$ 中有限多个成员的不交并。
:::

半代数 $\mathcal{S}$ 生成一个代数 $\mathcal{A}$：
$$\mathcal{A}=\{\text{all finite disjoint unions of sets from }\mathcal{S} \}.$$

第一步**半代数 $\mathcal{S}$ 上的有限可加测度 $\Rightarrow$ 代数 $\mathcal{A}$ 上的有限可加测度**：这一步是显然的，只需要验证定义不依赖于 $\mathcal{A}$ 作为 $\mathcal{S}$ 中集合不交并的表示方式即可。

第三步**代数 $\mathcal{A}$ 上的可数可加测度 $\Rightarrow$ $\sigma$- 域上的可数可加测度**：这一步总是可以做到的，由后面的测度扩张定理给出。

第二步**代数 $\mathcal{A}$ 上的有限可加测度 $\Rightarrow$ 代数 $\mathcal{A}$ 上的可数可加测度**：这一步并不总是可以做到。举个例子，在是整数集 $\mathbb{Z}$ 的所有子集上定义如下测度 $\mu$：若子集 $E$ 或者 $E^c$ 之一是有限集，则规定 $\mu(E)=0$，否则 $\mu(E)=1$。此测度有限可加但不是可数可加，所以也不会有可数可加的扩张。

最重要的半代数 $\mathcal{S}$ 的例子：所有形如 $\{(a, b],-\infty\leq a<b\leq \infty\}$ 的半开区间。

任何单调函数 $F$ 都可以给出其上的一个有限可加测度：$F((a, b])) = F(b) - F(a)$，从而可以扩张为代数 $\mathcal{A}$ 上的有限可加测度。**但是要使得这个测度是可数可加的，我们必须限制 $F$ 是右连续的**，这样的测度叫做 Stieltjes 测度，会在下一讲介绍。

# ✅ 3.1 Stieltjes Premeasures

本讲接着上一讲的内容，证明了当 $F$ 单调且右连续时，$\mu((a,b])=F(b)-F(a)$ 确实给出 Borel 域 $\mathcal{A}$ 上的一个可数可加测度。当然 Borel 域还是太复杂了 (虽然它们都是有限多个半开区间的不交并)，无法用可数可加的定义来验证。我们还是要回到由半开区间构成的半代数 $\mathcal{S}$ 上。

我们要从有限可加推出可数可加，而有限可加蕴涵了可数**超**可加，所以我们还缺少可数**次**可加。而 $\mathcal{A}(\mathcal{S})$ 上的可数次可加实际上可以由 $\mathcal{S}$ 上的可数次可加给出：

:::{.lemma .unnumbered}
代数 $\mathcal{A}(\mathcal{S})$ 上的有限可加测度 $\mu$ 是可数可加的，**当且仅当它限制在  $\mathcal{S}$ 上是次可数可加的**。
:::
这个话需要仔细解释清楚：$\mu$ 在 $\mathcal{S}$ 上次可数可加是指如果 $\{E_n\}$ 是半代数 $\mathcal{S}$ 中互不相交的集合，并且它们的可数并 $\uplus_{n} E_n$ 也在半代数 $\mathcal{S}$ 中，则 $\mu(\uplus_nE_n)\leq\sum_n\mu(E_n)$。

**证明概要**：$\Rightarrow$ 是显然的，可数可加必然蕴含次可数可加。

$\Leftarrow$：$\mu$ 作为 $\mathcal{A}(\mathcal{S})$ 上的有限可加测度自然是超可数可加的，要证明它可数可加，只要再证明它次可数可加：即若 $\uplus_n A_n$ 是 $\mathcal{A}(\mathcal{S})$ 中的可数不交并，则 $\mu(\uplus_n A_n)\leq\sum_n\mu(A_n)$。记住 $\uplus_n A_n$ 以及所有 $A_n$ 现在都是 $\mathcal{A}(\mathcal{S})$ 中的元素，所以 $\uplus_n A_n = \uplus_{j=1}^N E_j$，其中 $E_j\in\mathcal{S}$。于是
$$E_j = \uplus_n (A_n\cap E_j)=\uplus_n\uplus_{i=1}^{N_n}E_i^n\cap E_j.$$
利用 $\mu$ 在 $\mathcal{S}$ 上的次可数可加性有
$$\mu(E_j)\leq \sum_n\sum_{i=1}^{N_n}\mu(E_i^n\cap E_j).$$
再利用 $\mu$ 在 $\mathcal{A}(\mathcal{S})$ 上的有限可加性有
$$\sum_{i=1}^{N_n}\mu(E_i^n\cap E_j)=\mu(A_n\cap E_j).$$
于是
$$\mu(\uplus_j E_j)=\sum_{j=1}^N\mu(E_j)\leq\sum_{j=1}^N\sum_{n=1}^\infty\mu(A_n\cap E_j)=\sum_{n=1}^\infty\sum_{j=1}^N\mu(A_n\cap E_j)=\sum_{n=1}^\infty\mu(A_n).$$
即为所证。

:::{.theorem .unnumbered}
由单调右连续的函数 $F$ 给出的半代数 $\mathcal{S}=\{(a,b]\ -\infty\leq a<b\leq\infty\}$ 上的 Stieltjes 测度是次可数可加的，因而由上面引理它给出 $\mathcal{A}(\mathcal{S})$ 上的可数可加测度。
:::

**Todd-Kemp 的精彩证明讲解**：设 $(a,b]=\uplus_{i=1}^\infty (a_i, b_i]$，我们要证明 $$F(b)-F(a)=\mu((a, b])\leq\sum_{i=1}^\infty\mu((a_i,b_i])=\sum_{i=1}^\infty (F(b_i)-F(a_i)).$$
我们可以先假设 $a,b$ 都是有限的。

**不要幻想可以给区间 $(a_i,b_i]$ 之间按照大小排顺序，它们可能有无穷多个聚点**。

**想法是把 $(a, b]$ 缩小一点变成 $[a+\delta, b]$，把 $(a_i,b_i]$ 放大一点变成 $(a_i,b_i+\delta_i)$，这样可以使用紧集的有限开覆盖性质**。从而存在 $N$ 使得前 $N$ 个开区间就足以覆盖 $[a+\delta,b]$：
$$[a+\delta,b] \subseteq \cup_{j=1}^N (a_j, b_j+\delta_j).$$
现在 $\mu$ 作为一个有限可加测度，由于 $(a+\delta, b]$ 被 $\cup_{j=1}^N (a_j, b_j+\delta_j]$ 覆盖，因而必然有
$$\mu((a+\delta, b])\leq \sum_{j=1}^N \mu((a_j, b_j+\delta_j])\leq\sum_{j=1}^\infty \mu((a_j, b_j+\delta_j]).$$
上式左边等于 $F(b)-F(a+\delta)$，$\delta$ 是任意正数，所以令其趋于 0 并利用 $F$ 的右连续有 $F(a+\delta)\downarrow F(a)$，所以上式变为
$$\mu((a, b])\leq\sum_{j=1}^\infty\mu((a_j, b_j+\delta_j])=\sum_{j=1}^\infty \mu((a_j, b_j]) + \sum_{j=1}^\infty \mu((b_j, b_j+\delta_j]).$$
注意到 $\delta_j$ 也是任意的，并且 $F$ 右连续，所以对任何 $\epsilon>0$ 我们可以取 $\delta_j$ 足够小，使得
$F(b_j+\delta_j)- F(b_j) < \epsilon/2^j$。于是
$$\mu((a, b])\leq\sum_{j=1}^\infty\mu((a_j, b_j+\delta_j])=\sum_{j=1}^\infty \mu((a_j, b_j]) + \epsilon.$$
由 $\epsilon$ 任意性定理得证。


# 3.2 Outer Measure

这一节介绍了外测度的概念。

如果我们有一个集合族 $\mathcal{A}$ ($\mathcal{A}$ 一般是个代数)，以及其上的函数 $\mu:\ \mathcal{A}\to[0,+\infty]$，则我们可以定义 $2^{\Omega}$ 上的外测度 $\mu^\ast$ 为
$$\mu^\ast(E) = \inf\left\{\sum_{n=1}^\infty\mu(E_n),\ E_n\in\mathcal{A}, E\subset\bigcup_{n=1}^\infty E_n\right\}.$$
外测度 $\mu^\ast$ 满足：

> 1. $\mu^\ast(\emptyset)=0$。
> 2. 单调性。
> 3. 次可数可加性。

Todd Kemp 视频里面提到 $\mu^\ast$ 可以用来区别有限可加测度和预测度：


> 1. 如果 $(\mu, \mathcal{A})$ 是预测度，则**在 $\sigma(\mathcal{A})$ 上有 $\mu(E)\leq\mu^\ast(E)$，并且在 $\mathcal{A}$ 上有 $\mu=\mu^\ast$**。
> 2. 如果 $(\mu, \mathcal{A})$ 是有限可加测度，则**在 $\mathcal{A}$ 上有 $\mu(E)\geq\mu^\ast(E)$**。

# 4.1 Outer Pseudo-Metric

这一节介绍了 Carathéodory 测度扩张定理。设 $(\Omega,\mathcal{A},\mu)$ 是一个预测度空间。即 $\mu$ 是定义在代数 $\mathcal{A}$ 上的可数可加测度。我们将把它扩充为 $\sigma(\mathcal{A})$ 上的可数可加测度。

定义外测度 $\mu^\ast:2^\Omega\to[0,\infty]$ 为
$$\mu^\ast(E)=\inf\left\{\sum_{n=1}^\infty\mu(A_n):E\subseteq\bigcup_{n=1}^\infty A_n,A_n\in\mathcal{A}\right\}$$

:::{.theorem .unnumbered}
存在 $\sigma$- 域 $\mathcal{M}\supset\mathcal{A}$ 使得 $\mu^\ast\mid_{\mathcal{M}}$ 是可数可加测度。
:::

:::{.note}
Todd Kemp 评论说，$\mathcal{M}$ 最大可以是多大是一个非常深刻的技术问题。
:::

标准的证明途径是规定
$$\mathcal{M}=\{E\in\Omega\mid \mu^\ast(T)=\mu^\ast(T\cap E)+\mu^\ast(T\cap E^c),\forall T\in\Omega\}.$$

这里介绍了 Driver 的方法。这个方法稍微有一点缺陷，它要求 $\mu:\mathcal{A}\to[0,\infty)$ 是一个有限测度。稍后也可以扩展到 $\sigma$- 有限测度。在概率论中这足够了。


# ✅ 5.1 Radon Measures

本讲介绍了实直线上的 Radon 测度等价于 Stieltjes 测度。

Radon 测度是指对任何紧集 $K$ 有 $\mu(K)<\infty$ 的测度。这种测度的分布函数必然是单调、右连续的，从而根据之前介绍的预测度和测度扩张定理给出了实直线上的一个可数可加测度。


# ✅ 5.2 Lebesgue Measure

无要点

# ✅ 6.1 Random Variables Motivation

本节介绍了随机变量，分布函数的概念。样本空间 $\Omega$ (modelling space) 是难以接触到的，我们对其的观测是通过随机变量来进行的。

随机变量 $X$ 的分布函数为 $F(t) = \mathbb{P}(X\leq t),\, t\in\overline{\mathbb{R}}$。$F(t)$ 是单调递增且右连续的。



# ✅ 6.2 Measurable Functions

本讲介绍了测度空间上可测映射的概念。

:::{.lemma}
设 $f:\Omega\to\S$ 是一个映射，$\mathcal{A}\subset2^\S$ 是 $\S$ 中一个集合族，定义
$$f^{-1}(\mathcal{A}) = \{f^{-1}(E),E\in\mathcal{A}\}.$$
则 $\sigma(f^{-1}(\mathcal{A}))= f^{-1}(\sigma(\mathcal{A}))$。
:::

引理的证明不难， 只要注意到一个 $\sigma$- 域在映射下的像 (push forward) 和逆映射下的原像 (push back) 都是 $\sigma$- 域即可。

:::{.definition}
若 $(\O,\F)$ 和 $(\S, \B)$ 是两个可测空间，我们称 $f:\O\to\S$ 是一个可测映射，如果有 $f^{-1}(\B)\subseteq\F$。
:::

要检查一个映射是不是可测的，我们不必对每个 $B\in\B$ 都检查，只要对满足 $\sigma(\mathcal{A})=\B$ 的一个子集合族 $\mathcal{A}$ 检查有 $f^{-1}(\mathcal{A})\subseteq\F$ 即可。这是因为由上面的引理，
$$f^{-1}(\B)=f^{-1}(\sigma(\mathcal{A}))=\sigma(f^{-1}(\mathcal{A}))\subseteq\F.$$

:::{.corollary}
如果 $X_1,\ldots,X_n$ 都是测度空间 $(\O,\F)$ 上的可测函数，$f:\R^n\to\R$ 是一个连续或者 Borel 可测的多元函数，则 $Y=f(X_1,\ldots,X_n)$ 也是可测函数。
:::

**证明**：记 $X=(X_1,\ldots,X_n)$，我们要说明复合映射
$$\O\xrightarrow{\ X\ }\R^n\xrightarrow{\ f\ }\R$$
是可测的。由于 $f$ 显然可测，只要再说明 $X$ 是可测的。根据上面的引理，只要验证
$$X^{-1}\left((-\infty, t_1], (-\infty, t_2],\ldots, (-\infty, t_n]\right)=\bigcap_{i=1}^n \{X_i\leq t_i\}.$$
是可测的，这显然。$\blacksquare$


# ✅ 7.1 Robustness of Measurability

本讲主要介绍了可测函数集合在通常的运算，以及取极限的操作下得到的仍然是可测函数。

下面这个结论在整个课程中都会频繁用到：

:::{.theorem}
**Doob-Dynkin 分解** 设有限或者可数指标集 $I=\{1,\ldots,d\}$ 或者 $I=\mathbb{Z}^+$。
$$X(\omega)=(X_i(\omega))_{i\in I}\in \R^I.$$
其中每个 $X_i:(\Omega,\F)\to(\R, \B(\R))$ 都是可测函数。

设 $Y:(\Omega,\F)\to(\R,\B(\R))$ 且 $Y$ 关于 $\sigma(X_1,\ldots,X_i,\ldots)$ 可测。则存在 Borel 可测函数 $(\R^I,\B(\R^I))\to\R$ 使得
$$Y=f(X).$$
:::

**证明**：

:::{.lemma}
设 $T:\Omega\to\Omega'$ 为函数，$(\Omega,\mathcal F)$ 与 $(\Omega',\mathcal A')$ 为可测空间。函数 $f:\Omega\to[0,1]$ 关于 $\sigma(T)$ 可测，当且仅当存在 $\mathcal A'$ 可测的 $g:\Omega'\to[0,1]$ 使得
$$f=g\circ T.$$
:::

证明：由 $\sigma(T)$ 的定义，对任意 $A\in\sigma(T)$ 都存在 $A'\in\mathcal A'$ 使
$$A=T^{-1}(A').$$

**Step 1 示性函数**

若 $f=\ind_A$ 且 $A\in\sigma(T)$，取 $A'\in\mathcal A'$ 使 $A=T^{-1}(A')$，令 $g=\ind_{A'}:\Omega'\to[0,1]$，则 $g$ 可测且
$$g\circ T=\ind_{A'}\circ T=\ind_{T^{-1}(A')}=\ind_A=f.$$

**Step 2 简单函数**

若 $f=\sum_{k=1}^m a_k\ind_{A_k}$，其中 $a_k\in[0,1]$、$A_k\in\sigma(T)$。对每个 $k$ 取 $A_k'\in\mathcal A'$ 满足 $A_k=T^{-1}(A_k')$，并令
$$g:=\sum_{k=1}^m a_k\ind_{A_k'}:\Omega'\to[0,1].$$
则 $g$ 可测且 $g\circ T=f$。

**Step 3 一般可测函数**

取单调递增的简单函数列 $f_n\uparrow f$。由第二步，对每个 $n$ 存在可测 $g_n:\Omega'\to[0,1]$ 使 $f_n=g_n\circ T$。定义
$$g(x):=\sup_{n\ge1} g_n(x),\qquad x\in\Omega'.$$
对任意 $\omega\in\Omega$，
$$g\bigl(T(\omega)\bigr)=\sup_n g_n\bigl(T(\omega)\bigr)=\sup_n f_n(\omega)=f(\omega).
$$
于是 $f=g\circ T$。

**从 $[0,1]$ 推广到 $\mathbb R$**

取一个 Borel 同构 $\phi:\mathbb R\to(0,1)$（例如 $\phi(t)=\tfrac1\pi\arctan t+\tfrac12$）。若 $Y:\Omega\to\mathbb R$ 关于 $\sigma(T)$ 可测，则 $\phi\circ Y:\Omega\to(0,1)$ 亦可测。由引理存在可测 $g:\Omega'\to[0,1]$ 使
$$\phi\circ Y=g\circ T.$$
令
$$f:=\phi^{-1}\circ g:\Omega'\to\R.$$
则 $f$ Borel 可测且 $Y=f\circ T$。

**应用于 Doob–Dynkin（$\R^d$ 与 $\R^\infty$）**

取指标集 $I=\{1,\dots,d\}$（有限维）或 $I=\mathbb{Z}^+$。给定可测 $X_i:(\Omega,\F)\to(\R,\B(\R))$，定义
$$X:=(X_i)_{i\in I}:\Omega\to\mathbb R^{I}.$$
在 $\mathbb R^{I}$ 上取乘积拓扑的 Borel $\sigma$-代数 $\mathcal B(\mathbb R^{I})$。则有
$$
\sigma(X_1,X_2,\dots)=X^{-1}(\mathcal B(\mathbb R^{I})).
$$
若 $Y:\Omega\to\mathbb R$ 关于 $\sigma(X_1,X_2,\dots)$ 可测，取 $T=X$、$\Omega'=\mathbb R^{I}$、$\mathcal A'=\mathcal B(\mathbb R^{I})$，由上节得到 Borel 可测 $f:\mathbb R^{I}\to\mathbb R$ 使
$$
Y=f\bigl(X_1,X_2,\dots\bigr).
$$
上述论证对有限 $I$ 与可数 $I$ 完全一致。

:::{.note}
令 $X(\omega)=(X_i(\omega))_{i\in I}$，我们要证
$$
\sigma(X_1,X_2,\ldots)=X^{-1}\bigl(\mathcal B(\mathbb R^{I})\bigr).
\tag{$\ast$}
$$

设 $\mathcal C$ 为所有柱集的族。利用原像保持 $\sigma$-运算的事实，
$$X^{-1}\bigl(\sigma(\mathcal C)\bigr)=\sigma\bigl(X^{-1}(\mathcal C)\bigr).$$
但对任意柱集
$$
C=\prod_{i\in I}B_i\quad(\text{仅有限多 }B_i\neq\mathbb R)$$
都有
$$X^{-1}(C)=\bigcap_{i:\,B_i\neq\mathbb R} X_i^{-1}(B_i)\in \sigma(X_i:i\in I).$$
于是
$$
X^{-1}\bigl(\mathcal B(\mathbb R^{I})\bigr)
= X^{-1}\bigl(\sigma(\mathcal C)\bigr)
= \sigma\bigl(X^{-1}(\mathcal C)\bigr)
\subset \sigma(X_i:i\in I).
$$
另一方面
$$
\pi_i:\mathbb R^{I}\to\mathbb R,\qquad \pi_i\bigl((s_j)_{j\in I}\bigr)=s_i,
$$
为坐标投影。它是**连续**的。因此对任意 $B\in\mathcal B(\mathbb R)$，有
$$
\pi_i^{-1}(B)\in\mathcal B(\mathbb R^{I}).
$$
另一方面，
$$
X_i=\pi_i\circ X \quad\Rightarrow\quad
X_i^{-1}(B)=X^{-1}\bigl(\pi_i^{-1}(B)\bigr)\in X^{-1}\bigl(\mathcal B(\mathbb R^{I})\bigr).
$$
这对所有 $i$、所有 $B\in\mathcal B(\mathbb R)$ 都成立，于是由生成性得
$$
\sigma(X_i:i\in I)\subset X^{-1}\bigl(\mathcal B(\mathbb R^{I})\bigr).
$$
:::

# ✅ 7.2 Riemann-Stieltjes Integration

无要点。

# ✅ 8.1 Simple Integeration

无要点

# ✅ 8.2 Monotone convergence theorem

本讲给出了**非负可测函数积分**的定义：设 $f\in L^+$ 为非负可测函数，其积分定义为
$$\int f\du = \sup\left\{\int\varphi\du:\ \varphi\leq f,\ \varphi \text{ simple and measuable}\right\}.$$

这个定义的问题在于不容易直接得出积分的可加性：
$$\int (f+g) \du =\int f\du + \int g\du.$$

为此先证明了单调收敛定理：

:::{.theorem}
**单调收敛定理 (MCT)** 若 $\{f_n\}\in L^+$ 且 $f_n\uparrow f$，则 $\int f_n\du\uparrow \int f\du$。
:::

**证明概要**：显然 $\lim\limits_{n\to\infty}\int f_n\du$ 存在且小于等于 $\int f\du$。为了证明二者相等，只要证明对任何简单函数 $\varphi\leq f$ 有
$$\lim_{n\to\infty} \int f_n\du \geq \int \varphi\du$$
即可。**不要指望通过分析集合 $\{f_n\geq \varphi\}$ 来得出结论**，这完全可能对任何 $n$ 都是空集。但是如果可以证明对任何 $0<c<1$ 有
$$\lim_{n\to\infty} \int f_n\du \geq c \int \varphi\du$$
成立，那么令 $c\uparrow1$ 即得结论（两边都是非负的）。而集合 $E_n=\{f_n\geq c\varphi\}$ 满足 $E_n\uparrow\Omega$。于是由 $f_n\geq c\varphi\ind_{E_n}$ 以及积分单调性有
$$\int f_n\du \geq c\int\varphi\ind_{E_n}\du.$$
由于 $\varphi$ 是简单函数，所以可设 $\varphi = \sum_{k} a_k\ind_{A_k}$ 并代入上面右边，有
$$\int f_n\du \geq c\int\varphi\ind_{E_n}\du = c\sum_{k}a_k\mu(A_k\cap E_n).$$
令 $n\to\infty$ 并利用测度连续性 $\mu(A_k\cap E_n)\uparrow\mu(A_k)$ 即得
$$\lim_{n\to\infty} \int f_n\du \geq c\sum_ka_k\mu(A_k)= c \int \varphi\du.$$
单调收敛定理得证。$\blacksquare$

**MCT 告诉我们总是可以用一个只取有限多个值、每个值都有限的简单函数来逼近 $f$ 的积分**。

非负可测函数 $f$ 可以用简单函数序列
$$\varphi_n = \sum_{k=1}^{2^{2n}}\frac{k-1}{2^n}\ind_{\{\frac{k-1}{2^n}\leq f<\frac{k}{2^n}\}} + 2^n\ind_{\{f\geq 2^n\}}$$
来逼近。在第 $n$ 次切割中，我们将切割范围扩大为原来的 2 倍以逼近 $f$ 在 $\infty$ 的部分，同时将切割的间隔缩小为原来的 1/2 以保证逼近的误差是减小的。


# ✅ 9.1 Integrals and Null Sets

本讲主要是论证积分的基本结论在 $\ae$ 的情形下也都成立。此外介绍了非负可测函数列积分的 Fatou 定理，它是上一讲中单调收敛定理的直接推论：

:::{.theorem}
**Fatou 定理** 设 $f_n\in L^+$ 是非负可积函数列，则
$$\int\liminf f_n\du \leq \liminf \int f_n\du.$$
:::

**证明**：设 $g_n=\inf_{m\geq n}f_m$，则 $g_n\leq f_m$，所以
$$\int g_n\du\leq\int f_m\du,\quad n\leq m$$
从而 $\int g_n\du\leq\liminf\int f_m\du$。
另一方面 $g_n\uparrow\liminf f_n$，所以利用 MCT 有
$$\int\liminf f_n\du =\int\lim_{n\to\infty} g_n\du=\lim_{n\to\infty}\int g_n\du\leq\liminf\int f_m\du.$$
$\blacksquare$

另一个重要结论是 Borel-Cantelli 引理：

:::{.theorem}
**Borel-Cantelli (Ⅰ)** 如果 $\sum_{n=0}^\infty\mu(A_n)<\infty$，则 $\mu\{A_n,\ \io\}=0$。
:::

这个用积分很容易看出来：
$$\sum_{n=0}^\infty\mu(A_n)=\int\sum_{n=0}^\infty\ind_{A_n}\du.$$
左边如果有限，那么右边的函数必须几乎处处有限，所以 $\{A_n,\ \io\}$ 是零测集。


# ✅ 9.2 $L^1$ and the DCT

本讲引入了一般可积函数的定义，并证明了控制收敛定理。

:::{.definition}
称 $f\in\Lone$ 为可积函数，如果 $f^+,f^-$ 都是可积的：$\int f^{\pm}\du<\infty$。此时我们定义 $\int f=\int f^+-\int f^-$。或者等价地，$f$ 可积当且仅当 $\int |f|\du<\infty$。
:::

对可积函数，积分是**线性的**、**保持单调性的**。

如果我们将几乎处处相等的函数看作是同一个函数的话，$\|\cdot\|_{L^1}$ 是可积函数空间上的度量。

:::{.theorem}
**控制收敛定理** 设 $f_n, g$ 都是可积函数并且 $|f_n|\leq g$，$\lim\limits_{n\to\infty}f_n=f$。
则 $f$ 也是可积函数并且 $\lim\limits_{n\to\infty}\int f_n=\int f$。
:::

**证明概要**：显然 $|f|\leq g$，所以 $f$ 可积，从而由线性性质 $g\pm f$ 都是可积的。对可积函数序列 $g\pm f_n$ 使用 Fatou 引理，有
$$\int (g\pm f)\du=\int\varliminf_{n\to\infty} (g\pm f_n)\du\leq \varliminf_{n\to\infty}\int (g\pm f_n)\du = \int g\du\pm\varliminf_{n\to\infty}\int f_n\du.$$
比较两边有
$$\int (g\pm f)\du \leq \int g\du \pm \varliminf_{n\to\infty}\int f_n\du.$$
消去 $g$ 的积分，并注意对任何实数列 $\{a_n\}$ 有 $\varliminf\limits_{n\to\infty}(-a_n)=-\varlimsup\limits_{n\to\infty} a_n$，从而
$$\varlimsup\int f_n\du \leq \int f\du \leq \varliminf\int f_n\du.$$
即得结论。

# ✅ 10.1 Integrals and Derivatives

这一讲介绍了在何种条件下，可以在积分号下对参数求导。

我把视频中的结论作了一些加强，实际上是等价的：

:::{.theorem}

1. $f(t, \cdot)$ 对每个 $t$ 都是可测的，而且是 $L^1$ 可积的；
2. $\frac{\partial f}{\partial t}(t,\omega)$ 对几乎处处的 $\omega$ 有定义；
3. $|\frac{\partial f}{\partial t}(t,\omega)|\le g(\omega)$ 对某个 $g\in L^1$ 几乎处处成立。

则
$$\frac{\mathrm d}{\mathrm d t}\int f(t,\omega)\,\mu(\mathrm d\omega)=\int \frac{\partial f}{\partial t}(t,\omega)\,\mu(\mathrm d\omega).$$
:::

注意：对所有的 $t$，使得 2, 3 成立的那些 $\omega$ 组成的集合必须是固定的，不能随着 $t$ 变化而变化。反例：$(0,1)$ 上的 Lebesgue 测度，$f(t,\omega)=\ind_{\{\omega\le t\}}$。


# ✅ 11.1 The Radon-Nikodym Theorem

本讲介绍了 Radon-Nikodym 定理，不过没有给出证明。

**Motivation**: 设 $\mu,\nu$ 是两个测度，是否存在非负可测函数 $\rho$ 使得 $\nu(A)=\int_A\rho\du$ 对任何可测集 $A$ 成立？

**必要条件**：$\mu(A)=0\Rightarrow\nu(A)=0$。这时我们称 $\nu$ 关于 $\mu$ **绝对连续**，记作 $\nu\ll\mu$。

此条件同样也是充分的：若 $\nu$ 关于 $\mu$ 绝对连续，则存在 $\rho$ 使得 $\rho=\dfrac{\mathrm{d}\nu}{\mathrm{d}\mu}$。

**奇异连续测度的例子**：Cantor 函数 (devil staircase)。[YouTube 科普](https://www.youtube.com/watch?v=dQXVn7pFsVI)。此函数没有点质量，也没有密度函数，但是确实给出一个全质量为 1 的概率测度。

+ 此函数是连续递增的，所以是一个分布函数。
+ 此函数是连续的，所以没有点质量，即单个点的测度是 0。
+ 此函数是奇异的，因为它在除去 Cantor 集对应的点之外几乎处处是常数。


# ✅ 11.2 Probability Laws Revisited

:::{.theorem}
**积分的变量替换定理** 设 $X:\ (\Omega,\mathcal{F},\mu)\to(\mathcal{S},\mathcal{B})$ 是一个可测映射，$(\mathcal{S},\mathcal{B})$ 上的测度 $\nu$ 由 $\nu(E) = \mu(X^{-1}(E))$ 给出，$g:\ (\mathcal{S},\mathcal{B},\nu)\to\mathbb{R}$ 是一个可积函数，则 $$\int_{\Omega}g\circ X\du=\int_{\mathcal{S}}g\dv.$$
:::

示意图：

$$\underbrace{\Omega\xrightarrow{\ X\ }\overbrace{S\xrightarrow{\ g\ }\R}^{\int_{\S}g\dv}}_{\int_{g\circ X\du}}.$$

**证明概要**：首先考察 $g=\ind_B,\,B\in\B$ 是指标函数的情形。
$$\int_{\S} g\dv = \nu(B) = \mu(X^{-1}(B))=\int_{\O}\ind_{X^{-1}(B)}\du.$$
由于 $\omega\in X^{-1}(B)\Leftrightarrow X(\omega)\in B$，所以 $\ind_{X^{-1}(B)} = \ind_{B}\circ X$，所以上式右边的积分等于 $$\int_{\O}\ind_{B}\circ X\dv.$$
此时结论成立。根据积分的线性性质结论对简单函数也成立，从而进一步取极限可得对任何可积函数 $g$ 都成立。

# ✅ 12.1 $L^2$

无要点

# ✅ 12.2 The Weak Law of Large Numbers (WLLN)

这一讲证明了弱大数定律，即当 $\{X_n\}$ 是 $L^2$ 可积的 i.i.d 序列时有
$$\P\left(|\frac{S_n}{n} - a|\geq \epsilon\right) = O(\frac{1}{n}).$$

# ✅ 13.1 Convergence in measure

本讲介绍了可测函数的依测度收敛概念，及其与逐点收敛之间的联系。

:::{.definition}
称 $f_n\to_{\mu} f$ 为依测度收敛，如果对任意 $\epsilon >0$ 有
$$\lim_{n\to\infty}\mu\{|f_n-f|\geq0\}=0.$$
:::

**依测度收敛但不处处收敛的例子**：将区间 $[0, 1]$ 等分为 $2^n$ 份，将它们的指标函数排成一排，再对所有 $n$ 将这些片段排列起来得到序列 $f_n$，则 $f_n$ 依测度收敛到 0 但不逐点收敛。

**接下来是一个将测度和逐点收敛联系起来的重要技巧**：根据几乎处处收敛的定义，$f_n\to f,\ae$ 收敛即要求对任何 $\epsilon>0$ 有
$$\mu\{|f_n-f|\geq\epsilon,\ \io\} = 0.$$
这样就可以把逐点收敛和测度联系起来。有时候我们还可以使用更强的条件：
$$\mu\{|f_n-f|\geq 2^{-n},\ \io\} = 0.$$
这是因为对任何 $\epsilon$，$n$ 足够大时 $2^{-n}<\epsilon$, 从而 $\{|f_n-f|\geq\epsilon\}\subseteq\{|f_n-f|\geq 2^{-n}\}$，前者发生无穷多次自然意味着后者也发生无穷多次。这样就可以和 Borel-Cantelli 引理结合起来使用，只要
$$\sum_{n}\mu\{|f_n - f|\geq 2^{-n}\} < \infty,$$
就可以保证 $\{f_n\}$ 是几乎处处收敛的。

:::{.theorem}
逐点收敛可以推出依测度收敛。
:::

**简要证明**：对任何 $\epsilon>0$，记 $A_n=\{|f_n-f|\geq\epsilon\}$，则
$$\mu\{A_n,\ \io\} = \lim_{n\to\infty}\mu(\bigcup_{k\geq n}A_k)\geq \lim_{n\to\infty}\mu(A_n).$$

:::{.theorem}
设 $\{f_n\}$ 为依测度收敛的 Cauchy 序列：
$$\lim_{n,m\to\infty}\mu\{|f_n-f_m|\geq\epsilon\} = 0.$$
则 $f_n$ 必有逐点收敛的子序列 $f_{n_k}\to f\ \mathrm{a.e.}$，并且 $f_n$ 依测度收敛到 $f$。
:::

**必有逐点收敛的子序列**：利用上面介绍的技巧，归结为抽取子序列 $\{f_{n_k}\}$ 满足
$$\mu\{|f_{n_{k+1}} - f_{n_k}|\geq2^{-k},\ \io\} = 0.$$
利用 Borel-Cantelli 引理这只要让 $\sum_{k=1}^\infty\mu\{|f_{n_{k+1}} - f_{n_k}|\geq 2^{-k}\}<\infty$ 即可。为此又只要让 $\mu\{|f_{n_{k+1}} - f_{n_k}|\geq 2^{-k}\}\leq 2^{-k}$ 即可。根据 Cauchy 条件这是可以做到的。

**子序列的极限也是原序列的依测度极限**：对任何 $n$，取 $n_{k}>n$ 则有
$$\{|f_n-f|\geq\epsilon\}\subseteq \{|f_n-f_{n_k}|\geq\epsilon/2\}\cup \{|f_{n_k}-f|\geq\epsilon/2\}.$$
显然 $n$ 足够大时右边两个集合测度都趋于 0。


# ✅ 13.2 $L^p$ is Complete

首先我们来证明 $L^p$ 收敛可以推出依测度收敛。

:::{.theorem}
$L^p$ 度量是完备的，任何 Cauchy 序列必有极限。
:::

**证明概要**：$L^p$ Cauchy 列也都是依测度 Cauchy 列，从而有几乎处处收敛的子序列 $f_{n_k}\to f$。对固定的 $k$，当 $j>k$ 时有
$$\begin{align*}\int\|f_{n_k}-f\|^p\du&=\int\lim_{j\to\infty}\|f_{n_k}-f_{n_j}\|^p\du\leq\liminf_{j\to\infty}\int\|f_{n_k}-f_{n_j}\|^p\du\\
&\leq\limsup_{j\to\infty}\int\|f_{n_k}-f_{n_j}\|^p\du.\end{align*}$$
两边令 $k\to\infty$ 并利用 Cauchy 条件即得子序列 $f_{n_k}\xrightarrow{L^p}f$。再利用 Cauchy 条件可得原序列 $f_n\xrightarrow{L^p} f$。

:::{.theorem}
**依测度控制收敛定理** 设 $f_n$ 依测度收敛到 $f$，且 $|f_n|\leq f,\, f\in L^1$。则 $f_n\xrightarrow{L^1} f$。
:::

**证明概要**：假设 $f_n$ 不 $L^1$ 收敛到 $f$，则对任何 $\epsilon>0$，存在子序列 $f_{n_k}$ 满足：

+ $\|f_{n_k} - f\|_{L^1}\geq\epsilon$。
+ $f_{n_k}$ 几乎处处收敛到 $f$。

这与控制收敛定理矛盾。


# ✅ 14.1 Dynkin's Multiplicative Systems Theorem

本讲介绍了 Dynkin $\pi-\lambda$ 定理的函数形式的版本。

:::{.definition}
设 $(\Omega,\mathcal{F})$ 是一个可测空间，$f$ 是可测函数。如果存在 $M>0$ 使得
$$|f|\leq M,\quad \ae$$
成立，就称 $f$ 是一个有界可测函数。记 $\mathbb{B}(\Omega,\mathcal{F})$ 为全体有界函数构成的向量空间。若 $\{f_n\}\in\mathbb{B}(M,\F)$ 满足
$$|f_n|\leq M,\ \ae \quad \forall n$$
并且
$$\lim_{n\to\infty} f_n = f,\quad \ae$$
就称 $\{f_n\}$ **一致有界收敛到 $f$**。
:::

:::{.theorem}
设 $\H\subset\mathbb{B}(\Omega)$ 是一个向量空间，包含常函数 $\ind_\Omega$，并且在有界收敛下封闭。又设 $\M\subset\H$ 是一个乘法系：$f,g\in\M\Rightarrow f\cdot g\in\M$。则 $\H$ 包含所有关于 $\sigma(\M)$- 可测的有界可测函数：
$$\mathbb{B}(\Omega,\sigma(\M))\subset \H.$$
:::

**证明**：设 $\H=\H(\M)$ 是包含 $\M$ 和 1 的向量空间。且在有界收敛下封闭。

**Step 1 $\H$ 是一个代数**

固定 $f\in\H$，记 $\H^f =\{g\in\H\mid f\cdot g\in\H\}$。

+ $\H^f$ 是 $\H$ 的子空间
+ $\H^f$ 包含常数 1
+ $\H^f$ 在有界收敛下封闭

特别地，如果 $f\in\M$，由定义 $\M\subset\H^f$。所以
$$\H=\H(\M)\subset \H^f\subset \H.$$
即 $\H=\H^f$。但根据 $f$ 的任意性，这正说明对任何 $f,g\in\H$ 都有 $f,g\in\H$。从而 $\H$ 是一个代数。

**Step 2 $\F=\{A\subset\Omega\mid \ind_A\in \H\}$ 是 $\sigma$- 域**

这一步很容易

**Step 3 $\mathbb{B}(\Omega,\F)\subset\H$**

$\F$ 中的示性函数都在 $\H$ 中，从而简单函数也在 $\F$ 中。又因为有界收敛封闭，所以有界函数的 $f^+,f^-$ 也在 $\F$ 中，从而 $f$ 在 $\F$ 中。

**Step 4 $\sigma(\M)\subset \F$**

根据
$$\sigma(\M) = \sigma(\cup\{ f^{-1}\B(\R), f\in\M\})=\sigma(\ \bigcup\{f^{-1}(a,+\infty)\mid a\in\R, f\in\M\ \}).$$
所以我们只要证明所有形如 $\ind_{\{f>a\}},\forall f\in\M,a\in\R$ 的函数在 $\H$ 中即可。
设 $|f|\leq M$。首先我们构造连续函数列 $\psi_n\uparrow\ind_{(a,+\infty)}$，这总是可以的：

$$\psi_n(t)=\begin{cases}0,& t\le a\\
n(t-a), & a < t < a+1/n\\
1, & t\geq a+1/n
\end{cases}$$
故
$$\psi_n(f)\uparrow \ind_{\{f > a\}}.$$

由于 $\psi_n$ 在紧集 $[-M,M]$ 上连续，由 Weierstrass 逼近定理，存在多项式 $p_{n,k}$ 使得
$$\sup_{|t|\le M}|p_{n,k}(t)-\psi_n(t)|\leq\frac{1}{k}.$$
因为 $0\leq\psi_n\leq 1$，就有
$$\sup_{|t|\le M}|p_{n,k}(t)|\leq \sup_{|t|\le M}|\psi_n(t)|+\frac{1}{k} \le 2.$$
于是对所有 $n,k$ 有
$$\|p_{n,k}(f)\|_\infty \leq 2.$$

因为 $\H$ 是代数且 $f\in\M$，故 $p_{n,k}(f)\in\H$。
又根据 $p_{n,k}(f)\to \psi_n(f)$ 是有界收敛，所以 $\psi_n(f)\in\H$。再根据 $\psi_n(f)\uparrow \ind_{\{f>a\}}$ 也是有界收敛，得到结论。$\blacksquare$

:::{.corollary}
$\sigma(C_c(\R)) = \sigma(\mathbb{\R})$。
:::


:::{.corollary}
设 $\mu,\nu$ 是 $\R$ 上的 Borel 概率测度，并且对任何 $f\in C_c(\R)$ 都有
$$\int f\du = \int f\dv$$
成立，则 $\mu=\nu$。
:::
设 $\H$ 是使得上面积分相等的全体有界函数成立的集合，则 $\H$ 包含常数 1，在有界收敛下封闭，还包含乘法系 $C_c(\R)$，从而 $\H$ 包含所有的 $\mathbb{B}(\R, \sigma(C_c(\R)))=\mathbb{B}(\R, \B(\R))$。特别地，对任何 Borel 可测集 $E$ 有 $\ind_E\in\B(\R)\subset\H$，从而
$$\mu(E) = \int \ind_E\du = \int \ind_E\dv = \nu(E).$$


# ✅ 14.2 Product Measure

本讲介绍了乘积测度的构造。**记住乘积测度的构造是用到重积分的**。

**可测空间的乘积**：设 $(\Omega_1,\mathcal{F_1}),\,(\Omega_2,\mathcal{F_2})$ 是两个可测空间，其乘积空间定义为 $(\Omega_1\times\Omega_2,\,\sigma(\mathcal{F}_1\times\mathcal{F}_2))$。其中 $\mathcal{F}_1\otimes\mathcal{F}_2=\sigma(\mathcal{F}_1\times\mathcal{F}_2)$ 是由所有形如 $\{A_1\times A_2, A_i\in\mathcal{F}_i\}$ 的集合生成的 $\sigma$- 域。

$\mathcal{F}_1\otimes\mathcal{F}_2$ 还有一种等价的刻画：它是使得投影映射 $\pi_i(\omega_1,\omega_2)=\omega_i$ 均可测的最小 $\sigma$- 域。

:::{.lemma}
随机向量 $f:(\Omega, \mathcal{F})\to(\R^d,\B(\R^d))$ 是可测的，当且仅当其每个分量 $f_i$ 是可测的。
:::
**证明**：
x
$\Rightarrow$: 每个 $f_i=\pi_i\circ f$ 作为两个可测映射的复合当然是可测的。

$\Leftarrow$: 本质是证明如果每个 $X_i$ 都是随机变量，则 $X=(X_1,\ldots,X_n)$ 是随机向量。对任何形如 $E=E_i\times_{j\ne i}\B_i(\R)$ 的集合，$X^{-1}(E) =\{\omega\in\Omega: X_i(\omega)\in E_i\}$ 是可测集，而这样的 $E$ 生成了 $\B(\R^d)$，所以 $X^{-1}(E)$ 对任何 $E\subset\B(\R^d)$ 都可测。结论得证。

如果每个 $(\Omega_i,\F_i)$ 还是测度空间，其上的测度为 $\mu_i$，则我们可以在 $(\Omega_1\times\Omega_2,\F_1\otimes\F_2)$ 上定义测度 $\mu_1\otimes\mu_2$ 使得 $(\mu_1\otimes\mu_2)(E_1\times E_2)=\mu_1(E_1)\mu_2(E_2)$ 对任何 $E_i\in\F_i,\, i=1,2$ 成立。

实际上我们可以让这个乘积测度满足

$$\int_{\Omega_1\times\Omega_2}f_1\otimes f_2\mathrm{d}(\mu_1\otimes\mu_2) = \int_{\Omega_1}f_1\mathrm{d}\mu_1\cdot\int_{\Omega_2}f_2\mathrm{d}\mu_2.$$

首先我们假定 $\mu_1,\mu_2$ 都是有限测度。构建完毕以后再扩展到 $\sigma$- 有限的测度上去。

:::{.theorem}
设 $f$ 是一个非负的，关于 $(\Omega_1\times\Omega_2,\F_1\otimes\F_2)$ 可测的函数，则

1. $f(\cdot,\omega_2)$ 对任何 $\omega_2$ 都是 $\F_1$ 可测的。
2. $f(\omega_1,\cdot)$ 对任何 $\omega_1$ 都是 $\F_2$ 可测的。
3. $\int_{\Omega_2}f(\cdot,\omega_2)\mu_2(\mathrm{d}\omega_2)$ 是 $\F_1$ 可测的。注意这个积分值可能是无穷。
4. $\int_{\Omega_1}f(\omega_1,\cdot)\mu_1(\mathrm{d}\omega_1)$ 是 $\F_2$ 可测的。
5. $$\int_{\Omega_1}\left(\int_{\Omega_2}f(\omega_1,\omega_2)\mu_2(\mathrm{d}\omega_2)\right)\mu_1(\mathrm{d}\omega_1)=\int_{\Omega_2}\left(\int_{\Omega_1}f(\omega_1,\omega_2)\mu_1(\mathrm{d}\omega_1)\right)\mu_2(\mathrm{d}\omega_2).$$
:::

**证明**：我们先来验证结论对形如 $f_1\otimes f_2$ 的函数成立。

1. $f(\cdot,\omega_2) = f_1(\cdot)f_2(\omega_2)$ 当然是 $\F_1$ 可测函数。
2. 同 1。
3. $\int_{\Omega_2}f(\cdot,\omega_2)\mu_2(\mathrm{d}\omega_2)=f_1(\cdot)\int_{\Omega_2}f_2(\omega_2)\mu_2(\mathrm{d}\omega_2)$。
4. 同 3.
5. 两边都等于 $\int_{\Omega_1}f_1(\omega_1)\mu_1(\mathrm{d}\omega_1)\cdot\int_{\Omega_2}f_2(\omega_2)\mu_2(\mathrm{d}\omega_2)$。

令 $\H$ 是所有满足定理中条件的函数组成的集合，$\M$ 是所有形如 $\f_1\otimes f_2$ 的非负可测函数组成的集合。则 $\M$ 是乘法系。又因为 $\M$ 包含所有形如 $\ind_{B_1}\otimes\ind_{B_2}$ 的函数，所以 $\sigma(\M)=\F_1\otimes\F_2$。

又 $\H$ 是向量空间，包含 $\{1\}\cup\M$，并且在有界收敛下封闭。（对 5 需要用两次控制收敛定理或者非负函数的单调收敛定理）,所以根据 Dynkin 乘法系引理，$\H$ 包含所有 $\F_1\otimes\F_2$ 可测的有界函数（或者非负函数）。$\blacksquare$

由此我们可以定义乘积空间中的测度为

$$\mu(E)=\int_{\Omega_1}\left(\int_{\Omega_2}\ind_{E}\mu_2(\mathrm{d}\omega_2)\right)\mu_1(\mathrm{d}\omega_1)=\int_{\Omega_2}\left(\int_{\Omega_1}\ind_{E}\mu_1(\mathrm{d}\omega_1)\right)\mu_2(\mathrm{d}\omega_2).$$
不难验证这样定义的积分是有限可加的 (积分的线性性质)，可以取单调上升的极限，所以是可数可加的，并且当 $E$ 形如 $E_1\times E_2$ 时有 $\mu(E)=\mu_1(E_1)\mu_2(E_2)$，从而确实给出符合要求的乘积测度。

# ✅ 14.3 Tonelli-Fubini

:::{.theorem}
**Tonelli 定理**
如果 $f\in(\Omega_1\times\Omega_2,\F_1\otimes\F_2)$ 是**非负可测**的，则
$$\int_{\Omega_1\times\Omega_2} f\,\mathrm{d}(\mu_1\times\mu_2)
=\int_{\Omega_1}\left(\int_{\Omega_2} f\,\mathrm{d}\mu_2\right)\,\mathrm{d}\mu_1
=\int_{\Omega_2}\left(\int_{\Omega_1} f\,\mathrm{d}\mu_1\right)\,\mathrm{d}\mu_2.$$
:::

上一讲里面已经证明了右边两者相等。要把左边也连上，只需补一句标准话：用非负简单函数递增逼近 $f$，对简单函数这三者相等（按照乘积测度的定义，它就是集合示性函数的分部积分），再用单调收敛定理把等式传到极限。


令一般可测 $f$ 可积：$\int |f|\,\mathrm{d}(\mu_1\times\mu_2)<\infty$，写
$f=f^+-f^-$。

1. 由 Tonelli 可得
   $$
   \int |f|\, \mathrm d(\mu_1\times\mu_2)
   =\int\left(\int |f(\omega_1,\omega_2)|\,\mathrm d\mu_2\right)\,\mathrm d\mu_1
   =\int\left(\int |f(\omega_1,\omega_2)|\,\mathrm d\mu_1\right)\,\mathrm d\mu_2<\infty.
   $$
   因而对 $\mu_1$-几乎处处的 $\omega_1$，截面 $f(\omega_1,\cdot)\in L^1(\mu_2)$；同理交换坐标亦然。
2. 再对 $f^\pm$ 分别应用上一节的等式并相减，得到
   $$
   \int_{\Omega_1\times\Omega_2} f\, \mathrm d(\mu_1\times\mu_2)
   =\int_{\Omega_1}\left(\int_{\Omega_2} f\,\mathrm d\mu_2\right)d\mu_1
   =\int_{\Omega_2}\left(\int_{\Omega_1} f\,\mathrm d\mu_1\right)d\mu_2.
   $$
   且两个迭代积分都有限。这就是 **Fubini 定理**。

# ✅ 15.1 Independence

本讲介绍了事件和 $\sigma$- 域之间的独立性概念。

要点总结：

1. 若干个事件 $\{A_n\}$ 独立不是指它们两两独立，而是其中任何有限多个子事件都独立。
2. 验证若干 $\sigma$- 域 $\{\mathcal{F}_i\}$ 独立只需要验证生成它们的 $\pi$- 系 $\{C_i:\ \mathcal{F}_i=\sigma(C_i)\}$ 独立。

:::{.theorem}
**Borel-Cantelli 引理 II** 设 $\{A_n\}$ 是独立的事件列，则若 $\sum_{n=1}^\infty\P(A_n)=\infty$，则 $\P(\{A_n, \io\})=1$。
:::

想法还是要用独立性，转到事件的交上去。

$$\P(\{A_n,\ \io\})=\P(\bigcap_{n=1}^\infty\bigcup_{k\geq n}A_k)=\lim_{n\to\infty}\P(\bigcup_{k\geq n}A_k).$$
观察两边，要想用上独立性，就得取补：
$$1-\P(\bigcup_{k\geq n}A_k)=\P(\bigcap_{k\geq n}A_k^c)=\lim_{M\to\infty}\prod_{k=n}^M\P(A_k^c)=\lim_{M\to\infty y}\prod_{k=n}^M(1-\P(A_k)).$$
利用 $1-x\leq e^{-x}$ 有
$$\lim_{M\to\infty}\prod_{k=n}^M(1-\P(A_k))\leq\lim_{M\to\infty}\prod_{k=n}^Me^{-\P(A_k)}=\lim_{M\to\infty}e^{-\sum_{k=n}^M\P(A_k)}.$$
上式右边对任何固定的 $n$ 其极限都是 0，从而 $\P(\bigcup_{k\geq n}A_k)\to1$，结论得证。$\blacksquare$


# ✅ 15.2 Independent Random Variables

上一讲介绍了独立事件和独立事件域的概念，这一讲介绍了独立随机变量的概念。

:::{.theorem}
一族随机变量 $\{X_i\}_{i\in I}$ 称作是独立的，如果它们的 $\sigma-$ 域 $\{\sigma(X_i)\}_{i\in I}$ 是独立的。
:::

由于 $\sigma(X_i)$ 可以由 $\pi-$ 系 $\{X_i\in(-\infty, t_i]\}$ 生成，所以只要验证这个 $\pi$- 系的独立性即可。

:::{.theorem}
设 $X=(X_1,\ldots,X_n)$，其中每个 $X_i:(\O,\F,\P)\to(\S_i,\B_i)$ 是随机变量，$\mu_X$ 是 $\B_1\otimes\cdots\otimes\B_n$ 上的测度: $\mu_X(B)=\P(X\in B)$。则 $X_1,X_2,\ldots,X_n$ 独立当且仅当 $\mu_X=\mu_{X_1}\otimes\cdots\otimes\mu_{X_n}$。
:::

**证明**：$\Leftarrow$:

$$\begin{align*}\P(X_1\in B_1,\ldots,X_n\in B_n)&=\mu_X(B_1\times \cdots\times B_n)\\
&=\mu_{X_1}(B_1)\cdots\mu_{X_n}(B_n)\\
&=\P(X_1\in B_1)\cdots\P(X_n\in B_n).\end{align*}$$

$\Rightarrow$: 简单。

:::{.corollary}
如果 $X_1,X_2,\ldots,X_n$ 都是 $L^1$ 可积的随机变量，则 $X_1X_2\cdots X_n\in L^1$ 且 $\E[X_1\cdots X_n]=\E[X_1]\cdots\E[X_n]$。
:::

首先对 $|X_1X_2\cdots X_n|$ 用 Tonelli 定理得出 $|X_1X_2\cdots X_n|$ 可积，然后再对 $X_1X_2\cdots X_n$ 用 Fubini 定理。

:::{.corollary}
如果 $X_1,\ldots,X_n,Y_1,\ldots,Y_m$ 是一组独立的随机变量，则 $f(X_1,\ldots,X_n)$ 和 $g(Y_1,\ldots,Y_m)$ 也是独立的。
:::

这是因为 $\sigma(f(X_1,\ldots,X_n))\subseteq\sigma(X_1,\ldots,X_n)$，$\sigma(g(Y_1,\ldots,Y_m))\subseteq\sigma(Y_1,\ldots,Y_m)$，所以也是独立的。

# ✅ 16.2 Kolmogorov's Extension Theorem, Part 2

回忆一个 Radon 测度是指，它是一个有限的 Borel 测度，并且满足内外的正则性：从内部可以用紧集任意逼近，从外部可以用开集任意逼近。

:::{.theorem}
$\R^d$ 上的任何有限 Borel 测度都是 Radon 测度。
:::

**证明**：设 $\F$ 是所有可以从外部被开集任意逼近的那些子集构成的集合。我们要证明 $\F$ 包含 $\B(\R^d)$。

1. $\F$ 包含所有闭集。实际上对闭集 $F$，令 $G_\epsilon=\cup_{x\in F}B(x,\epsilon)$，则 $G_\epsilon\downarrow \overline{F}=F$。从而由测度连续性即得。
2. $\F$ 对有限集合运算封闭，从而 $\F$ 是一个代数。
3. $\F$ 对可数不交并封闭。

由此即得结论。$\blacksquare$


# ✅ 17.1 Kolmogorov's 0-1 Law

本讲介绍了独立随机变量序列的尾事件，以及 Kolmogrov 0-1 律。

设 $\{X_n\}$ 是独立的随机变量序列 (不是两两独立，而是任何有限多个都独立)称 $\mathcal{T}=\cap_{n=1}^\infty\sigma(X_n,X_{n+1},\ldots)$ 为尾事件域。

:::{.theorem}
**Kolmogrov 0-1 律** 对任何 $A\in\mathcal{T}$ 有 $\mathbb{P}(A)\in\{0,1\}$。
:::

**证明概要**：

+ $\sigma(X_1,\ldots,X_n)$ 和 $\sigma(X_{n+1},X_{n+2},\ldots)$ 是独立的。因为考虑如下两个集合族：
$$\{\text{all finite intersections like }\cap A_i, A_i\in\sigma(X_i),i=1,2,\ldots,n\}.$$
$$\{\text{all finite intersections like }\cap A_j, A_j\in\sigma(X_j),j=n+1,n+2,\ldots\}.$$
这俩都是 $\pi$- 系且互相独立，所以它们生成的 $\sigma$- 域也独立。前者可以生成 $\sigma(X_1,\ldots,X_n)$，后者可以生成 $\sigma(X_{n+1},X_{n+2},\ldots)$。
+ 于是 $\sigma(X_1,\ldots,X_n)$ 和 $\mathcal{T}$ 是独立的。
+ 于是 $\cup_{n=1}^\infty\sigma(X_1,\ldots,X_n)$ 作为代数，当然也是 $\pi$- 系，和 $\mathcal{T}$ 是独立的。
+ 于是 $\sigma$- 域 $\sigma(X_1,\ldots,X_n,\ldots)$ 和 $\mathcal{T}$ 独立，从而 $\mathcal{T}$ 和 $\mathcal{T}$ 独立，从而得证。

$\blacksquare$

:::{.proposition}
设 $\{X_i\}_{i=1}^\infty$ 是一个随机变量的无限序列，如果 $Y$ 是 $\sigma(X_1,X_2,\ldots)$ 可测的，且 $Y$ 有界，则对任何 $\epsilon>0$，都存在 $N$ 和 Borel 可测的有界函数 $F:\R^N\to\R$ 使得
$$\E|Y - F(X_1,\ldots,X_N)|<\epsilon,\quad \ae$$
:::

**证明**：记 $Y_n=\E[Y\mid\sigma(X_1,\ldots,X_n)]$，则 $\{Y_n\}$ 是一致可积鞅，且在 $L^1$ 范数下收敛到 $Y$。每个 $Y_n$ 根据 Doob-Dynkin 引理都形如 $Y_n=F(X_1,\ldots,X_n)$。此即为结论。

或者也可以这样证：先取简单函数
$$\varphi = \sum_{k=1}^n a_k\ind_{A_k},\quad A_k\in\B(\R^{\mathbb{N}})$$
满足 $|Y -\varphi|_1<\epsilon/2$。然后记 $M=\max\{|a_1|,\ldots,|a_k|\}$。对每个 $A_k$，取柱集 $C_k$ 使得
$$\mu(A_k\Delta C_k) < \frac{\epsilon}{2nM}.$$
于是
$$\left| \sum_{k=1}^n a_k\ind_{A_k} -  \sum_{k=1}^n a_k\ind_{C_k}\right|\leq  \sum_{k=1}^n |a_k| |\ind_{A_k}-\ind_{C_k}|= \sum_{k=1}^n |a_k|\ind_{A_k\Delta C_k}\leq M \sum_{k=1}^n\ind_{A_k\Delta C_k}.$$
右边函数每一项的积分 $<\epsilon/2n$，全部 $n$ 项合起来的积分 $<\epsilon$，所以简单函数 $ \sum_{k=1}^n a_k\ind_{C_k}$ 就是所求的 $F$。$\blacksquare$


# ✅ 17.2 Convolution

本讲介绍了概率测度之间的卷积。

:::{.definition}
两个概率测度 $\mu,\nu$ 之间的卷积定义为
$$\mu\ast \nu(B) = \int_{\R^d\times\R^d}\ind_B(x+y)\mu\otimes\nu(\dx\dy)=\int_{\R^d}\mu(B-y)\vd{y}.$$
:::

# ✅ 18.1 Strong Law of Large Numbers, Part 1

本讲介绍了 Kolmogrov 强大数定理的表述，以及证明思想。

基本思想是利用截断的序列与原序列是尾等价的，先对截断的序列证明结论，再回到原序列。

:::{.theorem}
**强大数定理** 设 $\{X_n\}$ 是 $\iid$ 的 $L^1$ 序列且 $\E [X_n]=a$，则 $\dfrac{S_n}{n}\to a, \ae$。
:::

:::{.definition}
同一个概率空间上的两个随机变量序列 $\{X_n\},\,\{Y_n\}$ 称作是尾等价的，如果
$$\sum_{n=1}^\infty\mathbb{P}(X_n\ne Y_n)<\infty.$$
:::

这样根据 Borel-Cantelli 引理，$\{X_n\ne Y_n\,\io\}$ 是零测集，从而 $X_n=Y_n$ 最终会几乎处处成立，从而二者的极限行为一致。

:::{.corollary}
如果 $\{X_n\}$ 和 $\{Y_n\}$ 是尾等价的，$b_n\uparrow\infty$，则
$$\lim\limits_{n\to\infty}\dfrac{1}{b_n}\sum_{j=1}^n X_n = X \Leftrightarrow \lim\limits_{n\to\infty}\dfrac{1}{b_n}\sum_{j=1}^n Y_n = X.$$
:::

:::{.lemma}
若 $X\in L^1,\,\epsilon>0$，则 $$\sum_{n=1}^\infty\mathbb{P}(X\geq n\epsilon) \leq\frac{1}{\epsilon}\mathbb{E}|X|.$$
:::

值得与 Markov 不等式比较一下，这个不等式更强。

**证明概要**：只要证明结论对 $\epsilon=1$ 成立即可。对任意实数 $x\ge 0$，我们有
$$\sum_{n=1}^{\infty}\ind_{[n,\infty)}(x)= \sharp\{n\in\mathbb{Z}_+\mid n\le x\}= \lfloor x\rfloor
\le x.$$
对 $|X|$ 使用上式得
$$\sum_{n=1}^{\infty}\ind_{[n,\infty)}(|X|)\le |X|.$$
两边求期望即得
$$\sum_{n=1}^\infty\P(|X|\ge n)\le \E|X|.$$
$\blacksquare$

:::{.corollary}
若 $\{X_n\}$ 是 $\iid$ 的 $L^1$ 序列，令 $Y_n = X_n\ind_{\{|X_n|\leq n\}}$，则 $\{Y_n\}$ 与 $\{X_n\}$ 是尾等价的。
:::

**证明**：
$$\sum_{n=1}^\infty\P(X_n\ne Y_n)=\sum_{n=1}^\infty\P(|X_n|>n)=\sum_{n=1}^\infty\P(|X_1|>n)\le\E|X_1|<\infty.$$
$\blacksquare$

于是接下来的任务就是证明 $S_n^Y = \dfrac{Y_1+\cdots+Y_n}{n}\to a,\,\ae$。


# ✅ 18.2 Kolmogorov's Convergence Criterion

本讲介绍了 Kolmogrov 收敛判定：独立随机变量序列如果是 $L^2$ 意义下的 Cauchy 序列，则也是逐点收敛意义下的 Cauchy 序列。

在上一讲中，我们通过把 $L^1$ 的序列 $\{X_n\}$ 取截断得到 $Y_n=X_n\ind_{\{|X_n|\leq n\}}$，这是一个与 $\{X_n\}$ 尾等价的序列。从而只要证明 $\frac{\sum_{k=1}^n Y_k}{n}\to a$。为此我们分两步：

1. 证明 $\frac{\sum_{k=1}^n (Y_k-\E Y_k)}{n}\to 0$。
2. 证明 $\E Y_n\to a$，从而 $\frac{\sum_{k=1}^n\E Y_k}{n}\to a$。结合上一点就证明了强大数定理。

2 用控制收敛定理很容易得出，所以关键是证明 1。

我们首先证明 $\sum_{k=1}^n \frac{Y_k-\E Y_k}{n}$ 是个收敛的序列，然后用下一讲介绍的 Kronecker 引理来得出 $\frac{\sum_{k=1}^n (Y_k-\E Y_k)}{n}\to 0$。

:::{.theorem}
**Kolmogrov 收敛判定**：若独立且 $L^2$ 可积的随机变量序列 $\{Y_n\}$ 满足
$$\sum\mathrm{Var}(Y_n)<\infty.$$
则
$$\sum_{n=1}^\infty(Y_n-\E Y_n)$$
几乎处处收敛。并且这个收敛也是 $L^2$ 收敛。
:::

**证明概要**：记 $Z_n=Y_n-\E Y_n$，则 $\E Z_n=0$ 且 $\sum_{n=1}^\infty\E Z_n^2<\infty$。我们来证明 $\sum_{n=1}^\infty Z_n$ 几乎处处收敛。

记 $S_n=\sum_{k=1}^nZ_k$，利用 Markov 不等式不难有
$$\P(|S_n|\geq\epsilon)\leq \frac{1}{\epsilon^2}\E[S_n^2].$$
有意思的是，上面的不等式中在左边把 $S_n$ 换成 $S_n^\ast=\max\limits_{1\leq i\leq n}|S_n|$ 仍然成立：

:::{.theorem}
**Kolmogrov 极大不等式**：对任何正数 $\epsilon>0$ 有
$$\P(S_n^\ast\geq\epsilon)\leq \frac{1}{\epsilon^2}\E[S_n]^2.$$
:::

**证明**：记 $\tau=\min\{j\mid |S_j|\geq\epsilon\}$。则 $\{S_n^\ast\geq\}=\{\tau\leq n\}$。
$$\E[S_n^2\ind_{\{S_n^\ast\geq\epsilon\}}]=\E[S_n^2\ind_{\{\tau\leq n\}}]=\sum_{k=1}^n\E[S_n^2\ind_{\{\tau=k\}}].$$
使用技巧 $S_n^2=(S_k + S_n - S_k)^2$ 我们有
$$\E[S_n^2\ind_{\{\tau=k\}}] = \E[(S_k^2 + (S_n-S_k)^2)\ind_{\{\tau=k\}}] + \E[2S_k(S_n-S_k)\ind_{\{\tau=k\}}].$$
注意到第二项
$$\E[2S_k(S_n-S_k)\ind_{\{\tau=k\}}] =2\E[S_k\ind_{\{\tau=k\}}]\cdot\E[S_n-S_k]=0.$$
所以
$$\E[S_n^2]\geq\sum_{k=1}^n\E[S_k^2\ind_{\{\tau=k\}}]\geq\epsilon^2\sum_{k=1}^n\E[\ind_{\{\tau=k\}}]=\epsilon^2\P(\tau\leq n)=\epsilon^2 \P(S_n^\ast\geq\epsilon).$$

回到 Kolmogrov 收敛定理的证明。

Kolmogrov 极大不等式告诉我们

$$\P(\max_{n\leq k \leq m}|S_k - S_n|\geq\epsilon)\leq \frac{1}{\epsilon^2}\E|S_m-S_n|^2=\frac{1}{\epsilon^2}\sum_{k=n}^m \E Z_k^2.$$
令 $m\to\infty$ 我们有
$$\P(\sup_{k\geq n}|S_k - S_n|\geq\epsilon)\leq\frac{1}{\epsilon^2}\sum_{k=n}^\infty \E Z_k^2.$$
于是
$$\P(\sup_{k,j\geq n}|S_k - S_j|\geq\epsilon)\leq\frac{2}{\epsilon^2}\sum_{k=n}^\infty \E Z_k^2.$$
所以随机变量序列
$$\delta_n := \sup_{k,j\geq n}|S_k - S_j|$$
依测度收敛到 0。但是 $\{\delta_n\}$ 是一个单调下降的非负序列，它必然有一个几乎处处收敛的极限 $\delta$，$\delta$ 也非负。$\{\delta_n\}$ 依测度收敛到 0，又几乎处处收敛到 $\delta$，那必须 $\delta$ 几乎处处为 0，即 $\{S_n\}$ 是 Cauchy 序列。$\blacksquare$


# 19.1 Strong Law of Large Numbers, Part 2

介绍了证明强大数定理的第二个工具：Kronecker 引理。

:::{.lemma}
**Kronecker 引理** 若 $\{b_k\}\uparrow\infty$ 且 $\lim\limits_{n\to\infty}\sum\limits_{k=1}^n\dfrac{x_k}{b_k}$ 存在，则 $\lim\limits_{n\to\infty}\dfrac{1}{b_n}\sum\limits_{k=1}^n x_k=0$。
:::

**证明概要**：记 $u_n=\sum\limits_{k=1}^n\dfrac{x_k}{b_k},\,u_0=0$，则 $\lim\limits_{n\to\infty}u_n=s$ 存在。
$$\begin{align*}\frac{1}{b_n}\sum_{k=1}^n x_k&=\frac{1}{b_n}\sum_{k=1}^n(u_k-u_{k-1})b_k=\frac{1}{b_n}\sum_{k=1}^nu_kb_k-\frac{1}{b_n}\sum_{k=0}^{n-1}u_kb_{k+1}\\&=u_n-\frac{b_n-b_1}{b_n}s-\sum_{k=1}^{n-1}\frac{b_{k+1}-b_k}{b_n}(u_k-s).\end{align*}$$
而最后一个余项的绝对值小于等于
$$\begin{align*}\sum_{k=1}^{n-1}\frac{b_{k+1}-b_k}{b_n}|u_k-s|=\left(\sum_{k=1}^{N}+\sum_{k=N+1}^{n-1}\right)\frac{b_{k+1}-b_k}{b_n}|u_k-s|\end{align*}$$
这里对 $n>N$ 有 $|u_n-s|<\epsilon$ 成立。

当 $n\to\infty$ 时第一个和项是一个有界的值除以 $b_n$ 从而趋于 0。第二个和项显然不大于 $\dfrac{b_n}{b_n}\epsilon$，所以这个余项可以任意小。

:::{.lemma}
$Y_n' = Y_n/n$ 满足 Kolmogrov 收敛判定。
:::

**证明概要**：
$$\begin{align*}\sum_{n=1}^\infty\mathrm{Var}(Y_n')&=\sum_{n=1}^\infty\frac{\mathbb{E}Y_n^2 - (\mathbb{E}Y_n)^2}{n^2}\leq \sum_{n=1}^\infty\frac{\mathbb{E}Y_n^2}{n^2}\\&=\sum_{n=1}^\infty\frac{\mathbb{E}X_n^2\ind_{\{|X_n|\leq n\}}}{n^2}\\&=\mathbb{E}\left[|X_1|^2\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}}\right]\\&\leq\mathbb{E}\left[|X_1|^2\sum_{n=1}^\infty\frac{1}{n^2},\ |X_1|\leq 2\right] + \mathbb{E}\left[|X_1|^2\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}},\ |X_1|>2\right]\\&\leq4\sum_{n=1}^\infty\frac{1}{n^2}+\mathbb{E}\left[|X_1|^2\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}},\ |X_1|>2\right] .\end{align*}$$
为什么要用 $|X_1|$ 是否大于 2 把它分成两部分？这里其实可以用任何大于等于 2 的数，不过 2 已经足够了，这样做的原因下面就会看到。

现在第一项是有限的，我们只要说明第二项也有限即可。你可能想把 $\ind_{\{|X_1|\leq n\}}$ 扔掉，但是注意强大数定律中 $|X_1|$ 是 $L^1$ 可积的，未必是 $L^2$ 可积的，所以扔掉是不行的。我们得把 $\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}}$ 这个东西估计一下。注意到对任何正整数 $k$，$\sum_{n=k}^\infty\frac{1}{n^2}$ 就是 $\frac{1}{\lfloor t\rfloor^2}$ 在 $[k,\infty)$ 上的积分， 所以当 $x>2$ 时
$$\begin{align*}
\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{x\leq n\}}&=\sum_{n\geq x}^\infty\frac{1}{n^2}=\sum_{n= \lceil x\rceil}^\infty\frac{1}{n^2}\\&=\int_{\lceil x\rceil}^\infty\frac{1}{\lfloor t\rfloor^2}\,\mathrm{d}t\\&\leq \int_{\lceil x\rceil}^\infty\frac{1}{(t-1)^2}\,\mathrm{d}t\\&=\frac{1}{\lceil x\rceil - 1}\\&\leq\frac{1}{x-1}<\frac{2}{x}.\end{align*}$$
所以取 $x>2$ 主要是为了最后一步的 $\frac{1}{x-1}<\frac{2}{x}$。

于是我们就证明了在 $|X_1|>2$ 上有
$$\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}}<\frac{2}{|X_1|}.$$
两边乘以 $|X_1|^2$ 并积分，则
$$\mathbb{E}\left[|X_1|^2\sum_{n=1}^\infty\frac{1}{n^2}\ind_{\{|X_1|\leq n\}},\ |X_1|>2\right] < 2\mathbb{E}|X_1|.$$
这就证明了结论。


# 19.2 Renewal Theory

本讲以灯泡寿命为例子，介绍了强大数定理在更新理论中的应用。

设灯泡的寿命互相独立，且服从某个共同的非负随机变量 $X,\ \E X<\infty$。设长度为 $t$ 的时刻内需要报废的灯泡数最多为 $N_t$，即 $S_{N_t}\leq t < S_{N_t+1}$。则
$$\lim_{t\to\infty}\frac{N_t}{t}\to\frac{1}{\E X},\quad \ae$$
实际上由定义有
$$\frac{S_{N_t}}{N_t}\leq \frac{t}{N_t} < \frac{S_{N_t+1}}{N_t}.$$
如果我们能证明 $t\to\infty$ 时同样有 $N_t\to\infty,\ae$，则利用强大数定理就有 $S_{N_t}/N_t\to\E X$，从而结论得证。

我们考虑 $\Omega_1=\{\omega\in\Omega\mid S_n(\omega)<\infty,\ \forall n\geq1\}$。$\Omega_1$ 作为一列递减的测度均为 1 的集合列的极限，测度显然也是 1。我们只要证明在 $\Omega_1$ 上有 $S_{N_t}/N_t\to\E X$ 成立。

首先 $N_t$ 随着 $t$ 递增是没有问题的，如果它对某个 $\omega$ 是有界的，则 $N_t(\omega)\leq M$ 对所有 $t$ 成立。即不管 $t$ 是多少都有 $S_M\leq t < S_{M+1}$，这只能要求 $S_{M+1}(\omega)=\infty$，从而 $\omega$ 不属于 $\Omega_1$。

一个有意思的引理：

> **引理**：设 $X\in L^1$，如果 $\{X_n\}$ 是一列 $\iid$ 且服从和 $X$ 同样的分布，则 $\dfrac{X_n}{n}\to0,\ae$。

老技巧，只要证明 $\P(\{|X_n|\geq n\epsilon,\ \io\})=0$ 即可。根据 Borel-Cantelli 引理，只要证明 $\sum_{n=1}^\infty\P(|X_n|\geq n\epsilon)<\infty$ 即可，而这在 18.1 中已经证明过了。

# ✅ 21.1 Total Variation

:::{.definition}
设 $\mu,\nu$ 是 $(S,\B)$ 上的两个概率测度。定义它们之间的全变差为
$$\dtv(\mu,\nu) = \sup_{B\in\B}|\mu(B)-\nu(B)|.$$
:::

:::{.lemma}
设 $\mu,\nu$ 是 $(S,\B)$ 上的两个概率测度，$\alpha$ 是有限测度且 $\mu,\nu\ll\alpha$。设 $\mathrm{d}\mu = f\,\mathrm{d}\alpha,\mathrm{d}\nu=g\,\mathrm{d}\alpha$，则
$$\dtv(\mu,\nu) = \frac{1}{2}\|f-g\|_{L^1(\alpha)}.$$
:::

**证明**：对任何 $B\in \B$，
$$|\mu(B) - \nu(B)| = \left|\int_B (f-g)\,\mathrm{d}\alpha\right|.$$
$$|\mu(B^c) - \nu(B^c)| = \left|\int_{B^c} (f-g)\,\mathrm{d}\alpha\right|.$$
上面两个式子，左边的值是一样的，右边之和大于等于 $\|f-g\|$，所以
$$\dtv(\mu,\nu)\le \|f-g\|.$$
另一方面，取 $A=\{f > g\}$，则由于 $\mu,\nu$ 是概率测度，所以
$$0=\int_S (f-g)\,\mathrm{d}\alpha=\int_A (f-g)\da + \int_{A^c}(f-g)\da=\int_A |f-g|\da - \int_{A^c}|f-g|\da.$$
即
$$\mu(A)-\nu(A)=\int_A (f-g)\da =\int_A |f-g|\da=\frac{1}{2}\|f-g\|_{L1}.$$
$\blacksquare$

给定一族 $\{\mu_n\}_{n\ge1}$，取
$$\alpha = \sum_{n=1}^\infty\frac{\mu_n}{2^n}.$$
则 $\mu_n\ll\alpha_n$。

:::{.corollary}
$\dtv$ 是 $(S,\B)$ 上的完备度量。
:::

**证明**：取 $\alpha$ 如上使得 $\mu_n\ll\alpha$，则问题转化为使用 $L^1(\alpha)$ 是完备度量空间。$\blacksquare$。


# ✅ 22.1 Weak Convergence

:::{.definition}
设 $\S$ 是一个度量空间，$\mu_n,\mu$ 是 $(\S,\B(\S))$ 上的概率测度。如果有
$$\int f\,\mathrm{d}\mu_n\to \int f \du,\quad \forall f\in C_b(\S).$$
就称 $\mu_n$ 弱收敛到 $\mu$。
:::

:::{.lemma}
设 $\{X_n\}, X$ 都是从概率空间 $(\Omega,\F,\P)\to (\S,\B(\S))$ 的随机变量。
如果 $X_n\to_\P X$ 且 $g$ 是连续函数，则 $g(X_n)\to_\P g(X)$。
:::

证明：设 $\epsilon,\delta>0$。记
$$B_{\epsilon,\delta}(g)=\{x\in\S\mid \exists y\in\S, d(x,y)\leq\delta, |g(x)-g(y)|\geq\epsilon\}.$$
$g$ 的连续性保证了对任何 $\epsilon>0$，$\lim_{\delta\to0}B_{\epsilon,\delta}(g)\downarrow \emptyset$。

于是
$$\{\omega\mid |g(X_n(\omega))-g(X(\omega))|\geq\epsilon\}\subset\{\omega\mid d(X_n(\omega), X(\omega))\geq\delta\}\cup\{\omega\mid X(\omega)\in B_{\epsilon,\delta}(g)\}.$$
于是
$$\P(|g(X_n(\omega))-g(X(\omega))|\geq\epsilon)\le \P(d(X_n(\omega), X(\omega))\geq\delta) + \P(X\in B_{\epsilon,\delta}(g)).$$
也就是
$$\P(|g(X_n)-g(X)|\geq\epsilon)\le \P(d(X_n, X)\geq\delta) +\mu_X(B_{\epsilon,\delta}(g)).$$
所以，对给定的 $\epsilon$，我们可以取 $\delta$ 使得第二项任意小，再取最后大的 $n$ 使得第一项任意小。这就证明了结论。$\blacksquare$

:::{.proposition}
如果 $X_n\to_\P X$，则 $X_n\to_w X$。
:::

证明：设 $f\in C_b(\S)$。则 $\int f\,\mathrm{d}\mu_{X_n}=\E[f(X_n)]$。于是我们要证明
$$\E[f(X_n)]\to \E[f(X)].$$
但是根据引理，$f(X_n)\to_\P f(X)$。又因为 $f$ 有界，所以由依测度收敛的控制收敛定理即得。$\blacksquare$

:::{.theorem}
**Portmanteau 定理**

设 $\{\mu_n\},\mu$ 都是空间 $(\S,\B(\S))$ 上的概率测度。以下结论是等价的：

1. $\mu_n\to_w\mu$。
2. $\int f\,\mathrm{d}\mu_n\to\int f\du,\quad \forall f\in\mathrm{Lip}_b(\S)$。
3. $\limsup \mu_n(F)\le \mu(F)$ 对任何闭集 $F$ 成立。
4. $\liminf \mu_n(G)\ge \mu(G)$ 对任何开集 $G$ 成立。
5. $\mu_n(A)\to \mu(A)$ 对任何满足 $\mu(\partial A)=0$ 的集合 $A\in\B(\S)$ 成立。
:::

:::{.note}
Portmanteau 的原意是把若干词拼起来组成新词。这里表示把一些看起来不同的结论放在一起。
:::

$1\Rightarrow 2$ 显然。

$2\Rightarrow3$：取 $\psi\in{\rm Lip}_b(\R)$ 为如下的截断函数：

$$\psi(x)=\begin{cases}
1, & x < 0\\
0, & x > 1\\
1-x, & 0\leq x\leq 1
\end{cases}$$
不难看出 $\|\phi\|_{\rm Lip}\leq1$。

给定闭集 $F$，考虑
$$f_k(x) = \phi(k \cdot d(x, F)).$$
则
$$|f_k(x)-f_k(y)|\leq k |d(x,F)-d(y,F)|\leq k\cdot d(x,y).$$
这里用到了距离到集合的函数是 1-Lipschitz。从而 $f_k\in{\rm Lip}_b(\S)$。
注意到
$$\lim_{k\to\infty}f_k(x)=\begin{cases}
f_k(x)\downarrow\psi(\infty) = 0, & d(x,F)> 0\\
f_k(x) = \phi(0) = 0, & d(x,F)=0
\end{cases} = \ind_F.$$
总之 $f_k\downarrow \ind_F$。于是
$$\limsup\mu_n(F)=\limsup\int \ind_F\,\mathrm{d}\mu_n\le \limsup\int f_k\,\mathrm{d}\mu_n = \int f_k\du$$
上面的式子对所有 $k$ 都成立。然而根据控制收敛定理，$\int f_k\du\to \int \ind_F\du = \mu(F)$。得证。

$3\Leftrightarrow4$：对闭集 $F=G^c$ 应用 3 即可。反之对 $G=F^c$ 应用 4。

$3,4\Rightarrow5$：如果 $\mu(\partial A)=0$，则 $\mu(A)=\mu(\overline{A})=\mu({\rm int}(A))$。
$$\varlimsup\mu_n(A)\le\varlimsup\mu_n(\overline{A}) \le\mu(\overline{A})=\mu(A)=\mu({\rm int}(A))\le\varliminf\mu_n({\rm int}(A))\le\varliminf\mu_n(A).$$

$5\Rightarrow1$：取任意 $f\in C_b(\mathcal S)$，记 $m=\inf f$, $M=\sup f$，并令
$$
g=\frac{f-m}{M-m}\in C_b(\mathcal S),\qquad 0\le g\le 1.
$$
若已证 $\int g\,\mathrm{d}\mu_n\to\int g\,\du$，则由线性缩放可还原对 $f$ 的结论。

对任意有限测度 $\nu$ 及 $0\le h\le 1$ 的可测函数，有层蛋糕表示：
$$
\int h\dv = \int_0^1 \nu\big(\{h\ge t\}\big)\dt.
$$
因为
$$h(x)=\int_0^{h(x)}\dt=\int_0^1\ind_{\{h(x)\ge t\}}\dt.$$
再用 Tonelli 交换积分次序。

据此，只需证明
$$
\int_0^1 \mu_n\big(\{g\ge t\}\big)\dt \longrightarrow\int_0^1 \mu\big(\{g\ge t\}\big)\dt.
$$
从而我们只要证明 $\mu_n(\{g\ge t\})\to \mu(\{g\ge t\})$ 对几乎处处的 $t\in[0,1]$ 成立即可。

对每个 $t\in[0,1]$，记
$$\{t\in[0,1]\mid \mu(\partial\{g\ge t\})>0\}\subset\{t\in[0,1]\mid \mu(\{g=t\})>0\}:=E.$$

:::{.note}
这里只是包含关系，不是相等关系。例如，取 $g(x)$ 是任何在 $[-1,1]$ 上为 0，在 $|x|>1$ 时取值在 $(0,1]$ 之间的连续函数，则
$$\{g(x)> 0 \}=(-\infty, -1)\cup(1,\infty),\quad \{g(x) = 0\} = [-1,1].$$
前者的边界只要两个点 $\pm1$，是后者严格的子集。
:::

则 $\mu_n(\{g\ge t\})\to \mu(\{g\ge t\})$ 对所有 $t\in[0,1]\setminus E$ 成立。
所以我们只要再证明 $E$ 是可数集合即可。

对每个 $k\in\mathbb N$，集合
$$
E_k:=\{t:\ \mu(\{g=t\})\ge 1/k\}
$$
必为有限集，否则将导致 $\sum_{t\in E_k}\mu(\{g=t\})=\infty$，与 $\mu(\mathcal S)=1$ 矛盾。从而 $E=\bigcup_{k\ge1}E_k$ 可数。$\blacksquare$

# ✅ 22.2 Weak Convergence over $\R^d$

:::{.theorem}
在 $\S=\R^d$ 的情形，$\mu_n\to_w \mu$ 等价于对任何 $f\in C_c(\R^d)$ 有
$$\int f\,\mathrm{d}\mu_n\to \int f\du.$$
注意，这里的 $f$ 加强为具有紧支集的函数。
:::

证明：只要证明当 $f\in C_c(\R^d)$ 时有
$$\int f\,\mathrm{d}\mu_n\to \int f\du.$$
即可。

:::{.lemma}
如果定理结论成立，则
$$\lim_{R\to\infty}\inf_n\mu_n(\overline B_R)=1.$$
:::
证明：令 $g_R(x):\R^d\to\R$ 是如下的连续　函数：当 $|x|< R/2$ 时 $g(x)=1$，当 $|x|>R$ 时 $g(x)=0$，当 $R/2\le |x|\le R$ 时 $g(x)$ 线性插值。则
$$\ind_{\overline B_{R/2}}\le g_R \le \ind_{\overline B_{R}}.$$
所以
$$\int g_R\,\mathrm{d}\mu_n\leq \int \ind_{\overline B_{R}}\,\mathrm{d}\mu_n=\mu_n(\overline B_R).$$
两边取下极限，并利用 $g_R$ 是具有紧支集的连续函数，得到
$$\liminf_n\mu_n(\overline B_R)\geq \liminf_n\int g_R\,\mathrm{d}\mu_n=\int g_R\du\geq\mu(\overline B_{R/2}).$$

给定 $\varepsilon>0$。由 $\mu(\overline B_{R/2})\uparrow 1$，可取 $R_0$ 使 $\mu(\overline B_{R_0/2})>1-\varepsilon$。
$$\liminf_{n}\mu_n(\overline B_{R_0})\ \ge\ 1-\varepsilon.$$
故存在 $N$ 使得对所有 $n\ge N$，$\mu_n(\overline B_{R_0})\ge 1-\varepsilon$。

对有限个指标 $n<N$，可取 $R_1,\dots,R_{N-1}$ 使
$\mu_n(\overline B_{R_n})\ge 1-\varepsilon$。令
$$R=\max\{R_0,R_1,\dots,R_{N-1}\}.$$
则对所有 $n$ 都有 $\mu_n(\overline B_R)\ge 1-\varepsilon$。于是
$$\inf_n \mu_n(\overline B_R)\ \ge\ 1-\varepsilon.$$
由 $\varepsilon$ 任意，遂得
$$\lim_{R\to\infty}\inf_n \mu_n(\overline B_R)=1.$$

回到定理证明。

现取任意有界连续函数 $f\in C_b(\R^d)$，令 $f_R:=f\cdot g_R\in C_c(\R^d)$。注意到
$$
0\le 1-g_R\le \ind_{\overline B_{R/2}^{c}},
\quad |f-f_R|=|f|\cdot (1-g_R)\le \|f\|_\infty\cdot\ind_{\overline B_{R/2}^{c}}.$$
因此对所有 $n$ 有
$$
\left|\int (f-f_R)\,\mathrm d\mu_n\right|
\le \|f\|_\infty\cdot\mu_n(\overline B_{R/2}^{c}),\quad
\left|\int (f-f_R)\du\right|
\le \|f\|_\infty\cdot\mu(\overline B_{R/2}^{c}).
\tag{1}
$$

由上一部分已得的统一紧性
$\displaystyle \lim_{R\to\infty}\inf_n\mu_n(\overline B_R)=1$
以及 $\mu(\overline B_R)\uparrow 1$，给定 $\varepsilon>0$，可取 $R$ 使得
$$\sup_n\mu_n(\overline B_{R/2}^{c})\le \varepsilon,\quad
\mu(\overline B_{R/2}^{c})\le \varepsilon.
\tag{2}$$
代回 (1) 得到
$$\sup_n\left|\int (f-f_R)\,\mathrm d\mu_n\right|\le \|f\|_\infty\varepsilon,
\quad
\left|\int (f-f_R)\du\right|\le \|f\|_\infty \varepsilon.
\tag{3}$$

另一方面，对这个固定的 $R$，由假设在 $C_c(\R^d)$ 上的收敛有
$$\int f_R\,\mathrm d\mu_n\to\int f_R\du \quad (n\to\infty)$$
故存在 $N$ 使得 $n\ge N$ 时
$$\left|\int f_R\,\mathrm d\mu_n-\int f_R\du\right|\le \varepsilon.
\tag{4}$$

现在分解
$$\int f\,\mathrm d\mu_n-\int f\du
=\int (f-f_R)\,\mathrm d\mu_n + \left(\int f_R\,\mathrm d\mu_n-\int f_R\du\right)
+\int (f-f_R)\du.$$

由 (3), (4) 得到当 $n\ge N$ 时
$$\left|\int f\,\mathrm d\mu_n-\int f\du\right|
\le 2\|f\|_\infty\varepsilon+\varepsilon.$$
由于 $\varepsilon>0$ 任意，便得
$$\int f\,\mathrm d\mu_n\to\int f\du\quad(n\to\infty).$$

:::{.corollary}
设 $\{\mu_n\},\mu$ 是 $\R^d$ 上的概率分部，则 $\mu_n\to_w\mu$ 当且仅当
$$\int f\,\mathrm{d}\mu_n\to \int f\du,\quad \forall f\in C_c^\infty(\R^d).$$
:::
这里进一步把 $f$ 加强成了具有紧支集且光滑的函数。

证明：任取一个光滑函数 $\rho$ 满足 $0\le \rho\le \ind_{\overline B_1}$。并归一化使得 $\rho$ 是概率密度。

任取 $\epsilon>0$，$f\in C_c(\R^d)$。令
$$f_\epsilon(x) = \int_{\R^d}f(x+\epsilon t)\rho(t)\dt=\frac{1}{\epsilon^d}\int f(y)\rho(\frac{y-x}{\epsilon})\dy.$$
直观上，$f_\epsilon$ 就是 $f$ 在半径为 $\epsilon$ 邻域内，以 $\rho$ 为密度的平均值。显然 $f_\epsilon$ 是光滑且具有紧支集的函数且
$$\|f - f_\epsilon\|_\infty \to 0.$$
取 $f_\delta$ 满足 $\|f - f_\delta\|_\infty<\epsilon.$$
$$\int f\du - \int f\,\mathrm{d}\mu_n = \int (f-f_\epsilon)\du + \int f_\epsilon\du - \int f_\epsilon\,\mathrm{d}\mu_n
+\int f_\epsilon-f\,\mathrm{d}\mu_n.
$$
第一项和第三项都不超过 $\epsilon$，中间项可以通过取 $n$ 足够大使得也不超过 $\epsilon$，
所以
$$\left|\int f\du - \int f\,\mathrm{d}\mu_n\right|\le 3\epsilon.$$
由 $\epsilon$ 任意性即得。

:::{.note}
我们来证明 $f_\varepsilon \to f$ 是一致收敛的：

由于 $f\in C_c(\mathbb{R}^d)$ 有界。设
$$\|f\|_\infty:=\sup_{x\in\mathbb{R}^d}|f(x)|<\infty.$$
（这是因为 $\operatorname{supp} f$ 紧且 $f$ 在紧集上连续，故取得最大值；在支集外 $f=0$。）

于是对任意 $h\in\mathbb{R}^d$ 与任意 $x$,
$$|f(x+h)-f(x)|\le |f(x+h)|+|f(x)|\le 2\|f\|_\infty.$$
对 $x$ 取上确界得到
$$\|f(\cdot+h)-f(\cdot)\|_\infty\le 2\|f\|_\infty.$$
再对所有 $|h|\le r$ 取上确界，便有
$$\omega_f(r):=\sup_{|h|\le r}\|f(\cdot+h)-f(\cdot)\|_\infty\le 2\|f\|_\infty <\infty.$$

设 $\rho\in C_c^\infty(\mathbb{R}^d)$，$\rho\ge0$，$\int \rho=1$，$\mathrm{supp}\,\rho\subset \overline{B_1(0)}$。令
$$
\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon),\quad
f_\varepsilon=f*\rho_\varepsilon.
$$
对任意 $x\in\R^d$，
$$
f_\varepsilon(x)-f(x)
=\int_{\mathbb{R}^d}\rho_\varepsilon(y)\bigl(f(x-y)-f(x)\bigr)\,dy.
$$
因为 $\mathrm{supp}\,\rho_\varepsilon\subset \overline{B_\varepsilon(0)}$，有
$$
|f_\varepsilon(x)-f(x)|
\le \int \rho_\varepsilon(y)\,\sup_{|y|\le \varepsilon}|f(x-y)-f(x)|\,dy
\le \omega_f(\varepsilon).
$$


由于 $f\in C_c(\mathbb{R}^d)$ 连续且支撑紧，$f$ 在 $\mathbb{R}^d$ 上一致连续，故 $\omega_f(r)\to0$ 当 $r\to0$。于是
$$
\|f_\varepsilon-f\|_\infty \xrightarrow[\varepsilon\to0]{} 0,
$$
这正是一致收敛。
:::

:::{.theorem}
当 $\S=\R$ 时，$\mu_n\to_w\mu$ 当且仅当
$$F_n(t)=\mu_n((-\infty, t])\to \mu((-\infty, t]) = F(t),\quad \forall t, \text{ $F$ continous at $t$}.$$
:::

证明：$\Rightarrow$ 由 Portmanteau 定理即得。

$\Leftarrow$：设 $f\in C_c(\R)$ 是具有紧支集的连续函数，则 $f$ 也是一致连续的。

设 $\pi= \{x_0<x_1<\cdots< x_k\}$ 是 $\supp f$ 的一个划分，满足：

1. $x_j$ 都是 $F$ 的连续点；
2. $|x_j-x_{j+1}|\leq \epsilon$；
3. $|f(x_j)-f(x_{j+1})|\leq\delta$。

则 $f_\pi = \sum_{j=1}^k \ind_{(x_{j-1},x_j]}$ 满足 $\|f_\pi - f\|_\infty < \epsilon$。
于是
$$\left|\int (f-f_\pi)\,\mathrm{d}\mu_n\right| \leq \epsilon.$$
$$\left|\int (f-f_\pi)\,\mathrm{d}\mu\right| \leq \epsilon.$$
$$\left|\int f_\pi\,\mathrm{d}\mu - \int f_\pi\du \right|\le \epsilon \sum_{j=1}^k|F_n(x_j) - F(x_j)|\xrightarrow{x\to\infty}0.$$


# ✅ 23.1 Vague Convergence

回忆弱收敛是指，一族概率测度 $\{\mu_n\}$ 收敛到一个概率测度 $\mu$。如果这些测度都是 $\R^d$ 上的，那么这等价于用连续有界函数 $C_b(\R^d)$，或者连续紧支集函数 $C_c(\R^d)$，甚至光滑紧支集函数 $C_c^\infty(\R^d)$ 的积分检查的收敛。

如果我们不要求 $\mu_n,\mu$ 是概率测度呢？只要求它们是 Borel 测度呢？

:::{.definition}
设 $\mu_n,\mu$ 是 $\R^d,\B(\R^d)$ 上的 Borel 测度。如果对任何 $f\in C_c(\R^d)$ 有
$$\int f\dun \to \int f\du.$$
就称 $\mu_n$ vaguely 收敛到 $\mu$。记作 $\mu_n\to_v\mu$。
:::

:::{.definition}
设 $\S$ 是一个拓扑空间。其上的一族概率测度 $\Lambda$ 称作是 tight 的，如果对任意 $\epsilon>0$，都存在紧集 $K_\epsilon$ 使得 $\mu_(K^c)<\epsilon$ 对任何 $\mu\in\Lambda$ 成立。
:::

:::{.theorem}
设 $\{\mu_n\}$ 是 $(\R^d,\B(\R^d))$ 上的概率测度，且 $\mu_n\to_v \mu$。则 $\mu$ 是概率测度当且仅当 $\{\mu_n\}$ 是 tight 的。这时 $\mu_n\to_w\mu$。
:::

**证明**：

$\Rightarrow$：如果 $\mu$ 是概率测度，则在 22.2 的引理中我们证明了
$$\lim_{R\uparrow\infty}\inf_n\mu_n(\overline B_R) = 1.$$
由此即得结论。

$\Leftarrow$：给定 $\epsilon > 0$。取紧集 $K_\epsilon$ 使得 $\mu_n(K_\epsilon)\ge1-\epsilon$。再取具有紧支集的 $f\in C_c(\R^d)$ 满足 $1_{K_\epsilon}\le f\le 1$。则
$$\mu(\R^d)=\int 1\du\ge \int f\du=\lim_{n\to\infty}\int f\dun\ge\varliminf_{n\to\infty}\int 1_{K_\epsilon}\dun=\varliminf_{n\to\infty}\mu_n(K_\epsilon)\ge 1-\epsilon.$$
由 $\epsilon$ 任意性可得 $\mu(\R^d)\ge1$。

另一方面，如果 $\mu(\R^d) > 1$ 的话，则我们可以取紧集 $K=\overline B_R$ 满足 $\mu(K)>1$。仍然取 $f\in C_c(\R^d)$ 满足 $1 \ge f \ge \ind_K$，则
$$1=\mu_n(\R^d)=\int 1\dun \ge\int f\dun \to \int f\du \ge \mu(K)>1.$$
矛盾！$\blacksquare$

# ✅ 23.2 Prokhorov's Compactness Theorem

:::{.theorem}
**Prokhorov 紧性定理** 设 $\S$ 是可分度量空间，$\{\mu_n\}$ 是 $(\S,\B(\S))$ 上的概率测度，则 $\{\mu_n\}$ 有 vaguely 收敛的子序列。
:::

**证明**：将有理数 $\mathbb Q$ 排列为 $\mathbb{Q}=\{q_1,q_2,\ldots\}$，并记 $F_n=F_{\mu_n}$。

+ $\{F_n(q_1)\}_{n=1}^\infty$ 是 $[0,1]$ 中的有界序列，所以存在收敛子序列 $\{F_{m_1(k)}(q_1)\}_{k=1}^\infty$。
+ $\{F_{m_1(k)}(q_2)\}_{k=1}^\infty$ 是 $[0,1]$ 中的有界序列，所以存在收敛子序列 $\{F_{m_2(k)}(q_2)\}_{k=1}^\infty$。
+ ...

这样我们会得到一串子序列 $\{m_j(k)\}$ 使得 $m_j(\cdot)$ 是 $m_{j-1}(\cdot)$ 的子序列；并且
$$F_{m_j(k)}(q_j)\to G(q_j).$$
于是 $F_{m_k(k)}(q) \to G(q)$ 对所有 $q\in\mathbb Q$ 成立。

现在的 $G$ 只在 $\mathbb Q$ 上有定义。我们想把它变成一个 $\R$ 上的分布函数。令

$$F(x) = \inf\,\{G(q)\mid q\in\mathbb{Q},\ q > x\}.$$
显然 $F$ 是递增的。我们来说明 $F$ 也是右连续的：设 $x_n\downarrow x$，则
$$\begin{aligned}
\lim_{n\to\infty}F(x_n)&=\inf F(x_n)=\inf_n\inf\,\{G(q)\mid q\in\mathbb{Q},\ q > x_n\}\\&=\inf\,\{G(q)\mid q\in\mathbb{Q}> \text{ some }x_n\}\\
&=\inf\,\{G(q)\mid q\in\mathbb{Q}> x\}\\
&=F(x).
\end{aligned}.$$
所以 $F$ 确实是右连续的。

:::{.note}
我们使用了 $\inf_n \inf S_n = \inf(\cup_{n=1}^\infty S_n)$ 对任何集合族 $\{S_n\}$ 成立这一事实。
:::

此外还有
$$\lim_{x\to -\infty} F(x) = \inf\{G(q)\}\geq 0,\quad \lim_{x\to \infty} F(x) = \sup\{G(q)\}\leq 1.$$
所以 $F$ 是一个次分布函数。它给出一个有限 Borel 测度。

要证明 $\mu_{n_k}\to_v\mu$，只要证明对任何 $F$ 的连续点 $x$ 有
$$F_{n_k}(x)\to F(x).$$
即可。设有理数序列 $q_j\uparrow x,r_j\downarrow x$。由于 $F_{n_k}$ 都是递增的，所以
$$F_{n_k}(q_j)\le F_{n_k}(x) \le F_{n_k}(r_j),\quad \forall k, j.$$
令 $k\to\infty$ 可得
$$G(q_j)\leq \varliminf_k F_{n_k}(x)\le \varlimsup_k F_{n_k}(x)\le G(r_j).$$
从而
$$\sup_j G(q_j)\leq \varliminf_k F_{n_k}(x)\le \varlimsup_k F_{n_k}(x)\le \inf_j G(r_j).$$
一方面右边 $\inf_{r>x}G(r)=F(x)$。

另一方面，对任意 $q < y < x$，由
$$G(q)\leq \inf_{s > y} G(s) = F(y).$$
对所有 $q<y$ 取上确界，再对所有 $y<x$ 取上确界，得
$$\sup_{q<x}G(q) = \sup_{y<x}\sup_{q<y}G(q)\le \sup_{y<x}F(y) = F(x-).$$
由于 $x$ 是连续点可得 $F(x)= \sup_{q<x}G(q)=\sup_j G(q_j)$。
于是 $F(x) = \varliminf_k F_{n_k}(x)= \varlimsup_k F_{n_k}(x)$。

先对 $\varphi\in C_c^1(\mathbb R)$。记 $K=\operatorname{supp}\varphi$ 紧。对每个 $k$,
$$\int \varphi\,\mathrm{d}\mu_{n_k}
=\int_{(-\infty,\infty)} \varphi\,\mathrm{d}F_{n_k}
=\Big[\varphi(x)F_{n_k}(x)\Big]_{-\infty}^{+\infty}
-\int F_{n_k}(x)\varphi'(x)\dx
= -\int_K F_{n_k}(x)\varphi'(x)\dx.$$
同理
$$\int \varphi\,\du= -\int_K F(x)\varphi'(x)\dx.$$
我们有 $F_{n_k}(x)\to F(x)$ 对 $x$ **几乎处处**成立，且 $0\le F_{n_k}\le 1$。支配收敛给出
$$\int\varphi\,\mathrm{d}\mu_{n_k}\to-\int_K F(x)\varphi'(x)\dx=\int \varphi\du.$$

再用 $C_c^1$ 在 $C_c$ 上的一致稠密性：给定任意 $\psi\in C_c(\mathbb R)$ 与 $\epsilon>0$，可取 $\varphi\in C_c^1$ 使 $\|\psi-\varphi\|_\infty<\epsilon$。因为 $\mu_{n_k},\mu$ 都是有限测度，
$$\left|\int \psi\,\mathrm d\mu_{n_k}-\int \psi\du\right|
\le \left|\int \varphi\,\mathrm{d}\mu_{n_k}-\int \varphi\du\right|
+ \epsilon\cdot(\mu_{n_k}(\mathbb R)+\mu(\mathbb R))
  \le \left|\int \varphi\,\mathrm{d}\mu_{n_k}-\int \varphi\du\right|+2\epsilon.$$
令 $k\to\infty$ 后，再令 $\epsilon\downarrow0$ 即得 $\mu_{n_k}\to_v\mu$。

:::{.corollary}
如果 $\{\mu_n\}$ 还是 tight 的，则存在弱收敛的子序列，其弱收敛的极限是一个概率测度 $\mu$。
:::



# ✅ 23.3 Skorohod's Theorem

:::{.theorem}
设 $\S$ 是可分度量空间，$\mu_n,\mu$ 都是 $(\S,\B(\S))$ 上的概率测度，如果 $\mu_n\to_w\mu$，则存在概率空间 $(\Omega,\F,\P)$ 和随机变量 $Y_n,Y: \Omega\to\S$ 满足：

1. $Y_n,Y$ 的分布分别是 $\mu_n,\mu$。
2. $Y_n\to Y\ \ae$。
:::

我们只在 $\S=\R$ 的情形证明这个结论。

**Inverting the CDF**

设 $F:\R\to [0,1]$ 是一个分布函数。$F$ 未必是单射。我们来试着定义 $F$ 的逆 $F^\leftarrow$。这里的问题在于 $F$ 的平坦处（即 $F$ 在区间 $(a,b)$ 上是常数），$F^{-1}$ 是没有定义的。这时我们一律规定取区间的左端点 $a$ 作为 $F^{-1}$：

$$F^\leftarrow(x)= \sup\{y\in\R\mid F(y)<x\}.$$

直观上，就是取高度为 $x$ 的水平横线与 $F$ 的图像的第一个交点的横坐标。

$F^\leftarrow$ 满足：

$$F^{\leftarrow}(u)\le t\Longleftrightarrow  F(t)\ge u.$$

几何上这很显然：$F(t)\ge u$ 说明在 $t$ 处，$F$ 的图像已经和高度为 $u$ 的水平线相交了，即交点横坐标必然在 $t$ 或者 $t$ 的左侧，即 $F^\leftarrow\le t$。

:::{.lemma}
取 $Y = F^\leftarrow$，则 $Y$ 的分布函数就是 $F$。
:::

证明：
$$\begin{aligned}
\P(Y\le t)&=\lambda(\{x\in(0,1): Y(x)\le t\})\\
&=\lambda(\{x\in(0,1): x\le F(t)\})\\
&=\lambda((0, F(t)])\\
&=F(t).
\end{aligned}
$$

回到 Skorohod 定理的证明。我们取 $(\Omega,\F,\P)=((0,1),\B(0,1),\lambda)$。$Y_n=F_n^\leftarrow$。$Y=F^\leftarrow$。这样就解决了“存在随机变量的分布恰好是 $\mu_n$ 和 $\mu$” 这一步。我们再来证明 $Y_n$ 几乎处处收敛到 $Y$。

记
$$E = \{t\in(0,1)\mid F^\leftarrow(t) < F^\to(t)\}.$$
即 $E$ 是 $F$ 的图像中的那些“平坦”对应的高度值。则 $E$ 是可数集。
我们要证明 $Y_n(x)\to Y(x)$ 对任何 $x\notin E$ 成立。


+ 取一列 $F$ 的连续点 $y_j\uparrow Y(x)$。弱收敛给出 $F_n(y_j)\to F(y_j)$ 对每个 $j$ 成立。由于
$$y_j<Y(x) = \sup\{u\mid F(u) < x\}.$$
所以 $F(y_j)<x$。从而 $F_n(y_j)<x$ 对充分大的 $n$ 成立。但这说明对这些充分大的 $n$ 也有
$$Y_n(x) = \sup\{y\mid F_n(y) < x\}\ge y_j.$$
于是
$$\varliminf_n Y_n(x)\ge \sup_j y_j = Y(x).$$

+ 取一列 $F$ 的连续点 $y_j\downarrow Y(x)$。弱收敛给出 $F_n(y_j)\to F(y_j)$ 对每个 $j$ 成立。由于 $x\in E$，所以
$$y_j>Y(x) = Y^\leftarrow(x) = Y^\to(x) = \inf\{u\mid F(u)>x\}.$$
所以 $F(y_j)>x$。从而 $F_n(y_j)>x$ 对充分大的 $n$ 成立。但这说明对这些充分大的 $n$ 也有
$$Y_n(x) = \sup\{y\mid F_n(y) < x\}\le y_j.$$
于是
$$\varlimsup_n Y_n(x)\le \inf_j y_j = Y(x).$$


# ✅ 24.1 Complex Integration and Dynkin's Theorem

这一节将 Dynkin 函数系引理推广到了复可测的函数上。

:::{.definition}
设 $(\Omega,\F,\mu)$ 是一个可测空间，$f:\Omega\to(\mathbb{C},\B(\R^2))$ 是一个可测函数。我们称 $f$ 是 $L^1$ 可积的，当且仅当 $f$ 的实部和虚部都是 $L^1$ 可积的。
:::

:::{.theorem}
**复版本的 Dynkin 函数系引理**

设 $\H\in\mathbb{B}(\Omega)$ 是一个由 $\mathbb{C}$- 值有界可测函数组成的 $\mathbb{C}$- 向量空间，满足：

+ 包含 1
+ 在有界收敛下封闭
+ 对复共轭封闭

又设 $\M\subset\H$ 是一个乘法系，则 $\H$ 包含所有关于 $\sigma(\M)$ 可测的有界函数。即

$$\mathbb{B}(\Omega,\sigma(\M))\subset\H.$$
:::

证明：

**把生成集从乘法系扩到代数：**令 $\A$ 为由 $\M$ 生成的（复）**代数**。由于 $\M$ 乘法封闭，$\A\subset\H$。显然 $\sigma(\A)=\sigma(\M)$。

记
$$\L:=\{f\in\mathbb{B}(\Omega,\sigma(\A)):\ f\in\H\}.$$
则 $\L$ 是一个复向量空间，且：

* $1\in\L$（因 $1\in\A\subset\H$ 且 $\sigma(\A)$-可测）；
* **有界收敛封闭：**若 $|f_n|\le C,\ f_n\to f$ 点态，且 $f_n\in\L$，则 $f$ 仍 $\sigma(\A)$-可测且 $f\in\H$，故 $f\in\L$；
* **复共轭封闭：**若 $f\in\L$，则 $\overline f\in\H$，且仍 $\sigma(\A)$-可测，因此 $\overline f\in\L$。并且 $\A\subset\L$。

应用**函数版单调类定理（实值）**：

$$\mathcal{C}_{\mathbb R}:=\{\Re a,\ \Im a:\ a\in\A\}\ \text{生成的实值代数}.$$
上一段的说明保证 $\mathcal{C}_{\mathbb R}\subset \L$（这里用到了**共轭封闭**来把 $\Re a,\Im a$ 放进 $\H$，从而放进 $\L$）。
于是得到：所有**有界实值**、$\sigma(\A)$-可测的函数都在 $\L\subset\H$。

任取有界复值 $\sigma(\A)$-可测 $f$。写 $f=u+iv$（(u,v) 。由第 2 步 $u,v\in\L\subset\H$。因 $\H$ 为复向量空间，$f=u+iv\in\H$。
结合 $\sigma(\A)=\sigma(\M)$，即得 $\mathbb{B}(\Omega,\sigma(\M))\subset\H$。$\blacksquare$


# ✅ 24.2 Characteristic Function

本讲介绍了随机变量的特征函数及其基本性质。整体内容比较基础。

# ✅ 25.1 The Riemann-Lebesgue lemma

:::{.theorem}
设 $f\in L^1(\R^n)$，则其特征函数
$$\varphi(t) = \int_{\R^n}e^{it\cdot x}f(x)\,\dx.$$
满足
$$\lim_{t\to\infty}\varphi(t) = 0.$$
:::

**证明**：首先，我们假设 $f$ 无穷次可微，并且具有紧支集。由分部积分，我们得到

$$it_j\varphi(t) = \int_{\R^n}\underbrace{it_je^{it\cdot x}}_{\frac{\partial x}{\partial x_j}e^{it\cdot x}}f(x)\,\dx =-\int_{\R^n}e^{it\cdot x}\frac{\partial x}{\partial x_j}f(x)\,\dx.$$
两边取绝对值，我们有
$$|t_j\varphi(t)|\leq \int_{\R^n}\left|\frac{\partial x}{\partial x_j}f(x)\right|\,\dx=M_j<\infty.$$
于是
$$|t|\cdot |\varphi(t)|\leq \sqrt{M_1^2+\cdots+M_n^2} < \infty.$$
所以在 $f$ 光滑且紧支集的情形，我们得到 $\varphi(t)=O(|t|^{-1})$。

对一般的 $L^1$ 型 $f$，我们用一个具有紧支集的光滑函数来逼近 $f$。首先
$$f\ind_{\overline{B}_R}\to f \text{ in }L^1 \text{ as }R\to\infty.$$
所以我们可以假设 $\mathrm{supp}(f)\subset\overline{B}_R$。
令
$$\H = \{h\in\mathbb{B}(\overline{B}_R)\mid \exists\ {g_n}\xrightarrow{L^1}h\text{ with }g_n\in C^\infty(\overline{B}_R)\}.$$
则

+ $1\in\H$；因为我们可以取类似“钟形”的光滑函数 $g_n\in C^\infty(\overline{B}_R)$ 使得 $g_n$ 在缩小一点的闭球 $\overline{B}_{R-1/n}$ 上恒为 1。
+ $\H$ 在有界收敛下封闭；因为如果 $h_n\to h$，则根据控制收敛定理，$|h_n-h|_1\to 0$。由于 $h_n\in\H$，设 $g_n\in C^\infty(\overline{B}_R)$ 满足 $|h_n-g_n|_1<1/n$，则
由三角不等式有
$$|h-g_n|\leq 1/n + ||h_n-g_n|_1\to 0.$$
记 $\M=C^\infty_c(\R^n)$ 是全体具有紧支集的光滑函数组成的集合，则 $\M$ 是乘法系，且 $\M\subset \H$。于是 $\mathbb{B}(\overline{B}_R,\sigma(\M))\subset\H$。但是 $\sigma(\M)=\mathcal{B}(\R^n)$，所以所有在 $\overline{B}_R$ 上有界，且 Borel 可测的函数都在 $\H$ 中。

最后，取 $g\in C^\infty_c(\R^n)$ 满足 $|f-g|_1<\epsilon$。则
$$|\varphi(t) - \hat{g}(t)|\leq |f-g|_1 < \epsilon.$$
而我们已经证明了 $|\hat{g}|=O(1/t)$，所以我们可以取 $R>0$ 使得 $|t|>R$ 时有 $|\hat{g}|<\epsilon$。从而 $|t|>R$ 时有
$$|\varphi(t)| < |\hat{g}(t)|+\epsilon < 2\epsilon.$$
$\blacksquare$

:::{.note}
证明中，我们不加证明使用了两个结论：

1. 光滑函数 $g_n$ 的存在性；
2. $\sigma(\M)=\mathcal{B}(\R^n)$。

这两点原因如下：任意 $\R^n$ 中的开球都能写成某个紧支撑光滑函数的开阈值原像。给定中心 $a\in\R^n$ 和半径 $r>0$，定义标准“钟形”函数
$$\phi_{a,r}(x)=\begin{cases}
\exp\Bigl(-\dfrac{1}{1-\frac{|x-a|^2}{r^2}}\Bigr), & |x-a|<r,\\
0,& |x-a|\ge r.
\end{cases}$$
则 $\phi_{a,r}\in C_c^\infty(\mathbb{R}^n)$，并且
$$\phi_{a,r}^{-1}((0,+\infty))=\{x\in\R^n\mid\phi_{a,r}(x)>0\}=B(a,r)$$。因此每个开球 $B(a,r)$ 都属于 $\sigma(\M)$。
:::

# ✅ 25.2 Fourier inversion

:::{.lemma}
对 $\xi\geq0$，定义函数
$$S(\xi) = \int_{-r}^r\frac{\sin\xi}{\xi}\dxi.$$
则 $S(\xi)$ 是 $[0,+\infty)$ 上的连续函数，并且
$$\lim_{\xi\to\infty}S(\xi) = \pi.$$
:::

**证明**：由于被积函数 $\frac{\sin\xi}{\xi}$ 在 $\R$ 上连续。由微积分基本定理，连续函数的变上限积分是连续的，故 $S$ 在 $[0,\infty)$ 上连续。

对 $a>0$ 定义
$$F(a)=\int_0^\infty e^{-ax}\frac{\sin x}{x}\dx.$$

可以在积分号下求导，得到
$$F'(a)=-\int_0^\infty e^{-ax}\sin x\dx=-\frac{1}{1+a^2}.$$
故
$$F(a)=C-\arctan a.$$
当 $a\to+\infty$ 时，$e^{-ax}$ 强衰减，$F(a)\to 0$，而 $\arctan a\to \frac{\pi}{2}$，故 $C=\frac{\pi}{2}$。于是
$$F(a)=\frac{\pi}{2}-\arctan a=\arctan\frac{1}{a}.$$
令 $a\downarrow 0$ 即得结论。$\blacksquare$


:::{.theorem}
设 $\mu$ 是 $(\R,\mathcal{B}(\R))$ 上的概率测度，则对任何 $a<b\in\R$ 有
$$\mu((a,b)) + \frac{1}{2}\mu(\{a,b\}) = \lim_{R\to\infty}\frac{1}{2\pi}\int_{-R}^R\frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi}\hat{\mu}(\xi)\dxi.$$
:::

**证明**：
$$\begin{aligned}
I(R) &= \frac{1}{2\pi}\int_{-R}^R\frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi}\hat{\mu}(\xi)\dxi\\
&=\frac{1}{2\pi}\int_{-R}^R \frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi} \dxi\int_\R e^{i\xi x}\ud{x} \\
&=\frac{1}{2\pi}\int_\R  e^{i\xi x} \ud{x} \int_{-R}^R \frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi} \dxi\\
&=\frac{1}{2\pi}\int_\R \ud{x} \int_{-R}^R \frac{e^{i\xi(x-a)}-e^{i\xi(x-b)}}{i\xi} \dxi\\
&=\frac{1}{2\pi}\int_\R \ud{x} \int_{-R}^R \frac{\sin\xi(x-a)-\sin\xi(x-b)}{\xi} \dxi.
\end{aligned}$$
这里我们可以使用 Fubini 定理交换关于 $\xi$ 和 $x$ 的积分顺序是因为
$$F(x,\xi)=e^{i\xi x}\frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi}\ind_{[-R,R]}(\xi).$$
满足
$$|F(x,\xi)|\le |a-b|\ind_{[-R,R]}(\xi).$$
从而
$$\int_{\R}\int_{\R}|F(x,\xi)|\du\dxi\leq \int_{\R}\int_{\R} |a-b|\ind_{[-R,R]}(\xi)\du\dxi
=|a-b|\cdot \mu(\R)\cdot (2R)<\infty.$$

然后注意到
$$\begin{aligned}
\int_{-R}^R\frac{\sin\xi(x-a)}{\xi}\dxi&=\int_{-R(x-a)}^{R(x-a)}\frac{\sin\eta}{\eta}\,\mathrm{d}\eta=\begin{cases}
S(R(x-a)), & x-a > 0,\\
-S(R(a-x)), & x - a < 0.
\end{cases} \\
&= \sgn(x-a)S(R|x-a|).
\end{aligned}$$
所以
$$I(R)=\frac{1}{2\pi}\int_\R\big[\sgn(x-a)S(R|x-a|) -\sgn(x-b)S(R|x-b|)\big]\ud{x}.$$
现在，被积函数是有界的（不超过 $S(r)$ 在 $[0,+\infty)$ 上的上界 x 2），所以可以用控制收敛定理得到
$$\lim_{R\to\infty}I(R)=
\frac{1}{2}\int_\R[\sgn(x-a)-\sgn(x-b)]\ud{x}.$$
注意到现在的被积函数满足
$$\sgn(x-a)-\sgn(x-b)=\begin{cases}
0, & x > b \text{ or } x < a,\\
1, & x = a \text{ or } x = b,\\
2, & a < x < b.
\end{cases}.$$
所以
$$\lim_{R\to\infty}I(R) = \frac{1}{2}\mu(\{a,b\}) + \mu((a,b)).$$
$\blacksquare$


:::{.corollary}
设 $\mu$ 是 $(\R,\mathcal{B}(\R))$ 上的概率测度，$\hat{\mu}$ 是关于 Legesgue $L^1$ 的，则其有密度函数 $\rho$，满足
$$\rho(x)=\frac{1}{2\pi}\int_\R e^{-itx}\hat{\mu}(t)\dt.$$
:::

**证明**：令 $\rho$ 如上定义，则
$$\begin{aligned}
\int_a^b\rho(x)\dx &= \frac{1}{2\pi}\int_a^b\dx\int_\R\hat{\mu}(\xi)e^{-i\xi x}\dxi\\
&=\frac{1}{2\pi}\int_\R\hat{\mu}(\xi)\dxi \int_a^b e^{-i\xi x}\dx\\
&=\frac{1}{2\pi}\int_\R\hat{\mu}(\xi)\frac{e^{-ia\xi}-e^{-ib\xi}}{i\xi}\dxi\\
&=\lim_{R\to\infty} I(R)\\
&=\mu((a,b)) + \frac{\mu(\{a,b\})}{2}.
\end{aligned}$$
$\blacksquare$

# ✅ 25.3 The Continuity Theorem

本讲介绍了测度弱收敛的连续性定理。

:::{.theorem}
如果 $\{\mu_n\}_{n=1}^\infty$ 是一列 $(\R^d,\B(\R^d))$ 上的概率测度。假设极限 $\varphi(t) = \lim\limits_{n\to\infty}\hat{\mu_n}$ 存在，并且 $\varphi(t)$ 在 $t=0$ 处连续，则存在概率测度 $\mu$ 使得 $\hat{\mu}=\varphi$，并且 $\mu_n\rightarrow_{w}\mu$。
:::

:::{.lemma}
设 $\mu,\nu$ 是 $(\R^d,\B(\R^d))$ 上的两个概率测度，$K>0$ 是任意正实数，则
$$\int_{\R^d}\hat{\mu}(Kx)\vd{x}=\int_{\R^d}\hat{\nu}(Ky)\ud{y}.$$
:::

**证明**：要证明的是
$$\int_{\R^d}\vd{x}\int_{\R^d}e^{iKx\cdot \xi}\ud{\xi}=\int_{\R^d}\ud{y}\int_{\R^d}e^{iKy\cdot \xi}\vd{\xi}.$$
直接 Fubini 即可。

:::{.lemma}
$$\int_{\R^d}[1-\Re\hat{\mu}(Kx)]\vd{x}=\int_{\R^d}[1-\Re\hat{\nu}(Ky)]\ud{x}.$$
:::

**证明**：在前一个引理中两边取实部，然后被 1 减去即可。


:::{.corollary}
假设 $\rho$ 是一个 $\R^d$ 上的概率密度，其支集位于闭的单位球 $\bar{B}_1$ 内。设 $M>0$ 使得 $|\hat{\rho}(t)|\leq1/2$ 对任何 $|t|\geq M$ 成立，则对任何 $(\R^d,\B(\R^d))$ 上的概率测度 $\mu$ 和正数 $\alpha>0$ 有
$$\mu\{x\in\R^d:\ |x|\geq\alpha\}\leq 2\int_{\bar{B}_1}\left[1-\Re\hat{\mu}\left(\frac{M}{\alpha}x\right)\right]\rho(x)\dx.$$
:::

**证明**：设
$$\hat{\mu}(t)=\int_{\R^d}e^{it\cdot x}\ud{x},\quad \hat{\rho}(t)=\int_{\R^d}e^{it\cdot x}\rho(x)\dx.$$
令 $K=\frac{M}{\alpha}$，由于 $\rho$ 的支集包含在 $\bar B_1$ 中，所以
$$2\int_{\bar B_1}\bigl[1-\Re\hat{\mu}(Kx)\bigr]\rho(x)\dx=2\int_{\R^d}\bigl[1-\Re\hat{\rho}(Ky)\bigr]\ud{y}.$$
由假设，当 $|y|\ge\alpha$ 时有 $|K y|=\frac{M}{\alpha} |y|\ge M$，从而
$$1-\Re\hat{\rho}(K y)\ge1-|\hat{\rho}(K y)|\ge\frac{1}{2}.$$
故 $|y|\ge\alpha$ 时有
$$2\bigl(1-\Re\hat{\rho}(K y)\bigr)\ge \ind_{\{|y|\ge\alpha\}}(y).$$
这个式子对 $|y|<\alpha$ 也成立，所以同时对 $\mu$ 积分得到
$$2\int_{\R^d}\bigl[1-\Re\hat{\rho}(K y)\bigr]\ud{y}\ge\int_{\R^d}\ind_{\{|y|\ge\alpha\}}\ud{y}=\mu(\{|y|\ge\alpha\}).$$
把左边换回原式即得
$$\mu(\{|x|\ge\alpha\})\le2\int_{\bar B_1}\left[1-\Re\hat{\mu}\left(\tfrac M\alpha x\right)\right]\rho(x)\dx.$$
$\blacksquare$

:::{.corollary}
设 $\{\mu_n\}_{n=1}^\infty$ 是 $(\R^d,\mathcal{B}(\R^d))$ 上的概率测度，且
$\varphi(t)=\lim\limits_{n\to\infty}\hat{\mu}_n(t)$ 处处存在，并且 $\varphi$ 在 $t=0$ 处连续。则 $\{\mu_n\}_{n=1}^\infty$ 是 tight 的。
:::

**证明**：记
$$I_n(\alpha)=2\int_{\bar B_1}\bigl[1-\Re\hat{\mu}_n(\tfrac M\alpha x)\bigr]\rho(x)\dx.$$

由于 $|1-\Re\hat{\mu}_n|\le 2$ 且 $\rho$ 为概率密度，故由控制收敛定理
$$\lim_{n\to\infty}I_n(\alpha)=I(\alpha)=2\int_{\bar B_1}\bigl[1-\Re\varphi(\tfrac M\alpha x)\bigr]\rho(x)\dx.$$

由于 $\varphi$ 在 $0$ 处连续且对每个 $x$ 有 $\tfrac M\alpha x\to 0$，仍由控制收敛定理得
$$I(\alpha)\xrightarrow{\alpha\to\infty}0.$$

给定 $\epsilon>0$。取 $\alpha_1$ 使得 $I(\alpha_1)\le\epsilon/2$。再取 $N$ 使得对所有 $n\ge N$ 有
$$I_n(\alpha_1)\le I(\alpha_1)+\epsilon/2\le \epsilon.$$

从而 $\mu_n(\{|x|\ge \alpha_1\})\le I_n(\alpha_1)\le\epsilon$ 对所有 $n\ge N$ 成立。

对那些 $n<N$，由于 $\hat{\mu}_n$ 作为特征函数在 0 处连续，$\alpha\to\infty$ 时 $I_n(\alpha)\to 0$，因此可取 $\alpha_0$ 使
$$\max_{1\le n<N}\mu_n(\{|x|\ge \alpha_0\})\le \max_{1\le n<N} I_n(\alpha_0)\le\epsilon.$$

令 $R=\max\{\alpha_0,\alpha_1\}$。则

+ 若 $n\ge N$，则 $\mu_n(\{|x|\ge R\})\le \mu_n(\{|x|\ge \alpha_1\})\le\epsilon$；
+ 若 $n< N$，同理 $\mu_n(\{|x|\ge R\})\le \mu_n(\{|x|\ge \alpha_0\})\le\epsilon$。

于是
$$\sup_{n\ge1}\mu_n(\{|x|\ge R\})\le\epsilon.$$
这正是 tightness 的定义。$\blacksquare$

:::{.corollary}
设 $\{\mu_n\}_{n=1}^\infty$ 是 $(\R^d,\mathcal{B}(\R^d))$ 上的概率测度，且
$\varphi(t)=\lim\limits_{n\to\infty}\hat{\mu}_n(t)$ 处处存在，并且 $\varphi$ 在 $t=0$ 处连续。则存在概率测度 $\mu$ 使得 $\varphi=\hat{\mu}$ 并且 $\mu_n\to_w \mu$。
:::

**证明**：由于 $\{\mu_n\}$ 是 tight 的，根据 Prokhorov，存在子序列 $\{\mu_{n_k}\}$ 弱收敛到某个概率测度 $\mu_{n_k}\to_w\mu$。于是
$$\varphi=\lim_{k\to\infty}\hat\mu_{n_k} =\hat{\mu}.$$
从而对整个序列也有
$$\varphi=\lim_{n\to\infty}\hat\mu_{n} =\hat{\mu}.$$
这样我们就证明了 $\varphi=\hat\mu$ 是概率测度 $\mu$ 的 Fourier 变换。

我们断言整个 $\{\mu_n\}$ 都弱收敛到 $\mu$。若不然，存在有界连续函数 $g$ 使得
$$\int_{\R^d} g \,\mathrm{d}\mu_n \nrightarrow \int_{\R^d} g \du.$$
于是对任何 $\epsilon>0$，存在子序列 $\{\mu_{n_k'}\}$ 使得
$$\left|\int_{\R^d} g \,\mathrm{d}\mu_n - \int_{\R^d} g \du\right|\ge\epsilon,\quad \forall k.$$
但是 $\{\mu_{n_k'}\}$ 也是 tight 的，所以再用一次 Prokhorov 定理，存在二级子序列 $\{\mu_{n_k''}\}\subset\{\mu_{n_k'}\}$ 使得 $\mu_{n_k''}\to_w\nu$。于是 $\hat\mu_{n_k''}\to \hat\nu$。我们上面已经证明了 $\hat\mu_{n_k''}\to\hat\mu$，从而 $\hat\mu=\hat\nu$，由 Fourier inversion 有 $\mu=\nu$。即 $\mu_{n_k''}\to_w\mu$。矛盾。$\blacksquare$

# ✅ 26.1 Central Limit Theorem

:::{.theorem}
**Basic Central Limit Theorem**

设 $\{X_n\}_{n=1}^\infty$ 是 i.i.d 的 $L^2$ 随机变量，具有共同的期望 $\E[X_n]=a$ 和 $\mathrm{Var}[X_n]=\sigma^2$。则
$$\frac{S_n-na}{\sigma\sqrt{n}}\to_w \N(0,1).$$
:::

**证明**：记 $Z_n = \frac{S_n-na}{\sigma\sqrt{n}}$。我们只要证明特征函数的收敛
$$\varphi_{Z_n}(t) \to e^{-t^2/2},\quad \forall t\in\R.$$
那么根据 Levy 连续性定理：

+ 若一列特征函数 $\varphi_{Z_n}$ 对每个 $t$ 都有极限 $\varphi(t)$，且 $\varphi$ 在 $t=0$ 处连续，那么
+ $\varphi$ 本身就是某个概率分布的特征函数；
+ $Z_n$ 的分布按弱收敛收敛到这个分布。

就得到 $Z_n\to_w \N(0,1)$，因为 $e^{-t^2/2}$ 显然在 0 处连续，且它就是标准正态的特征函数。

记 $Y_1=X_1-a$，则 $\E Y_1=0$ 且 $\E Y_1^2 = \sigma^2<\infty$，所以 $Y_1$ 的特征函数 $\varphi(t)$ 是 $C^2$ 的。根据 Taylor 展开，
$$\varphi(t) = \varphi(0)+\varphi'(0)t + \frac{1}{2}\varphi''(r(t))t^2,\quad 0<r(t)<t.$$
注意到
$$\varphi'(0) = \E[iY_1 e^{itY_1}]\Big|_{t=0}=i\E Y_1 = 0.$$
所以
$$\varphi(t) = \varphi(0)+\frac{1}{2}\varphi''(r(t))t^2,\quad 0<r(t)<t.$$
利用
$$\lim_{t\to 0}\varphi''(r(t))=\varphi''(0)=-\E Y_1^2 = -\sigma^2.$$
以及熟知的微积分结论
$$\lim_{n\to\infty}\left(1+ \frac{c_n}{n}\right)^n= e^c,\quad c_n\to c.$$
可得
$$\begin{aligned}
\lim_{n\to\infty}\left(\varphi\left(\frac{\xi}{\sigma\sqrt{n}}\right)\right)^n
&=\lim_{n\to\infty}\left(1+\frac{1}{2}\varphi''\left(r\left(\frac{\xi}{\sigma\sqrt{n}}\right)\right)\frac{\xi^2}{\sigma^2 n}\right)^n\\
&=\lim_{n\to\infty}\left(1+ \frac{-\xi^2/2}{n}\right)^n\\
&=e^{-\xi^2/2}.
\end{aligned}$$
$\blacksquare$

:::{.lemma}
**Cramer-Wold Device**
设 $\{X_n\}$ 和 $X$ 都是 $\R^d$ 中的随机向量。则 $X_n\to_w X$ 当且仅当对任何 $\xi\in\R^d$ 有 $\xi\cdot X_n\to_w \xi\cdot X$。
:::

**证明**：如果对 $\xi\in\R^d$ 有 $\xi\cdot X_n\to_w \xi\cdot X$，则
$$\exp(i\xi\cdot X_n)\to_w \exp(i\xi \cdot X).$$
所以
$$\E f(\exp(i\xi\cdot X_n))\to \E f(\exp(i\xi \cdot X)).\quad \forall f\in C_b(\mathbb{C}).$$
取 $f(z)$ 满足 $f(z)=z\,(|z|\leq 1)$ 和 $f(z)=1\,(|z|>1)$，则
$$\varphi_{X_n}(\xi) \to \varphi_X(\xi).$$
由连续性定理可得 $X_n\to_w X$。

反过来，若 $X_n\to_w X$，则对任何实数 $u$，
$$\varphi_{\xi\cdot X_n}(u)=\E[e^{iu\xi\cdot X_n}]\to \E[e^{iu\xi\cdot X}]=\varphi_{\xi\cdot X}(u).$$
由连续性定理，$\xi\cdot X_n\to_w \xi\cdot X$。$\blacksquare$

:::{.note}
这个结论的证明可以直接用 **Portmanteau 定理**：若 $X_n\to_w X$，则对任意**有界连续**函数 $h:\R^d\to\R$，有 $\E[h(X_n)]\to \E[h(X)]$。
:::

:::{.theorem}
**Multivariate CLT**

设 $X_1,X_2,\dots$ 是 $\R^d$ 上的 i.i.d. 随机向量，$\mu=\E X_1\in\mathbb R^d$，协方差矩阵 $\Sigma=\mathrm{Cov}(X_1)$（允许奇异）。令
$$S_n=\sum_{k=1}^n X_k,\qquad Z_n=\frac{S_n-n\mu}{\sqrt n}.$$
则
$$Z_n \ \to_w \ N_d(0,\Sigma).$$
:::

**取任意方向做投影，化为一维问题。**

对任意 $\xi\in\R^d$，令 $Y_{k,\xi}=\xi^\top (X_k-\mu)$。则 $Y_{1,\xi},Y_{2,\xi},\dots$ 是一维 i.i.d.，且
$$\E Y_{k,\xi}=0,\quad \mathrm{Var}(Y_{k,\xi})=\xi^\top\Sigma\xi.$$
并且
$$\xi^\top Z_n=\frac1{\sqrt n}\sum_{k=1}^n Y_{k,\xi}.$$

**对每个 $\xi$ 应用一维中心极限定理。**

由一维 CLT（Lindeberg–Lévy）得
$$\xi^\top Z_n \ \to_w\ \N\big(0,\ \xi^\top\Sigma\xi\big),\quad \forall\xi\in\R^d.$$

**用 Cramér–Wold 得出向量弱收敛。**

既然对所有 $\xi$ 都有 $\xi^\top Z_n \Rightarrow \N(0,\xi^\top\Sigma\xi)$，由 **Cramér–Wold**知 $Z_n\to_w Z$（某极限向量），并且该极限 $Z$ 的任意线性投影都是正态，且
$$\mathrm{Var}(\xi^\top Z)=\xi^\top\Sigma\xi,\quad \forall\xi.$$
这唯一刻画了 $Z$ 的分布为 $\N_d(0,\Sigma)$。因此
$$Z_n \Rightarrow \N_d(0,\Sigma).$$

# ✅ 26.2 Infinitely Divisible Distributions

:::{.definition}
$(\R,\B(\R))$ 上的一个概率分布 $\mu$ 称作是无穷可除的，如果对任何正整数 $n$，都存在 $(\R,\B(\R))$ 上的概率分布 $\mu_n$ 使得 $\mu=\mu_n^{\ast n}$。
:::

:::{.theorem}
$\mu$ 是无穷可除分布，当且仅当存在随机变量的三角列
$$\{X_{n,k}\}_{k=1}^{n}$$
满足对每个 $n$，$\{X_{n,k}\}$ 是 i.i.d 的，并且
$$S_n = \sum_{k=1}^{n}X_k \to_w X\overset{d}{=}\mu.$$
:::

**证明**：$\Rightarrow$：由无穷可除的定义，显然。

$\Leftarrow$: 固定任意 $l\in\mathbb N$。对第 $nl$ 行把和分成 $l$ 个相邻的块：
$$S_{nl}=\sum_{k=1}^{nl}X_{nl,k}=\sum_{i=1}^l S_n^{(i)},\qquad
S_n^{(i)}:=\sum_{j=n(i-1)+1}^{ni} X_{nl,j}.$$
由于同一行内独立同分布，$(S_n^{(1)},\dots,S_n^{(l)})$ 相互独立且同分布。

设 $\mu_{nl}=\mathcal L(S_{nl})$。因为 $S_{nl}\Rightarrow X$，${\mu_{nl}}$ tight。定义
$$\epsilon_l(r):=\sup_{n\ge1}\mathbb P(|S_{nl}|>r)\downarrow 0\quad (r\to\infty).$$
对任意 $r>0$ 与任意 $n$，由独立性有
$$\mathbb P(S_n^{(1)}>r,\dots,S_n^{(l)}>r)
=\prod_{i=1}^l\mathbb P(S_n^{(i)}>r)
\le \P(S_{nl}>lr)\le \epsilon_l(lr).$$
故 $\P(S_n^{(1)}>r)\le \epsilon_l(lr)^{1/l}$，同理
$\mathbb P(S_n^{(1)}<-r)\le \epsilon_l(lr)^{1/l}$，于是
$$\sup_{n}\mathbb P\big(|S_n^{(1)}|>r\big)\le 2\epsilon_l(lr)^{1/l}\xrightarrow{r\to\infty}0,$$
即 $\{\mathcal L(S_n^{(1)})\}_n$ 紧。由 Prokhorov 定理，存在子列 $n_j$ 使得
$$S_{n_j}^{(1)}\overset{j\to\infty}{\Rightarrow} Y_l.$$
由于 $\mathcal L(S_n^{(i)})=\mathcal L(S_n^{(1)})$，所以
$S_{n_j}^{(i)}\Rightarrow Y_l$ 亦成立。

对每个 $t\in\mathbb R$，有
$$\varphi_{S_{n_j l}}(t)
=\prod_{i=1}^l \varphi_{S_{n_j}^{(i)}}(t)
=\big(\varphi_{S_{n_j}^{(1)}}(t)\big)^{l}.
$$
当 $j\to\infty$ 时，左边因 $S_{n_j l}\Rightarrow X$ 收敛到 $\varphi_X(t)$；右边因
$S_{n_j}^{(1)}\Rightarrow Y_l$ 收敛到 $\big(\varphi_{Y_l}(t)\big)^l$。因此
$$\varphi_X(t)=\big(\varphi_{Y_l}(t)\big)^l,\qquad \forall t\in\mathbb R.$$
由 Lévy 连续性定理知 $\mu=\mu_{Y_1}{*l}$。由于 $l$ 任意，$\mu$ 为无穷可除。证毕。 $\blacksquare$

# ✅ 27.1 Average Uniformity

设 $\{X_{n,k}\}_{k=1}^n$ 是一个随机变量三角列，满足
$$\E[X_{n,k}]=0,\ \E[X_{n,k}^2]=\sigma_{n,k}^2,\ \sum_{k=1}^n\sigma_{n,k}^2=1.$$

+ **(DV) The decaying variance conditon**
$$\max_{1\leq k\leq n}\sigma_{n,k}^2\xrightarrow{n\to\infty} 0.$$
+ **(UAN) The uniform asymptotic negligiblility condition**
$$\forall \epsilon > 0,\ \lim_{n\to\infty}\max_{1\leq k\leq n}\P(|X_{n,k}|>\epsilon)=0.$$

:::{.lemma}
DV $\Rightarrow$ UAN.
:::

**证明**：由切比雪夫不等式 $\P(|X_{n,k}|>\epsilon) \leq \frac{\sigma_{n,k}^2}{\epsilon^2}$ 即得。

但是，仅有 DV 条件仍不能保证中心极限定理的成立。我们需要一个更强的条件：

:::{.definition}
**Lindberg 条件**

$$\lim_{n\to\infty}\sum_{k=1}^n \E[X_{n,k}^2: |X_{n,k}|>\epsilon ]=0,\quad\forall\epsilon>0.$$
:::

:::{.lemma}
Lindberg $\Rightarrow$ DV.
:::

证明：
$$\sigma_{n,k}^2=\E[X_{n,k}^2: |X_{n,k}|\leq\epsilon]+\E[X_{n,k}^2: |X_{n,k}|>\epsilon]\leq\epsilon^2 + \sum_{j=1}^n\E[X_{n,j}^2: |X_{n,j}|>\epsilon].$$

对 $k$ 取最大值得
$$\max_{1\le k\le n}\sigma_{n,k}^2\le \epsilon^2 + \sum_{j=1}^n \E\big[X_{n,j}^2:\ |X_{n,j}|> \epsilon\big].$$
由 Lindeberg 条件，右端和式随 $n\to\infty$ 收敛到 $0$，故
$$\limsup_{n\to\infty}\max_{1\le k\le n}\sigma_{n,k}^2\le \epsilon^2.$$
由于 $\epsilon>0$ 任意，必有
$$\max_{1\le k\le n}\sigma_{n,k}^2 \xrightarrow[n\to\infty]{} 0.$$
即 DV 成立。$\blacksquare$

:::{.theorem}
**Lindberg-Feller 中心极限定理**

如果 $\{X_{n,k}\}$ 满足 Lindberg 条件，则 $S_n\to_w\N(0,1)$。

反之，如果 $\{X_{n,k}\}$ 满足 DV 条件，且 $S_n\to_w\N(0,1)$，则 $\{X_{n,k}\}$ 也满足 Lindberg 条件。
:::


# ✅ 27.2 Lindberg-Feller CLT

:::{.lemma}
设 $a_j,b_j$ 是复数且 $|a_j|, |b_j|\leq1$，则
$$|a_1\cdots a_n - b_1\cdots b_n|\leq\sum_{j=1}^n |a_j-b_j|.$$
:::

证明：用归纳法即可。

:::{.lemma}
如果 $X$ 是 $L^2$ 可积的随机变量，$\varphi$ 是其特征函数，则
$$\left|\varphi(t) - 1 - it\E X + \frac{1}{2}\E[X^2]t^2\right|\leq \E\left[X^2\wedge\frac{|X|^3}{3!}t\right].$$
:::

证明：根据 Taylor 定理，
$$\left|e^{it} - 1 - it\right|\leq \frac{t^2}{2}.$$
$$\left|e^{it} - 1 - it+ \frac{1}{2}t^2\right|\leq \frac{|it|^3}{3!}.$$
合起来就得到
$$\left|e^{it} - 1 - it+ \frac{1}{2}t^2\right|\leq t^2\wedge \frac{|it|^3}{3!}.$$
取 $tX$ 代入并求期望，得到
$$\left|\E\left[e^{itX} - 1 - itX+ \frac{1}{2}t^2X^2\right]\right|\leq \E\left[t^2X^2\wedge \frac{|X|^3}{3!}t^3\right].$$
即为所证。$\blacksquare$


:::{.theorem}
**Lindberg-Feller CLT Part 1**

如果三角列 $\{X_{n,k}\}$ 满足 Lindberg 条件，则 $S_n\to_w\N(0,1)$。
:::

:::{.note}
注意 Lindberg-Feller CLT 仍然要求 $\{X_{n,k}\}$ 对每个 $n$ 都是 i.i.d 序列。
:::

**证明**：只要证 $\varphi_{S_n}\to e^{-t^2/2}$ 即可。

根据第一个引理，结合 $\sum_{k=1}^n\sigma_{n,k}^2=1$，我们得到

$$|\varphi_{S_n}(t) - e^{-t^2/2}|\leq \sum_{k=1}^n\left|\varphi_{X_{n,k}}(t) - e^{-\sigma_{n,k}^2t^2/2}\right|.$$
注意这个特征函数的分解就用到了 i.i.d 性质。

$$\begin{aligned}
|\varphi_{X_{n,k}}(t) - e^{-\sigma_{n,k}^2t^2/2}| &\le |\varphi_{X_{n,k}}(t)-(1-\frac{t^2\sigma_{n,k}^2}{2})|+|(1-\frac{t^2\sigma_{n,k}^2}{2})-e^{-\sigma_{n,k}^2t^2/2}|.
\end{aligned}$$
记第一项是 $A_{n,k}$，第二项是 $B_{n,k}$，问题转化为证明
$$\lim_{n\to\infty}\sum_{k=1}^n (A_{n,k}+B_{n,k})=0.$$
我们任取一个正数 $\epsilon>0$。注意到 $\E[X_{n,k}]=0$，所以
$$\begin{aligned}
A_{n,k}&=|\varphi_{X_{n,k}}(t)-(1-\frac{t^2\sigma_{n,k}^2}{2})|\leq t^2\left(\E X_{n,k}^2\wedge \frac{|X_{n,k}|^3}{3!}t\right)\\
&\le t^2\left(
\E\left[X_{n,k}^2\wedge \frac{|X_{n,k}|^3}{3!}t: |X_{n,k}|\leq\epsilon\right]
+\E\left[X_{n,k}^2\wedge \frac{|X_{n,k}|^3}{3!}t: |X_{n,k}|>\epsilon\right]
\right)\\
&\le |t|^3\frac{\epsilon}{3!}\E[X_{n,k}^2]+t^2\E\left[X_{n,k}^2: |X_{n,k}|>\epsilon\right]\\
&= |t|^3\frac{\epsilon}{3!}\sigma_{n,k}^2+t^2\E\left[X_{n,k}^2: |X_{n,k}|>\epsilon\right]
\end{aligned}$$
所以
$$\sum_{k=1}^n A_{n,k}\le |t|^3\frac{\epsilon}{3!}\sum_{k=1}^n\sigma_{n,k}^2+t^2\sum_{k=1}^n\E\left[X_{n,k}^2: |X_{n,k}|>\epsilon\right].$$
于是
$$\limsup_{n\to\infty}\sum_{k=1}^n A_{n,k}\leq \frac{|t|^3}{6}\epsilon.$$
由 $\epsilon$ 任意性即得。

再来估计 $B_{n,k}=|(1-\frac{t^2\sigma_{n,k}^2}{2})-e^{-\sigma_{n,k}^2t^2/2}|$。利用 $|e^{-u}-(1-u)|\leq\frac{u^2}{2}$，可得
$$\sum_{k=1}^n B_{n,k}\le\frac{1}{8}t^4\sum_{k=1}^n\sigma_{n,k}^4 \le\frac{1}{8}t^4\max_{k}\sigma_{n,k}^2.$$
由于 Lindberg 条件意味着 DV 条件，故 $n\to\infty$ 时上式右边趋于 0，得证。$\blacksquare$


# ✅ 30.2 Conditional Expectation, Part 1

无要点

# ✅ 31.1 Orthogonal Projections

一些关于 Hilber 空间 $L^2$ 的基本结论，无要点

# ✅ 32.3 Conditioning on Random Variables

:::{.proposition}
设 $X:(\Omega,\mathcal F)\to(S,\mathcal B)$，$Y:(\Omega,\mathcal F)\to(T,\mathcal C)$ 为随机变量。若 $X$ 与 $Y$ 独立，且 $f\in \mathbb B(S\times T,\mathcal B\otimes\mathcal C)$（有界可测），则对 $\mu_X$-a.e. 的 $x$ 有
$$\E\left[f(X,Y)\mid X=x\right]=\int_T f(x,y)\,\mu_Y(\mathrm d y).$$
等价地，
$$\mathbb E\left[f(X,Y)\mid \sigma(X)\right]= g(X)\quad a.s.,\quad
g(x):=\int_T f(x,y)\,\mu_Y(\mathrm d y).$$
:::

**证明**：由独立性，联合分布 $\mu_{X,Y}=\mu_X\otimes \mu_Y$。令
$$g(x):=\int_T f(x,y)\,\mu_Y(\dy).$$
则按核积分的可测性引理，$g$ 是 $\mathcal B$-可测且有界。

取任意 $h\in\mathbb B(S,\mathcal B)$，有（把期望写成对联合分布的积分并用 Fubini/Tonelli）
$$
\begin{aligned}
\mathbb E\left[f(X,Y)h(X)\right]
&=\int_{S\times T} f(x,y)h(x)\,(\mu_X\otimes\mu_Y)(\dx\dy)\\
&=\int_{S}\left(\int_{T} f(x,y)\,\mu_Y(\dy)\right) h(x)\,\mu_X(\dx)\\
&=\int_S g(x)h(x)\,\mu_X(\dx)\\
&=\mathbb E\left[g(X)h(X)\right].
\end{aligned}
$$
以上对一切有界 $\mathcal B$-可测 $h$ 成立，故按条件期望的刻画，
$$
\mathbb E\left[f(X,Y)\mid \sigma(X)\right]=g(X)\quad a.e.
$$
从而对 $\mu_X$-a.e. 的 $x$，
$$
\mathbb E\left[f(X,Y)\mid X=x\right]=g(x)=\int_T f(x,y)\,\mu_Y(\dy).
$$
证毕。


# ✅ 33.1 Probability Kernels, Part 1

本讲引入了概率核的概念。

设 $(S_i,\B_i), i=1,2$ 是两个可测空间，一个概率核 $Q(x, B):S_1\times\B_2\to[0,1]$ 是一个二元函数，满足：

1. 对任何 $x\in S_1$，$Q(x,\cdot):\B_2\to[0,1]$ 是 $(S_2,\B_2)$ 上的概率测度。
2. 对任何 $B\in \B_2$，$Q(\cdot, B):S_1\to[0,1]$ 是 $(S_1,\B_1)$ 上的可测函数。

:::{.lemma}
假设 $f(x,y)\in (S_1\times S_2, \B_1\otimes\B_2)$ 是乘积空间上的可测函数，并且是有界的或者非负的，则积分 $$x\to\int_{S_2}f(x,y)Q(x,\dy)$$ 是关于 $x$ 的可测函数。
:::

此引理不难从简单函数 $\ind_{B_1\times B_2}(x,y)=\ind_{B_1}(x)\ind_{B_2}(y)$ 出发，使用函数形式的 Dynkin 引理得到。

由此对任何 $(S_1,\B_1)$ 上的测度 $\mu$，我们可以定义乘积空间 $(S_1\times S_2, \B_1\otimes\B_2)$ 上的乘积测度 $\mu\otimes Q$：
$$(\mu\otimes Q)(E)=\int_{S_1}\ud{x}\int_{S_2}\ind_{E}(x,y)Q(x,\dy).$$
不过这真的是一个概率测度吗？你可以用积分的线性性质立刻看出它是有限可加的，并且利用积分项有界和控制收敛定理立刻看出它是可数可加的，所以确实是个概率测度。

有了概率核的乘积测度，我们自然要研究对这种测度的积分。由于这个测度本身就是通过对示性函数积分来定义的，所以其上的积分也具有类似的性质：

:::{.lemma}
假设 $f(x,y)$ 是乘积空间的可测函数，并且是有界或者非负的，则
$$\int_{S_1\times S_2}f\,\mathrm{d}(\mu\otimes Q) = \int_{S_1}\mu(\dx)\int_{S_2}f(x,y)Q(x,\dy).$$
:::


:::{.theorem}
若两核 $(Q,\tilde Q)$ 只在 $\mu$-零集上不同，即 $Q(x,\cdot)=\tilde Q(x,\cdot)$ for $\mu$-a.e. $x$，则由它们和边缘 $\mu$ 拼出来的“联合测度”是**同一个**测度：$\mu\otimes Q=\mu\otimes \tilde Q$。

反过来，如果 $\B_2$ 是可数生成的，则如果 $\mu\otimes Q=\mu\otimes \tilde Q$，那么 $Q(x,\cdot)=\tilde Q(x,\cdot)$ 对 $\mu$-a.e. 的 $x$ 成立。
:::

**意义**：正则条件分布/概率核通常只在 $\mu$-a.e. 意义下唯一。若 $\mu\otimes Q$ 会因零集上的改动而改变，那很多定义就不稳固了。这个结论保证：**任选一个版本**都得到**同一**联合测度与同一组期望值 $\displaystyle \int f\,\mathrm{d}(\mu\otimes Q)=\int \mu(\mathrm{d}x)\int f(x,y)\,Q(x,\mathrm{d}y)$。

**证明**：$\Rightarrow$：
$$\begin{aligned}
(\mu\otimes Q)(B_1\times B_2) &= \int_{S_1}\ud{x}\int_{S_2}\ind_{B_1}(x)\ind_{B_2}(y) Q(x,\dy)\\
&=\int_{B_1}\ud{x} Q(x,B_2) = \int_{B_1}\ud{x} \tilde Q(x,B_2).
\end{aligned}$$

$\Leftarrow$：如果 $\mu\otimes Q=\mu\otimes \tilde Q$，上面的计算给出
$$\int_{B_1}\ud{x}Q(x,B_2) = \int_{B_2}\ud{x}\tilde Q(x,B_2),\quad \forall B_1\in\B_1,B_2\in\B_2.$$
于是
$$\int_{S_1}[Q(x,B_2) - \tilde Q(x,B_2)]\ind_{B_1}(x)\ud{x} = 0,\quad\forall B_1\in\B_1.$$
从而
$$\int_{S_1}[Q(x,B_2) - \tilde Q(x,B_2)]h(x)\ud{x} = 0,\quad\forall h\in\mathbb{B}(S_1,\B_1).$$
这必须有 $Q(x,B_2) =\tilde Q(x,B_2)$ 几乎处处成立才行。$\blacksquare$


# ✅ 33.2 Regular Conditional Distributions

本讲使用概率核给出了 $\E[f(X, Y)\mid X=x]$ 这种条件期望的严格定义。

:::{.theorem}
设 $(\Omega,\F,\P)$ 是一个概率空间，$(S_i,\B_i),\,i=1,2$ 是两个可测空间。
$$X:(\Omega,\F)\to(S_1,\B_1),\quad Y:(\Omega,\F)\to(S_2,\B_2)$$
是两个随机变量。于是
$$(X,Y):(\Omega,\F)\to(S_1\times S_2,\,\B1\otimes\B_2)$$

是随机向量。记 $\mu_{X,Y}$ 为此随机向量在 $(S_1\times S_2,\,\B1\otimes\B_2)$ 上 push forward 给出的测度，$\mu_X$ 是 $X$ 在 $(S_1,\B_1)$ 上 push forward 给出的测度。如果存在概率核 $Q(x,B)$ 使得 $$\mu_{X,Y}=\mu_X\otimes Q.$$

则对任何 $f\in L^1(S_1\times S_2,\B1\otimes\B_2)$ 有
$$\E[f(X,Y)\mid X = x] = \int_{S_2}f(x,y)Q(x, \dy).$$
:::

这里需要解释 $\E[f(X,Y)\mid X = x]$ 这个记号的含义。这里其实引用了条件期望 (后面才会讲到) 的性质：$\E[f(X,Y)\mid X]$ 是一个关于 $\sigma(X)$ 可测的随机变量，从而由 Doob-Dynkin 表示定理，存在可测函数 $g$ 使得 $\E[f(X,Y)\mid X] = g(X)$，所以 $\E[f(X,Y)\mid X = x] = g(x)$。这个定理说的就是
$$g(x):=\E[f(X,Y)\mid X = x] = \tilde g(x):=\int_{S_2}f(x,y)Q(x, \dy).$$

**证明**：怎么证明两个关于 $\sigma(X)$ 可测的函数 (几乎处处) 相等呢？我们可以给它们同时乘以 $h(x)$，这里 $h(x)$ 是任何一个关于 $\sigma(X)$ 可测的有界函数，然后证明它们对 $\mu_X$ 积分以后的值相等，则这两个可测函数必相等。

$g(x)h(x)$ 这个函数对 $\mu_X$ 积分，根据积分变量替换定理，正是 $\E[g(X)h(X)]$。而根据 $g(x)$ 的定义和条件期望的性质，
$$\E[g(X)h(X)]=\E[\E[f(X,Y)|X]h(X)] = \E[\E[f(X,Y)h(X)|X]] = \E[f(X, Y)h(X)].$$
注意右边的期望悄悄地变成了关于 $\mu_X\otimes Q$ 的积分。这是因为上式最后的等号使用了条件期望的 telescoping 性质，而 $f(X,Y)g(X)$ 是关于 $\B_1\otimes\B_2$ 可测的函数。

另一方面，
$$\begin{aligned}
\E[f(X,Y)h(X)] &= \int_{S_1\times S_2}f(x,y)h(x)\mu_{X,Y}(\dx\dy) \\
&= \int_{S_1\times S_2}f(x,y)h(x)\mu_X\otimes Q \\
&= \int_{S_1}\ud{x} \int_{S_2}f(x,y)h(x)Q(x,\dy) \\
&= \int_{S_1}h(x)\ud{x} h(x)\int_{S_2}f(x,y)Q(x,\dy)\\
&= \int_{S_1}\tilde g(x)h(x)\ud{x}\\
&= \E[\tilde g(x)h(x)].
\end{aligned}$$
正是所要证明的。

不过在上面的证明中我们都假定了所有的可积性的前提。我们实际上需要假定 $f(x,y)$ 有界才能确保推导成立。对一般的 $f(x,y)\in L^1(S_1\times S_2,\B_1\otimes \B_2)$，取有界函数列 $f_n=f\ind_{|f|\le n}\xrightarrow{L^1}f$。由于条件期望是 contraction，所以
$$\E[f_n(X, Y)| X] \xrightarrow{L^1} \E[f(X,Y)|X].$$
我们上面已经证明了
$$\E[f_n(X, Y)| X] = \left.\int_{S_2}f_n(x,y)Q(x,\dy)\right|_{x=X}.$$
所以只要证明
$$\left.\int_{S_2}f_n(x,y)Q(x,\dy)\right|_{x=X} \xrightarrow{L^1} \left.\int_{S_2}f(x,y)Q(x,\dy)\right|_{x=X}.$$
即可。这个 $L^1$ 收敛的意思是对 $\mu_X$ 取积分，因此我们要估计
$$\int_{S_1}\mu(\dx)\int_{S_2}|f_n(x,y)-f(x,y)|Q(x,\dy).$$
这不正是 $|f_n-f|$ 对乘积测度的积分嘛，而我们已经知道了它是 $L^1$ 收敛的了。

所以如果我们能把一个联合分布分解为边际分布和一个概率核的乘积，则我们就得到了条件概率的一个表示。

> **问题**：$\mu_{X,Y}$ 总可以表示为 $\mu_X\otimes Q$ 的形式吗？

:::{.theorem}
如果概率核 $Q(x, B)$ 满足
$$\P(Y\in B | X=x) = Q(x, B)$$
(这个条件等价于
$$\E[h(Y) | X] = \left.\int h(y) Q(x,\dy)\right|_{x=X}.$$
对任何有界的可测函数 $h(y)$ 成立)

则对 $f(x,y)$ 同样有
$$\E[f(X,Y) | X] = \left.\int f(x,y) Q(x,\dy)\right|_{x=X}.$$
成立。
:::

这个定理可以先从 $f(x,y)=f(x)\otimes g(y)$ 形式的函数出发，然后用 Dynkin 函数系引理得到。

总结一下，至此我们讨论了：

1. 如果 $\mu_{X,Y}=\mu_X\otimes Q$，那我们就有了 $\E[f(X,Y)|X]$ 的计算方法：积分 $\int_{S_2}f(X,y)Q(X,\dy)$。特别地我们可以算条件概率了。
2. 反之如果我们有一个概率核给出条件概率：$\P(Y\in B | X=x) = Q(x, B)$，那么它就给出 $\mu_{X,Y}$ 的一个分解：$\mu_{X,Y}=\mu_X\otimes Q$。

:::{.theorem}
当 $S_2$ 是标准 Borel 空间或者 Polish 空间时，正则条件概率存在。
:::

**证明**：我们对 $S=\R$ 的情形证明。设 $(\Omega,\F,\P)$ 为概率空间，$\mathcal G\subset\F$ 为子 $\sigma$-代数，$Y:(\Omega,\F)\to(\R,\B(\R))$ 可测。

对每个 $q\in\mathbb Q$，设
$$G(q,\omega):=\mathbb P(Y\le q\mid \mathcal G)(\omega).$$
由 $\ind_{\{Y\le q_1\}}\le\ind_{\{Y\le q_2\}}$与条件期望的单调性，丢掉可数零集 $\bigcup_{q_1,q_2} \{\omega\mid G(q_1,\omega)\not\le G(q_2,\omega)\}$ 后可取版本使得对每个 $\omega$，$q\mapsto G(q,\omega)$ 非降。定义
$$
F(x,\omega):=\inf\{\,G(q,\omega):q\in\mathbb Q,\ q>x\,\}.
$$
则对每个 $\omega$，$F(\cdot,\omega)$ 非降、右连续，且 $\lim_{x\to-\infty}F(x,\omega)=0$、$\lim_{x\to+\infty}F(x,\omega)=1$。并且对任意 $A\in\mathcal G$ 与 $x\in\mathbb R$，取 $q_n\downarrow x$ 得
$$
\int_A F(x,\omega)\,\mathrm d\mathbb P(\omega)
=\lim_{n}\int_A G(q_n,\omega)\,\mathrm d\mathbb P(\omega)
=\lim_{n}\mathbb P\big(A\cap{Y\le q_n}\big)
=\mathbb P\big(A\cap{Y\le u}\big).
$$

令 $\nu(\omega,\cdot)$ 是以 $F(\cdot,\omega)$ 为分布函数的 Lebesgue–Stieltjes 概率测度，由上式可得对一切 $A\in\mathcal G$ 与 $x\in\mathbb R$，
$$
\int_A \nu\big(\omega,(-\infty,x]\big)\,\mathrm d\mathbb P(\omega)=\mathbb P\big(A\cap{Y\le x}\big).
$$
令
$$
\mathcal D:=\{B\in\mathcal B(\mathbb R):\ \omega\mapsto \nu(\omega,B)\ \ \mathcal G\text{-可测且}\ \int_A \nu(\omega,B)\,\mathrm d\mathbb P=\mathbb P\big(A\cap{Y\in B}\big),\ \forall A\in\mathcal G\}.
$$
则 $\mathcal D$ 为 $\lambda$-系且包含 $\pi$-系 $\{(a,b]\}$，故由 $\pi-\lambda$ 定理 $\mathcal D=\mathcal B(\mathbb R)$。于是对所有 Borel集 $B$，$\nu(\cdot,B)$ 为 $\mathcal G$-可测，且
$$
\int_A \nu(\omega,B)\,\mathrm{d}\mathbb P=\mathbb P\big(A\cap{Y\in B}\big),\qquad \forall A\in\mathcal G.
$$

定义
$$
Q(\omega,B):=\nu\big(\omega,B\big),\qquad B\in\mathcal S.
$$
则对每个 $\omega$，$B\mapsto Q(\omega,B)$ 为 $(S,\mathcal S)$上的概率测度；对每个 $B$，$\omega\mapsto Q(\omega,B)$ 为 $\mathcal G$-可测。并且对一切 $A\in\mathcal G$ 与 $B\in\mathcal S$，
$$
\int_A Q(\omega,B)\,\mathrm d\mathbb P
=\int_A \nu\big(\omega,B\big)\,\mathrm d\mathbb P
=\mathbb P\big(A\cap{Y\in B}\big).
$$
因此 $Q(\cdot, B)$ 正是 $\E[\ind_{\{Y\in B\}}|\mathcal G]$ 的一个版本。于是 $Q$ 是给定 $\mathcal G$ 的正则条件概率核。$\blacksquare$


# ✅ 34.1 Probability Kernels, Part 2

本讲介绍了概率核的本质是 Markov 生成元，即可测函数空间上的非负线性泛函。

当有一个概率核 $Q: S_1\times \B_2\to[0, 1]$ 时，
$$f\to \int_{S_2}f(y)Q(x,\dy),\quad f\in\mathbb{B}(S_2,\B_2)$$
给出了从 $L^\infty(S_2,\B_2)$ 到 $L^\infty(S_1,\B_1)$ 的线性映射 $L_Q$，$L_Q$ 满足

1. $L_Q(1)=1$。
2. 若 $f\geq 0$ 非负可测，则 $L_Q(f)\geq 0$ 也非负可测。
3. 若 $f_n\uparrow f$ 则 $L_Q(f_n)\uparrow L_Q(f)$。
4. $\|L_Q(f)\|_{\infty} \leq \|f\|_{\infty}$。

所以 $L_Q$ 是一个连续的正线性泛函？

反过来，如果有这样的一个泛函 $L$，$L$ 是否给出一个概率核 $Q$ 呢？

答案是否定的，一般来说这不成立。但是在 $(S_1,\B_1)=(S_2,\B_2)$ 的情形，这确实是对的。

:::{.theorem}
如果 $L:\mathbb{B}(S,\B)\to\mathbb{B}(S,B)$ 满足以上四个条件，则
$$Q(x, B) = L(\ind_B)(x)$$
给出一个概率核。并且 $L_Q=L$，即此概率核给出的线性泛函正是 $L$。
:::

**证明**：先证 $Q$ 为概率核。对任意固定 $B\in\mathcal B$，有
$$Q(\cdot,B)=L(\ind_B)\in\mathbb{B}(S,\mathcal B).$$
故 $x\mapsto Q(x,B)$ 可测。对任意固定 $x\in S$，由 $0\le \ind_B\le 1$ 与正性得
$$0\le Q(x,B)\le Q(x,S)=L(1)(x)=1.$$
且 $Q(x,\varnothing)=0$。设 $B=\biguplus_{k\ge1} B_k$ 两两不交，令 $f_n:=\sum_{k=1}^n \ind_{B_k}$，则 $0\le f_n\uparrow \ind_B$，由线性与单调连续性，
$$Q(x,B)=L(\ind_B)(x)=\lim_{n\to\infty}L(f_n)(x)=\lim_{n\to\infty}\sum_{k=1}^n L(\ind_{B_k})(x)=\sum_{k=1}^\infty Q(x,B_k).$$
故 $B\mapsto Q(x,B)$ 为概率测度。于是 $Q$ 是概率核。

记
$$L_Q(f)(x):=\int_S f(y)Q(x,\dy).$$
显然对任意 $B\in\mathcal B$，
$$L(\ind_B)=Q(\cdot,B)=\int_S \ind_B(y)Q(\cdot,\dy)=L_Q(\ind_B).
$$

设
$$\H=\{f\in\mathbb{B}(S,\mathcal B):\ L(f)=L_Q(f)\}.$$
则 $\H$ 是向量空间，并且对有界收敛封闭。$\H$ 包含乘法系
$$\M=\{\ind_B:\ B\in\mathcal B\}.
$$
显然 $\sigma(\M)=\B$。由 **Dynkin 的乘法系定理（函数版）**，对一切 $f\in\mathbb{B}(S,\mathcal B)$ 与 $x\in S$，
$$L(f)(x)=L_Q(f)(x)=\int_S f(y)Q(x,\dy).$$
即 $L=L_Q$。$\blacksquare$

如果 $Q_1,Q_2$ 是两个 $(S,\B)$ 到自身的概率核，则 $L_{Q_1}L_{Q_2}$ 也满足性质 1-4，因而也是由一个概率核给出：存在概率核 $Q$ 使得 $L_Q = L_{Q_1}L_{Q_2}$。我们可以把 $Q$ 明确的写出来：
$$L_Q(f) = L_{Q_1}L_{Q_2}(f)=\int_{S}Q_1(x,\dy)\left(\int_Sf(z)Q_2(y,\dz)\right).$$
这看起来很像乘积测度，实际上我们后面会讨论
$$Q_1(x,dy)Q_2(d, dz)= Q_1\otimes Q_2(x, dz)$$
的具体含义。


# ✅ 34.2 Random Dynamics

什么是随机动力系统：

有一个概率空间 $(\Omega,\F,\P)$，一个可测空间 $(R,\mathcal{G})$，以及一些 i.i.d 随机变量 $\xi_n:(\Omega,\F,\P)\to (R,\mathcal{G})$。此外设 $(S,\R)$ 是一个可测空间。

如果 $f$ 是一个 $(S, R)\to S$ 的可测函数映射满足

$$X_{n+1} = f(X_n, \xi_{n+1}) = F_n(X_0,\xi_1,\xi_2,\ldots,\xi_n),\quad F_n:S\times R^n\to S.$$
即 $f(\cdot,\xi_n)$ 是一个由随机序列 $\{\xi_n\}$ 驱动的映射，则我们就称这是一个随机动力系统。

注意 $X_n$ 由 $\xi_1\sim\xi_n$ 决定，所以 $\F_n=\sigma(X_0,X_1,\ldots,X_n) =\sigma(X_0,\xi_1,\ldots,\xi_n)$。

记 $Q_n(x,A)=\P(f(x, \xi_n)\in A)$，则 $Q_n$ 是一个概率核。设 $L_n$ 是其 Markov 生成元。
$$L_n(g)(x) = \int g(y) Q_n(x,\dy)=\E[g(f(x,\xi_n))].$$
则

$$\begin{align*}\E[g(X_{n+1})|\F_n] &= \E[g(f(X_n,\xi_{n+1}))|\F_n]\\
&=\left.\E[g\circ f(x,\xi_{n+1})]\right|_{x=X_n} \\
&=\left.\int g(y)Q_{n+1}(x,\dy)\right|_{x=X_n}\\
&=L_{n+1}(g)(X_n).\end{align*}$$
但是 $L_{n+1}(g)(X_n)$ 是 $X_n$ 的函数，所以它关于 $\sigma(X_n)$ 是可测的，而且是有界可测，从而两边对 $\sigma(X_n)$ 这个子 $\sigma$- 域取条件期望，并注意到 $\sigma(X_n)\subset\F_n$ 有
$$\E[g(X_{n+1})|\F_n] = \E[g(X_{n+1})|X_n].$$
这正是 Markov 性质。

# ✅ 35.1 Stochastic Processes

本讲介绍了随机过程的定义，以及它们的有限维分布、滤过 (filtration)、适应 (adapted) 等概念。

# ✅ 36.1 The Markov property

:::{.definition}
我们称随机过程 $X_t:(\Omega,\F_t)\to(S_,\B)$ 具有 Markov 性质，如果对任何有界可测函数 $f\in\mathbb{B}(S,\B)$ 有
$$\E[f(X_t)|\F_s] = \E[f(X_t)|X_s],\quad \ae\ \forall s < t.$$
:::
即对 $s$ 时刻之前的所有历史取条件期望，等于只对 $s$ 时刻的历史取条件期望。

根据 Doob-Dynkin 引理，不难验证这个定义等价于
$$\E[f(X_t)|\F_s] = F(X_s),\quad \ae\text{ for some } F\in\mathbb{B}(S,\B).$$

上面定义看起来是说，Markov 过程是关于过去和当前的。但实际上它也告诉了我们关于未来的信息：

:::{.corollary}
$$\E[Y|\F_s] = E[Y|X_s],\quad \forall Y\in\mathbb{B}(\Omega, \F^X_{\geq s}).$$
注意，$Y$ 来自 $\F^X_{\geq s}=\sigma(X_t:t\geq s)$，而不是 Filtration $\F_{\geq s}$。
:::

这个推论的证明很有意思，要用到 Dynkin multiplicative system。

**证明**：考虑所有形如
$$Y = g_0(X_{t_0})g_1(X_{t_1})\cdots g_n(X_{t_n})$$
的函数，这里 $s =t_0<t_1<\cdots <t_n$，且每个 $g_i$ 都是有界可测的，从而 $Y$ 也是有界可测的，并且 $Y\in\F^X_{\geq s}$。

:::{.lemma}
设
$$\mathcal{M} = \{g_0(X_{t_0})g_1(X_{t_1})\cdots g_n(X_{t_n})\mid n\in\mathbb{Z}_{\geq0},\ s=t_0<t_1<\cdots<t_n, g_j\in\mathbb{B}(S,\B)\}.$$
则 $\mathcal{M}$ 是乘法系，且 $\sigma(M) = \F^X_{\geq s}$。
:::

引理的证明很简单，这里省略。

回到推论的证明。

设 $\mathcal{H}$ 是所有满足推论要求的函数构成的空间。显然 $\mathcal{H}$ 满足：

1. 是向量空间；
2. 包含常函数 1；
3. 对有界收敛下封闭

我们只要再证明 $\mathcal{H}$ 包含乘法系 $\mathcal{M}$，从而根据 Dynkin 函数系引理它包含所有关于 $\sigma(\mathcal{M})=\F^X_{\geq s}$ 可测的有界可测函数，这正是所要证明的。

根据 Markov 性质和 Doob-Dynkin 引理，我们可以记 $\E_{\F_{t_{n-1}}}[g_n(X_{t_n})]=h(X_{t_{n-1}})$。于是

$$\begin{aligned}\E_{\F_s}[Y]&=\E_{\F_s}[E_{\F_{t_{n-1}}}[Y]]\\
&=\E_{\F_s}[g_0(X_{t_0})\cdots g_{n-1}(X_{t_{n-1}})h(X_{t_{n-1}})]\\
&=\E_{\F_s}[g_0(X_{t_0})\cdots \widetilde{g_{n-1}}(X_{t_{n-1}})]\\
&=\cdots\\
&=\E_{\F_s}[F(X_{s})]\\
&=F(X_s)
\end{aligned}$$
再利用 $\E_{X_s}[Y]=\E_{X_s}[\E_{\F_s}[Y]]=\E_{X_s}[F(X_s)]=F(X_s)$ 即得所证。$\blacksquare$

上面是 Markov 性质的第一种刻画：将对未来可测的函数对当前和过去取条件期望，相当于只对当前取条件期望。

本讲接下来用条件独立给出了 Markov 性质的第二种刻画：

:::{.theorem}
随机过程 $\{X_t\}$ 满足 Markov 性质当且仅当 $\F_s$ 和 $\F^X_{\geq s}$ 关于 $\sigma(X_s)$ 是条件独立的，即对任何有界可测函数 $Z\in\mathbb{B}(\Omega,\F_s)$，$Y\in\mathbb{B}(\Omega,\F^X_{\geq s})$ 有
$$\E[ZY\mid X_s] = \E[Z\mid X_s]\cdot \E[Y\mid X_s].$$
:::

注意到 $\F_s\supset\sigma(X_t: t\leq s)$ 以及 $\F^X_{\geq s}=\sigma(X_t:t\geq s)$，所以这个结论可以概括为：对 Markov 过程，给定当下，过去与未来独立。

**证明**：

$\Rightarrow$：由于 $Z$ 关于 $\F_s$ 可测，以及 Markov 性质，有
$$\E[ZY\mid\F_s] = Z\E[Y\mid \F_s]=Z\cdot \E[Y\mid X_s].$$
两边同时对 $\sigma(X_s)$ 取条件期望，并利用条件期望的 Tower 性质，得到
$$\E[ZY\mid X_s] = \E[Z\mid X_s]\cdot \E[Y\mid\F_s].$$

$\Leftarrow$：对任意 $Z\in\mathbb{B}(\Omega,\sigma(X_s))$，考虑 $\E[Z f(X_t)]$。由条件独立得：

$$\E[Z\cdot f(X_t)]= \E\big[\E[Z f(X_t)\mid X_s]\big]= \E\big[\E[Z\mid X_s]\cdot\E[f(X_t)\mid X_s]\big]=\E[Z\cdot h(X_s)].$$
其中 $h(X_s):=\E[f(X_t)\mid X_s]$。另一方面，根据条件期望定义，
$$\E[Z\cdot f(X_t)] = \E\big[Z \cdot\E[f(X_t)\mid \F_s]\big].$$
两个式子的右边相等，所以
$$\E\big[Z\cdot\E[f(X_t)\mid \F_s]\big]
= \E\big[Z\cdot h(X_s)\big].$$
而这正是条件期望的“投影特征”：由 $Z$ 的任意性，必然有
$$\E[f(X_t)\mid\F_s] = h(X_s) = \E[f(X_t)\mid X_s],\quad \ae$$
$\blacksquare$


# 36.2 Probability Kernels Revisited

回顾了之前概率核的概念。没啥新的。

# ✅ 37.1 Markov Processes

设 $\{X_t\}:(\Omega,\F)\to(\S,\B(\S))$ 是一族随机变量，满足 Markov 性质：
$$\E[f(X_t)\mid \F_s] = \E[f(X_t)\mid X_s],\quad \ae\ \forall s<t.$$
假设 $\S$ 足够 nice，于是我们可以定义正则条件概率 $q_{s,t}=\P(X_t\in B\mid X_s)$ 满足
$$\E[f(X_s)|X_t] = \int_\S f(y)q_{s,t}(X_s,\dy)=Q_{s,t}(f(X_s)).$$
那么，这些算子 $Q_{s,t}$ 之间应该满足怎样的关系呢？

固定 $r<s<t$，利用条件期望的 Tower 性质，可以得到
$$Q_{r,t}f(X_r)=\E[f(X_t)\mid X_r]=\E[\E[f(X_t)\mid X_s] \mid X_r]=\E[Q_{s,t}f(X_s)\mid X_r]=Q_{r,s}Q_{s,t}f(X_r).$$
于是正则条件概率 $\{q_{s,t}\}$ 满足
$$q_{r,t}(x, B)=\int q_{r,s}(x,\dy)q_{s,t}(y, B).$$
这就是所谓的 **Chapman-Kolmogorov** 方程。

:::{.definition}
Markov 过程就是满足 Markov 性质，并且存在概率转移核 $\{Q_{s,t}\}$ 使得
$$\E[f(X_t)\mid X_s] = Q_{s,t}f(X_s).$$
:::


:::{.proposition}
独立增量过程是 Markov 过程，其中
$$q_{s,t}(x,B) = \E[\ind_B(x + X_t - X_s)].$$
:::

视频接下来介绍了 Markov 过程的有限维分布。我们的目标是证明：对任意 $t_0<\cdots<t_n$ 与 $B_0,\ldots,B_n\in\mathcal B(\mathcal S)$，都有
$$\mathbb P(X_{t_0}\in B_0,\ldots,X_{t_n}\in B_n)=\int_{B_0}\mu_{t_0}(\mathrm d x_0)\int_{B_1}q_{t_0,t_1}(x_0,\mathrm d x_1)\cdots\int_{B_n}q_{t_{n-1},t_n}(x_{n-1},\mathrm d x_n).$$
更方便的做法是先证明一个函数版的等式：对任意有界 Borel 函数 $f_0,\dots,f_n:\mathcal S\to\mathbb R$，有
$$\mathbb E\Big[\prod_{k=0}^n f_k(X_{t_k})\Big]=\int_{\mathcal S}\mu_{t_0}(\mathrm dx_0)\,f_0(x_0)\int_{\mathcal S} q_{t_0,t_1}(x_0,\mathrm dx_1)\,f_1(x_1)\cdots\int_{\mathcal S} q_{t_{n-1},t_n}(x_{n-1},\mathrm dx_n)\,f_n(x_n).$$
然后取 $f_k=\mathbf 1_{B_k}$ 即得到有限维分布的核表示。

对 $n$ 的归纳，当 $n=0$ 时，
$$\mathbb E[f_0(X_{t_0})] = \int_{\mathcal S} f_0(x_0)\,\mu_{t_0}(\mathrm dx_0),
$$
这只是 $X_{t_0}$ 分布为 $\mu_{t_0}$ 的定义，因此命题成立。

现在假设 $(P_{n-1})$ 已经成立，固定任意有界 Borel 函数 $f_0,\dots,f_{n-1}$，它们在下面都视为给定的常量函数族。现在把注意力放在最后一个函数 $f_n$ 上。

对任意有界 Borel 函数 $g:\mathcal S\to\mathbb R$，定义
$$\Lambda(g):=\mathbb E\Big[\Big(\prod_{k=0}^{n-1} f_k(X_{t_k})\Big)\,g(X_{t_n})\Big],$$
$$\Phi(g)
:=\int_{\mathcal S}\mu_{t_0}(\mathrm dx_0)\,f_0(x_0)
\int_{\mathcal S}q_{t_0,t_1}(x_0,\mathrm dx_1)\,f_1(x_1)\cdots
\int_{\mathcal S}q_{t_{n-1},t_n}(x_{n-1},\mathrm dx_n)\,f_{n-1}(x_{n-1})\,g(x_n).$$
当我们能证明对所有有界 Borel $g$ 都有 $\Lambda(g)=\Phi(g)$ 时，把 $g=f_n$ 代入，就得到结论对 $n$ 的情形成立。

因此定义函数类
$$\mathcal H := \{g\in\mathcal B_b(\mathcal S):\ \Lambda(g)=\Phi(g)\}.$$

接下来要证明 $\mathcal H$ 满足 Dynkin 函数系引理的条件，从而 $\mathcal H=\mathcal B_b(\mathcal S)$。

首先，$\mathcal H$ 是向量空间。

其次，由单调收敛定理，$\mathcal H$ 对有界单调极限封闭。因此 $\mathcal H$ 是一个对线性组合与有界单调极限封闭的有界可测函数类，符合 Dynkin 函数系引理的结构要求。

接下来需要一个生成族。假设状态空间 $(\mathcal S,\mathcal B(\mathcal S))$ 是标准 Borel 空间（或足够 nice），则存在一个可数的 $\pi$-系统（或代数） $\mathcal C\subset\mathcal B(\mathcal S)$ 生成 $\mathcal B(\mathcal S)$。我们只需在每个 $C\in\mathcal C$ 上验证 $\mathbf 1_C\in\mathcal H$，即证明
$$
\Lambda(\mathbf 1_C)=\Phi(\mathbf 1_C).
$$

取任意 $C\in\mathcal C$。计算
$$
\begin{aligned}
\Lambda(\mathbf 1_C)
&=\mathbb E\Big[\Big(\prod_{k=0}^{n-1} f_k(X_{t_k})\Big)\,\mathbf 1_C(X_{t_n})\Big]\\
&=\mathbb E\Big[\Big(\prod_{k=0}^{n-1} f_k(X_{t_k})\Big)\,\mathbb E[\mathbf 1_C(X_{t_n})\mid\mathcal F_{t_{n-1}}]\Big].
\end{aligned}
$$

利用 Markov 性质和转移核的定义，
$$
\mathbb E[\mathbf 1_C(X_{t_n})\mid\mathcal F_{t_{n-1}}]
=\mathbb E[\mathbf 1_C(X_{t_n})\mid X_{t_{n-1}}]
=q_{t_{n-1},t_n}(X_{t_{n-1}},C),
$$
于是
$$
\begin{aligned}
\Lambda(\mathbf 1_C)
&=\mathbb E\Big[\Big(\prod_{k=0}^{n-2} f_k(X_{t_k})\Big)\,
f_{n-1}(X_{t_{n-1}})\,q_{t_{n-1},t_n}(X_{t_{n-1}},C)\Big]\\
&=\mathbb E\Big[\prod_{k=0}^{n-2} f_k(X_{t_k})\,h(X_{t_{n-1}})\Big],
\end{aligned}
$$
其中定义
$$
h(x):=f_{n-1}(x)\,q_{t_{n-1},t_n}(x,C).
$$
显然 $h$ 是有界 Borel 函数。

现在可以使用归纳假设 $(P_{n-1})$：它告诉我们，对任意有界 Borel 函数 $f_0,\dots,f_{n-2},h$，
$$
\mathbb E\Big[\prod_{k=0}^{n-2} f_k(X_{t_k})\,h(X_{t_{n-1}})\Big]
=
\int_{\mathcal S}\mu_{t_0}(\mathrm dx_0)\,f_0(x_0)
\cdots
\int_{\mathcal S}q_{t_{n-2},t_{n-1}}(x_{n-2},\mathrm dx_{n-1})\,h(x_{n-1}).
$$

代入当前的 $h$ 得
$$
\begin{aligned}
\Lambda(\mathbf 1_C)
&=\int_{\mathcal S}\mu_{t_0}(\mathrm dx_0)\,f_0(x_0)
\int_{\mathcal S}q_{t_0,t_1}(x_0,\mathrm dx_1)\,f_1(x_1)\cdots\\
&\quad\cdots
\int_{\mathcal S}q_{t_{n-2},t_{n-1}}(x_{n-2},\mathrm dx_{n-1})\,
f_{n-1}(x_{n-1})\,q_{t_{n-1},t_n}(x_{n-1},C).
\end{aligned}
$$

注意
$$
q_{t_{n-1},t_n}(x_{n-1},C)
=\int_{\mathcal S}\mathbf 1_C(x_n)\,q_{t_{n-1},t_n}(x_{n-1},\mathrm dx_n),
$$
于是
$$
\begin{aligned}
\Lambda(\mathbf 1_C)
&=\int_{\mathcal S}\mu_{t_0}(\mathrm dx_0)\,f_0(x_0)
\int_{\mathcal S}q_{t_0,t_1}(x_0,\mathrm dx_1)\,f_1(x_1)\cdots\\
&\quad\cdots
\int_{\mathcal S}q_{t_{n-2},t_{n-1}}(x_{n-2},\mathrm dx_{n-1})\,f_{n-1}(x_{n-1})
\int_{\mathcal S}q_{t_{n-1},t_n}(x_{n-1},\mathrm dx_n)\,\mathbf 1_C(x_n)\\
&=\Phi(\mathbf 1_C).
\end{aligned}
$$

因此对每个 $C\in\mathcal C$，$\mathbf 1_C\in\mathcal H$。

综上，$\mathcal H$ 是一个包含生成族指标函数的函数类，对线性组合和有界单调极限封闭。由 Dynkin 函数系引理可知
$$
\mathcal H = \mathcal B_b(\mathcal S),
$$


# ✅ 37.2 Kolmogorov's (Extended) Extension Theorem

怎么构造一个 Markov 过程？

记 $\Omega = \{\omega: T\to \S\}$ 是所有从时间 $T$ 到状态空间 $\S$ 的映射组成的集合。对 $t\in T$，令 $\pi_t$ 为坐标映射
$$\pi_t(\omega) = \omega(t).$$
定义 $\sigma$- 域 $\B^{\otimes T} = \sigma(\{\pi_t, t\in T\})$。即 $\B^{\otimes T}$ 是使得所有坐标映射都是可测映射的最小 $\sigma$- 域。

我们希望在这个乘积 $\sigma$- 域上定义测度 $\P$。我们有的是 $\P$ 的所有有限维投影：
$$\pi_\Lambda \P = \mu_{\Lambda}.$$
其中 $\Lambda\subset T$ 是一个有限集合。$\P$ 必须满足**相容性条件**。

考虑代数
$$\A = \cup_{\Lambda \subset T\text{ finite}}\sigma(\pi_\Lambda).$$
定义其上的概率为
$$\P(A) = \mu_\Lambda(B),\quad B = \pi_\Lambda(A).$$
这是一个良定义的概率，不依赖于 $\Lambda$ 的选择。但是，这只是代数上的有限可加测度，它是可数可加的吗？

Kolmogorov 本质上是一个拓扑结论，在一个可分度量空间上，其测度具有内正则性质：
$$\mu(E)=\sup\{\mu(K)\mid K\subset E,\ K \text{ compact }\}.$$
并且紧集也满足有限交性质，从而代数上的有限可加测度也是可数可加测度。

给定指标集 $T$，每个 $t\in T$ 上有 Polish 空间 $(X_t,\Sigma_t)$（$\Sigma_t$ 为 Borel $\sigma$ 代数）。对每个有限子集 $F\subset T$ 给定概率测度 $P_F$ 于 $(X_F,\Sigma_F)$，并满足相容性：若 $G\subset F$ 且 $E\in\Sigma_F$，则 $P_F(E)=P_G(\pi_{FG}(E))$。定义柱状代数
$$
\mathcal A=\text{由所有 }A\times X_{-F}\ (F\subset T\ \text{有限},\ A\in\Sigma_F)\ \text{生成的代数}.
$$
在生成元上置
$$
P(A\times X_{-F})=P_F(A).
$$
相容性保证 $P$ 在 $\mathcal A$ 上良定且有限可加；一般而言 $P$ 未必可数可加。若 $T$ 无穷，则 $\mathcal A$ 即无限乘积 $X=\prod_{t\in T}X_t$ 的有限维柱状代数。

:::{.lemma}
在 Polish 空间 $(X,\mathcal B(X))$ 上，每个有限 Borel 测度 $\mu$ 是紧集内正则：对任意 $A\in\mathcal B(X)$ 与任意 $\varepsilon>0$，存在紧集 $K\subset A$ 使得 $\mu(A)\le \mu(K)+\varepsilon$。
:::

证明：先取紧致逼近全集。由紧性定理，存在递增紧集 $K_n\uparrow X$ 使 $\mu(K_n)\uparrow\mu(X)$。对任意开集 $U$ 令
$$
F_{n,m}:=\{x\in U:\ \mathrm{dist}(x,X\setminus U)\ge 1/m\}\cap K_n,
$$
则 $F_{n,m}$ 紧且 $F_{n,m}\uparrow U$，据从下连续性有 $\mu(U)=\sup_{n,m}\mu(F_{n,m})$。对一般 $A$ 取开集 $U\supset A$ 使 $\mu(U)\le \mu(A)+\varepsilon$，再取某个 $F_{n,m}\subset U$ 使 $\mu(U)\le \mu(F_{n,m})+\varepsilon$，令 $K=A\cap F_{n,m}$ 即得 $\mu(A)\le \mu(K)+2\varepsilon$，令 $\varepsilon\downarrow0$ 即可。

:::{.lemma}
设 $E=\big(\prod_{t\in F}E_t\big)\times X_{-F}$ 为有限维可测矩形，$F$ 有限，$E_t\in\Sigma_t$。对任意 $\varepsilon>0$，存在紧集 $K_t\subset E_t$ 使
$$
C:=\Big(\prod_{t\in F}K_t\Big)\times X_{-F}\subset E,\qquad P(E)\le P(C)+\varepsilon .
$$
:::

证明：令 $Q_t$ 为 $P_F$ 的第 $t$ 坐标边缘。由上引理，取紧 $K_t\subset E_t$ 使 $Q_t(E_t)\le Q_t(K_t)+\varepsilon/|F|$。由联合到边缘的粗估计得 $P(E)-P(C)\le \sum_{t\in F}\big(Q_t(E_t)-Q_t(K_t)\big)<\varepsilon$。

:::{.lemma}
记
$$
\mathcal C=\Big\{\Big(\prod_{t\in F}K_t\Big)\times X_{-F}: F\subset T\ \text{有限},\ K_t\subset X_t\ \text{紧}\Big\}\subset\mathcal A .
$$
则对任意有限维可测矩形 $E$ 与任意 $\varepsilon>0$，有
$$
P(E)=\sup\{P(C): C\in\mathcal C,\ C\subset E\}.
$$
:::

证明：由上一个引理取紧矩形 $C\subset E$ 使差值小于 $\varepsilon$，取上确界即得。

:::{.lemma}
若 $\{C_n\}_{n\ge1}\subset\mathcal C$ 且 $\bigcap_{n\ge1}C_n=\varnothing$，则存在 $N$ 使 $\bigcap_{n=1}^NC_n=\varnothing$。
:::

证明：写作 $C_n=\big(\prod_{t\in F_n}K_{n,t}\big)\times X_{-F_n}$，令 $J=\bigcup_n F_n$（可数）。则
$$
\bigcap_{n\ge1}C_n=\Big(\prod_{t\in J}\bigcap_{n:\,t\in F_n}K_{n,t}\Big)\times X_{-J}.
$$
若左端为空，则存在 $t_0\in J$ 使 $\bigcap_{n:\,t_0\in F_n}K_{n,t_0}=\varnothing$。因紧集族满足有限交性质，存在有限子族已交空，对应得到某个有限 $N$ 使 $\bigcap_{n=1}^NC_n=\varnothing$。

:::{.lemma}
若 $E_n\downarrow\varnothing$ 于 $\mathcal A$，则 $P(E_n)\downarrow0$。
:::

证明：给定 $\varepsilon>0$，由内逼近引理取 $C_n\in\mathcal C$，$C_n\subset E_n$，且 $P(E_n)\le P(C_n)+\varepsilon 2^{-n}$。若 $\bigcap_n C_n\ne\varnothing$ 则与 $E_n\downarrow\varnothing$ 矛盾，据上引理得某个 $N$ 使 $\bigcap_{n=1}^NC_n=\varnothing$。由有限可加性与单调性，
$$
0=P\Big(\bigcap_{n=1}^N C_n\Big)\ge \sum_{n=1}^N\big(P(C_n)-P(E_{n+1})\big).
$$
令 $N\to\infty$ 并代入 $P(E_n)\le P(C_n)+\varepsilon 2^{-n}$ 得 $\limsup_n P(E_n)\le \varepsilon$，再令 $\varepsilon\downarrow0$ 即得 $P(E_n)\downarrow0$。

:::{.theorem}
上述 $P$ 在柱状代数 $\mathcal A$ 上可数可加，故由 Carathéodory 定理存在唯一扩张 $\overline P$ 于 $\sigma(\mathcal A)=\bigotimes_{t\in T}\Sigma_t$，并满足对每个有限 $F$ 有 $\overline P\circ\pi_F^{-1}=P_F$。
:::

# ✅ 38.1 Path Space

设 $\Omega$ 是一个集合，$\mathcal C\subset\mathcal P(\Omega)$ 任意一族集合
（可以是不可数的）。记 $\sigma(\mathcal C)$ 为由它生成的 $\sigma$-代数。

:::{.lemma}
对任意 $A\in\sigma(\mathcal C)$，都存在一个**可数子族**
$\mathcal C_A\subset\mathcal C$，使得
$$A\in\sigma(\mathcal C_A).$$
:::

也就是说：**每一个可测集合，只需要可数多个生成元就够了。**

**证明**：定义
$$
\mathcal D := \{A\subset\Omega:\ \exists\text{可数 } \mathcal C_0\subset\mathcal C,\ A\in\sigma(\mathcal C_0)\}.$$

1. $\mathcal C\subset\mathcal D$：
   对任意 $E\in\mathcal C$，取 $\mathcal C_0=\{E\}$（显然是可数的），
   那么 $E\in\sigma(\mathcal C_0)$，所以 $E\in\mathcal D$。

2. $\mathcal D$ 是一个 $\sigma$-代数：

   * 若 $A\in\mathcal D$，由某个可数 $\mathcal C_0$ 生成，
     那 $A^c\in\sigma(\mathcal C_0)$，故 $A^c\in\mathcal D$。
   * 若 $A_n\in\mathcal D$，各自对应可数 $\mathcal C_n$，
     取 $\mathcal C'=\bigcup_n\mathcal C_n$，
     可数个可数集的并仍然是可数，所以 $\mathcal C'$ 可数；
     每个 $A_n\in\sigma(\mathcal C_n)\subset\sigma(\mathcal C')$，
     因而 $\bigcup_n A_n\in\sigma(\mathcal C')$，故 $\bigcup_n A_n\in\mathcal D$。


由 1 和 2：$\mathcal D$ 是一个 $\sigma$-代数且包含 $\mathcal C$，所以 $\sigma(\mathcal C)\subset\mathcal D$。

另一方面，对任何 $A\in\mathcal D$，有 $A\in\sigma(\mathcal C_0)\subset\sigma(\mathcal C)$，所以 $\mathcal D\subset\sigma(\mathcal C)$。

于是 $\mathcal D = \sigma(\mathcal C)$。$\blacksquare$

在路径空间里面，$\mathcal C$ 可以取为所有的有限维柱集，它们生成了乘积空间上的 $\sigma$- 域 $\B^{\otimes T}$。所以这里面任何可测集实际上只依赖于可数多个有限维柱集，从而只依赖于可数多个坐标。于是像 $\{\omega(t)\text{ is continous}\}$ 这种依赖不可数多个坐标的事件就不可能在乘积 $\sigma$- 域里面。

在独立增量过程的情形，转移概率核为
$$q_{s,t}(x, B) = \E[\ind_B(x + X_t - X_s)].$$
这是因为
$$\P(X_t\in B\mid X_s = x) = \P((X_t - X_s) + x\in B).$$

# 38.2 Time Homogeneous Markov Processes

:::{.theorem}
设 $X$ 是齐次 Markov 链，$F\in\B(\S^{\otimes T})$，则
$$x\to \E^x[F(X)]$$
是可测函数。进一步，对任何初始分布 $\nu_0$，
$$\E^{\nu_0}[F(X_{t+})\mid\F_t] = \E^{\nu_0}[F(X_{t+})\mid X_t]=\E^{X_t}[F(X)].$$
:::
注意这里第一个断言不需要齐次性质。但是第二个是需要的。

这个定理的意义是，记 $g(x) =\E^x[F(X)]$，根据第一个断言这是关于 $x$ 的可测函数，则第二个断言说：
$$g(X_t) = \E^{X_t}[F(X)].$$

**证明**：2 的前半部分是 36.1 节 Markov property 中的内容。下面只要证 1 和 2 的后半部分。

设 $0=t_0<t_1<\cdots<t_n$，$F$ 形如
$$F(\omega)=\prod_{k=0}^nf_k(\omega(t_k)).$$
我们将对这样的 $F$ 证明，然后使用 Dynkin 的函数形式引理。

1. 对这样的 $F$ 有
$$\E^x[F(X)] = \E^x[\prod_{k=0}^n f_k(X_{t_k})]=\int \delta_x\,\mathrm{d}x\int q_{t_0,t_1}(x_0,\,\mathrm{d}x_1)\cdots\int q_{t_{n-1},t_n}(x_{n-1},\,\mathrm{d}x_n)\prod_{k=0}^nf(x_k).$$
上式等于
$$\E_{\delta_x}[f_0Q_{t_0,t_1}(\cdots f_{n-1}(Q_{t_{n-1},t_n}f_n)\cdots)]=f_0(x)Q_{t_0,t_1}(\cdots f_{n-1}(Q_{t_{n-1},t_n}f_n)\cdots)(x).$$
没问题。
2. 还是取
$$0=t_0<t_1<\dots<t_n,\quad F(\omega)=\prod_{k=0}^n f_k(\omega(t_k)).$$
则
$$F(X_{t+})=\prod_{k=0}^n f_k\big(X_{t+t_k}\big).$$
设 $s_k=t+t_k$，于是
$$t=s_0<s_1<\dots<s_n,\quad F(X_{t+})=\prod_{k=0}^n f_k(X_{s_k}).$$
固定 $x$，考虑从时间 $t$ 开始、初值为 $x$ 的链 $(X_{t+s})_{s\ge0}$。对这个过程，用 1 里已经写出的公式（只是把 $t_0$ 从 0 换成 $t$）得到：
$$\E^x\Big[\prod_{k=0}^n f_k(X_{s_k})\Big]= f_0(x)\,Q_{s_0,s_1}\Big(f_1\,Q_{s_1,s_2}(\cdots f_{n-1}(Q_{s_{n-1},s_n}f_n)\cdots)\Big)(x).$$
注意这里 $s_0=t,s_1=t+t_1,\dots$。

由于链是齐次的，所以 $Q_{s_{k-1},s_k}=Q_{t_{k-1},t_k}$ 对所有 $k$ 成立，于是上面的式子化简为
$$\E^x[F(X_{t+})]
= f_0(x)\,Q_{t_0,t_1}\Big(f_1\,Q_{t_1,t_2}(\cdots f_{n-1}(Q_{t_{n-1},t_n}f_n)\cdots)\Big)(x).$$

但右边正是第 1 点中得到的 $\E^x[F(X)]$ 的表达式。所以我们得到一个关键等式：
$$\E^x[F(X_{t+})]=\E^x[F(X)]=g(x)$$
对所有 $x$ 均成立。

也就是说：**从时刻 (t)** 往后的整条“未来路径”的分布与“从 0 开始、初值为 $x$”的那条链是一样的，这一步用到了齐次性。
由 36.1 的 Markov 性质，我们已经知道存在某个可测函数 $h$ 使得
$$\E^{\nu_0}[F(X_{t+})\mid X_t]=h(X_t).$$
并且按定义有
$$h(x)=\E^x[F(X_{t+})].$$

第一步刚刚证明了 $\E^x[F(X_{t+})]=\E^x[F(X)]=g(x)$，因此
$$h(x)=g(x),\quad\forall x.$$
从而
$$\E^{\nu_0}[F(X_{t+})\mid X_t]=g(X_t)=\E^{X_t}[F(X)].$$
这就完成了第二点的后半部分，对柱状 $F$ 成立。

# ✅ 39.1 Markov Matrix

无要点

# ✅ 39.2 Markov Generator

这一讲介绍了，Chapman-Kolmogorov 方程给出的算子方程
$$Q_{t+s}=Q_tQ_s,\quad Q_0=I.$$
其解应该形如 $Q = \exp(tA)$，其中 $A$ 是某个有界算子。

$A$ 不难猜出来，它就是
$$A = \lim_{t\to 0}\frac{\mathrm d}{\mathrm{d}t}Q_t\bigg|_{t=0}.$$


# ✅ 40.1 Operator Norm Continuity

介绍了一些泛函中关于算子范数的内容（这里不再整理）。还介绍了可数情形的算子，如果算子可以用矩阵的形式表示时，算子的范数。

如果 $a=(a_{ij})$ 满足

$$\|a\|=\sup_{i}\sum_{j}|a_{ij}|<\infty.$$

那么由
$$Af(i) = \sum_j a_{ij}f(j)$$
定义的算子是有界算子，并且 $\|A\|=\|a\|$。



# ✅ 40.2 Bounded Generators

设 $B_b(S)$ 是测度空间 $(S,\mathcal B)$ 上有界可测函数的 Banach 空间，范数为 $\|f\|_\infty$。
$(Q_t)_{t\ge0}$ 是一族 **Markov 迁移算子**，也就是：

* 每个 $Q_t : B_b(S)\to B_b(S)$ 是线性的、正的；
* $Q_t\mathbf 1=\mathbf 1$；
* 半群性质：$Q_{t+s}=Q_tQ_s$，$Q_0=I$（恒等算子）。

因为 $Q_t$ 是 Markov 算子，在 $\|\cdot\|_\infty$ 下都是压缩映射，$\|Q_t\|_{\mathrm{op}}\le 1$。

假设再多一点正则性：

$$\lim_{t\downarrow 0}\|Q_t - I\|_{\mathrm{op}} = 0.$$

这叫“在 $t=0$ 的算子范数连续”，也就是很小时间步 $t$ 对任意有界可测函数几乎“不做事”。

:::{.theorem}
在上述假设下，存在一个有界线性算子
$$A = \lim_{t\downarrow0}\frac{Q_t - I}{t}$$
（极限在算子范数意义下存在），并且对所有 $t\ge0$,
$$Q_t = e^{tA} := \sum_{n=0}^\infty \frac{t^n}{n!} A^n.$$
级数在算子范数下收敛。

从而 $t\mapsto Q_t$ 在 $[0,\infty)$ 上在算子范数意义下可微，并满足
$$\frac{d}{dt}Q_t = Q_tA = AQ_t, \qquad Q_0=I.$$
这是 Kolmogorov 的正向 / 反向方程的算子形式。
:::

**证明**：**第一步：从 $0$ 点连续到各点连续**

利用半群性质和 $\|Q_t\|\le1$，先说明：只要在 $0$ 点算子范数连续，则在每个 $t$ 都算子范数连续，并且在每个有限区间上一致连续。

对任意固定 $s\ge0$ 以及 $h>0$，由半群性质有
$$
Q_{s+h}-Q_s=Q_sQ_h-Q_s=Q_s(Q_h-I).
$$
于是
$$\|Q_{s+h}-Q_s\|
\le\|Q_s\|\cdot\|Q_h-I\|
\le\|Q_h-I\|.$$
由已知 $\|Q_h-I\|\to0$，得出 $t\mapsto Q_t$ 在任意 $s$ 处右连续。类似地，由
$$
Q_s-Q_{s-h}=Q_{s-h}(Q_h-I)
$$
得到左连续。故 $t\mapsto Q_t$ 在每个 $t\ge0$ 都算子范数连续。
再注意到上述估计与 $s$ 无关，可知在任意有限区间 $[0,T]$ 上 $t\mapsto Q_t$ 一致连续。

**第二步：定义平滑算子 $B_\varepsilon$ 并证明其可逆**

固定 $\varepsilon>0$，定义有界算子
$$B_\varepsilon=\frac{1}{\varepsilon}\int_0^\varepsilon Q_s\,\mathrm{d}s.
$$
即对 $f\in B_b(S)$ 和 $x\in S$，
$$
(B_\varepsilon f)(x)=\frac{1}{\varepsilon}\int_0^\varepsilon Q_sf(x)\,\mathrm{d}s.
$$

由于对任意 $f\in B_b(S)$，有
$$
\|Q_{s+h}f-Q_sf\|_\infty\le\|Q_{s+h}-Q_s\| \|f\|_\infty\xrightarrow[h\to0]{}0.
$$
所以对每个 $x\in S$，函数
$$
s\longmapsto Q_sf(x)
$$
在每个 $s$ 处连续，从而可积，上式定义良好。并且
$$
\|B_\varepsilon\|\le\frac{1}{\varepsilon}\int_0^\varepsilon\|Q_s\|\,\mathrm{d}s\le1.
$$

注意到
$$B_\epsilon Q_t f = \frac{1}{\epsilon}\int_0^\epsilon Q_{t+s}f\,\mathrm{d}s.$$
即
$$B_\epsilon Q_t  = \frac{1}{\epsilon}\int_0^\epsilon Q_{t+s}\,\mathrm{d}s = \frac{1}{\epsilon}\int_t^{t+\epsilon} Q_{s}\,\mathrm{d}s.$$
所以函数 $t\to B_\epsilon Q_t$ 是可微的，其导数为
$$\frac{\mathrm d}{\mathrm{d}t} (B_\epsilon Q_t) = \frac{Q_{t+\epsilon}-Q_t}{\epsilon} $$

# 42.2 Hitting Times

:::{.theorem}
$$\E^x[F(X)] = \int_S q(x,\dy)\E^y[F(x, X)].$$
:::

# ✅ 44.2 Invariant Distributions

# ✅ 45.1 Stopping Times

关于停时的基本知识，无要点。

# ✅ 46.1 The Strong Markov Property

:::{.theorem}
设 $\nu$ 是 Markov 链的初始分布，$\tau$ 是停时，则
$$\E^\nu[F(X_{\tau+})\mid\mathcal F_\tau] = \E^x [F(X)]\Big|_{x=X_\tau},\quad \text{a.e. on }\{\tau<\infty\}.$$
:::

**证明**：
$$\begin{aligned}
\E^\nu[F(X_{\tau+})\mid\mathcal F_\tau]\ind_{\{\tau<\infty\}}&=\sum_{n=0}^\infty \E^\nu[F(X_{\tau+})\mid\mathcal F_n]\ind_{\{\tau=n\}}\\
&=\sum_{n=0}^\infty \E^\nu[F(X_{\tau+})\ind_{\{\tau=n\}}\mid\mathcal F_n]\\
&=\sum_{n=0}^\infty \underbrace{\E^\nu[F(X_{n+})\mid\mathcal F_n]}_{\E^x [F(X)]\Big|_{x=X_n}}\ind_{\{\tau=n\}}.
\end{aligned}$$
即如果令 $g(x)=\E^x[F(X)]$，则
$$\text{The above }=\sum_{n=0}^\infty g(X_n)\ind_{\{\tau=n\}}=g(X_\tau)\ind_{\{\tau<\infty\}}.$$
$\blacksquare$

:::{.corollary}
设 $(X_n)_{n\ge0}$ 是一个取值在离散空间 $S$ 中的 Markov 链。对任何 $x\in S$，对 $A_x=\{\tau<\infty,X_\tau=x\}$ 取条件，则 $\mathcal F_\tau$ 和 $X_{\tau + n}$ 是独立的，且 $(X_{\tau + n})$ 和 $(X_n)$ 有相同的分布。
:::

**证明**：设 $Y\in\mathbb{B}(\Omega,\mathcal F_\tau)$，则
$$\begin{aligned}
\E^\nu[F(X_{\tau+})\,Y\ind_{A_x}]&=\E^\nu[\E[F(X_{\tau+})\mid\mathcal F_\tau]\,Y\ind_{A_x}]\\
&\overset{\text{strong Markov property}}{=}\E^\nu[\E^{X_\tau}[F(X)]\,Y\ind_{A_x}]\\
&\overset{\E^x[F(X)]\text{ is a scalar}}{=}\E^x[F(X)]\cdot \E^\nu[Y\ind_{A_x}].
\end{aligned}$$
两边同时除以 $\mathbb{P}^\nu(A_x)$ 可得
$$\E^\nu[F(X_{\tau+})Y \mid A_x] = \E^x[F(X)]\cdot \E^\nu[Y\mid A_x].$$

特别地，取 $Y\equiv1$，得
$$\mathbb E^\nu[F(X_{\tau+})\mid A_x]=\mathbb E^x[F(X)].$$
所以在事件 $A_x$ 条件下，
$$(X_{\tau+}) \overset{d}{=} (X) \ \text{under }\mathbb{P}^x.$$
不仅如此，代入以后我们还有对任意有界 $Y\in\mathcal F_\tau$ 与任意未来泛函 $F$，都有乘积分解：
$$\E^\nu[F(X_{\tau+})\,Y\ind_{A_x}]=\E^\nu[F(X_{\tau+})\ind_{A_x}]\cdot\E^\nu[Y\ind_{A_x}].$$
这表明在 $\mathbb P^\nu(\cdot\mid A_x)$ 下 $\mathcal F_\tau$ 与 $\sigma(X_{\tau+n},n\ge0)$ 条件独立。$\blacksquare$


# 46.2 Markov Chain Ergodic Theorem

:::{.theorem}
**遍历定理** 令 $V_j(N)$ 为前 $N$ 个时刻访问状态 $j$ 的次数：
$$V_j(N)=\sum_{n=0}^N \ind_{\{X_n=j\}}.$$
则
$$\lim_{N\to\infty}\frac{V_j(N)}{N}=\frac{1}{\E^i[\tau_i]}=1,\ \text{a.e.}\quad \forall i,j.$$
:::

:::{.definition}
$$\sigma_j^{(1)}=\inf\{n\ge 1: X_n=j\}.$$
$$\sigma_j^{(n)}=\inf\{n\ge 1: X_{n+\sigma_j^{(n-1)}}=j\}.$$
:::

:::{.lemma}
$\{\sigma_j^{(n)}\}_{n=1}^\infty$ 是 i.i.d 序列。
:::

证明：定义 $\tau_j^{(0)}=0$，
$$\tau_j^{(n)}=\inf\{n>\tau_{j-1}^{(n)}:\ X_n=j\}.$$
注意到
$$\sigma_j^({n+1})(X_0,X_1,\ldots) = \sigma_j^{(1)}(X_{\tau_j^{(n)}},X_{\tau_j^{(n)}+1},\ldots).$$

# ✅ 46.3 Wald's Identity

本讲介绍了 Wald 引理。

:::{.theorem}
**Wald 引理** 设 $\{X_n\}$ 是 $\iid$ 的随机变量序列，$\tau$ 是一个停时，则在 $\E|X_1|<\infty$ 且 $\E\tau<\infty$ 的条件下有 $\E\sum\limits_{n=1}^\tau X_n=\E X_1\cdot \E\tau$。
:::

这里的关键在于将上面的求和变成一个二重级数求和，然后交换求和次序。

$$\begin{aligned}
\sum_{n=1}^\tau\E X_n&=\sum_{n=1}^\infty\E X_n\cdot \ind_{\tau\geq n}=\sum_{n=1}^\infty\E X_n\cdot\sum_{k=n}^\infty\ind_{\tau=k}\\&=\sum_{k=1}^\infty\ind_{\tau=k}\sum_{n=1}^k\E X_n\\&=\E X_1\sum_{k=1}^\infty k\cdot\ind_{\tau=k}\\&=\E X_1\cdot \E\tau.\end{aligned}$$

我们为什么可以在第一行的第二个等号处交换求和次序？这是因为上面的推导对 $|X_n|$ 是成立的，并且离散积分值 $\E|X_1|\cdot\E \tau<\infty$，所以由控制收敛定理对原序列 $X_n$ 交换求和也是 OK 的。


# ✅ 48.1 Uniform Integrability

这一讲介绍了随机变量集合的一致可积性，要点非常多。

对任何 $L^1$ 的随机变量 $X$，总是可以找一个紧集 $K$，使得 $|X|$ 在 $K^c$ 上的积分任意小：对任何 $\epsilon>0$，存在 $a>0$ 使得 $\E[|X|:\ |X|\geq a]<\epsilon$。但是如果是一族可积的随机变量的话，这个统一的 $a$ 就未必存在了。

如果这样的 $a$ 总是存在的话，我们就称这族随机变量是一致可积的。

:::{.definition}
随机变量列 $\{X_n\}$ 称作是一致可积的 (UI) 的，如果它们满足以下条件：

1. 每个 $X_i$ 都是 $L^1$ 的。
2. 对任何 $\epsilon>0$，存在 $a>0$ 使得 $\sup_n\E[X_n:\ |X_n|\geq a]< \epsilon$。
:::

不难验证如果 $\{X_n\}$ 被一个可积随机变量控制，则它们是一致可积的：

:::{.example}
如果 $|X_n|\leq Y,\ Y\in L^1$，则 $\{X_n\}$ 是一致可积的。
:::

这是因为被积函数和积分区域都可以放大：$\E[|X_n|:\ |X_n|\geq a]\leq\E[|Y|:\ |Y|\geq a]$。

:::{.example}
如果 $\{X_n\}$ 是 $L^p,\,p>1$ 一致有界的：$\sup_n\E |X_n|^p<\infty$，则 $\{X_n\}$ 是一致可积的。
:::

这是因为被积函数可以放大：
$$\E[|X|: |X|\geq a]\leq \E[|X|\cdot\frac{|X|^{p-1}}{a^{p-1}}: |X|\geq a] = \frac{1}{a^{p-1}}\E[|X|^p: |X|\geq a]\leq \frac{M}{a^{p-1}}.$$

这个例子中的 $p>1$ 是不能减弱为 $p\geq1$ 的。不过我们可以证明 UI 的变量族必然是 $L^1$ 一致有界的：

:::{.theorem}
若 $\{X_n\}$ 一致可积，则 $\sup_n E|X_n| <\infty$。
:::

**证明**：取 $a$ 使得 $\sup_n \E[|X_n|: |X_n|\geq a] < 1$，则不难证明 $\E |X_n| < a+1$。$\blacksquare$

现在我们来给出一致绝对连续的概念，并将说明**一致可积 = $L^1$ 一致有界 + 一致绝对连续**。

:::{.definition}
随机变量序列 $\{X_n\}$ 是一致绝对连续的，如果对任何 $\epsilon>0$，都存在 $\delta>0$，使得只要集合 $B$ 满足 $\mu(B)<\delta$，就有 $\sup_n\E[|X_n|: B]<\epsilon$。
:::

:::{.theorem}
$\{X_n\}$ 一致可积当且仅当它们 $L^1$ 一致有界且一致绝对连续。
:::
**证明**：

$\Rightarrow$: $L^1$ 一致有界已经有了。下证一致绝对连续性质。对任何可测集 $B$，我们考虑用一个待定的 $a>0$ 把积分 $\E[|X_n|: B]$ 变成
$$\E[|X_n|: B,\ |X_n|\geq a] + \E[|X_n|: B,\ |X_n|<a].$$
第一项小于等于  $\E[|X_n|: |X_n|\geq a]$，由一致可积性我们可以取 $a$ 使得它小于 $\epsilon/2$。第二项小于等于 $a\mu(B)$。所以只要 $\mu(B)<\delta=\frac{\epsilon}{2a}$ 即可。

$\Leftarrow$: 我们可以料想 $\{|X_n|\geq a\}$ 的测度是会一致地越来越小的：

$$\P(\{|X_n|\geq a\})=\E[1: |X_n|\geq a]\leq \E[\frac{|X_n|}{a}: |X_n|\geq a]\leq \frac{\E|X_n|}{a}=\frac{K}{a}.$$
其中 $K$ 是 $\{X_n\}$ 的 $L^1$ 上界。所以确实可以取 $a$ 适当大使得 $\{|X_n|\geq a\}$ 的测度一致地小于一致绝对连续性中所需要的那个 $\delta$。

:::{.theorem}
一致可积性是平移不变的： $\{X_n\}$ 一致可积且 $Y\in L^1$，则 $\{X_n+Y\}$ 也是一致可积的。
:::

为此只要证明它们一致 $L^1$ 有界且一致绝对连续。其中一致 $L^1$ 有界是显然的。

对于一致绝对连续，我们有
$$\E[|X_n+Y|: B]\leq\E[|X_n|:B] + \E[|Y|: B].$$
取 $\delta_1$ 使得只要 $\mu(B)<\delta_1$ 就有 $\E[|X_n|:B]<\frac{\epsilon}{2}$，再取 $\delta_2$ 使得只要 $\mu(B)<\delta_2$ 就有 $\E[|Y|:B]<\frac{\epsilon}{2}$，则 $\delta=\min\{\delta_1,\delta_2\}$ 符合要求。

最后一个重要定理是：**依 $L^1$ 范数收敛 = 一致可积 + 依测度收敛**。

:::{.theorem}
随机变量序列 $X_n\xrightarrow{L^1} X$ 当且仅当 $X_n\xrightarrow{\P}X$ 且 $\{X_n\}$ 一致可积。
:::
**证明**：

$\Rightarrow$：$L^1$ 收敛当然可以得出依测度收敛 (Markov 不等式一步即得)。要证明一致可积，我们只要根据平移不变性，证明 $Y_n=X_n-X$ 是一致可积的即可。固定 $\epsilon>0$。取 $N$ 使得 $\sup_{n\ge N}\E|Y_n|<\epsilon$，于是对所有 $a>0$，
$$
\sup_{n\ge N}\E\big[\,|Y_n|\mathbf 1_{\{|Y_n|\ge a\}}\,\big]\le \sup_{n\ge N}\E|Y_n|<\epsilon.
$$
对有限个指标 $n<N$，由于每个 $Y_n\in L^1$，存在 $a$ 足够大使
$$
\max_{n<N}\mathbb E\big[\,|Y_n|\mathbf 1_{\{|Y_n|\ge a\}}\,\big]<\epsilon.
$$
综上得到
$$
\sup_{n}\mathbb E\big[\,|Y_n|\mathbf 1_{\{|Y_n|\ge a\}}\,\big]<\epsilon
$$
即 $\{Y_n\}$ 一致可积。

$\Leftarrow$: $Y_n\ind_{\{|Y_n|<a\}}$ 是一个不大于 $a$ 的函数序列，且依测度收敛到 0，从而由**依测度的控制收敛定理**有 $Y_n\ind_{\{|Y_n|<a\}}\xrightarrow{L^1}0$。
从而
$$\|X_n-X\|_{L^1} = \E[Y_n\ind_{\{|Y_n|<a\}}] + \E[Y_n\ind_{\{|Y_n|\geq a\}}].$$
第一项取 $n$ 大于某个 $N$ 就可以任意小，第二项对有限多个 $n\le N$，$a$ 足够大也可以任意小，得证。$\blacksquare$

:::{.corollary}
正则鞅 $X_n = \E[X|\mathcal{F}_n]$ 是一致可积的。
:::

反过来也是对的：鞅序列如果是一致可积的，则一定是正则鞅。


# 49.1 Optional Stopping and Sampling

这一节介绍了停时，以及停时鞅序列 $\{X_{n\wedge \tau}\}$ 的性质。

一个简单的股票市场模型：设 $\{X_n\}_{n=0}^\infty$ 是股票价格，$\{U_n\}_{n=1}^\infty$ 是你的投资策略，即在时刻 $n-1$ 买入 $U_n$ 并在时刻 $n$ 抛出。或者说，$U_n$ 是你在 $(n-1,n]$ 这个时间区间内的股票交易数量，那么到时刻 $n$ 时，你的净收益为
$$I_n(U,X) = \sum_{j=1}^n U_j(X_j-X_{j-1}).$$
这里 $U_n$ 必须是关于 $\F_{n-1}=\sigma(X_0,X_1,\ldots,X_{n-1})$ 可测。

第一个重要观察是：

:::{.theorem #martingale-discrete-integration}
如果 $\{X_n\}$ 是鞅/下鞅/上鞅，并且 $U_n\geq0$，则 $I_n(U,X)$ 也是鞅/下鞅/上鞅。
:::

证明：对下面的恒等式两边关于 $\F_n$ 取条件期望即可。
$$I_{n+1}(U,X) = \underbrace{I_{n}(U,X)}_{\in\F_n} + \underbrace{U_{n+1}}_{\in\F_n}\underbrace{(X_{n+1}-X_{n})}_{\rm (sub/sup)martingale}.$$

我们可以设定两个随机时间，比如 $\sigma$ 是股票首次低于 1 美元的时刻, 这时立刻买入；$\tau$ 是股票首次高于 10 美元的时刻，这时立刻抛出；在区间 $(\sigma,\tau]$ 中保持持有股票，即 $U_j=\ind_{\sigma<j\leq \tau}$。于是 $U_j\ind_{n\geq j}=\ind_{(\sigma\wedge n, \tau\wedge n]}(j)$。

那么净收益
$$I_n(U,X) = \sum_{j=1}^n \ind_{\sigma\wedge n<j\leq \tau\wedge n} (X_j-X_{j-1})=X_{\tau\wedge n} - X_{\sigma\wedge n}.$$

特别地，取 $\sigma=0$，则 $U_j=\ind_{j\leq\tau}$，则我们有如下结论：

:::{.theorem #stopping-time-also-martingale}
如果 $\{X_n\}$ 是鞅，那么 $\{X_{n\wedge \tau}\}$ 也是鞅。
:::

证明：首先每一项 $X_{n\wedge \tau}$ 可以看成是一个关于 $X_1,\ldots,X_n$ 的部分和：

$$X_{n\wedge \tau} = \sum_{k=0}^n\ind_{\tau=k}X_k.$$

显然 $X_{n\wedge \tau}$ 是可积的。

另一方面在 @Pre:martingale-discrete-integration 中取 $U_n=\ind_{n\leq\tau}$，则 $X_{n\wedge \tau} - X_0 = I_n(U,X)$ 仍然是鞅，那么加上一个 $X_0$ 得到的 $X_{n\wedge\tau}$ 当然还是鞅。

# ✅ 49.2 Hölder's Inequality

:::{.lemma}
**Young 不等式**
给定 $a,b\ge0$，$p,q>1$ 且 $\tfrac1p+\tfrac1q=1$，有
$$ab\le\frac{a^p}{p}+\frac{b^q}{q}.$$
且当且仅当 $a^p=b^q$ 取等号。
:::

**证明**：对任意 $u,v\ge0$，$\theta\in(0,1)$，
$$u^{\theta}v^{1-\theta}\le \theta u+(1-\theta)v.$$
这是因为 $\ln$ 函数凹，Jensen 不等式给出
$$\ln(\theta u+(1-\theta)v)\ge \theta\ln u+(1-\theta)\ln v.$$
两边取指数即得。

取 $\theta=\frac1p,1-\theta=\frac1q,u=a^p,v=b^q$ 代入即得 Young 不等式，且等号当且仅当 $a^p=b^q$。$\blacksquare$


设 $1/p+1/q=1$，$1<p,q<\infty$。对任意 $a,b\ge 0$ 有 **Young 不等式**
$$ab\le \frac{a^{p}}{p}+\frac{b^{q}}{q}.$$
令
$$u(x)=\frac{|f(x)|}{\|f\|_p},\qquad v(x)=\frac{|g(x)|}{\|g\|_q}.$$
则逐点有
$$u(x)v(x)\le u(x)^{p}/p+v(x)^{q}/q.$$
两边对 $\mu$ 积分并用 $\int u^{p}=1,\ \int v^{q}=1$ 即得 Hölder 不等式。

$p=1,q=\infty$ 时
$$\int |fg|\le \|g\|_{\infty}\int |f|=\|f\|_1\|g\|_{\infty}.$$
故结论成立。
