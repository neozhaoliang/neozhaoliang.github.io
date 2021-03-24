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

本文整理自我读研时的笔记，目的是介绍 Coxeter 群的一些基本知识。

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

长度函数 $l(\cdot)$ 是研究 Coxeter 群结构的基本工具。注意 $l(\cdot)$ 的定义依赖于生成元集 $S$ 的选择：对一个 Coxeter 群 $(W,S)$，完全可能选择其另一组不同的生成元 $S'\ne S$ 使得 $(W,S)=(W,S')$，这时其上的长度函数，根系，Bruhat 序等都可能随之改变。这就是为什么在描述一个 Coxeter 群 $(W,S)$ 时要指明 $S$ 的原因。


# 作为反射群的 Coxeter 群：几何实现


## 单个反射变换


## 两个反射变换生成的二面体群


## Coxeter 群的标准几何实现


# 根系


# Tits 锥


# 有限 Coxeter 群的分类