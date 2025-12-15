---
title: "Coxeter 群笔记（三）：Tits 锥"
categories: [Coxeter Groups]
date: 2021-12-06
url: "coxeter-groups-tits-cone"
---

\newcommand{\lfun}[2]{\langle #1,\,#2\rangle}
\newcommand{\R}{\mathbb{R}}
\newcommand{\gl}{\mathrm{GL}}
\newcommand{\inn}{(\cdot,\cdot)}
\newcommand{\fd}{\mathcal{D}}
\newcommand{\tc}{\mathcal{C}}
\newcommand{\barfd}{\overline{\mathcal{D}}}
\newcommand{\cone}[1]{\mathrm{cone}(#1)}
\newcommand{\negf}[1]{\mathrm{Neg}(#1)}
\newcommand{\stab}[1]{\mathrm{Stab}(#1)}
\newcommand{\plc}[1]{\mathrm{PLC}(#1)}
\newcommand{\barc}{\overline{C}}
\newcommand{\bartc}{\overline{\tc}}
\newcommand{\sthe}[1]{\dfrac{\sin #1\theta}{\sin\theta}}
\newcommand{\shthe}[1]{\dfrac{\sinh #1\theta}{\sinh\theta}}
\newcommand{\span}{\mathrm{span}}

本文主要参考了 Bob Howlett 教授的讲义 [@Howlett-note]。

# Tits 锥

在获得了 $V$ 中关于根系的一些知识后，我们下面转移到 $V$ 的对偶空间 $V^\ast$ 中讨论万花筒的结构。

<!--more-->

设 $V^\ast$ 是 $V$ 的对偶空间，$V$ 和 $V^\ast$ 之间存在自然的双线性映射
$$V\times V^\ast\to\R: \lfun{v}{f}= f(v).$$
注意 $\lfun{\,}{}$ 和内积 $\inn$ 的区别：$\lfun{\,}{}$ 是 $V\times V^\ast$ 的自然配对，用尖括号表示；$\inn$ 是 $V$ 上的内积。

$V$ 上的可逆线性变换 $g\in\gl(V)$ 同样作用在 $V^\ast$ 上：对 $f\in V^\ast$，线性泛函 $g\cdot f$ 定义为
$$(g\cdot f)(v) = f(g^{-1} v).$$
为了简便我们省略 $g\cdot f$ 中的 $\cdot$，把它写作 $gf$。

这样定义的目的是为了让 $g$ 保持双线性映射 $\lfun{\,}{}$ 不变：
$$\lfun{gv}{gf} = \lfun{v}{f}.$$
用 $g^{-1}f$ 代替 $f$，我们得到
$$\lfun{gv}{f} = \lfun{v}{g^{-1}f}.$$
特别当 $g=s$ 是一个反射时，由于 $s=s^{-1}$ 所以
$$\lfun{sv}{f} = \lfun{v}{sf}.$$
这种将单个反射在 $\inn{\,}{}$ 两边「跳来跳去」的技巧后面会经常用到。

由于 $V$ 和 $V^\ast$ 互为对偶空间，所以 $\Delta=\{\alpha_s\}$ 是 $V^\ast$ 上的一组线性无关的泛函，定义它们的正半空间的交为
$$\fd = \bigcap_{s\in S}\{x\in V^\ast\mid \lfun{\alpha_s}{x} > 0\}.$$
$\fd$ 总是 $V^\ast$ 中的非空开集，其闭包记作 $\barfd$。你可以把 $\fd$ 理解为万花筒中被镜子围起来的原像房间，超平面的集合 $\{\alpha_s=0\}$ 是房间的墙壁。$\barfd$ 就是 $\fd$ 加上了房间四周的墙壁。

$W$ 也作用在 $V^\ast$ 上：
$$\lfun{v}{w f} = \lfun{w^{-1}v}{f}.\quad v\in V,\,f\in V^\ast.$$
在 [上文](/coxeter-groups/root-system/#faithful) 中我们已经证明了 $W$ 忠实地作用在 $V$ 上。不难验证在此定义下，$W$ 也忠实地作用在 $V^\ast$ 上，即若 $wf=f$ 对任何 $f\in V^\ast$ 成立，则 $w=1$。

:::{.definition}
Tits 锥定义为
$$\tc = \bigcup_{w\in W} w\barfd.$$
:::

显然 $\tc$ 是 $W$- 不变的。$\tc$ 可以理解为万花筒，它由原像房间 $\barfd$ 在 $W$ 下的所有虚像构成。

读者可能有疑问为什么 Tits 锥位于对偶空间 $V^\ast$ 中。看起来更自然的做法是，直接取以 $\Delta$ 为法向量的正半空间之交作为基本区域：
$$\fd=\bigcap_{s\in S}\{v\in V\mid(\alpha_s, v)>0\}$$
在内积 $\inn$ 非退化时，这样做是可以的；但是在 $\inn$ 退化时，这样定义可能导致 $\fd$ 是空集。以仿射 $\widetilde{A_1}$ 为例，它的 Coxeter 矩阵是
$$\begin{pmatrix}1 & \infty\\\infty&1\end{pmatrix}.$$
在 $a_{s,t}=1$ 时对应的 Gram 矩阵是
$$\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.$$
设 $v=a\alpha_s+b\alpha_t$ 满足 $(v,\alpha_s)>0$ 且 $(v,\alpha_t)>0$，你会发现这要求 $a>b$ 且 $b>a$，即 $\fd$ 是空集！但是通过区分 $W$ 在 $V$ 和 $V^\ast$ 上的作用就可以避免这个问题。因为 $\Delta$ 作为 $V$ 的一组基构成 $V^\ast$ 上一组线性无关的泛函，它们在 $V^\ast$ 中正半空间的交是非空的拓扑开集。

读者可能注意到了：我们使用了 Tits 锥这个称呼，但 $\tc$ 真的是一个锥吗？这可不显然。要证明 $\tc$ 确实是锥，我们需要它的另一种等价刻画。

我们回顾锥的定义：

::: definition
设 $C$ 是某实向量空间的子集。如果对任何实数 $\alpha\geq0$ 都有 $\alpha C\subset C$，就称 $C$ 是一个**锥**。如果 $C$ 还是凸集，就称 $C$ 是**凸锥**。凸锥满足对任何 $x,y\in C$ 和非负实数 $\alpha,\beta\geq0$，$\alpha x + \beta y$ 仍然属于 $C$。
:::

设 $X$ 是某实向量空间的子集，定义其生成的凸锥为：
$$\cone{X} = \left\{\sum_{i=1}^n c_ix_i\mid x_1,\ldots,x_n\in X,\, c_i\geq0.\right\}.$$
显然 $\cone{X}$ 是包含 $X$ 的最小凸锥。

:::{.note}
当 $X$ 是有限集时，$\cone{X}$ 总是闭集；但是当 $X$ 是无限集时则未必。例如当 $X$ 是 $\R^2$ 中直线 $y=1$ 上的全体整点时，$\cone{X}=\{y>0\}\cup\{0\}$ 不是闭集。
:::

::: {.definition #fundamental-weights}
设 $\Delta^\ast=\{\omega_t\}\subset V^\ast$ 是 $\Delta$ 的一组对偶基，满足 $\lfun{\alpha_s}{\omega_t}=\delta_{st}$，$\Delta^\ast$ 叫做**基本权**。记
$$\Omega=\bigcup_{w\in W}w\Delta^\ast.$$
$\Omega$ 中的元素叫做**权**。
:::

::: {.proposition #fund-cone}
$\barfd=\cone{\Delta^\ast}$。
:::

**证明**：任何 $x\in V^\ast$ 可以表示为 $x=\sum_{s\in S}c_s\omega_s$，其中 $c_s=\lfun{\alpha_s}{x}$，于是
$$x\in\cone{\Delta^\ast}\Leftrightarrow c_s\geq0,\ \forall s \in S \Leftrightarrow \lfun{\alpha_s}{x}\geq 0,\ \forall s\in S \Leftrightarrow x\in\barfd.
$$
$\blacksquare$

:::{.definition}
对任意 $x\in V^\ast$，定义
$$\negf{x}= \{\lambda\in \Phi^+\mid \lfun{\lambda}{x}<0\}.$$
$\negf{x}$ 是正根 $\Phi^+$ 的子集，表示 $x$ 位于哪些镜子的「背面」。即这些镜子挡在 $x$ 和基本区域 $\fd$ 之间。
:::

显然 $\barfd=\{x\in V^\ast\mid\negf{x}=\emptyset\}$。

:::{.theorem #tits-neg-finite}
Tits 锥 $\tc = \{x\in V^\ast \mid |\negf{x}| < \infty\}$。
:::

::: note
这个定理的几何意义是，Tits 锥恰好由那些和基本区域 $\barfd$ 之间只隔着有限多个镜子的点组成，这样的点一定可以通过有限次单反射变换到 $\barfd$ 中，即下面的 `while` 循环可以在有限次后结束：

```python
while dot(x, alpha_s) < 0 for some s in S:
    x = reflect(x, alpha_s)
```

下面的动画展示了双曲 Coxeter 群 $\Delta(3,3,7)$ 的 Tits 锥中那些反射次数 $\leq10$ 的点：

![](/images/coxeter/337-anim.gif){width=400 .fig}
:::

**证明**：

$\Rightarrow$：设 $x\in\tc$，则 $x$ 可以表示为 $x=wv$，其中 $w\in W,v\in\barfd$。设 $\lambda\in\negf{x}$，则
$$0>\lfun{\lambda}{x}=\lfun{\lambda}{wv}=\lfun{w^{-1}\lambda}{v}.$$
然而 $v\in\barfd$，这说明 $w^{-1}\lambda\in\Phi^-$，从而 $\negf{x}\subseteq N(w^{-1})$，从而
$$|\negf{x}|\leq |N(w^{-1})|=l(w)<\infty.$$

$\Leftarrow$：反之若 $|\negf{x}|<\infty$，我们来论证存在 $w\in W$ 使得 $wx\in\barfd$。这里的想法是，每次选择一个单根 $\alpha_s$ 对应的镜面，使得 $x$ 落在这个镜子的背面，然后将 $x$ 关于 $\alpha_s$ 反射过去变到 $\alpha_s$ 的正面，这个操作会将遮挡在 $x$ 和 $\barfd$ 之间的镜子个数严格减少 1。如此这般直到 $x$ 落入 $\barfd$ 为止。

具体论证如下：

若 $\negf{x}=\emptyset$，则 $x\in\barfd$，结论显然成立。

若 $\negf{x}\ne\emptyset$，$\negf{x}$ 中一定包含某个单根 $\alpha_s$。考虑 $x$ 关于 $\alpha_s$ 的镜像 $sx$，$sx$ 位于 $\alpha_s$ 的正面，所以 $\alpha_s\notin\negf{sx}$。于是对任何正根 $\lambda\in\negf{sx}$，[$s\lambda$ 仍然是正根且 $s\lambda\ne\alpha_s$](/coxeter-groups/root-system/#simple-ref)。对这样的 $\lambda$，我们有
$$0>\lfun{\lambda}{sx}=\lfun{s\lambda}{x}\Rightarrow s\lambda\in\negf{x}.$$
这说明
$$s\cdot\negf{sx}\subseteq\negf{x}\setminus\{\alpha_s\}.$$
从而 $\negf{sx}$ 的元素个数严格小于 $\negf{x}$。

记 $y=sx$，对 $y$ 重复此过程，我们可以逐步将 $\negf{y}$ 减少为空集，即最终 $y$ 落在 $\barfd$ 中。于是存在 $s_1,\ldots,s_k$ 使得 $y=(s_1\cdots s_k)\cdot x\in\barfd$。取 $w=s_1\cdots s_k$，则 $x= w^{-1}y\in\tc$。这就证明了结论。$\blacksquare$

:::{.corollary #tits-convex}
Tits 锥 $\tc$ 是凸锥。
:::

**证明**：设 $x, y\in\tc$ 和 $\alpha,\beta\geq0$，我们要证明 $z=\alpha x+\beta y\in\tc$。由于
$$\negf{z}\subseteq\negf{x}\cup\negf{y},$$
根据 @Pre:tits-neg-finite，$\negf{x},\,\negf{y}$ 都是有限集，所以 $\negf{z}$ 也有限，从而 $z\in\tc$，即 $\tc$ 是凸锥。$\blacksquare$

::: {.corollary}
$\tc=\cone{\Omega}$。
:::

**证明**：由于 $\Omega\supset\Delta^\ast$，以及根据 @Pre:fund-cone 有 $\cone{\Delta^\ast}=\barfd$，所以
$$\cone{\Omega}\supset\cone{\Delta^\ast}=\barfd.$$
又因为 $\cone{\Omega}$ 是 $W$- 不变的，所以它包含 $\bigcup_{w\in W}w\barfd=\tc$。

另一方面 $\tc\supset\barfd\supset\Delta^\ast$，并且 $\tc$ 也是 $W$- 不变的，所以
$$\tc\supset\bigcup_{w\in W}w\Delta^\ast=\Omega.$$
而 @Pre:tits-convex 证明了 $\tc$ 是凸锥，所以 $\tc\supset\cone{\Omega}$。$\blacksquare$

# Tits 锥的内点

接下来我们来讨论 $\tc$ 的内点集 $\tc^\circ$。我们将证明 $\tc^\circ$ 由那些稳定化子群是有限群的点组成：
$$\tc^\circ = \{x\in V^\ast \mid |\stab{x}| < \infty\}.$$

:::{.theorem #stabilizer-parabolic-subgroup}
对任何 $x\in\barfd$，记 $J=\{s\in S \mid \lfun{\alpha_s}{x}=0\}$，则 $\stab{x} = W_J$。
:::

::: note
这个定理的含义是，在原像房间 $\barfd$ 中，每个点的稳定化子群是一个标准椭圆子群，由包含该点的那些镜子生成。
:::

**证明**：

任取 $s\in J$ 和 $v\in V$，我们有
$$\lfun{v}{sx} = \lfun{sv}{x}=\lfun{v-2(v,\alpha_s)\alpha_s}{x}=\lfun{v}{x}.$$
由 $v$ 的任意性可得 $sx=x$，从而 $W_J\subseteq\stab{x}$。

再证明反向包含关系。设 $w=s_1\cdots s_k\in\stab{x}$ 是一个既约表示，我们从最末一个元素 $s_k$ 开始，向左逐个验证它们属于 $J$。

记 $w'=s_1\cdots s_{k-1}$，则 $l(ws_k)=l(w')<l(w)$，于是 $w\alpha_k\in\Phi^-$。由于 $x\in\barfd$，我们有
$$0\geq \lfun{w\alpha_k}{x} = \lfun{\alpha_k}{w^{-1}x} = \lfun{\alpha_k}{x}\geq0.$$
于是上面的不等式中等号都成立，从而 $\lfun{\alpha_k}{x}=0$，即 $s_k\in J$ 且 $s_kx=x$。进一步 $w'$ 也满足 $w'x=x$。对 $w'$ 重复此论证，便得到 $s_1,\ldots,s_k$ 都属于 $J$。$\blacksquare$

::: {.proposition #fd-finite-stabilizer}
设 $x\in\barfd$，则 $x\in\tc^\circ$ 当且仅当 $\stab{x}$ 是有限群。
:::

**证明**：

$\Rightarrow$：思路：如果 $x$ 是 $\tc$ 的内点，并且经过 $x$ 的镜面有无穷多个，那么可以在 $x$ 的附近取一点 $z$，$z$ 仍然是 $\tc$ 的内点，使得这无穷多个镜子都挡在基本区域和 $z$ 之间，从而 $\negf{z}$ 是无限集，从而 $z\notin\tc$，导致矛盾。

具体论证如下：

记 $J$ 和 $W_J$ 如 @Pre:stabilizer-parabolic-subgroup，则 $\stab{x}=W_J$。

![一个示意图，$z$ 落在所有 $\Phi_J$ 中镜子的背面](/images/coxeter/WJ.svg){width=300}

任取 $y\in\fd$。由于 $x\in\tc^\circ$，所以在线段 $\overline{[y, x]}$ 上我们可以朝着 $x$ 的方向延伸一点点，得到点 $z$，使得 $z$ 仍然位于 $\tc^\circ$ 中。$z$ 可以表示为
$$z=(1-t)x+ty,\quad t<0.$$

于是对所有 $s\in J$ 都有 $\lfun{\alpha_s}{z}=t\lfun{\alpha_s}{y} < 0$，从而 $\Phi_J^+\subset\negf{z}$。如果 $W_J$ 是无限群，那么 $\Phi_J^+$ 也无限，从而 $\negf{z}$ 无限，这与 $z\in\tc$ 矛盾！

$\Leftarrow$：反之若 $W_J$ 是有限群，仍然任取 $y\in\fd$。

![$y$ 在 $W_J$ 下的像全部位于镜面 $\alpha_s=0$ 的正侧，故 $\lfun{\alpha_s}{wy}$ 对 $w\in W_J$ 总为正](/images/coxeter/WJ2.svg){width=300}

设 $s\in S\setminus J$，则 $\lfun{\alpha_s}{x}>0$。对任何 $w\in W_J$，[$w^{-1}\alpha_s$ 仍然是正根](/coxeter-groups/root-system#remain-positive-root)，所以
$$\lfun{\alpha_s}{wy}=\lfun{w^{-1}\alpha_s}{y}>0.$$
于是
$$\delta = \min\left\{\frac{\lfun{\alpha_s}{x}}{\lfun{\alpha_s}{wy}}\,\middle|\, \alpha_s\in S\setminus J,\, w\in W_J\right\}>0.$$
将上面的分母乘到左边然后对 $w\in W_J$ 求和，我们有
$$\delta\cdot\lfun{\alpha_s}{\sum_{w\in W_J}wy}\leq \lfun{\alpha_s}{x}\cdot |W_J| < 2\lfun{\alpha_s}{x}\cdot |W_J|,\quad s\in S\setminus J.\tag{1}\label{eq:strict}$$
注意这个不等式两边关于 $\alpha_s$ 都是线性的。

既然对 $s\in S\setminus J$ 上面的不等式是严格的，那么对 $s\in J$ 又如何呢？这时右边 $\lfun{\alpha_s}{x}=0$。又因为 $\sum_{w\in W_J}wy$ 在 $W_J$ 下保持不动，所以根据 @Pre:stabilizer-parabolic-subgroup 可得 $\lfun{\alpha_{s}}{\sum_{w\in W_J}wy}=0$，从而上面的不等式变成了等式（两边都是 0）：
$$0=\delta\cdot\lfun{\alpha_s}{\sum_{w\in W_J}wy}= 2\lfun{\alpha_s}{x}\cdot |W_J|,\quad s\in J.\tag{2}\label{eq:equal}$$
对任何 $\lambda\in\Phi^+\setminus\Phi_J^+$，设
$$\lambda=\sum_{s\in S\setminus J}c_s\alpha_s + \sum_{t\in J}d_t\alpha_t,\quad c_s,\,d_t\geq0.$$
其中至少有一项 $c_s$ 严格大于 0。将 $\lambda$ 代入 $(\ref{eq:strict})$ 中 $\alpha_s$ 的位置，严格不等式仍然成立。即
$$\delta\cdot\lfun{\lambda}{\sum_{w\in W_J}wy}< 2\lfun{\lambda}{x}\cdot |W_J|.$$
注意对 $w\in W_J$，$w^{-1}\lambda$ 作为 $\lambda$ 和 $\{\alpha_s\mid s\in J\}$ 的线性组合仍然是正根，并且不在 $\Phi_J^+$ 中，所以上面的求和中每一项 $\lfun{\lambda}{wy}=\lfun{w^{-1}\lambda}{y}>0$，我们可以只取 $w=1$ 对应的项，其余全扔掉，得到
$$\delta\cdot\lfun{\lambda}{y}< 2\lfun{\lambda}{x}\cdot |W_J|.$$
记 $z = 2|W_J|x - \delta y$，我们得到 $\lfun{\lambda}{z}>0$ 对任何 $\lambda\in\Phi^+\setminus\Phi_J^+$ 成立。

另一方面对任何 $\mu\in\Phi_J^+$，由于 $\lfun{\mu}{x}=0$，所以 $\lfun{\mu}{z}=-\delta\lfun{\mu}{y}<0$，于是 $\negf{z}=\Phi_J^+$ 是有限集，从而 $z\in\tc$。

实际上我们有 $z\in\tc^\circ$，这是因为对任何 $\lambda\in\Phi$，$\lambda$ 必然属于 $\pm\Phi^+_J,\pm(\Phi^+\setminus\Phi^+_J)$ 之一，而我们已经看到 $\lfun{\lambda}{z}$ 总不是 0，所以 $z$ 不落在任何镜面上。设 $z=wv,\,v\in\barfd$，那么
$$\lfun{\alpha_s}{v}=\lfun{w\alpha_s}{wv}=\lfun{w\alpha_s}{z}\ne0$$
对任何 $\alpha_s\in\Delta$ 成立，所以 $v\in\fd\subset\tc^\circ$，从而 $z=wv\in w\fd\subset\tc^\circ$。

![我们证明 $z$ 只落在 $\Phi_J$ 中镜面的背面，从而 $z\in\tc$；并证明 $z$ 不属于任何镜面，从而 $z\in\tc^\circ$](/images/coxeter/WJ3.svg){width=300}

现在 $x$ 是 $z$ 和 $y$ 的线性组合 $x = \frac{1}{2|W_J|}(z + \delta y)$。由于 $z,y\in\tc^\circ$ 而 $\tc$ 是凸锥，所以 $\frac{1}{2|W_J|}z, \frac{\delta}{2|W_J|}y\in\tc^\circ$，即存在开集 $A,B$ 满足 $\frac{1}{2|W_J|}z\in A\subset\tc^\circ$，$\frac{\delta}{2|W_J|}y\in B\subset \tc^\circ$。于是 $x\in A+B=\cup_{p\in B}(A+p)$，这是一组开集的并，每个 $A+p$ 都在 $\tc$ 中，所以 $x\in\tc^\circ$。$\blacksquare$

:::{.theorem #tits-int-finite-stabilizer}
设 $y\in\tc$，则 $y\in\tc^\circ$ 当且仅当 $\stab{y}$ 是有限群。
:::

**证明**：$y$ 可以写成 $y=wx\,(w\in W,\,x\in\barfd)$ 的形式，从而 ${\rm Stab}(y)=w{\rm Stab}(x)w^{-1}$，二者同为有限群或者无限群；而且 $x,y$ 同时属于或者同时不属于 $\tc^\circ$。由 @Pre:fd-finite-stabilizer 即得结论。$\blacksquare$


# Tits 锥的对偶锥

这一节来讨论 Tits 锥的对偶锥。研究对偶锥对理解 Tits 锥本身的结构也很有帮助。

:::{.definition #dual-cone}
设 $C$ 是 $V$ 中的一个锥，定义 $C$ 的对偶锥 $C^\ast\in V^\ast$ 为
$$C^\ast = \{f\in V^\ast\mid f(v)\geq0,\ \forall v\in C\}.$$
即 $C^\ast$ 是对偶空间中那些在 $C$ 上取值均非负的线性泛函组成的集合。
:::

不难看出 $C^\ast$ 也构成 $V^\ast$ 中的一个锥，所以我们又可以取其对偶锥 $C^{\ast\ast}\subset V$。

:::{.theorem #dual-dual-cone}
$C^{\ast\ast} = \overline{C}$。其中 $\overline{C}$ 是 $C$ 的拓扑闭包。
:::

**证明**：显然 $\overline{C}\subseteq C^{\ast\ast}$，只要论证 $C^{\ast\ast} \subseteq \overline{C}$ 即可。

对任何 $x\notin\overline{C}$，根据凸集分离定理，存在超平面 $H$，其法向量 $n$ 满足 $(n,C)\geq 0$ 但是 $(n,x) < 0$。于是线性泛函 $(n,\cdot)\in C^\ast$ 且由于 $(n,x)<0$ 从而 $x\notin C^{\ast\ast}$。反向包含得证。$\blacksquare$

:::note
对不熟悉凸集分离定理的读者，下面是一点细节补充：设 $u\in\overline{C}$ 是 $\overline{C}$ 中与 $x$ 距离最近的点：$|x-u|=\inf_{z\in \overline{C}}|x-z|$。对任何 $z\in\overline{C}$，考虑线段 $[u,z]$ 上的点与 $x$ 的距离 $$f(t) = |u + t(z-u) - x|,\quad 0\leq t\leq1.$$
$f$ 在 $t=0$ 时取得最小值： $$ |u-x|^2 \leq |u-x|^2 + 2t(u-x, z-u) + t^2|z-u|^2.$$ 即 $$0\leq t\cdot\left(2(u-x,z-u) + t|z-u|^2\right)\leq 2(u-x,z-u) + t|z-u|^2.$$ 令 $t\to0^+$ 可得 $(u-x,z-u)\geq 0$。 这个式子对任何 $z\in\overline{C}$ 成立，特别地取 $z=tu$ 代入有 $$(1-t)\cdot(u-x, u)\geq0.$$ 上式对任何 $t\geq0$ 成立必须只能是 $(u-x, u)=0$。于是不等式 $$(u-x,z-u)\geq 0$$ 可以改写为 $$(u-x,z)\geq0$$ 对任何 $z\in\overline{C}$ 成立。而 $(u-x,x)=-(u-x,u-x)<0$。所以 $u-x$ 即为所求的法向量 $n$。
:::

回到 Tits 锥 $\tc$ 的讨论上来。记 $\tc^\ast$ 是 $\tc$ 的对偶锥，则 $\tc^\ast\in V$。我们有如下定理：

:::{.theorem #tits-cone-dual}
$\tc^\ast=\bigcap\limits_{w\in W}w(\cone{\Delta})$。
:::

可见 $\tc^\ast$ 也是 $W$- 不变的。

**证明**：显然 $\cone{\Delta}$ 是 $V$ 中的一个闭凸锥，它在 $V^\ast$ 中的对偶锥是 $\barfd$：
$$\barfd = \{x\in V^\ast\mid \lfun{\lambda}{x}\geq0,\ \forall \lambda\in\cone{\Delta}\}.$$
我们有
$$
\begin{align}
\tc^\ast &=\{v\in V \mid \lfun{v}{x}\geq 0 \text{ for all } x \in \tc\}\\
&= \{v\in V \mid \lfun{v}{wz}\geq0 \text{ for all } z\in\barfd \text{ and } w \in W\}\\
&= \{v\in V \mid \lfun{w^{-1}v}{z}\geq0 \text{ for all }z\in\barfd \text{ and } w \in W\}\\
&= \{v\in V \mid w^{-1}v\in (\barfd)^\ast \text{ for all } w \in W\}\\
&\stackrel{(\ast)}{=} \{v\in V \mid w^{-1}v\in \cone{\Delta} \text{ for all } w \in W\}\\
&= \{v\in V \mid v\in w(\cone{\Delta}) \text{ for all } w \in W\}.
\end{align}
$$

其中 $(\ast)$ 一步正是将 @Pre:dual-dual-cone 应用在 $C=\cone{\Delta},\,C^\ast=\barfd$ 上得到的。注意我们使用了 $\cone{\Delta}$ 是闭集这一点：$\cone{\Delta}=\overline{\cone{\Delta}}$。$\blacksquare$

:::{.corollary #tits-cone-dual-pointed}
$\tc^\ast$ 是点锥：$\tc^\ast\cap -\tc^\ast=\{0\}$。
:::

**证明**：根据 @Pre:tits-cone-dual 有 $\tc^\ast\subset\cone{\Delta}$，但显然 $\cone{\Delta}\cap-\cone{\Delta}=\{0\}$。$\blacksquare$

虽然我们得到了上面关于 $\tc^\ast$ 的刻画，但是它并不好用。我们下面用内积的形式给出 $\tc^\ast$ 的一个更好的刻画。

:::{.proposition #dual-cone-dot-neg}
如果 $v\in\cone{\Delta}$ 满足对任何 $\alpha_s\in\Delta$ 有 $(v,\alpha_s)\leq0$，则 $v\in\tc^\ast$。
:::

**证明**：根据 @Pre:tits-cone-dual，只要证明对任何 $w$ 都有 $wv\in\cone{\Delta}$ 即可。

对 $l(w)$ 归纳：$l(w)=0$ 的情形是已知。当 $l(w)>0$ 时，设 $w=w's$，其中 $l(w')<l(w)$，则 $w'\alpha_s\in\Phi^+\subset\cone{\Delta}$。于是

$$
\begin{align}wv &= w'sv\\
&=w'(v - 2(v,\alpha_s)\alpha_s)\\
&=w'v - 2(v,\alpha_s)w'\alpha_s.
\end{align}
$$

根据归纳假设 $w'v\in\cone{\Delta}$，所以 $wv$ 是 $\cone{\Delta}$ 中两个向量的非负线性组合，从而 $wv\in\cone{\Delta}$。$\blacksquare$

:::{.proposition #dual-cone-nonspace}
对任何 $u,v\in\tc^\ast$ 有 $(u,v)\leq 0$。
:::

:::{.note}
我是在与 [Bob Howlett](https://www.maths.usyd.edu.au/u/bobh/) 教授的邮件交流中学到这个结论的。这个证明我相信改进自 [@Maxwell82]。
:::

**证明**：对 $v = \sum_{s\in S}c_s\alpha_s\in V$，定义 $S(v)=\sum_{s\in S}c_s$ 为所有系数的和。注意当 $v\in\tc^\ast\subset\cone{\Delta}$ 时，每个 $c_s$ 都是非负的，所以 $S(v)\geq0$。

用反证法，设 $u,v\in\tc^\ast$ 满足 $(u,v)>0$，不妨设 $(u,v)=1$。记 $n=|S|$ 和 $M=S(u)$。定义

$$X=\{x\in\tc^\ast\mid S(x)\leq S(v) \text{ and $(z,x)\geq1$ for some $z\in\tc^\ast$ with $S(z)\leq M$}\}.$$

显然 $v\in X$。

记 $\epsilon=2/(nM)$，我们将证明对任何 $x\in X$，都存在 $y\in X$ 使得 $S(y)\leq S(x)-\epsilon$。

对 $x\in X$，设 $z=\sum_{s\in S}z_s\alpha_s\in\tc^\ast$ 满足 $S(z)\leq M$ 和 $(z,x)\geq1$，则
$$(z,x)=\sum_{s\in S}z_s(\alpha_s, x)\geq1.$$
所以必有某个 $\alpha_s$ 使得 $z_s(\alpha_s,x)\geq 1/n$。由于 $z_s\leq S(z)\leq M$，我们有
$$(\alpha_s,x)\geq 1/(nz_s)\geq 1/(nM)=\epsilon/2.$$

考察
$$y=sx=x-2(x,\alpha_s)\alpha_s.$$
由于 $x\in\tc^\ast$ 以及 $\tc^\ast$ 是 $W-$ 不变的所以 $y\in\tc^\ast$。又注意到
$$S(y)=S(x)-2(x,\alpha_s)\leq S(x)-\epsilon.$$
所以要证明 $y$ 符合要求，只要再找到某个 $z'\in\tc^\ast$ 满足 $S(z')\leq M$ 和 $(z',y)\geq1$ 即可。

如果 $(z,\alpha_s)<0$，那么 $z'=z$ 就满足要求，因为这时
$$(z,y)=(z,x-2(x,\alpha_s)\alpha_s)=(z,x)-2\underbrace{(x,\alpha_s)}_{\geq\epsilon/2}\underbrace{(z,\alpha_s)}_{<0}>(z,x)\geq1.$$

反之如果 $(z,\alpha_s)>0$，我们来验证 $z'=sz=z-2(z,\alpha_s)\alpha_s$ 满足要求：由于 $z\in\tc^\ast$ 所以 $z'\in\tc^\ast$，并且 $S(z')=S(z)-2(z,\alpha_s)<S(z)$，以及
$$(z', y)=(sz, sx)=(z,x)\geq1.$$

于是从 $v$ 出发，我们可以经过有限次取 $y\in X$ 的操作使得 $S(y)$ 是负数，但这与 $y\in X\subset\tc^\ast$ 矛盾。$\blacksquare$

