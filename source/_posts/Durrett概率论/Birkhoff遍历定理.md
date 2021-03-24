---
title: "Birkhoff 遍历定理"
date: 2013-04-21
tags:
  - 遍历论
  - Durrett 概率论
  - Ergodic theorem
categories: [Durrett 概率论]
url: "Birkhoff-ergodic-theorem"
---

Birkhoff 遍历定理最初由 Birkhoff 本人在 1931 年发表，原文长达 50 页。随后在 1939 年 K.Yosida (吉田耕作) 和 S.Kakutani (角谷) 利用极大遍历定理给出了一个 10 页的简洁证明，不过他们关于极大遍历定理的证明还是啰嗦了点，后来 Garsia 给出了极大遍历定理的一个仅有寥寥数行的惊人证明，这也是当前大多数教材采用的途径 (比如 Durrett 的书)，本文就来介绍这一证明。

<!-- more -->

# 记号与约定


给定一个概率空间 $(\Omega,\mathcal{F},\mu)$，$T:\Omega\rightarrow \Omega$ 是一个可测变换，即对任何 $E\in\mathcal{F}$ 有 $T^{-1}E\in\mathcal{F}$。


{% blockquote %}
**定义 1**： 如果一个可测集 $E$ 满足 $T^{-1}E=E$，就称 $E$ 是一个 $T-$ 不变集合。这里集合的相等指的是不计一个零测集的意义下的相等。不难验证所有的 $T-$ 不变集合
$$\mathcal{I}=\{E\in\mathcal{F}\ |\ T^{-1}E=E\ \}$$
构成 $\mathcal{F}$ 的一个子 $\sigma-$ 代数。
{% endblockquote %}

{% blockquote %}
**定义 2**： 如果对任何可测集 $E\in\mathcal{F}$ 有 $\mu(T^{-1}E)=\mu(E)$，就称 $T$ 是一个保测变换。
{% endblockquote %}

在本文中，$T$ 始终代表一个保测变换。

保测变换有如下性质：

{% blockquote %}
**引理 1**：如果 $f\in L^1(\Omega)$ 是一个可积的随机变量，则
$$\int_\Omega f\,\mathrm{d}\mu=\int_\Omega f\circ T\,\mathrm{d}\mu.$$
{% endblockquote %}

证明就是从集合的示性函数出发：若 $E\in\mathcal{F}$，注意到 $\mathbf{1}_{E}\circ T=\mathbf{1}_{\{T^{-1}E\}}$，因此
$$\int_\Omega \mathbf{1}_E\,\mathrm{d}\mu=\mu(E)=\mu(T^{-1}E)=\int_\Omega \mathbf{1}_{\{T^{-1}E\}}\,\mathrm{d}\mu=\int_\Omega \mathbf{1}_E\circ T\,\mathrm{d}\mu.$$
从而结论对任何简单可测函数也成立，取极限即得一般的可测函数结论成立。

{% blockquote %}
**引理 2**： 一个 $\Omega$ 上的随机变量 $X$ 关于 $\mathcal{I}$ 可测，当且仅当有
$$X\circ T=X\quad \text{a.e.}$$
成立。这时我们称 $X$ 是 $T-$ 不变的随机变量。
{% endblockquote %}

证明仍然类似于引理 1，也是从示性函数到简单函数，再过度到一般可测函数，不再赘述。


# Birkhoff 遍历定理


设 $f$ 是 $\Omega$ 上的随机变量，对每个整数 $n\geq 1$，令
$$S_n(\omega)= \sum_{k=0}^{n-1} f(T^k(\omega)).$$
我们有如下的定理：

{% blockquote %}
**Birkhoff 遍历定理**：设 $T$ 是概率空间 $(\Omega,\mathcal{F},\mu)$ 上的保测变换，则对任何 $f\in L^1(\Omega)$ 有
$$\lim_{n\to\infty}\frac{S_n}{n}\rightarrow \mathbb{E}(f\,|\,\mathcal{I})\quad\text{a.s.}$$
{% endblockquote %}

证明 Birkhoff 遍历定理定理的关键是证明如下的极大遍历定理：

{% blockquote %}
**极大遍历定理**：定义极大算子
$$M_f(\omega)=\sup_{n\geq 1}\frac{1}{n}S_n(\omega),$$
则对 $f\in L^1(\Omega)$ 和任一 $a\in\mathbb{R}$，有
$$\int_{\{M_f>a\}} f\,\mathrm{d}\mu\geq a\mu(\{M_f>a\}).$$
{% endblockquote %}

