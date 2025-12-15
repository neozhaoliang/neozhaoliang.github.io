---
title: "Todd Kemp 概率论课程笔记"
date: 2021-03-01
url: todd-kemp
---
<!-- md texcmd.md -->





# 16.1/16.2 Kolmogorov's Extension Theorem

这两讲的目的是介绍 Kolmogorov 扩张定理，即构造无穷乘积可测空间使得其有限维分布为给定的、满足相容性条件的有限维分布。

Kolmogorov 扩张定理看起来是一个纯测度论定理，但它本质与空间的拓扑性质有关。

设 $I$ 是指标集，$\{\A_i,\, i\in I\}$ 是某个样本空间 $\O$ 的一族子 $\sigma-$ 代数（每个 $\A_i$ 都是一个 $\sigma-$ 代数），满足条件：对任何两个 $\sigma-$ 代数 $\A_\alpha,\A_\beta$，都存在 $\A_\gamma$ （$\A_\gamma$ 未必唯一）使得 $\A_\alpha\subset\A_\gamma,\,\A_\beta\subset\A_\gamma$。

设 $\P_i$ 是 $\A_i$ 上的概率测度，如果对任何 $\A_\alpha\subset\A_\gamma$ 还有
$$\P_\gamma \big|_{A_\alpha} = \P_\alpha.$$
这时我们就称概率空间 $\{(\A_i,\P_i)\}$ **满足 Kolmogorov 相容性条件**。

这就自然地引出一个问题：是否存在代数 $\A=\cup_{i\in I}\A_i$ 上存在一个可数可加的概率测度 $\P$，使得它是所有 $\P_i$ 的扩张？即对任何 $\A_i$ 都有 $\P\big|_{\A_i}= \P_i$？如果有这样的 $\P$，我们就可以用 Carathéodory 定理将 $\P$ 扩张为 $\sigma(\A)$ 上的可数可加测度。

基本逻辑是：

1. 根据 Carathéodory 测度扩张定，我们只要证明代数 $\mathcal{A}=\cup_{n=1}^\infty\B_n$ 上的有限可加测度是可数可加的。这里
    $$\B_n=\B([0,1])^n\times Q,\quad Q=[0,1]^{\infty}.$$
    而这只要证明测度的连续性：若 $B_n\in\mathcal{A}, B_n\downarrow$ 且 $\inf_n\P(B_n)=\epsilon>0$，则 $\cap B_n\ne\emptyset$。
2. 我们可以不妨假设 $B_n\in\B_n$。这可以通过拉伸整个序列，在缝隙中塞上 $\Omega_k$ 或者 $B_k$ 来得到。
3. 我们可以取紧集 $K_n\in B_n$ 使得 $\mu(B_n\backslash K_n)<\epsilon/2^n$，然后证明对任何 $N$，$\cap_{n=1}^NK_n$ 非空，然后利用 $Q$ 的紧性，和紧集的有限交性质，证明 $\cap_{n=1}^\infty K_n$ 非空，从而 $\cap_{n=1}^\infty B_n$ 非空。
4. 在上一步中，可以取这样的紧集 $K_n$ 要用到 $R^d$ 上的概率测度是 Radon 测度这一性质：它们同时被开集从外部逼近和紧集从内部逼近。$Q$ 的紧性是用了 Tychonoff 定理。

> **引理**：$K$
