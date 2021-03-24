---
title: "Coxeter 群，有限状态机与均匀密铺"
tags:
  - Coxeter group
  - Uniform tilings
  - POV-Ray
  - Automata
  - Minimal roots
  - Regular language
  - DFA minimization
  - Hyperbolic tilings
  - Spherical tilings
  - Euclidean tilings
categories: [pywonderland 项目]
date: 2019-12-15
url: "coxeter-groups-and-uniform-tilings"
---

终于完成了一个新的 Python 小程序，虽然还有一些功能有待实现，但是大致的效果已经出来了。这个程序是我最近半年多来利用几乎所有业余时间呕心沥血、披星戴月、艰苦攻关完成的新作品，是一个纯粹的、优雅的、有益于广大人民欣赏数学之美的程序。代码在 [github](https://github.com/neozhaoliang/pywonderland/tree/master/src/uniform-tilings) 上，目前还有许多不尽人意的地方，后面还会继续维护和改进。

这个程序是我目前为止写过的所有程序中最难的一个，它涉及的数学知识相当复杂，使用了 Coxeter 群的一些深刻性质，所以理解起来可能不太容易。但是这个程序可以做的事情相当惊人，它可以用来绘制二维和三维欧式空间、双曲空间和球面上的各种均匀密铺 ([uniform tilings](https://en.wikipedia.org/wiki/Uniform_tiling))，生成的图片效果非常优美。我最好还是先有图有真相：


# 例子


+ 下图是二维的欧式密铺 omnitruncated (4, 2, 4)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-4-2-4.png" width="600"/>

<!-- more -->

+ 下图是二维的 Poincaré 圆盘上的正双曲密铺 (2, 3, 13)，绘制了 3447 个顶点，6971 条边，3549 个多边形：

    <img style="margin:0px auto;display:block" src="/images/coxeter/2-3-13.png" width="500"/>


+ 下图是二维的上半平面模型中的双曲密铺 omnitruncated (4, 3, 3):

    <img style="margin:0px auto;display:block" src="/images/coxeter/uhp-4-3-3.png" width="600"/>

+ 下图是三维的 Poincaré 单位球中的正双曲密铺 (3, 5, 3)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/3-5-3.png" width="600"/>

+ 下图是三维的 Poincaré 单位球中的正双曲密铺 (5, 3, 5)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/5-3-5.png" width="600"/>

+ 下图是三维的 Poincaré 单位球中的正双曲密铺 (5, 3, 4)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/5-3-4.png" width="600"/>

+ 下图是三维的 Poincaré 单位球中的正双曲密铺 (4, 3, 5)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/4-3-5.png" width="600"/>

+ 以上四个密铺是三维双曲空间中仅有的正且每个胞腔为紧集的双曲密铺。如果去掉每个胞腔为紧集的限制的话，但是要求每个胞腔的体积有限的话，则还有 10 个正双曲密铺，如下图的 (6, 3, 3)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/6-3-3.png" width="600"/>

    你可以看到每个胞腔都有一个理想顶点，它位于空间的无穷远处 (即单位球面上)。这 10 个密铺也叫做仿紧的 (paracompact)，因为每个胞腔的体积仍然是有限的。如果再去掉每个胞腔的体积有限的条件的话，得到的密铺叫做非紧的，这样的正密铺有无限多个。

+ 如果去掉正密铺这个限制，只考虑均匀密铺的话，那例子就非常多了。比如我们可以从正密铺出发通过截断操作得到许多均匀密铺，如 rectified (3, 5, 3) 和 rectified (5, 3, 4)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/rectified-3-5-3.png" width="600"/>

    <img style="margin:0px auto;display:block" src="/images/coxeter/rectified-5-3-4.png" width="600"/>

    还有来自 [5, 3<sup>1,1</sup>] 的密铺 [cantic order-5 cubic](https://en.wikipedia.org/wiki/Uniform_honeycombs_in_hyperbolic_space#[5,31,1]_family)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/cantic-order-5-cubic.png" width="600"/>

+ 下图是一个二维的球面密铺 omnitruncated (5, 2, 3)，绘制在了三维的球面上：

    <img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-5-2-3.png" width="500"/>

+ 最后是一个 shader 程序，仍然来自 Matt Zucker 的 [shadertoy 项目](https://www.shadertoy.com/view/3tsSzM)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/wythoff_shader.png" width="600"/>

双曲密铺可玩的花样是无穷无尽的，以上只是这个小程序的部分输出。


# 图像的绘制原理


目前我所知的所有绘制均匀密铺的程序其原理大都基于 [Wythoff 构造法](https://en.wikipedia.org/wiki/Wythoff_construction)，这个程序也不例外。Wythoff 构造法与万花筒的原理是一样的，即在空间中摆放若干反射平面 (镜子)，然后从一个初始点出发，依次关于这些镜子作反射变换，得到一些镜像点，再对新的镜像点重复此步骤，一直下去，子子孙孙无穷匮也，就得到了密铺的全部顶点。

下面的视频演示了 Wythoff 构造法的效果。我们在二维的 Poincaré 双曲圆盘中的一个房间四周放置若干镜子，则房间中的场景就会在镜子中反复成像，仿佛填满了整个空间。但实际上这个场景里面只有一个初始房间是真实的 (即相机所在的这个)，其它的房间都是它在镜子中的虚像。

<video src="/images/coxeter/wythoff.mp4" width="600" controls></video>

> 特别鸣谢 Jos Leys 教给我怎样在 POV-Ray 中制作这一视频。

Wythoff 构造法中最关键的部分在于如何快速地、不重复地计算所有顶点坐标，以及它们之间的边、面、胞腔的关系。这正是这个程序的优雅之处，它采用的是群论的方法，首先在密铺的对称群中进行符号计算，得出每个顶点在最短字典序下对应的单词表示，边的下标，面的下标等信息，然后将每个顶点对应的单词作用在初始顶点上得到该顶点的坐标。换句话说，在计算每个顶点的最终坐标之前，它已经提前计算好了有多少个顶点，每个顶点是由初始顶点经过哪些反射得到的，哪些顶点构成边，哪些顶点构成面，哪些顶点构成胞腔，等等。这些计算仅涉及整数运算，完全避免了浮点数精度损失的问题。是不是很神奇呢？

下面我用一个例子来演示这个具体的步骤。


# 例子：omnitruncated (7, 2, 3) 密铺


Omnitruncated (7, 2, 3) 密铺对应的 Coxeter-Dynkin 图如下：

<img style="margin:0px auto;display:block" src="/images/coxeter/coxeter723.svg" width="250"/>

这是一个二维的双曲密铺 [^1]，其对称群是由 Coxeter 矩阵

$$M=\begin{pmatrix} 1 & 7 & 2 \\ 7 &1 &3\\ 2 & 3 &1\end{pmatrix}$$

确定的 Coxeter 群

$$W=\langle s_0,s_1, s_2\ |\ s_0^2=s_1^2=s_2^2=(s_0s_1)^7=(s_1s_2)^3=(s_0s_2)^2=1\rangle.$$

初始顶点不包含于任何镜面上，所以其稳定化子群只包含单位元 1，从而根据[轨道—稳定化子定理](https://en.wikipedia.org/wiki/Wroup_action_(mathematics)#Orbit-stabilizer_theorem) $W$ 的每一个元素都对应密铺中的一个顶点。

$W$ 中每个元素 $g$ 都可以表示为生成元 $s_0,s_1,s_2$ 的乘积，我们称任何这样的表示方式为 $g$ 的一个单词表示。$g$ 的单词表示不是唯一的，比如从定义 $W$ 的生成关系中可以看出 $s_0s_2=s_2s_0$, $s_1s_2s_1=s_2s_1s_2$ 等等。但是在 $g$ 的所有单词表示中，我们总是可以选择“最小的”那个来作为 $g$ 的**规范表示**，这个排序的依据就是最短字典序 (shortlex order)：首先规定生成元 $s_0,s_1,s_2$ 之间的字母顺序关系为 $s_0<s_1<s_2$，然后将这个顺序扩展到任何两个单词 $w_1$ 和 $w_2$ 上去：

{% blockquote %}
**定义**：设 $w_1=s_{i_1}s_{i_2}\cdots s_{i_n}$ 和 $w_2=s_{j_1}s_{j_2}\cdots s_{j_m}$ 是两个不同的单词，它们二者之间的顺序关系由如下方式确定：

1. 先比较长度，长度长的为较大者，即若 $n<m$ 则 $w_1<w_2$，$n>m$ 则 $w_1>w_2$。
2. 若长度相等则按字母顺序从左到右逐项比较，设 $k$ 使得对任何 $l<k$ 有 $s_{i_l}=s_{j_l}$ 但 $s_{i_k}\ne s_{j_k}$，则规定 $w_1,w_2$ 之间的大小关系与 $s_{i_k},s_{j_k}$ 之间的大小关系相同。
{% endblockquote %}

由于最短字典序是所有由 $s_0,s_1,s_2$ 组成的单词集合上的全序，在这个全序下任何 $g\in W$ 都有唯一的规范表示，任何两个 $g,g'\in W$ 之间的大小顺序就规定为它们的规范表示之间的大小关系。一个元素 $g\in W$ 的长度定义为其规范表示的长度。

定义 $\mathcal{SL}(W)$ 为 $W$ 中所有元素的规范表示组成的集合，下面列出了 $\mathcal{SL}(W)$ 中所有长度不超过 5 的元素，一共有 37 个：(从小到大按行排列)

$$
\begin{array}{lllll}e&s_{0}&s_{1}&s_{2}&s_{0}s_{1}\\s_{0}s_{2}&s_{1}s_{0}&s_{1}s_{2}&s_{2}s_{1}&s_{0}s_{1}s_{0}\\s_{0}s_{1}s_{2}&s_{0}s_{2}s_{1}&s_{1}s_{0}s_{1}&s_{1}s_{0}s_{2}&s_{1}s_{2}s_{1}\\s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{1}&s_{0}s_{1}s_{0}s_{2}&s_{0}s_{1}s_{2}s_{1}&s_{0}s_{2}s_{1}s_{0}\\s_{1}s_{0}s_{1}s_{0}&s_{1}s_{0}s_{1}s_{2}&s_{1}s_{0}s_{2}s_{1}&s_{1}s_{2}s_{1}s_{0}&s_{2}s_{1}s_{0}s_{1}\\s_{0}s_{1}s_{0}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{1}s_{2}&s_{0}s_{1}s_{0}s_{2}s_{1}&s_{0}s_{1}s_{2}s_{1}s_{0}&s_{0}s_{2}s_{1}s_{0}s_{1}\\s_{1}s_{0}s_{1}s_{0}s_{1}&s_{1}s_{0}s_{1}s_{0}s_{2}&s_{1}s_{0}s_{1}s_{2}s_{1}&s_{1}s_{0}s_{2}s_{1}s_{0}&s_{1}s_{2}s_{1}s_{0}s_{1}\\s_{2}s_{1}s_{0}s_{1}s_{0}&s_{2}s_{1}s_{0}s_{1}s_{2}&\end{array}
$$

注意由 $s_0,s_1,s_2$ 组成的且长度不超过 5 的单词 (单位元 $e$ 也算在内) 总共有 $1+3+\cdots+3^5=364$ 个，上表告诉我们实际上它们只包含了 $W$ 中 37 个不同的元素，即将它们作用在密铺中的初始顶点上只会得到 37 个顶点，其余 364 - 37 = 327 个都是重复的。进一步计算可得长度不超过 6 的单词有 1093 个而实际上只包含了 53 个不同的元素。所以如果我们能够快速地生成 $\mathcal{SL}(W)$ 中的元素而不是去遍历所有可能单词的话，就可以大大提高计算效率。

那么怎么才能既快速，又精准，不遗漏地生成 $\mathcal{SL}(W)$ 中的元素呢？这就引出了一个关于 Coxeter 群的重要结论：

{% blockquote %}
**定理 [Brigitte Brink & Robert B. Howlett, 1993]**：若 $W$ 是有限生成 Coxeter 群，则 $\mathcal{SL}(W)$ 是一个[正则语言](https://en.wikipedia.org/wiki/Regular_language)。
{% endblockquote %}

正则语言这个术语来自计算机科学，关于正则语言的一个基本事实是，一个有限字符集上的正则语言总是可以被一个确定的有限状态自动机 (definite finite automaton) 识别，这样的有限状态机不是唯一的，但是在等价意义下总是存在一个最小的 (含有的状态数目最少)，下图显示的是识别 (7, 2, 3) 这个群的 $\mathcal{SL}(W)$ 的最小状态机：

<img style="margin:0px auto;display:block" src="/images/coxeter/dfa_723.svg" width="600"/>

你可以看到在上图中一共有 19 个节点 (即状态)，每个状态都有一个编号，这个编号并没有实际意义，可以不用理会，实际上给状态重新编号不影响有限状态机识别的语言。真正有意义的是顶点之间的关系以及边的编号。圈红的节点 0 是初始状态。

图中的每条有向边规定了状态之间的转移规则，边的标号 $i$ 代表生成元 $s_i$。从初始状态出发，每次沿着一条有向边移动到下一个状态，经过的路径给出了一个由 $s_0,s_1,s_2$ 组成的单词，所有的路径给出的单词组成的集合就是这个有限状态机识别的语言，即 $\mathcal{SL}(W)$。

举个例子：

1. 长度为 0 的路径对应的是 $W$ 的单位元。
2. 长度为 1 的三条路径 $0\xrightarrow{\ s_0\ }1$, $0\xrightarrow{\ s_1\ }2$, $0\xrightarrow{\ s_2\ }8$ 对应的是 $W$ 的三个长度为 1 的元素 $s_0,s_1,s_2$。
3. 长度为 2 的 5 条路径 $0\xrightarrow{\ s_0\ }1\xrightarrow{\ s_1\ }2$, $0\xrightarrow{\ s_0\ }1\xrightarrow{\ s_2\ }8$, $0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_0\ }3$, $0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_2\ }8$, $0\xrightarrow{\ s_2\ }8\xrightarrow{\ s_1\ }9$ 对应的是 $W$ 的 5 个长度为 2 的元素 $s_0s_1,s_0s_2,s_1s_0,s_1s_2,s_2s_1$。

以此类推，我们可以很容易用宽度优先搜索来不重复不遗漏地遍历任意长度范围内的群元素。特别地如果你按图索骥地验证一下的话可以发现所有长度不超过 5 的路径一共有 37 条，它们正对应前面列出的 $\mathcal{SL}(W)$ 中长度不超过 5 的 37 个单词。

注意无限 Coxeter 群的有限状态机必然含有回路，而有限 Coxeter 群的有限状态机则必然是一个以初始状态为根节点的有向树，例如下图显示的是正四面体的对称群 $S_4$ 的有限状态机：

<img style="margin:0px auto;display:block" src="/images/coxeter/tetrahedron.svg" width="600"/>

不难遍历得出其 24 个不同的路径，它们分别对应 $S_4$ 的 24 个元素的最短字典序表示：

$$
\begin{array}{llll}e&s_{0}&s_{1}&s_{2}\\s_{0}s_{1}&s_{0}s_{2}&s_{1}s_{0}&s_{1}s_{2}\\s_{2}s_{1}&s_{0}s_{1}s_{0}&s_{0}s_{1}s_{2}&s_{0}s_{2}s_{1}\\s_{1}s_{0}s_{2}&s_{1}s_{2}s_{1}&s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{2}\\s_{0}s_{1}s_{2}s_{1}&s_{0}s_{2}s_{1}s_{0}&s_{1}s_{0}s_{2}s_{1}&s_{1}s_{2}s_{1}s_{0}\\s_{0}s_{1}s_{0}s_{2}s_{1}&s_{0}s_{1}s_{2}s_{1}s_{0}&s_{1}s_{0}s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{2}s_{1}s_{0}\end{array}
$$

既然通过 $\mathcal{SL}(W)$ 来生成群元素如此方便，那问题来了：

{% blockquote %}
**问题 1**：怎样计算 $\mathcal{SL}(W)$ 对应的有限状态机？
{% endblockquote %}

此问题技术太过复杂，完整介绍全部内容的话本文难以承受，我在后面附有一个简单的解释。我在创作这个程序时主要参考了 Casselman 的讲义 [^2] [^3] [^4]，他的一份未公开的 Java 代码，以及 Humphreys 的教材 [^5]。

有了每个群元素的唯一的规范表示，我们就可以很容易地计算密铺中每个顶点的坐标了：

设 $w=s_{i_0}s_{i_1}\cdots s_{i_n}$，初始顶点为 $v_0$，则 $w$ 在 $v_0$ 上的作用为
$$w\cdot v_0 = s_{i_0}(s_{i_1}(\cdots s_{i_n}(v_0)).$$
即从右到左依次计算每个生成元作用的结果。当然由于 $W$ 是无限群，我们只能计算那些长度不超过一定范围的群元素对应的顶点。假设我们已经有了前面这 37 个顶点，把它们按照最短字典序排序存储在一个列表 $L$ 里。为了绘制密铺中的边，我们还需要计算 $L$ 中哪些顶点是相邻的，这个怎么解决呢？

首先我们需要计算一个 $L$ 中元素之间的乘法表 $T$，$T$ 的作用是帮助我们查找任何一个单词，其规范表示在 $L$ 中的下标 (不在 $L$ 中的话则返回 `None`)。$T$ 是一个大小为 $|L|\times 3$ 的二维数组，其第 $i$ 行对应 $L$ 中的第 $i$ 个群元素 $w_i$，第 $j$ 列对应群的生成元 $s_j$，$T[i][j]$ 的值等于 $s_jw_i$ 这个元素 (**注意这个乘积未必是个规范表示**) 的规范表示在 $L$ 中的下标。如果这个元素不在 $L$ 中则以 `None` 代替。

在我们的例子中 $T$ 的值如下，$L$ 中的元素放在了第二列：

<details>
<summary><font color="#D00">**点击展开列表 $T$**</font></summary>
<div>
| V | word | $s_0$ | $s_1$ | $s_2$|
|:-----:|:-----:|:-----:|:-----:|:-----:|
|0|$e$|1|2|3|
|1|$s_{0}$|0|6|5|
|2|$s_{1}$|4|0|8|
|3|$s_{2}$|5|7|0|
|4|$s_{0}s_{1}$|2|12|11|
|5|$s_{0}s_{2}$|3|13|1|
|6|$s_{1}s_{0}$|9|1|15|
|7|$s_{1}s_{2}$|10|3|14|
|8|$s_{2}s_{1}$|11|14|2|
|9|$s_{0}s_{1}s_{0}$|6|20|19|
|10|$s_{0}s_{1}s_{2}$|7|21|18|
|11|$s_{0}s_{2}s_{1}$|8|22|4|
|12|$s_{1}s_{0}s_{1}$|16|4|24|
|13|$s_{1}s_{0}s_{2}$|17|5|23|
|14|$s_{1}s_{2}s_{1}$|18|8|7|
|15|$s_{2}s_{1}s_{0}$|19|23|6|
|16|$s_{0}s_{1}s_{0}s_{1}$|12|30|29|
|17|$s_{0}s_{1}s_{0}s_{2}$|13|31|28|
|18|$s_{0}s_{1}s_{2}s_{1}$|14|32|10|
|19|$s_{0}s_{2}s_{1}s_{0}$|15|33|9|
|20|$s_{1}s_{0}s_{1}s_{0}$|25|9|35|
|21|$s_{1}s_{0}s_{1}s_{2}$|26|10|36|
|22|$s_{1}s_{0}s_{2}s_{1}$|27|11|34|
|23|$s_{1}s_{2}s_{1}s_{0}$|28|15|13|
|24|$s_{2}s_{1}s_{0}s_{1}$|29|34|12|
|25|$s_{0}s_{1}s_{0}s_{1}s_{0}$|20|None|None|
|26|$s_{0}s_{1}s_{0}s_{1}s_{2}$|21|None|None|
|27|$s_{0}s_{1}s_{0}s_{2}s_{1}$|22|None|None|
|28|$s_{0}s_{1}s_{2}s_{1}s_{0}$|23|None|17|
|29|$s_{0}s_{2}s_{1}s_{0}s_{1}$|24|None|16|
|30|$s_{1}s_{0}s_{1}s_{0}s_{1}$|None|16|None|
|31|$s_{1}s_{0}s_{1}s_{0}s_{2}$|None|17|None|
|32|$s_{1}s_{0}s_{1}s_{2}s_{1}$|None|18|None|
|33|$s_{1}s_{0}s_{2}s_{1}s_{0}$|None|19|None|
|34|$s_{1}s_{2}s_{1}s_{0}s_{1}$|None|24|22|
|35|$s_{2}s_{1}s_{0}s_{1}s_{0}$|None|None|20|
|36|$s_{2}s_{1}s_{0}s_{1}s_{2}$|None|None|21|
</div>
</details>

于是对任意的单词 $w=s_{i_0}s_{i_1}\cdots s_{i_n}$，我们可以从 $T$ 的第 0 行出发，先找到 $s_{i_n}$ 在 $L$ 中对应的元素，假设是第 $k$ 个，那么就跳到第 $k$ 行，由 $s_{i_{n-1}}$ 对应的列找到 $s_{i_{n-1}}s_{i_n}$ 在 $L$ 中对应的元素，再顺藤摸瓜找到 $s_{i_{n-2}}s_{i_{n-1}}s_{i_n}$ 在 $L$ 中对应的元素，...，如此下去即可确定 $w$ 在 $L$ 中对应的元素 (或者 `None`)。

假设初始顶点 $v_0$ 关于第 $i$ 面镜子反射后得到的虚像是 $v_1=s_i(v_0)$，则 $e=(v_0,v_1)$ 构成一条类型为 $i$ 的边。边 $e$ 的稳定化子群就是标准椭圆子群 $H=\langle s_i\rangle$。根据轨道稳定化子定理，密铺中所有类型为 $i$ 的边都可以通过将 $W/H$ 中某个代表元作用在 $e$ 上得到。显然 $e$ 的两个端点对应的规范表示分别是单位元 1 和 $s_i$，则对任一 $w\in W$，我们首先计算 $w$ 关于 $H$ 的陪集代表元 $w_H$ (这一步需要配合去重，去掉重复的陪集代表元)，$w_H\cdot e$ 的两个端点对应的单词分别是 $w_H$ 和 $w_Hs_i$，然后按照上面的步骤找到它俩在 $L$ 中对应的元素下标 (如果有一个是 `None` 说明这条边连接了不在 $L$ 中的顶点)，这就得到了边的下标。

$L$ 中 37 个顶点构成的边如下：

<img style="margin:0px auto;display:block" src="/images/coxeter/723_edges.png" width="500"/>

图中标号 0 的顶点是初始顶点，其对应的单词是单位元 1。边中白色的线条个数表示这条边对应的生成元：0 条表示 $s_0$，1 条表示 $s_1$，2 条表示 $s_2$。

从这个图里可以看出很多有用的信息，非常有助于理解 Coxeter 群的最短字典序表示与密铺顶点的对应关系：

1. 首先可以看出将顶点 0 关于三个镜面进行一次反射得到的新虚像是 1, 2, 3，它们对应的单词是 $L$ 中长度为 1 的 $s_0,s_1,s_2$。
2. 将顶点 0 关于各个镜面进行两次反射得到的新虚像是 4, 5, 6, 7, 8，它们对应的单词是 $L$ 中长度为 2 的 $s_0s_1,s_0s_2,s_1s_0,s_1s_2,s_2s_1$。
3. 所有顶点与初始顶点之间的最短路径的长度都不超过 5。
4. 从图中我们可以看出每个顶点对应的单词的规范表示。例如从 0 号顶点到 33 号顶点有两条最短路径：$$
\begin{align*}&0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_0\ }6\xrightarrow{\ s_2\ }13\xrightarrow{\ s_1\ }22\xrightarrow{\ s_0\ }33.\\
&0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_2\ }7\xrightarrow{\ s_0\ }13\xrightarrow{\ s_1\ }22\xrightarrow{\ s_0\ }33.
\end{align*}$$
只要按顺序连起来 (从左到右) 就可以得到 33 号顶点对应的两个单词：$s_1s_0s_2s_1s_0$ 和 $s_1s_2s_0s_1s_0$，它们都把 0 号顶点变为 33 号顶点，但是前者才是最短字典序表示。这一点也可以从顶点标号中看出来：从二号顶点开始两条路径分别去了 6 号和 7 号顶点，由于 6 号顶点在 $\mathcal{SL}(W)$ 中更小，因此这条路径必然才是 33 号顶点规范表示对应的路径。
5. 一个单词 $w=s_{i_0}s_{i_1}\cdots s_{i_n}$ 作用在 0 号顶点上 ($s_{i_n}$ 先作用，$s_{i_0}$ 在最后) 的结果是一条从 0 号顶点出发，标号依次为 $s_{i_0}, s_{i_1},\ldots,s_{i_n}$ 的路径 ($s_{i_0}$ 在先，$s_{i_n}$ 在最后)，与作用的顺序相反。

你可能要问，直接计算 $w_H$ 和 $w_Hs_i$ 的规范表示，然后去 $L$ 中查找下标不就可以了吗？为什么计算这个表 $T$ 呢？这里我的考虑有两个：

1. 表 $T$ 的计算是一次性的，而且查表速度很快。不借助 $T$ 的话就要每条边都计算两次规范表示然后进行两次 $L$ 中的逐项比较查找。

2. 表 $T$ 也同样用于计算面和胞腔。不借助 $T$ 的话就要对每个胞腔的每个顶点 (一个胞腔是一个多面体，可能有几十个顶点) 计算一次规范表示并逐项比较查找。

{% blockquote %}
**问题 2**：给定任一单词 $w$ 和标准椭圆子群 $H$，怎样计算 $w$ 的规范表示？怎样计算 $w$ 关于 $H$ 的陪集代表元？
{% endblockquote %}

简单的介绍见后，详细证明见 Casselman 的文章，本文暂且按下不表。

计算面的步骤也是完全类似的，初始顶点关于 $i, j$ 两面镜子的反射的复合是一个旋转，这个旋转连续作用 $m$ 次可以生成一个正多边形的面，其中 $m$ 是 Coxeter 矩阵中的 $(i,j)$ 分量。这个多边形的稳定化子群是标准椭圆子群 $H=\langle i, j\rangle$，我们仍然可以得出每个顶点对应的一个单词表示，用 $W/H$ 里的代表元作用在上面，然后去 $L$ 里面查找对应的规范表示的下标。

最终得到的图像如下图，计算了 30517 个顶点，42057 条边，11541 个多边形：

<img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-7-2-3.png" width="500"/>


# 关于代码


代码中最核心的部分是一个叫 `coxeter` 的模块，它主要实现的是 `CoxeterGroup` 类，这个类由一个 Coxeter 矩阵初始化，负责计算该 Coxeter 群的极小根反射表、实现群元素的乘法、陪集的计算，计算并绘制有限状态机。在另一个 `tiling.py` 文件中调用此类，计算密铺的顶点、边、面并绘制。

绘制 $\mathcal{SL}(W)$ 的有限状态机需要使用 [pygraphviz](https://pygraphviz.github.io/) 模块，这个模块依赖于 [graphviz](http://graphviz.org/) 软件和 `libgraphviz-dev`。

我把密铺的绘图大部分外包出去了，二维双曲空间的绘图用的是一个叫 [hyperbolic](https://github.com/cduck/hyperbolic/) 的三方库，这个库的代码写的挺糟糕的，然而我一时也没有精力分出来再写一个，所以暂且先凑合着。二维情形的绘图主要麻烦的地方在为了绘制具有常双曲宽度的边需要计算对应的 [hypercycle](https://en.wikipedia.org/wiki/Hypercycle_(hyperbolic_geometry))。球面和三维双曲情形的绘图用的是 POV-Ray，主要使用了 `sphere_sweep` 这个对象。


# 算法运行效率


这个算法比较耗时的地方有两个：

1. 计算群 $W$ 的**极小根**部分。计算 Coxeter 群的极小根是计算 $\mathcal{SL}(W)$ 的有限状态机、计算群的规范表示所必须的重要步骤，而极小根的计算量依赖于 Coxeter 群的复杂度：对 $(p, q, r)$ 这样的 triangle 群，当 $p,q,r$ 都不大于 10 时计算还比较快 (双曲的话稍慢些，要花个几秒钟)，然而对 (19, 20, 21) 这样的群计算速度就很慢了。这一点与逆像素反射方法是不同的，逆像素反射法的计算量几乎不随群的变化而变化。

2. 计算乘法表 $T$。对于三维双曲密铺要生成一个效果较好的场景至少需要几十万个顶点，对这么多顶点计算乘法表非常耗时，内存和查找开销都很大。这种情形我采用的是有限状态机生成群元素结合传统的浮点数去重，一边计算一边输出以节省空间开销。

总结起来就是对不太复杂的群，或者需要生成的数据量不太大的时候这种方法的速度还不错。


# 附录：对若干关键点的解释


在这里我简单介绍计算 $\mathcal{SL}(W)$ 的有限状态机、计算任一单词的规范形式、计算陪集代表元的步骤。需要你了解 Coxeter 群的几何实现、Tits 锥、Coxeter 群的根系等预备知识，这部分内容可以参考 Humphreys 的教材。

以上所有的计算都基于一个叫做**极小根反射表**的东西。仍然以 (7, 2, 3) 这个群为例子，先看下图：

<img style="margin:0px auto;display:block" src="/images/coxeter/roots.png" width="600"/>

这个图和上图一样，只不过多了 12 个标记出的镜面，这 12 个镜面有特殊的含义：它们是群 $W$ 的根系中的 12 个极小根。

你可以把 $W$ 的根系理解为图中所有的圆弧，每个圆弧都是一个反射镜面，它交单位圆的边界于两点。这些镜面都是 $\Delta ABC$ 三条边所在的初始镜面 (编号为 0, 1, 2) 在群 $W$ 作用下的结果。每个镜面把单位圆 (即整个双曲空间) 分割成两部分，这两部分分别对应根系中的一个正根和一个负根，其中基本区域三角形 $\Delta ABC$ 所在的半空间是正根对应的部分。

从直观上说，极小根 $r$ 是那些满足如下条件的镜面：不存在任何镜面 $r'\ne r$，使得一个人站在 $\Delta ABC$ 的内部往外看，视线会被 $r'$ 完全挡住而看不到 $r$ 的任何部分。单根必然都是极小根 (它们是基本区域的边界)。关于极小根的一个重要事实是，**任何有限生成 Coxeter 群的极小根的个数都是有限的**。这个结论在 Brink 和 Howlett 的证明中起到最关键的作用。

极小根的反射表 `reftable` 定义如下：这也是一个二维数组，其第 $i$ 行对应第 $i$ 个极小根 $\alpha_i$，其第 $j$ 列对应第 $j$ 个生成元 $s_j$，其 $(i, j)$ 位置填入的是 $\beta=s_j(\alpha_i)$ 的结果：

1. 如果 $\beta=\alpha_k$ 是第 $k$ 个极小根，则填入 $k$。
2. 如果 $\beta$ 是一个负根 (此情形发生当且仅当 $\alpha_i$ 是第 $j$ 个单根)，则填入 `-1`。
3. 如果 $\beta$ 是一个正根，但不是极小根，则填入 `None`。

(7, 2, 3) 群的极小根反射表如下：

| root | $s_0$ | $s_1$ | $s_2$|
|:-----:|:-----:|:-----:|:-----:|
|0|-1|3|0|
|1|4|-1|5|
|2|2|5|-1|
|3|6|0|7|
|4|1|8|9|
|5|9|2|1|
|6|3|10|11|
|7|11|7|3|
|8|10|4|None|
|9|5|None|4|
|10|8|6|None|
|11|7|None|6|

设 $W$ 的所有极小根之集为 $\Sigma$，$\mathcal{W}$ 的有限状态机的状态都是 $\Sigma$ 的子集，状态之间的转移关系规定如下：

$$S\xrightarrow{\ s_i\ } \{s_i\} \cup (s_i(S)\cup\{ s_i(\alpha_j),j<i\})\cap\Sigma.$$

由此不难利用宽度优先搜索获得所有的状态以及它们之间的转移关系，然后用 [Hopcroft 算法](https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft's_algorithm)将得到的有限状态机最小化。

下图显示的是 (7, 2, 3) 这个群的状态机中，每个状态对应的 $\Sigma$ 的子集：

<img style="margin:0px auto;display:block" src="/images/coxeter/723_dfa_subsets.png" width="600"/>

计算两个群元素乘法的规范表示的代码如下，其中 `s` 是一个生成元，`word` 是一个逆最短字典序下的单词 (逆最短字典序就是把最短字典序中的单词反过来)，函数返回的也是对应结果在逆最短字典序下的规范形式：

```python
def left_mul_invshortlex(reftable, s, word):
    word = tuple(word)
    t = s
    k = -1
    mu = s
    for i, s_i in enumerate(word):
        if mu is None:
            return word[:k+1] + (t,) + word[k+1:]
        elif mu < 0:
            return word[:i] + word[i+1:]
        elif mu < s_i:
            t = mu
            k = i
        else:
            continue
    return word[:k+1] + (t,) + word[k+1:]
```

由此函数不难计算任何两个单词相乘的逆最短字典序下的规范形式，倒过来自然也就解决了最短字典序下的乘法问题。

这里先在逆字典序下计算然后再倒过来获得字典序是为了和 Casselman 的文章中的论述保持一致。

计算一个规范表示 `word` 关于某个标准椭圆子群的陪集是最简单的：设 $W_T$ 是一个标准椭圆子群，其生成元是 $W$ 的生成元 $S$ 的一个子集 $T$，则计算 `word` 关于 $W_T$ 的左陪集代表元的伪代码如下：

```plain
x := word
u := 1
while l(xt) < l(x) for some t in T
    x = xt
    u = tu
end

return x
```

其中 $l(\cdot)$ 是 Coxeter 群上的长度函数。这个算法会把 `word` 分解为形如 $x^T\cdot w_T$ 的形式，其中 $w_T\in W_T$，且对任何 $t\in T$ 有 $l(x^Tt)>l(x^T)$。最终得到的陪集代表元 $x^T$ 是规范表示。

对有限 Coxeter 群，其所有正根都是极小根；对仿射 Coxeter 群，其根系由一些平行的镜面族构成，每族镜面中的反射镜面互相平行。每个族中存在一对极小根，它们把基本区域 $\Delta ABC$ 夹在中间并完全挡住本族中外面的镜面，所以只有它俩才是极小根。下图显示的是 (6, 2, 3) 密铺 (对称群为仿射 $\widetilde{G}_2$) 的 12 个极小根：

<img style="margin:0px auto;display:block" src="/images/coxeter/roots_623.png" width="600"/>



[^1]: 一个密铺的类型可以由其 Cartan 矩阵 $C=-\cos(\pi/M)$ 确定，是球面密铺当且仅当 $C$ 是正定的，是欧式密铺当且仅当 $C$ 是半正定的，是双曲密铺当且仅当 $C$ 是不定的，且 Coxeter-Dynkin 图的任何连通子图给出的密铺都是球面的或者欧式的。

[^2]: [Automata to perform basic calculations in Coxeter groups, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/banff.pdf).

[^3]: [Computation in Coxeter groups I. Multiplication, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/cm.pdf).

[^4]: [Computation in Coxeter groups II. Constructing minimal roots, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/roots.pdf).

[^5]: Reflection Wroups and Coxeter Wroups, by James E. Humphreys.