极大遍历定理的称呼来源于分析中的 Hardy - Littlewood 极大函数，这一类的不等式统称为极大不等式。不过我打算把极大遍历定理的证明放在最后，先用它来证明 Birkhoff 遍历定理。


# Birkhoff 遍历定理的证明


首先可以假定 $\mathbb{E}(f|\mathcal{I})=0$，否则就以 $f-E(f|\mathcal{I})$ 代替 $f$ (注意这里要用到 $\mathbb{E}(f|\mathcal{I})$ 是 $T-$ 不变的这一点)。这样问题变成在 $\mathbb{E}(f|\mathcal{I})=0$ 的条件下证明
$$\lim\limits_{n\to\infty}\frac{S_n}{n}=0.\quad \text{a.s.}$$
设 $a$ 是任一正数，考虑集合
$$A= \{\omega\ |\ \varlimsup_{n\to\infty}\frac{S_n}{n}>a\}.$$
我们想证明 $\mu(A)=0$。若真如此，则有 $\varlimsup\limits_{n\to\infty}S_n/n\leq a$ 几乎处处成立，根据 $a$ 的任意性就得到 $\varlimsup\limits_{n\to\infty}S_n/n\leq 0$ 几乎处处成立。再把这个结果用在 $-f$ 上就得到 $\varliminf\limits_{n\to\infty}S_n/n\geq 0$ 也几乎处处成立，这样就证明了 $\lim\limits_{n\to\infty}S_n/n=0$ 几乎处处成立。(好拗口的说)

但是请注意 $\varlimsup\limits_{n\to\infty}$ 和 $\sup\limits_{n\geq 1}$ 的区别，它们定义的是两个不同的随机变量。我们要估计的 $A$ 是用 $\varlimsup\limits_{n\to\infty}$ 定义的，而极大遍历定理中说的是 $\sup\limits_{n\geq 1}$。注意到
$$A=\{\varlimsup_{n\to\infty}\frac{S_n}{n}>a\}\subseteq \{ \sup_{n\geq 1}\frac{S_n}{n}>a\}= \{M_f>a\},$$
所以只要证明这样一个结论就好了：

> 设 $A\subseteq \{M_f>a\}$ 而且 $A$ 是一个 $T-$ 不变集合，那么极大遍历定理仍然成立：
$$\int_A f\,\mathrm{d}\mu\geq a\mu(A).$$

而这只要对函数 $g=f\cdot\mathbf{1}_A$ 应用极大遍历定理即可：
$$\int_{\{M_g>a\}} f\cdot\mathbf{1}_A\,\mathrm{d}\mu\geq a\mu(\{M_g>a\}).$$
但是 $M_g=M_f\cdot\mathbf{1}_A$，这一点要用到 $A$ 是 $T-$ 不变集合这个条件，请自行验证，因此
$$\{M_g>a\}=\{M_f>a\}\cap A =A.$$因此确实有
$$\int_A f\,\mathrm{d}\mu\geq a \mu(A),$$
这样就证明了 Birkhoff 遍历定理。

实际上定理中的收敛也是一个依 $L^1$ 范数的收敛，这点的证明相比几乎处处收敛就容易多了，一般的书上也都有，比如 Durrett 的书，这里就不再费笔墨了。

最后来证明极大遍历定理。


# 极大遍历定理的证明


只要证明 $a=0$ 的情形，然后对一般的 $a$，将结论应用在函数 $f-a$ 上即可。定义 $S_0=0$ 以及 $M_n =\max\{S_0,S_1,\cdots,S_n\}$。对每个 $k=1,\ldots,n$ 有
$$S_k=f+S_{k-1}\circ T\leq f+M_n \circ T.$$
从而
$$\max_{1\leq k\leq n}S_k\leq f+M_n \circ T.$$

但是在集合 $\{M_n>0\}$ 上，$M_n=\max\limits_{1\leq k\leq n}S_k$，因此
$$M_n\leq f+M_n \circ T,\quad \omega\in \{M_n>0\}.$$
注意 $M_n$ 总是非负的随机变量，从而
$$\begin{align*}\int_{\{M_n>0\}} f &\geq \int_{\{M_n>0\}}M_n -\int_{\{M_n>0\}}M_n\circ T\\ & = \int_\Omega M_n- \int_{\{M_n>0\}}M_n\circ T\\&\geq \int_\Omega M_n-\int_\Omega M_n\circ T\\&=0.\end{align*}$$
最后由于 $\{M_n>0\}\uparrow \{M_f>0\}$，所以由控制收敛定理即可得到
$$\int_{\{M_f>0\}}f\geq 0,$$
极大遍历定理得证。