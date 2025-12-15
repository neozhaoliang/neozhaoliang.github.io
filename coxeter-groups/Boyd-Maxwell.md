---
title: "Coxeter 群笔记（六）：Boyd-Maxwell 球堆"
categories: [Coxeter Groups]
date: 2021-12-09
url: "coxeter-groups-boyd-maxwell"
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
\newcommand{\span}{\mathrm{span}}
\newcommand{\rad}{\mathrm{rad}}
\newcommand{\cl}[1]{\overline{ #1 }}
\newcommand{\Q}{\mathcal{Q}}
\newcommand{\N}{\mathcal{N}}
\newcommand{\cone}[1]{\mathrm{cone}(#1)}
\newcommand{\bfA}{\mathbf{A}}
\newcommand{\P}{\mathcal{P}}
\newcommand{\S}{\mathcal{S}}
\newcommand{\H}{\mathcal{H}}
\newcommand{\tcr}{\overline{\mathcal{C}_r}}
\newcommand{\sign}[1]{\mathrm{sgn}(#1)}
\newcommand{\Rntwo}{\mathbb{R}^{n+1,1}}
\newcommand{\PR}{\mathrm{P}(\mathbb{R}^{n+1,1})}
\newcommand{\L}{\mathbb{L}^{n+1}}
\newcommand{\PL}{\mathrm{P}(\mathbb{L}^{n+1})}
\newcommand{\LR}{\mathbb{R}^{n+1,1}}
\newcommand{\ER}{\overline{\mathbb{R}^n}}
\newcommand{\x}{\mathbf{x}}
\newcommand{\y}{\mathbf{y}}
\newcommand{\a}{\mathbf{a}}
\newcommand{\n}{\mathbf{n}}

本文的内容主要来自 [@Maxwell82] 和 [@Maxwell89]，并修复了一些错误。Maxwell 在 [@Maxwell82, pp 81] 中写到：

:::{.simple}
When $\Gamma$ is hyperbolic, the cone

$$\{v\in V\mid (v,v)\leq0\}$$

has two connected components (after deleting 0), which are also the equivalent classes for the relation
$$u\sim v\Leftrightarrow (u,v)\leq0.$$
:::

这显然是错误的，因为如果 $u$ 是 light-like 的向量，$u$ 和 $-u$ 属于不同的分支。这个错误导致后面 [@Maxwell82, prop 3.1] 的证明需要作一些修改。详情见下面的 @Pre:thm-sphere-packing。


<!--more-->

# 射影模型

设 $V=\R^{n+1,1}$ 是 $n+2$ 维 Lorentzian 空间，$\{e_1,e_2,\ldots,e_{n+2}\}$ 是一组标准正交基，对应的 Gram 矩阵为 $\left(\begin{smallmatrix}I_{n+1} &\\ & -1\end{smallmatrix}\right)$。令
$$e_0=\frac{e_{n+2}-e_{n+1}}{2},\quad e_\infty=\frac{e_{n+2}+e_{n+1}}{2}.$$
则 $\{e_0,e_1,\ldots,e_n,e_\infty\}$ 也构成 $V$ 的一组基，内积在这组新基下的 Gram 矩阵为
$$\begin{pmatrix}0&&&-\frac{1}{2}\\&I_n&&\\-\frac{1}{2}&&&0\end{pmatrix}.$$
任何 $v,w\in V$ 可以表示为：
$$\begin{aligned}
v&=ae_0 + \x + be_\infty,\\
w&=ce_0 + \y + de_\infty.
\end{aligned}$$
其中 $\x,\y\in\span\{e_1,\ldots,e_n\},\,a,b\in\R$。则 $v,w$ 之间的内积为
$$(v,w) = (\x, \y) - \frac{ad+bc}{2}.$$
使用 $\{e_0,e_1,\ldots,e_n,e_\infty\}$ 这组基在处理 $\R^n$ 中的球时更方便一些。

记 $[v]$ 为向量 $v\in\R^{n+1,1}$ 在射影空间 $\PR$ 中的等价类。

::: definition
定义光锥 (light cone/null cone) 为
$$\L = \{v\in \LR \mid(v,v)=0\}.$$
以及
$$\PL=\{[v]\mid v\in\L\setminus\{0\}\}.$$
$\PL$ 是 $\L$ 中所有直线组成的集合。
:::

熟知 $\ER=\R^n\cup\{\infty\}$ 和 $\R^{n+1}$ 中的单位球 $S^n=\{x_1^2+x_2^2+\cdots+x_{n+1}^2=1\}$ 在球极投影下是一一对应的（北极点为 $e_{n+1}$）。

![$S^2$ 到 $\overline{\R^2}$ 的球极投影，by Keenan Crane](/images/coxeter/stereo-projection.svg){width=400}

我们将看到，$\PL$ 同时与 $\ER$ 和 $S^n$ 一一对应，并且当 $\x\in\ER$ 和 $\y\in S^n$ 在球极投影下对应时，它们在 $\PL$ 对应中同一个点。

:::{.simple}
$\PL$ **的第一种参数化表示** \

我们在 $\{e_1,\ldots,e_{n+2}\}$ 这组基下计算。

设 $\y=y_1e_1+\cdots+y_{n+1}e_{n+1}\in\R^{n+1}$，则
$$\y\in S_n\Leftrightarrow |\y|=1\Leftrightarrow \y+e_{n+2}\in\L.$$
即我们有一一映射：
$$
\begin{aligned}
S^n&\mapsto S^n_1\\
\y &\mapsto \y+e_{n+2}.
\end{aligned}$$
其中 $S^n_1$ 是平面 $y_{n+2}=1$ 与 $\L$ 相交给出的截线。由于 $\PL$ 中每个元素在 $S^n_1$ 中有唯一代表元，所以
$$\jmath\colon\ S^n\to\PL: \y\to [\y+e_{n+2}],$$
是一一对应，此即为 $\PL$ 的第一种参数化表示。
:::

:::{.simple #second-param}
$\PL$ **的第二种参数化表示** \

我们在 $\{e_0,e_1,\ldots,e_n,e_\infty\}$ 这组基下计算。对 $[v]\in\PL$：

+ 如果 $v$ 的 $e_0$ 分量不为 0，则 $v$ 形如
$$v=e_0 + \x + be_\infty,\quad \x\in\span\{e_1,\ldots,e_n\}.$$
由于 $v\in\L$ 所以 $b=|\x|^2$，即 $v=e_0 + \x + |\x|^2e_\infty$。
+ 如果 $v$ 的 $e_0$ 分量等于 0，则 $v$ 形如
$$v=\x+be_\infty,\quad \x\in\span\{e_1,\ldots,e_n\}.$$
$v\in\L$ 说明 $\x=0$，从而 $[v] = [(0,0,b)]=[e_\infty]$。

于是我们可以定义如下从 $\ER$ 到 $\PL$ 的一一对应:
$$
\imath(\x)=\begin{cases}[e_0 + \x + |\x|^2e_\infty] & \x\in\R^n,\\
[e_\infty] & \x = \infty.
\end{cases}
$$
此即为 $\PL$ 的第二种参数化表示。
:::

![红色的圆是超平面 $(\cdot, e_{n+2})=1$ 与光锥的截线，可以通过将 $S^n$ 沿着 $e_{n+2}$ 平移一个单位得到；$\ER$ 对应蓝色的 horosphere，它是超平面 $(\cdot, e_0)=\frac{1}{2}$ 与光锥的截线。$e_\infty$ 不在 horosphere 上](/images/coxeter/Horosphere.svg){width=500 .fig}

设 $\y=y_1e_1+\cdots+y_{n+1}e_{n+1}\in S^n$，$\y$ 在以 $e_{n+1}$ 为北极的球极投影下对应的点是
$$\x=\begin{cases}
\sum\limits_{i=1}^n\dfrac{y_i}{1-y_{n+1}}e_i & y_{n+1}\ne1,\\
\infty & y_{n+1}=1.
\end{cases}
$$
我们来验证 $\jmath(\y)=\imath(\x)$，即：
$$[\y + e_{n+2}] = \begin{cases}[e_0 + \x + |\x|^2e_\infty] & y_{n+1}\ne1\\
[e_\infty] & y_{n+1}=1.
\end{cases}.$$

+ $y_{n+1}=1$ 时 $\y=e_{n+1}$ 从而 $\y+e_{n+2}= e_{n+1}+e_{n+2}=2e_\infty$，显然与 $e_\infty$ 射影等价。

+ $y_{n+1}\ne 1$ 时，由 $\y\in S^n$ 可得 $\sum_{i=1}^ny_i^2=1-y_{n+1}^2$，从而
$$|\x|^2=\frac{\sum_{i=1}^n y_i^2}{(1-y_{n+1})^2}= \frac{1+y_{n+1}}{1-y_{n+1}}.$$
把 $\y+e_{n+2}$ 转化为 $\{e_0,e_1,\ldots,e_n,e_\infty\}$ 这组基下的表示：
$$\y+e_{n+2} = (1-y_{n+1})e_0+\sum_{i=1}^ny_ie_i + (1+y_{n+1})e_\infty.$$
从而
$$[\y+e_{n+2}] = \left[e_0+\sum_{i=1}^n\frac{y_i}{1-y_{n+1}}e_i +\frac{1+y_{n+1}}{1-y_{n+1}}e_\infty\right] = [e_0 + \x + |\x|^2e_\infty].$$

# 球面

记 $\S=\{v\in\LR\mid( v,v)=1\}$ 是所有 space-like 的单位向量组成的集合。我们来建立 $\R^n$ 中的球（包括超平面）和 $\S$ 之间的一一对应。

设 $B(\a,r)=\{\x\in\R^n\mid |x-\a|=|r|\}$ 是 $\R^n$ 中以 $\a$ 为中心，半径为 $r\ne 0$ 的球，它将 $\R^n$ 分成有界和无界两个连通分支。我们允许 $r$ 是负数以区分 $B$ 的内部和外部：

+ $r>0$ 时 $B$ 的内部是满足 $|\x-\a|< r$ 的有界分支；
+ $r<0$ 时 $B$ 的内部是满足 $|\x-\a|>|r|$ 的无界分支。

把 $\a$ 看作 $\span\{e_1,\ldots,e_n\}\cong\R^n$ 中的点，记
$$k = \frac{e_0 + \a + (|\a|^2 - r^2)e_\infty}{r}.$$
不难验证 $(k,k)=1$，因此 $k\in\mathcal{S}$。

对 $\x\in\R^n$，根据 $\PL$ 的 [第二种](#second-param) 参数化表示，有
$$(\imath(\x),k)=\frac{r^2-|\x-\a|^2}{2r}.$$

于是：

+ $\x\in B$ 当且仅当 $(\imath(\x),k)=0$；
+ $\x$ 落在 $B$ 的内部当且仅当 $(\imath(\x),k)>0$。

鉴于此，我们也把 $B$ 的内部叫做 $B$ 的**正半空间**，$k$ 是指向 $B$ 的正半空间的单位法向量。

注意到 $\imath(\x)$ 和 $\jmath(\x)$ 只差一个正的倍数，所以 $\x\in B$ 等价于 $(\jmath(\x),k)=0$。$V$ 中所有形如 $(\jmath(\x),k)=0\,(\x\in\R^n)$ 的点构成 $S^n_1$ 与超平面 $k^\bot$ 的截线。

设 $H(\n,d)=\{\x\in\R^n\mid (\x,\n)=d\}$ 是超平面，$\n$ 是 $B$ 的单位法向量。我们将 $H(\n,d)$ 对应到
$$k=\n + 2d e_\infty.$$
不难验证同样有 $k\in\S$，并且对 $\x\in\R^n$ 有
$$(\imath(\x),k)=(\x,\n)-d.$$
于是：

+ $\x\in B$ 当且仅当 $(\imath(\x),k)=0$；
+ $\x$ 属于 $B$ 的正半空间当且仅当 $(\imath(\x),k)>0$。

反过来，任意 $k\in\S$ 都唯一对应 $\R^n$ 中的某个球或者超平面。具体方法是将 $k$ 表示为
$$k=be_\infty+\a+ce_\infty\in\S,\quad b,c\in\R.$$
并根据 $b$ 是否等于 0 将 $k$ 对应为球 $B(\a/b ,1/b)$ 或者超平面 $H(\a, c/2)$ 即可。

# 球面的 seperation

设 $B_1(\a_1,r_1),\,B_2(\a_2,r_2)$ 是两个球，它们对应的 $\S$- 向量分别是
$$\begin{aligned}
k_1&=\frac{1}{r_1}e_0 + \frac{\a_1}{r_1} + \frac{|\a_1|^2-r_1^2}{r_1}e_\infty,\\
k_2&=\frac{1}{r_2}e_0 + \frac{\a_2}{r_2} + \frac{|\a_2|^2-r_2^2}{r_2}e_\infty.\\
\end{aligned}.$$
直接计算验证可以得到
$$(k_1,k_2)=\frac{r_1^2+r_2^2 - |\a_1-\a_2|^2}{2r_1r_2}.$$
我们称内积 $(k_1,k_2)$ 为 $B_1$ 和 $B_2$ 的 **seperation**。

:::{.note}

[见 @ratcliffe section 3.2]

在 Lorentzinian 内积下，两个 space-like 的单位向量 $k_1,k_2$ 之间的内积有如下解释：

1. 若 $|(k_1,k_2)|\leq1$，则 $(k_1,k_2)=\cos\theta$，其中 $\theta$ 是两条以 $x,y$ 为切向量的测地线之间的夹角；
2. 若 $|(k_1,k_2)|>1$，则 $(k_1,k_2)=\pm\cosh\eta$，其中 $\eta$ 是以 $x,y$ 为法向量的两个超平面之间的双曲距离。
:::

根据内积 $(k_1,k_2)$ 的大小，可以判断球体之间的位置关系：

1. 当 $|(k_1,k_2)|\leq1$ 时两球相交或者相切，这时 $(k_1,k_2)=\cos\theta$，$\theta$ 是两个球面交点处的内法向量夹角（用外法向量也可以，因为同时将内法向量变成外法向量，夹角的余弦不变）。特别地，$(k_1,k_2)=-1$ 时两球外切，$(k_1,k_2)=1$ 时两球内切。
2. 当 $|(k_1,k_2)|>1$ 时两球既不相交也不相切，这时 $|(k_1,k_2)|=\cosh\eta$，$\eta$ 是 $k_1,k_2$ 对应的双曲空间中测地线的距离。两球在 $(k_1,k_2)<-1$ 时没有公共的内部，在 $(k_1,k_2)>1$ 时一个完全包含另一个。

|   |   |
|:---:|:---:|
| $(k_1,k_2)=\cos\theta(\ell_1,\ell_2)$ |  $(k_1,k_2)=\cosh d(\ell_1,\ell_2)$  |
|![](/images/coxeter/image0.jpg){width=150} | ![](/images/coxeter/image1.jpg){width=150}  |
| $(k_1,k_2)=-\cosh d(\ell_1,\ell_2)$    | $(k_1,k_2)=-\cosh d(\ell_1,\ell_2)$|
|![](/images/coxeter/image2.jpg){width=150} | ![](/images/coxeter/image3.jpg){width=150}|

上述结论同样适用于球面和超平面的情形。例如设 $B_1$ 是球面，$B_2$ 是超平面，$k_2=\n+2de_\infty$，则
$$(k_1,k_2)=\frac{(\a_1,\n)-d}{r_1}.$$
此时：
+ 若 $B_1,B_2$ 相交，则 $(k_1,k_2)$ 等于 $B_1$ 在交点处的内法向量和 $B_2$ 的法向量 $\n$ 夹角的余弦；
+ 若不相交，则 $(k_1,k_2)$ 是 $B_1$ 的球心到 $B_2$ 的有向距离除以 $r_1$。

类似地当 $B_1,B_2$ 都是超平面时，$(k_1,k_2)=(\n_1,\n_2)$ 是它们法向量夹角的余弦。

::: {.proposition #suff-for-disjoint}
设 $B_1,B_2$ 是两个球，且 $B_1,B_2$ 的内部不相交。设 $k_1,k_2$ 分别是它们对应的 space-like 的单位向量，则 $(k_1,k_2)\leq-1$。
:::

:::{.note}
这个命题反过来是不对的。
:::

**证明**：$B_1$ 和 $B_2$ 内部不相交有如下几种可能：

1. $B_1,B_2$ 都是球，半径 $r_1,r_2$ 都大于 0，并且 $r_1+r_2 \geq |\a_1-\a_2|$。
2. $B_1,B_2$ 都是球，半径 $r_1>0,\, r_2<0$，且 $B_1$ 位于 $B_2$ 另一侧的有界区域，即 $-r_2-r_1\geq |\a_1-\a_2|$。
3. $B_1$ 是球，其半径 $r_1>0$；$B_2$ 是超平面，且 $B_1$ 位于 $B_2$ 的负半空间，从而其球心 $\a_1$ 到 $(\n,\x)=d$ 的有向距离 $\leq-r_1$，即 $(\a_1,\n)-d\leq -r_1$。
4. $B_1,B_2$ 是互相平行的超平面，且法向量相反的，即 $(\n_1,\n_2)=-1$。

不难验证这些都可以推出 $(k_1,k_2)\leq-1$。$\blacksquare$

# 球的反演

这一节读者可以参考 [@Iversen_1992, section I.7]。

:::{.definition}
关于球 $B(\a, r)$ 的反演定义为
$$\begin{aligned}
\tau\colon\ \ER&\mapsto\ER\\
\tau(\x)&=\frac{r^2}{|\x-\a|^2}(\x-\a) +\a.
\end{aligned}$$
:::
$\tau$ 是 $\ER$ 中关于球面镜 $B$ 的反射，它保持 $B$ 的表面不动，将 $B$ 的内部映射为外部（反之亦然），并且 $\tau^2=1$。

![](/images/coxeter/sphere-inversion.svg){width=400 .fig}

我们来说明 $\tau$ 可以实现为 $\PR$ 中的射影正交变换。

设 $B(\a,r)$ 对应 $k\in\S$，考察以 $k$ 为法向量的镜面反射
$$\begin{aligned}
\rho\colon\ \LR&\mapsto\LR\\
\rho(v) &= v - 2(v,k)k.
\end{aligned}$$
则 $\rho$ 是 $\LR$ 上的正交变换，从而也给出 $\PR$ 上的射影变换。

注意 $\rho$ 保持光锥的两个分支不变，即 $\rho(\Q_\pm)\subset\Q_\pm$。这是因为，如果 $v\in\Q_+$，则 $(v,v)\leq0$，并且 $(v, \rho(v)) = (v,v) - 2(v,k)^2\leq0$。若不等号严格成立，自然有 $v\sim\rho(v)$。若等号成立，则 $(v,v)=(v,k)=0$，从而 $\rho(v)=v$。

我们来计算 $\rho$ 作用在 $\imath(\x)\,(\x\in\R^n)$ 上的效果：（注意 $(\imath(\x),k)=\frac{r^2-|\x-\a|^2}{r}$）
$$\begin{aligned}
\begin{pmatrix}1\\\x\\ |\x|^2\end{pmatrix} &\xrightarrow{\rho}
\begin{pmatrix}1\\\x\\ |\x|^2\end{pmatrix} -\frac{r^2-|\x-\a|^2}{r}\begin{pmatrix}\frac{1}{r}\\\frac{\a}{r}\\ \frac{|\a|-r^2}{r}\end{pmatrix}\\
&=\begin{pmatrix}\frac{|\x-\a|^2}{r^2}\\\x+\left(\frac{|\x-\a|^2-r^2}{r^2}\right)\a\\ \ast \end{pmatrix}\\
&\stackrel{+}{\sim} \begin{pmatrix}1\\\a+\frac{r^2}{|\x-\a|^2}(\x-\a)\\ \ast \end{pmatrix}\\
&=\begin{pmatrix}1\\\tau(\x)\\ |\tau(\x)|^2 \end{pmatrix}.
\end{aligned}$$
这里我们不用关心 $\ast$ 是什么，中间的 $\stackrel{+}{\sim}$ 表示两个向量**正**射影等价。

于是我们有如下的交换图：

$$\require{amsCd}
\begin{CD}
\ER @>{\imath}>> \PL\\
@V{\tau}VV  @VV{\rho}V \\
\ER @>{\imath}>> \PL
\end{CD}$$

进一步，将任意球 $B'$ 关于 $B$ 作反演也可以通过 $\rho$ 来计算。设 $k'$ 是 $B'$ 对应的 space-like 的单位向量，则 $\rho(k')$ 也是 space-like 的单位向量，从而 $\rho(k')$ 对应某个球 $B''$。根据上面的交换图有 $\rho\imath=\imath\tau$，于是
$$\x\in B'\Leftrightarrow (\imath(\x), k')=0
\Leftrightarrow(\rho\imath(\x), \rho(k'))=0
\Leftrightarrow(\imath\tau(\x), \rho(k'))=0
\Leftrightarrow \tau(\x)\in B''.
$$
即关于 $B$ 的反演 $\tau$ 将 $B'$ 映射为 $B''$。


# 双曲球堆


:::{.definition}
如果非空集合 $\P\subset \S$ 满足对任意 $k\ne k'\in\P$ 有 $(k,k')\leq -1$，则称 $\P$ 是一个**球堆**。
:::

如果 $\P$ 形如 $\P=\{k,-k\}$，就称 $\P$ 是平凡的，因为它由一个球的内部和外部组成。否则就称 $\P$ 是非平凡球堆。$-\P=\{-k\mid k\in\P\}$ 也是球堆，它是通过翻转 $\P$ 中每个球的内部和外部得到的。

:::{.definition}
记超平面 $\{v\in V\mid (v,e_{n+2})=1\}$ 与 $\Q_+$ 的“截面”为
$$\H = \{v\in \Q_+\mid (v, e_{n+2})=1\}.$$
给定 $k\in S$，定义球帽
$$C_k = \{v\in\H\mid (v,k)\geq0\}.$$
:::

根据定义球帽总是位于同一个分支 $\Q_+$ 中，因此 $u\sim v$ 对所有 $u\in C_k,v\in C_{k'}$ 成立。

下面的引理告诉我们，如果 $v$ 严格落在 $C_k$ 的内部，则我们可以稍微“扰动” $v$，得到无限多个落在 $C_k$ 中的 time-like 的向量。

:::{.lemma #perturb}
设 $\P$ 是球堆，$k\in\P$。设 $v\in C_k$ 满足 $(v,k)=a>0$。则对任何 $0<t\leq a$，$u=v-tk$ 都满足：

1. $u$ 是 time-like 的并且 $u\sim v$；
2. $(u,k)>0$。

从而 $u$ 的某个正倍数 $u'\in C_k$。进一步，如果 $k'\ne k\in\P$ 满足 $v\in C_k\cap C_{k'}$，则同样有 $u'\in C_k\cap C_{k'}$。
:::

**证明**：直接计算可得：

$$\begin{aligned}
(u,u)&=(v,v)-2at + t^2 \leq -2at+t^2 < 0,\\
(u,v)&=(v,v)-at \leq at<0.
\end{aligned}$$
即 $u$ 是 time-like 的并且 $u\sim v$，从而 $u$ 的某个正倍数 $u'\in \H$。又因为 $(u,k)=a-t\geq0$，所以也有 $(u',k)\geq0$，从而 $u'\in C_k$。

如果存在 $k'\ne k\in\P$ 使得 $v\in C_{k'}$，则 $(v,k')\geq0$，从而
$$(u,k')=(v,k') - t(k,k')\geq t>0.$$
于是 $(u',k')\geq0$，所以 $u'$ 也属于 $C_{k'}$。$\blacksquare$

:::{.lemma #contain-time-like}
设 $\P$ 是球堆且 $k_1\ne k_2\in\P$。则以下三点等价：

1. $|C_{k_1}\cap C_{k_2}|>1$；
2. 存在 $v\in C_{k_1}\cap C_{k_2}$ 且 $v$ 是 time-like 的；
3. 存在 $v\in C_{k_1}\cap C_{k_2}$ 使得不等式 $(v,k_1)>0$ 和 $(v,k_2)>0$ 至少有一个成立。
:::

**证明**：首先由 $(k_1+k_2,k_1+k_2)=2+2(k_1,k_2)\leq0$ 可知 $k_1+k_2$ 是 time/light-like 的。

$1\Rightarrow 2$：设 $u\ne v\in C_{k_1}\cap C_{k_2}$，则 $u,v$ 不共线，从而 $(u,v)<0$。记 $z=u+v$，$z$ 是 time-like 的，并且 $z$ 的某个正倍数 $z'$ 属于 $\H$。$z'$ 即为所求。

$2\Rightarrow 3$：设 $v\in C_{k_1}\cap C_{k_2}$ 是 time-like 的，则 $(v,k_1)\geq0,\, (v,k_2)\geq0$。我们断言这两个不等式至少有一个是严格的。若不然，则 $(v,k_1+k_2)=0$。然而 $k_1+k_2$ 是 time/light-like 的，而 $v$ 是 time-like 的，这不可能。

$3\Rightarrow 1$：不妨设 $a=(v,k_1)>0$。根据 @Pre:perturb，对任何 $t\in(0,a]$ 我们都可以得到对应的 $u'\in C_k\cap C_{k'}$。不难看到不同的 $t$ 给出的 $u'$ 互不相同，于是 $|C_{k_1}\cap C_{k_2}|=\infty > 1$。
$\blacksquare$

::: {.lemma #disjoint-pair}
设 $\P$ 是球堆且 $k_1\ne k_2\in\P$，则集合 $C_{k_1}\cap C_{k_2}$ 和 $C_{-k_1}\cap C_{-k_2}$ 中必有一个至多只包含一个点。并且当这两个集合中的某个恰好只含一个点时，此点与 $k_1+k_2$ 共线，并且有 $(k_1,k_2)=-1$ 成立。
:::

**证明**：
若 $C_{k_1}\cap C_{k_2}$ 和 $C_{-k_1}\cap C_{-k_2}$ 均不为空，取 $u\in C_{k_1}\cap C_{k_2}$，$v\in C_{-k_1}\cap C_{-k_2}$，则
$$(u, k_1+k_2)\geq0,\quad (v,k_1+k_2)\leq0.$$
如果上面两个不等号都是严格成立的，则 $u\not\sim k_1+k_2$ 但是 $v\sim k_1+k_2$，这与 $u\sim v$ 矛盾。所以至少有一个等号是成立的，即 $u,v$ 之中必有一个与 $k_1+k_2$ 共线，并且 $k_1+k_2$ 是 light-like 的向量。由此可得 $(k_1,k_2)=-1$ 并且 $|C_{k_1}\cap C_{k_2}|\leq1$ 和 $|C_{-k_1}\cap C_{-k_2}|\leq1$ 中至少有一个成立。

如果这两个集合，不妨设为 $C_{k_1}\cap C_{k_2}$，恰好只有一个点。记这个点为 $u$。如果 $u$ 与 $k_1+k_2$ 不共线的话，则必有 $(u,k_1+k_2)>0$，从而 $(u,k_1)$ 和 $(u,k_2)$ 中至少有一个大于 0。根据 @Pre:contain-time-like 有 $|C_k\cap C_{k'}|=\infty$，矛盾。所以 $u$ 必然与 $k_1+k_2$ 共线。$\blacksquare$


::: {.theorem #thm-sphere-packing}
设 $\P$ 是非空集合，则下面两点是等价的：

1. $\P$ 是一个非平凡的球堆。
2. 对 $\P$ 或者 $-\P$ 之一，其包含的任何两个球帽 $C_k$ 和 $C_{k'}$ 至多有一个公共点。
:::
**证明**：

1 $\Rightarrow$ 2：根据 @Pre:disjoint-pair，不妨设 $k_1,k_2\in\P$ 使得 $|C_{k_1}\cap C_{k_2}|\leq1$，我们要证明对任何 $k\ne k'\in\P$ 同样有 $|C_k\cap C_{k'}|\leq1$。如果 $\{k,k'\}=\{k_1,k_2\}$ 结论显然成立，所以不妨设 $k\notin\{k_1,k_2\}$。用反证法，若 $|C_k\cap C_{k'}|>1$，根据 @Pre:contain-time-like，存在 time-like 的向量 $v\in C_k\cap C_{k'}$。令 $w=k_1-(k_1,k_2)k_2$，则有
$$(w,w)=1-(k_1,k_2)^2\leq0,\quad (w, k)<0,\quad (w, k')\leq0.$$
我们来证明 $v\sim w$。若如此，则 $w$ 的某个正倍数 $w'\in\H$，并且
$$(w',-k)>0,\quad (w',-k')\geq0.$$
从而由 @Pre:contain-time-like 有 $|C_{-k}\cap C_{-k'}|>1$，与 @Pre:disjoint-pair 矛盾。由于 $v$ 是 time-like 的，我们只要证明有 $(v,w)\leq0$ 成立即可。利用
$$(v,w)=(v, k_1) - (v,k_2)(k_1,k_2) = (v-(v,k_2)k_2, k_1).$$
并记 $u=v-(v, k_2)k_2$，问题转化为证明 $(u,k_1)\leq0$。计算可得
$$\begin{aligned}
(u,k_2) &= (v,k_2) - (v,k_2)(k_2,k_2)=0,\\
(u,u)&=(u,v)-(v,k_2)(u,k_2) = (u,v),\\
(u,v)&=(v,v)-(v,k_2)^2 \leq (v,v)<0.
\end{aligned}
$$
即 $u$ 是 time-like 的且 $u\sim v$。于是 $u$ 的某个正倍数 $u'$ 属于 $\H$。如果 $(u,k_1)>0$ 的话则 $u'$ 是 time-like 的向量且满足 $(u',k_1)>0$ 和 $(u',k_2)=0$，从而 $u'\in C_{k_1}\cap C_{k_2}$。但根据 @Pre:contain-time-like 这会导致 $|C_{k_1}\cap C_{k_2}|>1$，矛盾。因此 $(u,k_1)\leq0$。

2 $\Rightarrow$ 1: 不妨设 $\P$ 中任何两个球帽至多只有一个交点。对 $k_1\ne k_2\in\P$，$U=\span\{k_1,k_2\}$ 肯定不是 space-like 的，否则 $U^\bot=k_1^\bot\cap k_2^\bot$ 是 time-like 的，则存在 time-like 的向量 $v$ 满足 $(v,k_1)=(v,k_2)=0$。给 $v$ 乘以适当实数后可以使得 $v\in\H$，从而 $v\in C_{k_1}\cap C_{k_2}$，这与 @Pre:contain-time-like 矛盾。所以 $U$ 不是 space-like 的，即 $|(k_1,k_2)|\geq1$。如果 $(k_1,k_2)\geq1$，则 $C_{k_1}\cap C_{-k_2}$ 和 $C_{-k_1}\cap C_{k_2}$ 中必有一个至多只包含一个点，不妨设 $|C_{k_1}\cap C_{-k_2}|\leq1$。但是根据已知 $C_{k_1}\cap C_{k_2}$ 也至多只包含一个点，从而 $C_{k_1}$ 作为二者的并至多只有一个点，矛盾。所以只能是 $(k_1,k_2)\leq-1$，从而 $\P$ 是球堆。
$\blacksquare$


:::{.definition}
记 $\Omega_r=\{\omega\in\Omega\mid (\omega,\omega)>0\}$ 是所有实权组成的集合，$\tc_r=\cone{\Omega_r}$ 是由所有实权生成的凸锥。
:::

::: {.theorem #real-cone-closure}
如果 $W$ 是不可约、双曲的，且 level 大于等于 2，则 $\tcr = \cl{\tc}$。
:::

**证明**：只要证明 $\tcr$ 包含那些非实的基本权 $(\omega_s, \omega_s)\leq 0$ 即可。若如此，则 $\tcr$ 包含全部基本权 $\Delta^\ast$，从而也包含 $\cone{\Delta^\ast}=\barfd$，再结合 $\tcr$ 是 $W$- 不变的，即得 $\tcr$ 包含 $\bigcup\limits_{w\in W}w\barfd=\tc$，从而包含 $\cl{\tc}$。

设 $\omega_s$ 是任一非实的基本权，记 $I=S-\{s\}$，$W_I$ 为标准椭圆子群。分情况讨论：

$\color{blue}(\omega_s,\omega_s)<0$

这时 $\omega_s$ 是 time-like 的，其正交补 $V_I=\span\{\alpha_t\mid t\ne s\}$ 是 space-like 的，从而 $W_I$ 是有限群。任取一个实的基本权 $(\omega_t,\omega_t)>0\,(t\in I)$ 并考虑
$$v = \sum_{w\in W_I}w(\omega_t).$$
显然 $v\in\tcr$，并且 $W_I$ 保持 $v$ 不动。特别地对任何 $t\in I$ 都有 $t(v)=v$。这是 $n-1$ 个独立的线性约束，其解空间是一维的，所以 $v$ 和 $\omega_s$ 共线：存在 $a\in\R$ 使得 $v=a\omega_s$。两边同时与 $\alpha_s$ 作内积得到
$$a = (\alpha_s,v)=\sum_{w\in W_I}(\alpha_s,w(\omega_t))=\sum_{w\in W_I}(w^{-1}(\alpha_s), \omega_t)=\sum_{w\in W_I}(w(\alpha_s), \omega_t).$$
对任何 $w\in W_I$，$w\alpha_s=\alpha_s+\sum_{i\in I}c_i\alpha_i$ 仍然是正根，所有的系数 $c_i$ 都非负。所以上式右边的每一项
$$(w(\alpha_s), \omega_t)=\sum_{i\in I}c_i(\alpha_i, w_t) = c_t\geq0.$$
我们来选择一个特殊的 $w\in W_I$ 使得 $c_t>0$：由于 $\Gamma$ 是连通的，所以 $\Gamma$ 中存在一条从 $s$ 到 $t$ 的路径 $s\sim s_1\sim\cdots\sim s_m=t$，其中每个 $s_i\,(i\geq1)\in I$  且互不相同。不难验证对 $w=s_m\cdots s_1\in W_I$，$w\alpha_s$ 的系数 $c_t>0$，所以 $a$ 严格大于 0，从而 $\omega_s=v/a\in\tcr$。

$\color{blue}(\omega_s, \omega_s)=0$

这个情形要麻烦一些。这时 $\omega_s$ 的正交补 $\omega_s^\bot$ 是 light-like 的，即子图 $\Gamma\setminus\{s\}$ 是仿射的。所以 $\Gamma\setminus\{s\}$ 由一些仿射或者有限的连通成分组成，由于内积是双曲的，这些连通成分中有且恰有一个是仿射的。任取一个实的基本权 $(\omega_t,\omega_t)>0\,(t\in I)$，分两种情况：

1. 如果 $\omega_t$ 属于某个有限型的连通成分 $Y$，类似上面的讨论，$v$ 是 $\omega_s$ 的某个正倍数，从而 $\omega_s\in\tcr$。

2. 如果 $\omega_t$ 属于某个仿射型的连通成分 $X$，记 $\Gamma_1=X\cup \{s\}$，$Y=\Gamma\setminus\Gamma_1$，则 $Y$ 是有限型，并且 $X$ 和 $Y$ 互不连通（它们必然通过 $s$ 连在一起），从而
$$\omega_s = \underbrace{(\omega_s, \omega_s)}_{=0}\alpha_s + \sum_{t\ne s} (\omega_s, \omega_t)\alpha_t=\sum_{t\in X} (\omega_s,\omega_t)\alpha_t + \sum_{t\in Y} (\omega_s,\omega_t)\alpha_t=v_1+v_2.$$
这里 $v_1$ 和 $v_2$ 是正交的。于是
$$(\omega_s, \omega_s)=0\Rightarrow (v_1+v_2,v_1+v_2)=0\Rightarrow (v_1,v_1) + (v_2,v_2) = 0.$$
由于 $V_X$ 是不可约仿射的，$V_Y$ 是有限的，所以 $v_2=0$，并且 $\R v_1=\rad(V_X)$。从而 $\omega_s=v_1$，并且 $\R \omega_s=\rad(V_X)$。$\omega_s$ 表示为 $\{\alpha_i\mid i\in X\}$ 的线性组合时，所有的系数 $(\omega_s,\omega_i)$ 系数都是非零且同号的。我们断言它们都小于 0。实际上在
$$\omega_s=\sum_{i\in X} (\omega_s,\omega_i)\alpha_i$$
两边同时用 $\alpha_s$ 作内积有
$$1=\sum_{i\in X} (\omega_s, \omega_i)\underbrace{(\alpha_s,\alpha_i)}_{\leq0}.$$
所以必须所有 $(\omega_s, \omega_i)<0$。\
于是 $\Gamma_1$ 满足 [这个结论](/coxeter-groups/level/#ideal-vertex) 的条件（取 $I=X,\,p=\omega_t,\,\omega_s=\omega_s$ 代入），从而我们得到
$$\omega_s\in\cl{\cone{\bigcup_{w\in W_X}w(\omega_t)}}\subset\tcr.$$
$\blacksquare$

:::{.definition}
规定 $\hat{\Omega}_r=\{\hat{\omega}\mid \omega\in\Omega_r\}$，其中 $\hat{\omega}=\omega/\sqrt{(\omega,\omega)}$ 是将 $\omega$ 归一化得到的单位向量。
:::

::: {.theorem #max-packing}
若 $W$ 是双曲的，则 $\hat{\Omega}_r$ 是非平凡的球堆当且仅当 $\Gamma$ 的 level 是 2，这时 $\hat{\Omega}_r$ 还是极大球堆。
:::

**证明**：若 $\Gamma$ 的 level 是 2，则 [$\Omega_r$ 中的元素两两分离](/coxeter-groups/level#level-12)，将其归一化后得到的 $\hat{\Omega}_r$ 仍然两两分离，所以 $\hat{\Omega}_r$ 的元素两两之间的内积 $\leq -1$，从而 $\hat{\Omega}_r$ 给出一个球堆。由于基本权是线性无关的，$\hat{\Omega}_r$ 显然是非平凡的球堆。如果存在某个 space-like 的向量 $k$ 满足 $(k,k)=1$ 且 $k$ 对应的 $C_k$ 与 $\hat{\Omega}_r$ 中的任何球都没有公共内部的话，则有 $(k,\hat{\omega})\leq -1$ 对任何 $\hat{\omega}\in\hat{\Omega}_r$ 成立，自然就有 $(k,\omega)<0$ 对任何 $\omega\in\Omega_r$ 成立，从而 $(k,y)\leq0$ 对任何 $y\in\tcr=\cone{\Omega_r}$ 成立。根据 @Pre:real-cone-closure，$\tcr=\cl{\tc}$，这意味着 $(k,y)\leq0$ 对任何 $y\in\tc$ 成立，即 $-k\in\tc^\ast$。由于 [对偶锥 $\tc^\ast$ 中的向量范数 $\leq0$](/coxeter-groups/tits-cone/#dual-cone-nonspace)，$(k,k)=(-k,-k)\leq0$，这与 $(k,k)=1$ 矛盾。这就证明了 level 2 时 $\Omega_r$ 是极大球堆。

反之若 $\hat{\Omega}_r$ 是一个非平凡球堆，则 $W$ 的 level 必然大于 1，且所有的实权之间两两分离。于是任何两个基本权生成的二维子空间 $\span\{\omega_i,\omega_j\}$ 都是 time-like 或者 light-like 的。又由于 $W$ 是双曲的，从而 $\Gamma\setminus\{i,j\}$ 是 space-like 或者 light-like 的，所以 $\Gamma$ 的 level 只能是 2。$\blacksquare$


# 计算例子


本节我们来介绍怎样用程序实际绘制一个二维的 Boyd-Maxwell 球堆。

以 $K_4$ 完全图为例，每条边的标号是 4：

![](/images/coxeter/K4.svg){.fig width=150 #K4}

这个群的 rank 是 4，level 是 2，所以给出的是 $\R^2$ 上的二维极大球堆。

单根系 $\Delta=\{\alpha_i\}_{i=1}^4$ 满足 $(\alpha_i,\alpha_i)=1$，它们对应 4 个虚球。前面已经介绍了，以 $\alpha_i$ 为法向量的单反射 $s_i$ 对应关于 $B_i$ 的反演变换，它们生成了 $(W,S)$。

由于删掉 $K_4$ 的任何顶点后，剩下的是双曲三角群 $\Delta(4,4,4)$，所以基本权 $\Delta^\ast = \{\omega_i\}_{i=1}^4$ 都是实的。归一化以后 $\{\hat{\omega}_i\}_{i=1}^4$ 给出 4 个互相分离的实球。由于 $i\ne j$ 时 $(\alpha_i,\omega_j)=0$，所以 $\alpha_i$ 和 $\hat{\omega}_j$ 正交。又因为 $(\alpha_i,\omega_i)=1$，以及 $\omega_i$ 满足 $0<(\omega_i,\omega_i)\leq1$，所以归一化以后 $(\alpha_i,\hat{\omega}_i)\geq1$，即球 $\alpha_i$ 和 $\hat{\omega}_i$ 有包含关系。我们要求对每个 $i$，实球 $\hat{\omega}_i$ 包含在虚球 $\alpha_i$ 的内部（即正半空间）。这是因为在计算时，我们要反复将平面上的点关于 $\{\alpha_i\}$ 作反演，直到它落入基本区域 $\barfd$ 为止，然后判断这个最终位置属于哪个实球。所以我们一定要让虚球 $\alpha_i$ 包含实球 $\hat{\omega_i}$。

将 $W$ 作用在实球 $\{C_i\}$ 上，得到的所有球即为所要绘制的球堆 $\P=\bigcup_{w\in W,\,1\leq i\leq 4}w(\hat{\omega}_i)$。

我们按照如下步骤来分别计算 $\{\alpha_i\}$ 和 $\{\hat{\omega}_j\}$：

1. 第一个实球 $\hat{\omega}_1$ 总是可以取为单位球 $B(\mathbf{0},1)$。**并且 $\hat{\omega}_1$ 是无界球**。由于实球之间互不相交，所以 $\hat{\omega}_2,\hat{\omega}_3,\hat{\omega}_4$ 都落在单位球内。
2. 两个虚球 $\alpha_3,\alpha_4$ 可以取为过原点的两条直线，法向量分别为
$$\begin{aligned}
\n_3&=(1, 0),\\
\n_4&=(-\cos\frac{\pi}{m_{3,4}},\sin\frac{\pi}{m_{3,4}})=(-\cos\frac{\pi}{4},\sin\frac{\pi}{4}).
\end{aligned}$$
3. 第二个虚球 **$\alpha_2=B(\a_2,r_2)$ 是一个无界球**，即 $r_2<0$。我们可以认为 $r_2>0$，但是在列方程时将 $B$ 与其它球的内积取负：
    + 由 $\alpha_2$ 与 $\hat{\omega}_1$ 正交可得 $|\a_2|^2=r_2^2+1$；
    + 计算 $\alpha_2$ 与 $\alpha_3,\alpha_4$ 的夹角可得（注意 $\cos$ 前面没有负号了）
    $$\begin{aligned}
    \frac{(\a_2,\n_3)}{r_2}&=\cos\frac{\pi}{m_{23}}=\cos\frac{\pi}{4},\\
    \frac{(\a_2,\n_4)}{r_2}&=\cos\frac{\pi}{m_{24}}=\cos\frac{\pi}{4}.
    \end{aligned}$$

   由这三个方程可以解出 $\a_2$ 和 $r_2$。
4. 第一个虚球 **$\alpha_1=B(\a_1,r_1)$ 也是一个无界球**，即 $r_1<0$。我们同样认为 $r_1>0$，并在列方程时将它与其它球的内积取负：
   + 计算 $\alpha_1$ 与 $\alpha_3,\alpha_4$ 夹角可得
   $$\begin{aligned}
    \frac{(\a_1,\n_3)}{r_1}&=\cos\frac{\pi}{m_{13}}=\cos\frac{\pi}{4},\\
    \frac{(\a_1,\n_4)}{r_1}&=\cos\frac{\pi}{m_{14}}=\cos\frac{\pi}{4}.
    \end{aligned}$$
   + 计算 $\alpha_1$ 与 $\alpha_2$ 夹角可得
   $$\frac{r_1^2+r_2^2-|\a_1-\a_2|^2}{2r_1r_2}=-\cos\frac{\pi}{m_{12}}=-\cos\frac{\pi}{4}.$$
   注意由于 $\alpha_1,\alpha_2$ 都是无界球，所以负号又回来了。

   由这三个方程可以得到一个二次方程，解出的 $r_1$ 有两个值，我们取较小的那一个。（原因在后面解释）
5. 我们还剩下三个实球 $\hat{\omega}_2,\hat{\omega}_3,\hat{\omega}_4$ 需要解出。$\hat{\omega}_2$ 需要和 $\alpha_3,\alpha_4$ 正交，所以它是一个以原点为中心的球，而它又要和 $\alpha_1$ 正交，所以 $\hat{\omega}_2$ 的半径为 $\sqrt{|\a_1|^2-r_1^2}$。
6. $\hat{\omega}_3$ 与 $\alpha_1,\alpha_2,\alpha_4$ 正交，这可以得到三个方程。联立解出 $\hat{\omega}_3$。
7. $\hat{\omega}_4$ 与 $\alpha_1,\alpha_2,\alpha_3$ 正交，也可以得到三个方程，联立解出 $\hat{\omega}_4$。

结果如下图所示，单根 $\alpha_i$ 对应的虚球用虚线绘制，$\hat{\omega}_i$ 对应的实球用实线绘制，同样的 $i$ 使用同样的颜色。上标 $\ast$ 表示该球以无界区域为内部。所以我们有三个无界的球 $\alpha_1,\alpha_2,\omega_1$。

![](/images/coxeter/compute_example_K4.svg){width=500 .fig}

注意到关于 $\hat{\omega}_1$ 的反演保持虚球 $\alpha_2,\alpha_3,\alpha_4$ 不变，因为它们都与 $\hat{\omega}_1$ 正交；同时将 $\alpha_1$ 变成另一个关于 $\hat{\omega}_1$ 对称的球 $\gamma_1$。反演变换是保角的，所以 $\{\gamma_1,\alpha_2,\alpha_3,\alpha_4\}$ 也是一组夹角符合要求的镜面球，但是包含关系发生了改变，变成了 $\gamma_1$ 包含在 $\hat{\omega}_1$ 的内部。这是错误的。这就是为什么前面求解 $\alpha_1$ 的半径时我们要取那个较小的解（这两个解给出的球心形如 $r_1\x$ 和 $r_2\x\,(\x\in\R^2)$，所以半径较小者一定在单位球内部）。

我们再举一个只有一个实权的例子：

![](/images/coxeter/337.svg){.fig width=250 #337}

这个群只有第一个顶点是实的，所以整个球堆完全由一个实球 $\hat{\omega}_1$ 生成：

![](/images/coxeter/compute_example_337.svg){width=500 .fig}

具体的计算步骤可以参考 shadertoy 动画代码中的注释：

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/WdGBz3?gui=true&t=0&paused=true&muted=false" allowfullscreen></iframe>

可以看到，每个实球都呈现一个二维的 Poincaré 密铺图案。这很好理解，因为如果 $\omega_i$ 是实权，记 $I=S\setminus\{i\}$，则实球 $\hat{\omega}_i$ 与虚球 $\{\alpha_j\mid j\in I \}$ 都正交，这些虚球在 $\hat{\omega}_1$ 中围成一个测地三角形，关于这个三角形三条边的反射生成的群是标准椭圆子群 $W_I$。$W_I$ 保持 $\hat{\omega}_i$ 不动，同时将测地三角形映射为 $\hat{\omega}_i$ 中的双曲密铺。在前面 [$K_4$ 的例子](#K4) 中，有 4 个初始实球，它们每一个都呈现 $\Delta(4,4,4)$ 的双曲密铺；在 [${\rm\color{red}o\color{red}}-{\rm o}-{\rm o}\overset{7}{-}{\rm o}$ 的例子](#337) 中，只有一个初始实球，它呈现 $\Delta(2,3,7)$ 的双曲密铺。