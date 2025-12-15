---
title: "Coxeter 群笔记（七）：极小根与正则语言性质"
categories: [Coxeter Groups]
date: 2021-12-06
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
\newcommand{\ra}{r_\alpha}
\newcommand{\rb}{r_\beta}
\newcommand{\inn}{(\,,)}
\newcommand{\bbR}{\mathbb{R}}
\newcommand{\dom}{\,\mathrm{dom}\,}
\newcommand{\dp}[1]{\mathrm{dp}(#1)}
\newcommand{\dpa}{\dp{\alpha}}
\newcommand{\dpb}{\dp{\beta}}
\newcommand{\no}{\mathrm{NO}}
\newcommand{\shlex}{\mathcal{L}}
\newcommand{\low}{\mathcal{R}}

\DeclareMathOperator{\span}{span}


:::{.proposition}
若 $\alpha,\beta\in\Phi$ 满足 $|(\alpha,\beta)|<1$，则必然有 $(\alpha,\beta)=\cos(p\pi/q)$，其中 $p,q$ 是互素的正整数，而且反射 $s_\alpha,s_\beta$ 生成的二面体群是有限群。
:::


**证明**：由已知，内积限制在二维平面 $U=\span{\{\alpha,\beta\}}$ 上是正定的。所以 $V=U\oplus U^\bot$。

我们可以不妨假定 $\alpha$ 是正根，以及 $\beta=\alpha_s$ 是单根。设
$$\alpha = c_s\alpha_s + \sum_{t\ne s }c_t\alpha_t.$$
由于 $\alpha$ 不可能与 $\beta=\alpha_s$ 共线，所以 $\gamma=\alpha - c_s\alpha_s\in U$ 且 $\gamma\ne0$。

注意到如果 $a,b\in\bbR$ 使得 $a\gamma+b\alpha_s\in\Phi$，则 $a,b$ 必须同时非负，或者同时非正。如果 $\alpha,\beta$ 所夹的角度是 $\pi$ 的无理数倍，那么 $s_\alpha s_\beta$ 是 $U$ 上角度为 $\pi$ 的无理数倍的旋转，它的各次幂会将 $\alpha$ 映射为 $U$ 中单位圆周上稠密的集合，特别地必然有某个 $k$ 使得 $(s_\alpha s_\beta)^k\alpha$ 位于扇形区域 $\{a\gamma+b\alpha_s\mid a > 0, b<0\}$ 中，这与此区域不包含任何根矛盾。所以 $\alpha,\beta$ 所夹的角度必须是 $\pi$ 的有理数倍，形如 $p\pi/q$，从而 $s_\alpha,s_\beta$ 生成一个有限二面体群 $D$。又因为 $D$ 作用在 $U^\bot$ 上是平凡的，所以 $D$ 在全空间上的作用也是有限二面体群。$\blacksquare$
