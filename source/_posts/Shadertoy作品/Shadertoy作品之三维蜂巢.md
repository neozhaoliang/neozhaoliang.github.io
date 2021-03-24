---
title: "Shadertoy 作品：三维欧式蜂巢、双曲蜂巢和 Coxeter 群的几何实现"
date: 2020-12-22
categories: [Shadertoy 作品]
tags:
  - Shadertoy
  - Poincaré unit ball
  - Hyperbolic geometry
  - Euclidean geometry
  - Coxeter group
  - Uniform honeycombs
  - Reflection groups
  - Tits cone
  - Standard geometric realization
url: "shadertoy-uniform-honeycombs"
---

本文介绍我最近完成的两个 Shadertoy 小项目，它们的目的是演示怎样用一种统一的方式从 [Coxeter diagram](https://en.wikipedia.org/wiki/Coxeter%E2%80%93Dynkin_diagram) 出发构造三维欧式空间 $E^3$ 和三维双曲空间 $H^3$ 中的均匀密铺，即所谓的[蜂巢结构](https://en.wikipedia.org/wiki/Honeycomb_(geometry))。我写这两个项目的目的是为了帮助自己更好的理解 Coxeter 群的标准几何实现，尤其是其中涉及的 Tits 锥的概念。球面蜂巢 $S^3$ 的情形因为之前使用 Python + POV-Ray 实现过了，所以这里就没有再重复。由于个人水平和精力所限，我没有在场景美观上下太多功夫，也没有处理 dual 和 snub 的情形，主要目的还是展示背后的数学。

<!-- more -->

{% blockquote %}
在这两个动画中，你可以用鼠标调整视角，也可以点击窗口左上角的标题前往 Shadertoy 网页查看源代码。
{% endblockquote %}

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/3sVBWV?gui=true&t=10&paused=true&muted=false" allowfullscreen>
</iframe>

默认绘制的蜂巢是正则 (5, 3, 5)，如果要查看其它不同的蜂巢需要修改代码中 `diagram` 和 `active_mirrors` 的值。[维基百科](https://en.wikipedia.org/wiki/Uniform_honeycombs_in_hyperbolic_space)上列出了所有可能的双曲蜂巢。由于超采样导致帧率比较卡，主要是为了效果好看。默认的超采样指数 `AA=3`，即每个像素采样 9 次。

这个项目可以绘制紧 (compact) 和仿紧 (paracompact) 类型的蜂巢，以下是一些效果图：

|||
|:---:|:---:|
|regular (4, 3, 5)|regular (4, 4, 4)|
|<img src="/images/honeycomb/435.png" width=300>|<img src="/images/honeycomb/444.png" width=300>|
|omnitruncated (3, 6, 3)|rectifid (3, 5, 3)|
|<img src="/images/honeycomb/363.png" width=300>|<img src="/images/honeycomb/353.png" width=300>|

第二个项目展示的是欧式空间 $E^3$ 中的均匀蜂巢：

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/3tccWf?gui=true&t=10&paused=true&muted=false" allowfullscreen>
</iframe>

$E^3$ 中的均匀蜂巢只有三种不同的对称性，它们分别对应仿射 Coxeter 群 $\widetilde{A}_3,\widetilde{B}_3,\widetilde{C}_3$。同样你可以点击窗口左上角的标题进入 Shadertoy 网页，修改 `diagram` 和 `active_mirrors` 的值来查看不同的蜂巢结构。
 
以下是一些效果图：

|||
|:---:|:---:|
|regular $\widetilde{A}_3$|regular $\widetilde{B}_3$|
|<img src="/images/honeycomb/333.png" width=300>|<img src="/images/honeycomb/343.png" width=300>|
|regular $\widetilde{C}_3$|truncated $\widetilde{C}_3$|
|<img src="/images/honeycomb/434.png" width=300>|<img src="/images/honeycomb/434-1100.png" width=300>|


这两个动画虽然绘制的都是三维的场景，但是绝大部分计算都是在四维空间中进行的，这是因为在四维空间中这些蜂巢的对称性可以统一用反射变换来描述，过程非常简单，而在三维空间中还需要针对不同的几何额外处理反演和平移，过程比较繁琐。

“在四维空间中计算三维的场景”听起来比较玄妙，我来解释下：

注意到三维蜂巢的对称群 $W$ 是 rank 为 4 的 Coxeter 群，它可以看作是 $\mathbb{R}^3$ 中的反射群，即在 $\mathbb{R}^4$ 中摆放一些过原点的反射平面，平面之间的夹角是精心选择的，从而 $W$ 可以由关于这些平面的反射生成。这些平面的正半空间之交是一个闭的凸锥形区域 $C$，$C$ 叫做基本区域，$C$ 以及它在 $W$ 作用下的所有镜像之并仍然是一个闭的凸锥 $\mathcal{C}$，$\mathcal{C}$ 叫做 Tits 锥。根据 $W$ 不同，以及各个反射镜面摆放方式的不同，$\mathcal{C}$ 的形状也不同。但是在标准几何实现中，$\mathcal{C}$ 的形状是容易确定的：

1. 在球面蜂巢的情形，$\mathcal{C}$ 是全空间 $\mathbb{R}^4$，这时 $W$ 是有限 Coxeter 群。

2. 在欧式蜂巢的情形，$\mathcal{C}$ 是半空间
$$\{ w > 0 \,|\, (x,y,z,w)\in\mathbb{R}^4\}.$$
这时 $W$ 是仿射 Coxeter 群，是无限群。

3. 在双曲蜂巢的情形，$\mathcal{C}$ 是 Minkowski 度量下的光锥
$$\{x^2+y^2+z^2-w^2 < 0 \,|\, (x,y,z,w)\in\mathbb{R}^4\}.$$
这时 $W$ 是双曲 Coxeter 群，也是无限的。

这三种情形对应的三维蜂巢图案可以通过用一个三维的超曲面 $S$ 截 $\mathcal{C}$ 得到，当然我们没法真的在四维空间中画曲面，所以下面的插图都用三维的情形来代替，但是原理是一样的：

1. 球面蜂巢的情形 $S$ 是单位球面 $x^2+y^2+z^2=1$。
    
    <img style="margin:0px auto;display:block" width=350 src="/images/honeycomb/Tits_spherical.png"/>

    图中红色的部分 (其实是一个无穷长的三棱锥) 为基本区域 $C$，它在 $W$ 的作用下其 Tits 锥 $\mathcal{C}=\cup_{w\in W} wC$ 会填满整个 $\mathbb{R}^3$，用球面去截得到的是二维球面密铺。

2. 欧式蜂巢的情形 $S$ 是平面 $z=1$。

    <img style="margin:0px auto;display:block" width=350 src="/images/honeycomb/Tits_euclidean.png"/>

    同样红色的部分 (也是一个无穷长的三棱锥) 为基本区域 $C$，它在 $W$ 的作用下其 Tits 锥 $\mathcal{C}=\cup_{w\in W} wC$ 会填满整个上半空间 $z>0$，用平面 $z=1$ 去截得到的是二维欧式密铺。

3. 双曲蜂巢的情形 $S$ 是双曲面 $x^2+y^2-z^2=-1$。

    <img style="margin:0px auto;display:block" width=350 src="/images/honeycomb/Tits_hyperbolic.png"/>

    同样红色的部分 (无穷长的三棱锥) 为基本区域 $C$，它在 $W$ 的作用下其 Tits 锥 $\mathcal{C}=\cup_{w\in W} wC$ 会填满光锥 $x^2+y^2-z^2<0$，用双曲面 $x^2+y^2-z^2=-1$ 去截得到的是二维双曲密铺。

总之通过绘制 Tits 锥在 $S$ 上的横截面我们就得了相应的蜂巢图案，这一方法对其它维数的密铺都是成立的。

但是我们为什么要选择球面、平面、双曲面来截断 Tits 锥呢？这是因为对称群 $W$ 会分别保持这个三个超曲面不变，即将 $S$ 上的点仍然映射为 $S$ 上的点。特别在球面和双曲的情形，$W$ 是 Euclidean 和 Minkowski 度量下的正交变换群。

于是球面、欧式、双曲三种类型的蜂巢可以用统一的方式来处理，它分为两步：

1. 对给定的 Coxeter diagram，首先确定其对应的几何类型 (球面/欧式/双曲)，然后确定反射镜面以及对应的反射变换。

2. 在用 raymarching 方法渲染场景时，对三维空间中一点 $p$，我们首先将 $p$ 提升为超曲面 $S$ 上的点 $q$，并将 $q$ 关于各个镜面反复进行反射变换，直到 $q$ 落入基本区域内 (这些反射操作都封装在一个函数 `fold` 里面)，然后在四维空间中估计 $q$ 到基本区域的各元素 (顶点/边/面) 的距离，由此来判断 $p$ 是顶点、边、面或者都不是，再进行对应的渲染。

所以问题的关键就在于应该怎样摆放反射平面的位置，并写出对应的反射变换的表达式。这就要用到 Coxeter 群的标准几何实现。


# Coxeter 群的标准几何实现

设 $(W, S)$ 是一个 Coxeter 群，生成元集合 $S$ 满足对任何 $s,t\in S$ 有 $s^2=t^2=(st)^{m_{s,t}}=1$，其中 $m_{s,t}\in\{1,2,\ldots,\infty\}$ 是正整数或者 $\infty$。记 $|S|=n$，$V = \mathbb{R}^n$，取对偶空间 $V^\ast$ 的一组基 $\Delta=\{\alpha_s \,|\, s\in S\}$，则我们总可以找到 $V$ 中的一组向量 $\Delta^\vee=\{\alpha_s^\vee \,|\, s\in S\}$ 使得对任何 $s,t\in S$ 有 $$c_{s,t} = (\alpha_s, \alpha_t^\vee) = -2\cos\frac{\pi}{m_{s,t}}.$$

注意 $\Delta$ 是对偶空间 $V^\ast$ 的一组基，而 $\Delta^\vee$ 未必构成 $V$ 的一组基 (比如在仿射 Coxeter 群的情形)。

矩阵 $C=(c_{s,t})$ 叫做 Cartan 矩阵，这是一个对称矩阵，它的惯性指数决定了对应蜂巢的类型：

1. 球面蜂巢对应 $C$ 正定，即 $C$ 的惯性指数为 $(n,0)$。
2. 欧式蜂巢对应 $C$ 半正定且秩为 $n-1$，即 $C$ 的惯性指数为 $(n-1,0)$。
3. 双曲蜂巢对应 $C$ 的惯性指数为 $(n-1,1)$。

对任何 $s\in S$，定义 $V$ 上的线性变换 $\sigma_s$ 为
$$\sigma_s(v) = v - (\alpha_s, v)\alpha_s^\vee,\quad v\in V.$$

容易验证 $\sigma_s^2=1$，且 $\sigma_s$ 保持超平面 $H_s=\{v\in V \,|\, \alpha_s(v)=0\}$ 不变，并且由于 $(\alpha_s,\alpha_s^\vee) = 2$ 所以 $\sigma_s$ 把 $\alpha_s^\vee$ 变为 $-\alpha_s^\vee$，从而 $\sigma_s$ 是一个关于超平面 $H_s$ 的反射。不难验证 $(\sigma_s\sigma_t)^{m_{s,t}}=1$，所以 $s\to\sigma_s$ 给出了 $G\to\mathrm{GL}_n(V)$ 的一个表示，这个表示叫做 $G$ 的标准几何实现。

总之只要确定了 $\{\alpha_s\}$ 和 $\{\alpha_s^\vee\}$，就可以得出所有反射 $\{\sigma_s\}$ 的表达式。

我们分别用一个欧式蜂巢和一个双曲蜂巢为例子来说明这个步骤，首先是欧式蜂巢 $(4, 3, 4)$，它对应的 Coxeter diagram 如下：

<img style="margin:0px auto;display:block" width="350" src="/images/honeycomb/434.svg">

它包含四个反射，其对应的 Cartan 矩阵为
$$(c_{ij}) = \begin{pmatrix}
1 & -\cos\frac{\pi}{4} & 0 &; 0\\
-\cos\frac{\pi}{4} & 1 & -\cos\frac{\pi}{3} & 0\\
0 & -\cos\frac{\pi}{3} & 1 & -\cos\frac{\pi}{4}\\
0 & 0 & -\cos\frac{\pi}{4} &  1\\
\end{pmatrix}.
$$

我们可以先取四个单位向量
$$\begin{align*}
\alpha_1^\vee &= (1, 0, 0, 0),\\
\alpha_2^\vee &= (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0, 0),\\
\alpha_3^\vee &= (0, -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0),\\
\alpha_4^\vee &= (0, 0, -1, 0).
\end{align*}$$

这四个向量满足 $\langle\alpha_i^\vee, \alpha_j^\vee\rangle = c_{ij}$，但它们不是线性无关的 (最后一个分量都是 0)，所以你不能直接把这四个向量当作反射平面的法向量，否则实际上只会有三个平面起效果，得到的蜂巢将是退化的。但是我们可以把最后一个镜面稍加修改得到满足要求的一组反射：由于前三个向量 $\alpha_1^\vee, \alpha_2^\vee,\alpha_3^\vee$ 是线性无关的，所以我们可以直接取它们为对应的线性泛函，即令线性泛函
$$\alpha_i(v) = \langle\alpha_i^\vee, v\rangle,\quad i=1,2,3.$$

其中 $\langle\cdot\rangle$ 是普通的欧式内积。而取 $\alpha_4$ 为将 $\alpha_4^\vee$ 的最后一个分量改为 1 得到的线性泛函，即由向量 $\beta=(0, 0, -1, 1)$ 确定的线性泛函：
$$\alpha_4(v)=\langle\beta, v\rangle = -v_3+v_4.$$

不难验证 $\alpha_i(\alpha_j^\vee)=c_{ij}$ 对任何 $i,j$ 仍然成立，这就给出了所有反射的表达式。这时基本区域 $C$ 是所有半空间 $\{v \,|\, \alpha_i(v)>0\}$ 的交。

{% blockquote %}
你可以把 $\alpha_4^\vee$ 的最后一个分量修改为任何非 0 值，这只会影响基本区域的大小。
{% endblockquote %}

---

再举一个双曲蜂巢 $(5, 3, 5)$ 的例子，其 Coxeter diagram 为

<img style="margin:0px auto;display:block" width="350" src="/images/honeycomb/535.svg"></p>

对应的 Cartan 矩阵为
$$(c_{ij}) = 
\begin{pmatrix}
1 & -\cos\frac{\pi}{5} & 0 & 0\\
-\cos\frac{\pi}{5} & 1 & -\cos\frac{\pi}{3} & 0\\
0 & -\cos\frac{\pi}{3} & 1 & -\cos\frac{\pi}{5}\\
0 & 0 & -\cos\frac{\pi}{5} &  1\\
\end{pmatrix}.$$

这时 Cantan 矩阵的惯性指数为 $(3, 1)$，从而合同于对角矩阵 $\mathrm{diag}(1,1,1,-1)$，即存在可逆矩阵 $A$ 使得
$$C = A^T\begin{pmatrix}1&&&\\&1&&\\&&1&\\&&&-1\end{pmatrix}A.$$

记 $A$ 的列向量为 $\{\alpha_1^\vee,\alpha_2^\vee,\alpha_3^\vee,\alpha_4^\vee\}$，则
$$\langle \alpha_i^\vee,\alpha_j^\vee\rangle_L = c_{ij}.$$

其中 $\langle\cdot\rangle_L$ 是 Lorentz 内积
$$\langle x,y\rangle_L = x_1y_1 + x_2y_2 + x_3y_3-x_4y_4.$$

所以我们可以直接取泛函 $\alpha_i$ 为
$$\alpha_i(v) = \langle \alpha_i^\vee,v\rangle_L.$$

特别注意 $\langle \alpha_i^\vee,\alpha_i^\vee\rangle_L = 1$，即每个 $\alpha_i^\vee$ 都是 space-like 的。

不难写出如下的一组 $\{\alpha_i^\vee\}$：
$$\begin{align*}
\alpha_1^\vee &= (1, 0, 0, 0),\\
\alpha_2^\vee &= (-\cos\frac{\pi}{5}, \sin\frac{\pi}{5}, 0, 0),\\
\alpha_3^\vee &= (0, -\frac{1}{2\sin\frac{\pi}{5}}, \sqrt{1-\frac{1}{4\sin^2\frac{\pi}{5}}}, 0),\\
\alpha_4^\vee &= (0, 0, -\frac{\cos\frac{\pi}{5}}{\sqrt{1-\frac{1}{4\sin^2\frac{\pi}{5}}}}, a).
\end{align*}$$

其中 $a$ 满足 $\langle \alpha_4^\vee,\alpha_4^\vee\rangle_L = 1$。$a$ 有两种选择，这取决于你选择的 hyperboloid 的分支。如果你选择上半分支 $w>0$ 的话，为了保证所有半空间 $\{\alpha_i>0\}$ 之交属于上半分支需要取 $a<0$。这是因为对 $p=(x,y,z,w),w>0$，$\langle \alpha_1^\vee,p\rangle_L > 0$ 说明 $x>0$，进而 $\langle \alpha_2^\vee,p\rangle_L > 0$ 说明 $y>0$，继续 $\langle \alpha_3^\vee,p\rangle_L > 0$ 说明 $z>0$，而 $\langle \alpha_4^\vee,p\rangle_L > 0, w>0$ 必须有 $a<0$ 才能成立。

总之在 Cartan 矩阵对应的双线性型非退化的情形，可以用对应的内积来定义反射，这一点对球面的情形也是一样的。