---
title: "The glowing gasket"
subtitle: "The vision of Felix Klein"
date: 2025-01-23
url: "the-glowing-gasket"
---
\DeclareMathOperator{\tr}{Tr}
\newcommand{\fix}{\mathrm{Fix}\,}

:::{.simple}
Four circles to the kissing come. \
The smafter are the benter. \
The bend is just the inverse of The distance from the centre. \
Though sheir intrigue left Euclid dumb There’s now no need for nule of thumb. \
Since zero bend’s a dead straight line And concave bends have minus sign. \
The sum of the squares of alt four bends Is half the square of their sum.

The Kiss Precise, Sir Frederick Soddy [^1]

四圆相吻巧相连，大小虽异自周全。\
曲率正是心距倒，欧几里得愁煞然。\
拇指法则今无用，零曲率者乃直线。\
若为凹者曲率负，四曲率平方来加。 \
其和平方恰一半。

精确之吻，弗雷德里克·索迪爵士
:::


![Figure 7.1. The Apollonian gasket. The lacy web in the two pictures is the same: on the left, it is drawn in the complex plane and, on the right, on the sphere. As you might imagine, many people have tried calculating the Hausdorff dimension of the gasket. Curt McMullen has found the most accurate value, which is estimated as about 1.305688. \
图 7.1. 阿波罗尼奥斯垫片。两幅图中的蕾丝网状结构是相同的：左边是在复平面上绘制的，右边是在球面上绘制的。你可能已经猜到，许多人都曾尝试计算该垫片的豪斯多夫维数。柯特·麦克马伦（Curt McMullen）给出了目前最精确的估计值，约为 1.305688。](/images/indra/fig-7.1.jpg){width=600 .fig #fig-7.1}

:::{.simple}
The lacy web in Figure 7.1 is called the Apollonian gasket. Usually, it is constructed by a simple geometric procedure, dating back to those most famous of geometers, the ancient Greeks. We shall start by explaining the traditional construction, but as we shall disclose shortly, the gasket also represents another remarkable way in which the Schottky dust can congeal. The pictures you see here were actually all drawn using a refinement [^2] of the DFS algorithm for tangent Schottky circles.
:::

[图 7.1](#fig-7.1) 中蕾丝状的图案被称为阿波罗尼奥斯垫片。其构造基于一种简单的几何方法，这种方法可以追溯到最著名的几何学家——古希腊人。我们将首先解释这种传统的构造方式，但很快你会看到，这种圆垫其实还展现了另一个非同寻常的形式，即所谓的 Schottky 尘埃如何聚集成形。你所看到的这些图像，实际上都是使用一种针对相切 Schottky 圆的 DFS 算法改进版本 [^2] 绘制出来的。

:::{.simple}
The starting point of the traditional construction is a chain of three non-overlapping disks, each tangent to both of the others. A region between three tangent disks is a ‘triangle’ with circular arcs for sides. This shape is often called an ideal triangle: the sides are tangent at each of the three vertices so the angle between them is zero degrees.[^3] The gasket is activated by the fact that in the middle of each ideal triangle there is always a unique ‘inscribed disk’ or incircle, tangent to the three outer circles. It is really better to think of the gasket as a construction on the sphere. Insides and outsides don’t matter any more, so we may as well start with any three mutually tangent circles. You can see lots of disks and incircles in Figure 7.2.
:::

传统构造的起点是由三个互不重叠的圆盘组成的一条链，每个圆盘都与另外两个相切。三个相切圆盘之间的区域构成了一个“三角形”，其边界是由圆弧构成的。这种形状常被称为理想三角形：由于其三条边在三个顶点处相切，因此它们之间的夹角为零度。该垫片（gasket）的关键在于，每个理想三角形的中间总存在一个唯一的“内切圆”，即同时与三个外接圆相切的圆。事实上，更好的理解方式是将这个垫片看作是在球面上的一种构造。在球面上，内侧与外侧的区别已不复存在，因此我们可以从任意三个两两相切的圆开始。你可以在 [图 7.2](#fig-7.2) 中看到大量的圆盘和它们的内切圆。

![Figure 7.2. Activating the gasket. On the top left, the three largest disks which activate the gasket are shown in blue. One of the three disks appears as the outer blue region which frames the picture, because it contains the point $\infty$, the North Pole on the Riemann sphere. On the top right, two of the disks are tangent at $\infty$, so that you see them in the picture as parallel blue strips. Removing the blue circles leaves two red ideal triangles. Inside each ideal triangle is an incircle, coloured yellow. Below, we see more levels of incircles. \
图 7.2. 激活垫片。左上图中，标出的三个最大圆盘以蓝色呈现，正是它们激活了垫片。其中一个圆盘显示为环绕整幅图像的外部蓝色区域，这是因为它包含了点 $\infty$，即黎曼球面上的北极点。右上图中，其中两个圆盘在 $\infty$ 处相切，因此在图中呈现为两条平行的蓝色带状区域。当我们移除这些蓝色圆盘后，图中便显现出两个红色的理想三角形。每个理想三角形内部都嵌有一个黄色内切圆。下方图示进一步展示了更深层次的内切圆结构。](/images/indra/fig-7.2.jpg){width=600 .fig #fig-7.2}

:::{.simple}
In the figure, we show two initial configurations of three tangent blue disks. When you take out the three blue disks you are left with two red ideal triangles. Each red ideal triangle has a yellow incircle. See how each yellow incircle divides the red triangle into three more triangles. For repetitive people (a necessary quality in this subject, you might say), it is only natural to draw the incircles in these new triangles, resulting, of course, in even more triangles of the same kind. The bottom frame shows this subdivision carried out twice more, with green and then even smaller purple disks. In The Cat in the Hat Comes Back,’ the cat takes off his hat to reveal Little Cat, who then removes his hat and releases Little Cat, who then uncovers Little Cat, and so on. Now imagine there are not one but three new cats inside each cat’s hat. That gives a good impression of the explosive proliferation of these tiny ideal triangles. Carry out this process to infinity, and Voom, the Apollonian Gasket appears.
:::

图中展示了三个相切蓝色圆盘的两种初始配置。当你移除这三个蓝色圆盘时，剩下的是两个红色理想三角形。每个红色理想三角形都有一个黄色的内切圆。观察每个黄色内切圆如何将红色三角形分割成三个更小的三角形。

对于那些乐此不疲的人（或许正是研究这一主题的必备素质），在新三角形中继续绘制内切圆简直是顺理成章的事。这当然会催生出更多相似的三角形。下方的子图展示了这种细分过程再执行两次的结果——先是绿色圆盘，接着是更小的紫色圆盘，密密层层地堆叠起来。这让我想起《戴帽子的猫又来了》中的情节——大猫摘下帽子，露出一只小猫；小猫摘下自己的帽子，又冒出一只更小的小猫；接着更小的小猫再摘帽……如此反复进行。现在，想象每顶帽子里不是藏着一只，而是三只小猫，那你就能体会这些微型理想三角形是如何爆炸式增长的了。让这一过程无限延续，砰——阿波罗尼奥斯分形就出现了。

:::{.simple}
The Apollonian gasket is indeed very pretty, but the reason for introducing it here is that, remarkably, it is also the limit set of a Schottky group made by pairing tangent circles. Exactly the same intricate mathematical object can created by completely different means! You can see better how this works in the beautiful glowing version in Figure 7.3. The solid red circles in this picture are the initial Schottky circles in a very special configuration which we will look at closely in the next section. The glowing yellow limit set can be recognized as the same as the Apollonian gasket of Figure 7.1. The picture was made by pairing four tangent circles arranged in the configuration shown in Figure 7.4. The four circles are tangent not only in a chain; there are also extra tangencies between $C_a$ and $C_A$, and between $C_b$ and $C_B$.
:::

阿波罗尼奥斯分形确实非常美丽，但我们在此介绍它的原因是：令人惊讶的是，它也是由切圆配对生成的肖特基群的极限集。完全不同的方式也能创造出完全相同的复杂数学对象！您可以通过 [图 7.3](#fig-7.3) 中的荧光渲染图更好地理解它是如何运作的。图中的实心红色圆环是以一种特殊配置排列的初始肖特基圆（具体分析请参见下一节），其荧黄色的极限集与 [图 7.1](#fig-7.1) 中的阿波罗尼奥斯垫片完全一致。这幅图像是通过配对四个相切圆生成的，排列方式如 [图 7.4](#fig-7.4) 所示：这些圆不仅形成了链式相切的关系，而且在 $C_a$ 和 $C_A$、$C_b$ 和 $C_B$ 之间还存在额外的切点。

![Figure 7.3. (Overleaf.) The glowing gasket. This picture was created by applying the generating transformations $a,A,b,B$ to the chain of four solid red disks bounding the black ideal triangles. At higher levels, the image circles tone from red to orange to yellow, through green to blue, finally cycling back to red. Don’t let the picture fool you - the red circles are not the circles which activate the gasket in the traditional construction. The ones which appear in the traditional construction are the ‘dual’ circles with the yellow glow. \
图 7.3. 荧光垫片。此图像是通过对围绕黑色理想三角形的四个实心红色圆盘施加生成变换 $a,A,b,B$ 而生成的。在更高的层级中，图像中的圆环色调从红色渐变为橙色、黄色，接着是绿色，再到蓝色，最终循环回红色。需要特别注意的是：图中的红色圆并非传统阿波罗尼奥斯构造中激活垫片的圆——在传统构造中，起激活作用的是发出黄色光辉的“对偶圆”。](/images/indra/fig-7.3.jpg){width=600 #fig-7.3}

:::{.simple}
As you iterate the pairing transformations $a$ and $b$, the extra tangency proliferates, with the effect that inside each disk $D$ you see three further Schottky disks tangent to $D$ and each of the other two. In our version, the circles have been coloured depending on their level, starting with red at the first or lowest level, gradually changing to yellow, green and then blue. The small yellow and blue circles pile up, highlighting the limit set with a mysterious glow.
:::

当你不断迭代配对变换 $a$ 和 $b$ 时，额外的切点会迅速增殖。结果是在每个圆盘 $D$ 内部，都会涌现出三个新的肖特基子圆盘——它们不仅与 $D$ 相切，而且两两之间也彼此相切。在我们的可视化方案中，圆盘根据迭代的层级依次着色——最底层从红色起步，逐步过渡到黄色、绿色、蓝色。随着黄色和蓝色的小圆盘层层堆叠，突出了极限集，并散发出一种神秘的光辉。

:::{.simple}
In this chapter, we shall be exploring various features of the gasket. Notwithstanding the extra tangency, it turns out that each limit point is still associated to exactly one or two infinite words in the generators $a,b,A$ and $B$. You will be able to make your own version of the glowing gasket by running our DFS algorithm for the group generated by the transformations $a$ and $b$. The algorithm draws this complicated lacework as a continuous curve, which is hard to imagine until you see it in progress on a computer screen. The curve snakes its way through the gasket, apparently leaving one region for quite a while until finally weaving its way back. Animation is the true reward of successfully implementing the program we have been learning to build.
:::

在本章中，我们将深入探索垫片结构的各种特性。尽管存在额外的相切关系，但事实证明，每个极限点仍然对应于生成元 $a, b, A, B$ 所构成的一至两个无限字。通过运行我们为变换群 $\langle a,b\rangle$ 特别设计的深度优先搜索（DFS）算法，你将能够制作出自己专属的发光垫片。该算法将这种复杂的蕾丝结构绘制成一条连续的曲线——这种奇妙的生成过程，唯有在计算机屏幕上亲眼目睹，方能真正感受到其变幻莫测之美。曲线如同灵蛇般在垫片中蜿蜒穿梭，仿佛要彻底离开某个区域，却又在某个时刻悄然折返。成功实现我们精心构建的程序后，最令人欣喜的收获正是这些跃然屏上的动态演绎。

:::{.simple}
**Apollonius, circa 250-200 BC** \

Apollonius, known to his contemporaries as the Great Geometer, lived in Perga, now part of Turkey. One of the giants of Greek mathematics, he was famed for his 8 volume treatise Conics which studied ellipses, hyperbolas and parabolas as sections of a cone by a plane at various angles. His writings swiftly became standard texts in the ancient world. Many are now lost and we know them only through mention in other commentaries, among them works on regular solids, irrational numbers, and approximations to $\pi$. Ptolemy credits Apollonius with the theory of epicycles on which he based his theory of planetary motion.

One of Apollonius’ lost works is a book called Tangencies, reported to provide methods of constructing circles tangent to various other combinations of lines and circles, for example finding a circle tangent to two given lines and another circle. You can think of the problem of finding the incircle of an ideal triangle in this way. The most difficult problem, that of constructing the two circles tangent to three other given disjoint circles, was probably not solved in ancient times, however Sir Isaac Newton wrote down a proof. According to Pappus, Tangencies gave a formula for the radius of the incircle to an ideal triangle in terms of the radii of the circles which bound its three sides. Be that as it may, exactly such a formula was described by Descartes in 1643, and a version was known in eighteenth century Japan. In fact this formula seems to have been rediscovered many times, most recently by Sir Frederick Soddy, in whose honour the incircles are sometimes known as Soddy circles. Awarded the Nobel prize in 1921, for the discovery of isotopes, Soddy had a natural interest in how to pack spherical atoms of differing size.

Soddy was so taken with the formula that he published it in the unusual form of a poem, which appeared in the journal Nature in 1936. The central part is contained in the middle verse quoted at the head of this chapter. For those who feel more comfortable with symbols, suppose the radii of the chain of three circles are $a,b$
and $c$, and that the incircle has radius $d$. Soddy’s formula is:
$$\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}\right)^2=2\left(\frac{1}{a^2}+\frac{1}{b^2}+\frac{1}{c^2}+\frac{1}{d^2}\right).$$

阿波罗尼奥斯，被同时代人誉为伟大的几何学家，生活在佩尔加，即现今土耳其的一部分。作为希腊数学的巨擘之一，他因八卷本专著《圆锥曲线论》而闻名，该著作研究了椭圆、双曲线和抛物线作为平面以不同角度切割圆锥所得截面的性质。其著作迅速成为古代世界的标准教材。许多作品现已遗失，我们仅通过其他评论中的提及了解它们，其中包括关于正多面体、无理数及对 $\pi$ 的近似值的研究。托勒密将本轮理论归功于阿波罗尼奥斯，这一理论成为他行星运动学说的基础。

阿波罗尼奥斯遗失的著作之一名为《切触》，据记载，该书提供了构建与各种直线和圆组合相切的圆的方法，例如寻找与两条给定直线及另一个圆相切的圆。你可以将寻找理想三角形内切圆的问题视为此类问题。最难的难题，即构建与三个给定且互不相交的圆相切的两个圆，在古代可能并未解决，然而艾萨克·牛顿爵士记录了一个证明。根据帕普斯的说法，《切触》给出了一个公式，用于计算理想三角形内切圆的半径，该半径与限定其三条边的圆的半径有关。尽管如此，笛卡尔在 1643 年确实描述了这样一个公式，且在 18 世纪的日本也已知晓其版本。实际上，这个公式似乎被多次重新发现，最近一次是由弗雷德里克·索迪爵士完成的。为了纪念他，内切圆有时被称为索迪圆。索迪因发现同位素而于 1921 年获得诺贝尔奖，他对如何排列不同大小的球形原子自然产生了兴趣。

索迪对这个公式深深着迷，以至于他以一首诗的形式将其发表，这首诗出现在 1936 年的《自然》杂志上。其核心部分包含在本章开头引用的中间诗句中。对于那些更偏好使用符号的读者，假设三个连锁圆的半径分别为 $a, b$ 和 $c$，内切圆的半径为 $d$。索迪的公式为：

$$\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}\right)^2=2\left(\frac{1}{a^2}+\frac{1}{b^2}+\frac{1}{c^2}+\frac{1}{d^2}\right).$$
:::

# Generating the gasket

:::{.simple}
The configuration of tangent circles which produced the gasket is shown in the right frame of Figure 7.4. The picture has been arranged so that $C_a$ goes through $\infty$, hence it appears in the figure as a straight line. In addition, $C_A$ and $C_a$ are tangent at 0 and $C_B$ and $C_b$ are tangent at $-i$. You can see how this picture is made by creating extra tangencies among a kissing chain of four circles by comparing with the nearby arrangement of four circles in the left hand frame.
:::


生成垫片的相切圆配置如 [图 7.4](#fig-7.4) 右图所示。图中特意令圆 $C_a$ 经过 $\infty$，从而它在图中呈现为一条直线。此外，我们令圆 $C_A$ 与 $C_a$ 在原点 0 处相切，圆 $C_B$ 与 $C_b$ 在$-i$ 处相切。通过与左边图中四个圆的排列进行对比，可以清晰观察到右图通过在四圆相切链中引入额外切点形成的特殊结构。

![Figure 7.4. The right frame shows the starting configuration of tangent Schottky circles which produces the glowing gasket. The red circles $C_a$ and $C_A$ are paired by the transformation $a$ and the blue circles $C_B$ and $C_b$ by $b$. Using notation from the last chapter, the tangency points $P,Q,R$ and $S$ are at $1,-1,-0.2-0.4i$ and $0.2-0.4i$ respectively. On the left is a nearby Schottky configuration of circles which are not quite tangent and $a$
and $b$ are loxodromic. This is similar to the configuration shown in frame (vi) of Figure 6.10. The centre frame is an intermediate stage where $a$ is parabolic but $b$ is not. \
图 7.4. 右图展示了生成发光垫片的相切 Schottky 圆的初始配置。红色圆 $C_a$ 与 $C_A$ 通过变换 $a$ 配对，蓝色圆 $C_B$ 与 $C_b$ 通过变换 $b$ 配对。根据前一章的记号，切点 $P, Q, R, S$ 分别位于坐标 $1, -1, -0.2-0.4i$ 和 $0.2-0.4i$ 处。左图展示了一个相似的 Schottky 圆配置，其中圆未完全相切，且变换 $a$ 和 $b$ 均为斜航的。该配置与 [图 6.10](#fig-6.10) (vi) 中的结构相似。中间图呈现了过渡状态，其中变换 $a$ 是抛物线型的，而 $b$ 不是。](/images/indra/fig-7.4.jpg){width=600 #fig-7.4 .fig}

:::{.simple}
The generating matrices for the gasket are quite simple:
$$a=\begin{pmatrix}1&0\\-2i&1\end{pmatrix}\quad\text{and}\quad b=\begin{pmatrix}1-i&1\\1&1+i\end{pmatrix}.$$

We shall have more to say about how we arrived at these particular formulas later on. Note that $\tr{a}=\tr{b}=2$, so $a$ and $b$ are parabolic. Looking at the arrangement of Schottky circles in Figure 7.4, you see the fixed point of $a$ is 0, the tangency point of the circles $C_a$ and $C_A$. In Figure 7.3, you can see two chains of tangent circles nesting down on 0 from above and below. The same phenomenon occurs at $-i$, the tangency point of $C_B$ and $C_b$ and the fixed point of $b$. Notwithstanding extra tangencies, the generators $a$ and $b$ still pair opposite circles in the initial tangent chain $C_a,C_b,C_A$ and $C_B$. This means that for nesting circles we still need the commutator condition $\tr{abAB}=2$, which is not hard to check.
:::

生成该垫片的矩阵非常简单：

$$a=\begin{pmatrix}1&0\\-2i&1\end{pmatrix}\quad\text{and}\quad b=\begin{pmatrix}1-i&1\\1&1+i\end{pmatrix}.$$

关于这两个特定的矩阵，我们稍后会详细解释它们的推导过程。注意到 $\tr{a}=\tr{b}=2$，因此 $a$ 和 $b$ 都是抛物型变换。观察 [图 7.4](#fig-7.4) 中 Schottky 圆的排列，可以看到 $a$ 的不动点是 0，即圆 $C_a$ 和 $C_A$ 的切点。在 [图 7.3](#fig-7.3) 中，你可以看到两条相切的圆链从上下两侧分别向 0 点逐渐嵌套收缩。相同的现象也出现在 $-i$ 处，这既是圆 $C_b$ 和 $C_B$ 的切点，也是变换 $b$ 的不动点。尽管存在额外的切点，生成元 $a$ 和 $b$ 依然将初始的相切链 $C_a,C_b,C_A,C_B$ 中的圆配对。这意味着要实现圆链的无穷嵌套，我们仍需满足交换子条件 $\tr{abAB}=2$，这一点并不难验证。

:::{.simple}
We have been speaking as if there is only one Apollonian gasket, but could we not get different gaskets by starting with different tangent chains? Not really, because it turns out that any chain of three tangent circles can be conjugated to any other three. As you can work out in Project 7.1, this stems from the fact that there is always a Möbius map carrying any three points to any other three. Since the gasket is activated by its initial ideal triangle, and since the procedure at each step consists in adding incircles, a Möbius map which conjugates one ideal triangle to another carries the whole gasket along in its wake.

This explains why it makes sense to talk about the Apollonian gasket, because up to conjugation by Möbius maps there is really only one.
:::

我们此前的讨论似乎一直都默认了阿波罗尼奥斯垫片是独一无二的，但如果我们从不同的初始相切圆链出发，难道不会得到不同的垫片吗？其实不能。事实上，任何由三个相切圆组成的链，都可以通过某个莫比乌斯变换转化为另一组任意的相切圆链。正如你在 [项目 7.1](#proj-7.1) 中可以推导出的那样，这源于总有一个莫比乌斯映射将任意三个点映射到其他任意三个点。由于垫片的构造源于其初始理想三角形，而每一步的操作都是添加内切圆，一个将一个理想三角形共轭到另一个理想三角形的莫比乌斯映射会将整个垫片一起带走。

这就解释了为什么谈论“阿波罗尼奥斯垫片”是有意义的，因为在莫比乌斯变换的共轭意义下，归根结底，阿波罗尼奥斯垫片只有一个。

![Figure 7.5. The strip gasket. This shows the gasket as it appears when we conjugate so that the extra tangency point of $C_b$ and $C_B$ is at $\infty$. Any parabolic with a fixed point at $\infty$ is a Euclidean translation, in this case $b(z)=z+2$, which explains the translational symmetry along the infinite strip. \
图 7.5. 带状垫片。图中展示了当我们进行共轭变换，使得 $C_b$ 和 $C_B$ 的额外切点位于 $\infty$ 处时，垫片的样貌。任何以 $\infty$ 为不动点的抛物型变换都是欧几里得平移，在本例中为 $b(z)=z+2$，这解释了沿着无限带的平移对称性。](/images/indra/fig-7.5.jpg){width=600 #fig-7.5}

另一个著名的垫片版本可以在 [图 7.5](#fig-7.5) 中看到。为了得到这个，我们进行了共轭，使得 $C_a$ 和 $C_A$ 在 0 处相切，因此它们是垂直线。映射 $a$ 和 $b$ 现在在 $0$ 处有一个不动点。该群的生成元为：

$$a=\begin{pmatrix}2&-i\\-i&0\end{pmatrix}\quad\text{and}\quad b=\begin{pmatrix}1&2\\0&1\end{pmatrix}.$$

# Pinching tiles

![Figure 7.6. Dr. Stickler meets Apollonius. Placing Dr. Stickler in the Apollonian gasket, we let the group of symmetries carry him around. He appears exactly in those disks which were pink in Figure 7.4. If we had started him off in a white one, his images would fill the white disks instead. The symmetry $a$ is parabolic and on both sides of its fixed point 0, circles of Sticklers are streaming out. A startling feature is the circle of Sticklers streaming out from and into 1. Every alternate Stickler is standing on his head! The upright Sticklers are just powers of $abAB$
(which fixes 1) applied to the Stickler standing on the right hand horizontal axis, while the upside down ones are the images of this same Stickler under $(abAB)^nA$. \
图 7.6. Stickler 博士邂逅阿波罗尼奥斯分形。我们将 Stickler 博士置于阿波罗尼奥斯垫片中，然后让对称群带他四处转转。结果，他恰好出现在 [图 7.4](#fig-7.4) 里那些粉红色的圆盘中。若是他最初出现在某个白色圆盘中，那么他的身影就会填满所有的白色圆盘。对称 $a$ 是抛物型的，在它的不动点 0 的两侧，成群的 Stickler 博士正沿着圆圈向外扩散。最令人惊奇的是，在坐标 1 附近，竟然出现了一圈 Stickler 博士首尾相连、双向流动的奇妙图案。更绝的是，相邻的 Stickler 博士还头朝上、头朝下交替出现。那些站得笔直的 Stickler 博士，是通过不断对右侧水平轴上那位 Stickler 施加变换 $(abAB)^n$（该变换以 1 为不动点）得到的。而那些倒立的 Stickler 博士，则是这位 Stickler 在变换 $(abAB)^nA$ 作用下的映射结果。](/images/indra/fig-7.6.jpg){width=600 #fig-7.6}

:::{.simple}
Figure 7.6 is a wonderful picture of what happened when we introduced Dr. Stickler to Apollonius! It is a pretty intricate arrangement, so let’s take a bit of time understanding what has happened to the tiles. To get a grasp on the situation, look back at the three pictures in Figure 7.4, and watch the progression across the three frames. On the left the limit set is a loop or quasicircle, so the ordinary set - what is left when you take away the limit set - has two parts, a pink inside and a white outside. In the central picture, the pink part has collapsed into a myriad of tangent disks, and the red Schottky circles $C_a$ and $C_A$ touch at 0. On the right, the gasket group, the ‘horns’ of the pink region have also come together, causing the white outside to fracture into disks as well. Notice how the memory of which was inside and which was outside still persists, because what were the ‘inside’ disks are pink while the ‘outside’ ones are white.
:::

[图 7.6](#fig-7.6) 是一幅精彩的画面，生动展现了当我们邀请 Stickler 博士探索阿波罗尼奥斯分形时所发生的奇妙事情！图中的结构相当复杂，因此我们不妨花些时间，仔细剖析图案的变化。要理解这一过程，不妨回顾 [图 7.4](#fig-7.4) 的三幅子图，并观察这三帧之间的演变：左图中的极限集是一个回路或拟圆，因此普通集（即去掉极限集后剩下的部分）分为粉色的内部和白色的外部。中间的图中，粉色区域已收缩成无数相切的圆盘，而红色的肖特基圆 $C_a$ 和 $C_A$ 在 0 处相切。右图则展示了垫片群，其中粉色区域的“触角”也汇聚在一起，使得白色外部区域也裂解成圆盘。令人惊奇的是，尽管整体结构支离破碎，内外区域仍清晰保留着原始的记忆——曾经“内部”的圆盘依旧是粉色，而“外部”的圆盘依旧是白色。

:::{.simple}
In each picture, the initial Schottky circles are blue and red. Watch them to follow the fate of the tiles. On the left, as usual for a kissing Schottky group, they surround the central inner four sided tile. If we transported this tile around by the group, we would see a tessellation　of the pink region similar to the one in Figure 6.6. (There is also an outer tile, the region outside the four Schottky circles, which as usual you can see more clearly by imagining it on the Riemann sphere.) The inner and outer parts of the ordinary set are invariant under the group, so if you apply any transformation of the group to any tile in the pink region ‘inside’ the limit set, you get another tile which is also ‘inside’.
:::

在每幅图中，最初的 Schottky 圆分别是蓝色和红色。仔细观察它们的变化，有助于追踪瓷砖的运动轨迹。在左图中，和典型的“亲吻” Schottky 群一样，这些圆环绕着中央的四边形瓷砖。如果我们将这块瓷砖沿着群的变换不断移动，就会在粉色区域中形成类似于 [图 6.6](#fig-6.6) 的镶嵌图案（此外，还有一个外部瓷砖，即位于四个 Schottky 圆之外的区域，通常，通过在黎曼球面上想象它的位置，可以更清楚地看到它的轮廓）。普通集的内部和外部在群作用下各自保持不变，因此，如果对极限集“内部”粉色区域中的某块瓷砖施加群中的某个变换，得到的仍会是另一块位于“内部”的瓷砖。

:::{.simple}
In the central picture, where $a$ has become parabolic, the inner tile has been pinched into two halves. Each half-tile is an ideal triangle, with two red sides and one blue. You should think of this pair of triangles as one composite two-part tile. Moved around by the group, the composite tile will cover all the pink circles. There is an outer tile in this picture too, which (on the Riemann sphere) remains in one piece.

On the right, in the gasket group, both $a$ and $b$ have been pinched so that now $C_b$ and $C_B$ also tuch at $-i$. Now there are four basic half-tiles. The two pink ones will produce a tiling of the pink circles and the white ones will make a tiling of the white circles. In the glowing gasket picture, these four tiles are black. The upper two ‘horizontal’ ideal triangles are the remnants of the inner Schottky tile, while the lower ‘vertical’ triangle is a remnant of the outer one. If you look carefully, you can just see its twin peeping out in the bottom centre of the page.
:::

在中央的图片中，$a$ 已变成了抛物型，内部的瓷砖被挤压成了两半。每个半瓷砖都是一个理想三角形，带有两条红边和一条蓝边。你可以把这对三角形视作一个由两部分组成的复合瓷砖。通过群的作用，这个复合瓷砖将覆盖所有的粉色圆盘。图中还有一个外部瓷砖，它在黎曼球面上依然保持完整。

在右侧的垫片图中，$a$ 和 $b$ 都被挤压变形，使得 $C_b$ 和 $C_B$ 现在也在 $-i$ 处相切。此时出现了四个基本的半瓷砖。两块粉色的会铺满粉色圆盘，而两块白色的则会铺满白色圆盘。在那幅发光的垫片图中，这四块瓷砖都呈现为黑色。上方的两个“水平”理想三角形是内部 Schottky 瓷砖的残迹，而下方的“垂直”三角形则是外部瓷砖的残迹。仔细观察，你会在页面底部中央隐约发现它的孪生兄弟正悄悄探出头来。

:::{.simple}
Now we can go back to the picture of Dr. Stickler meeting Apollonius. The party is taking place in the remnants of the ‘pink’ circles. If you compare with the half-tiles in Figure 7.4, something rather odd has happened to Dr. Stickler - when the original tile split in two, his head ended up in the green half-tile and his feet in the blue one. Fortunately, there is a transformation of the group (namely $B$) which carries the blue Stickler to the green one, moving the blue half-tile containing the blue feet to the yellow half-tile containing the green feet. Had we not pointed out his difficulties you might not even have noticed that anything was wrong. After gluing the yellow half-tile to the green halftile, the relieved (but still slightly greenish) Dr. Stickler stands reunited in a new and complete tile whose images under the group map to all the Sticklers in the picture.
:::

现在我们可以回到 Stickler 博士与阿波罗尼奥斯相遇的画面。聚会正在“粉色”圆圈的残迹中举行。对照 [图 7.4](#fig-7.4) 中的半瓷砖，你会发现 Stickler 博士身上发生了一件相当奇怪的事——当原始瓷砖裂成两半时，原始瓷砖裂成两半时，他的头跑到了绿色半瓷砖里，而他的脚却留在了蓝色半瓷砖上。幸好，群中有一个变换（即 $B$）可以将蓝色的 Stickler 带到绿色 Stickler 的位置，把装着蓝色脚丫的蓝色半瓷砖挪到装着绿色脚丫的黄色半瓷砖上。要不是我们特意指出这种窘况，你可能根本没发现哪里不对劲。等到黄色半瓷砖和绿色半瓷砖粘合完毕，那位如释重负（却仍然带着一丝“绿意”）的 Stickler 博士终于又完整地站在了一块崭新的瓷砖上。通过群的映射，这块瓷砖的影像铺展开来，构成了画面中所有 Stickler 博士的身影。

# And pinching surfaces

:::{.simple}
What happened to the tiles in the last section, has, of course, also an interpretation in terms of surfaces. Looking back to the picture on p. 190 which showed how tiles were glued up in a kissing Schottky group, we can work out what happens when we bring the four circles together to make the gasket. It takes a bit of stretching and squeezing to do this, which we have illustrated in Figure 7.7.

The result, shown in the last panel, is our old friend the pretzel with three circles pinched to points or cusps: the waist as in the last chapter and, in addition, loops around the top and bottom tori. Both top and bottom are now ‘spheres’ with three cusps or punctures each. One pair of cusps on each sphere are joined together like ‘horns’, and these two ‘horned spheres’ are themselves joined together at the last two cusps.
:::

上一节中瓷砖的演变过程，当然也可以从曲面角度得到诠释。回顾第 190 页展示的亲吻 Schottky 群的基本域粘合过程的示意图，我们可以推导出当将四个圆粘合为垫片群时会发生什么。这一过程需要一些拉伸和压缩，我们在 [图 7.7](#fig-7.7) 中进行了直观展示。

最终结果呈现于最后一幅示意图中，正是我们熟悉的椒盐脆饼造型——三个圆周被压缩为尖点（cusp）：其中一个是上一章提到的“腰部”尖点，另外两个则是围绕顶部和底部的环面。此时，顶部与底部都变成了各自有三个尖点（或称穿孔）的"球面"。每个球面上的一对尖点像"犄角"一样连接在一起，而这两个“带角球面”则通过它们剩下的两个尖点相互连接。

:::{.simple}
The gasket group is called doubly cusped because we have pinched two extra loops, $a$
and $b$. It is also sometimes called maximally cusped, because, after all this squeezing, there are no more curves left to pinch. In Chapter 9, we shall see that you can make many variants of the gasket group by imposing more complicated relationships between the curves we choose to pinch on the top and bottom halves of the pinched pretzel.
:::

垫片群被称为双尖群，因为我们挤压了两个额外的环路 $a$ 和 $b$。它也常被称为“极大尖群”，因为经过这般操作后，已不存在可供进一步挤压的曲线。在第九章中我们将看到，通过在挤压后的椒盐卷曲曲面（pretzel）的上下半部之间，对选定挤压曲线施加更复杂的关联约束，可以构造出多种垫片群的变体。

:::{.simple #fig-7.7}
Figure 7.7. Pinching curves. How gluing up the gasket configuration of tangent circles leads to a pair of triply-punctured spheres. The $a$ and $b$ curves we have to shrink are are marked $L$ and $M$. Instead of pulling the upper and lower partially glued-up cylinders logether right away, as we did in Figure 6.16, it now takes some effort first to twist them relative to each other in such a way that when we glue-up, the dotted loops are in their proper position ready to be shrunk.

图 7.7. 捏合曲线。如何通过粘合垫片的切圆得到一对带有三穿孔球面。需要收缩的 $a$ 和 $b$ 曲线分别标记为 $L$ 和 $M$。与 [图 6.16](#fig-6.16) 中直接粘合上下圆柱体的操作不同，此时需要先使两者相对扭转，确保粘合时虚线环处于正确位置以便后续收缩。

![BEGIN WITH A PLANE WITH FOUR HOLES, EACH OF WHICH JUST TOUCHES THREE OTHERS, WHAT HAPPENS WHEN WE GLUE $A$ TO $a$ (THE SMALL ONE) AND $B$ TO $b$? \
从一个带有四个孔的平面开始，每个孔都与另外三个孔相切。当我们将 $A$ 粘合到 $a$（较小的孔），并将 $B$ 粘合到 $b$ 时，会发生什么？](/images/indra/fig-7.7-1.jpg){width=200}

![FIRST PULL a AWAY FROM A AND B AWAY FROM b ALONG THE ARCS $L$ AND $M$. HOW WE SEE A DISTORTED BUT FAMILIAR PICTURE: $ABab$. \
首先，沿弧线 $L$ 将 $a$ 从 $A$ 处拉开，沿弧线 $M$ 将 $B$ 从 $b$ 处拉开。此时会呈现一个扭曲但熟悉的图案：$ABab$。](/images/indra/fig-7.7-2.jpg){width=200}

![ADO THE POINT AT INFINITY TO WRAP UP THE PLANE. \
通过添加无穷远点使平面闭合。](/images/indra/fig-7.7-3.jpg){width=200}

![STRETCH TO MAKE THIS FAMILIAR SURFACE. NOTE ARCS $L$ AND $M$. \
拉伸形成我们熟悉的曲面。注意观察弧线 $L$ 和 $M$。](/images/indra/fig-7.7-4.jpg){width=200}

![NOW SOMETHING STRANGE: PULL TOGETHER THE TOP HALVES OF $A$ AND $a$ AND THE BOTTOM HALVES OF $B$ AND $b$. \
进行奇怪的操作：将 $A$ 和 $a$ 的上半部分、$B$ 和 $b$ 的下半部分别拉到一起。](/images/indra/fig-7.7-5.jpg){width=200}

![GUE TOP OF $A$ TO TOP of $a$, BOTTOM OF $B$ TO BOTTOM OF $b$. \
将 $A$ 的顶部和 $a$ 的顶部粘在一起，将 $B$ 的底部和 $b$ 的底部粘在一起。](/images/indra/fig-7.7-6.jpg){width=200}

![NOW JOIN THE REST OF $A$ TO $a$ ANP $B$ TO $b$. \
继续完成 $A$ 与 $a$、$B$ 与 $b$ 剩余部分的粘合。](/images/indra/fig-7.7-7.jpg){width=200}

![FINALLY, SHORTEN THE ARCS $L$ AND $M$ … \
最终收缩弧线 $L$ 和 $M$ …](/images/indra/fig-7.7-8.jpg){width=200}

![UNTIL EACH ARC SHRINKS TO A POINT, MAKING TWO TRIPLY-PUNCTURED SPHERES. \
直至每个弧线都坍缩为一点，形成两个三穿孔球面。](/images/indra/fig-7.7-9.jpg){width=200}
:::

# Tiling the inner disks

:::{.simple}
Figure 7.6 is made up of lots of disks full of Dr. Sticklers, each tiled by ideal triangles shown in grey. These disks are the remnants of the pink region in Figure 7.4. For most of the rest of this chapter, we shall be occupied with the tiling of just one of these disks. The same tiling fills out the insides of each of the glowing circles in Figure 7.3. The group of symmetries which goes with this very special disk tessellation is called the modular group and has been the well-spring of a huge body of mathematics.
:::

[图 7.6](#fig-7.6) 由无数布满 Sticklers 博士身影的圆盘构成，每个圆盘都被灰色的理想三角形所镶嵌。这些圆盘正是 [图 7.4](#fig-7.4) 中粉色区域的残迹。在本章接下来的大部分篇幅里，我们将专注于研究其中一个圆盘的密铺结构。同样的密铺图案也出现在 [图 7.3](#fig-7.3) 中每个发光圆圈的内部。这种独特的圆盘镶嵌的对称群称为模群，它一直是众多数学成果的源泉。

:::{.simple}
Since the tiling in each disk is the same, we may as well focus on the large disk through -1 and 0, shown in yellow in Figure 7.8. To understand how these ideal triangle tiles cover the yellow disk we need to find the subgroup of all the transformations in the gasket group which map the inside of this disk to itself. This subgroup (which is of course also a group in its own right), or any of its conjugates, is what we call the modular group. The basic tile is made up of two ideal triangles, the ones coloured green and yellow in Figure 7.6. The two triangles together form one of our familiar four-sided pinched-off tiles with four circular arc sides. Moved around by the modular group, they tile the whole yellow disk.
:::

由于每个圆盘中的密铺方式相同，我们可以将注意力集中在通过 -1 和 0 的大圆盘上，这在 [图 7.8](#fig-7.8) 中以黄色部分表示。为了理解这些理想三角形如何覆盖黄色圆盘，我们需要找出垫片群中所有将圆盘内部映射到自身的变换子群。这个子群（显然，它本身也是一个群），或者它的任何共轭子群，便是我们所称的模群。基本的瓷砖由两个理想三角形组成，即 [图 7.6](#fig-7.6) 中绿色和黄色的三角形。这两个三角形合在一起，构成了我们熟悉的四边弧形瓷砖。通过模群的作用，它们密铺了整个黄色圆盘。

![Figure 7.8. The set-up of tangent circles for the modular subgroup. The left frame is just to get oriented. The red circles $C_A$ and $C_a$, together with the level 2 green circles $B(C_a)=C_{Ba}$ and $B(C_A)=C_{BA}$ form the boundary of the new four-sided tile. The arrows show how $a$ pairs $C_A$ to $C_a$ and $b$ pairs $C_B$ to $C_b$. The boundary of the yellow disk is the limit set of the modular group generated by $a$ and $BAb$. \
图 7.8. 模群的切线圆配置。左侧子图仅用于帮助定位。红色圆圈 $C_A$ 和 $C_a$，以及二级绿色圆圈 $B(C_a)=C_{Ba}$ 和 $B(C_A)=C_{BA}$ 共同构成了新四边形瓷砖的边界。箭头指示了变换 $a$ 如何将 $C_A$ 和 $C_a$ 配对，变换 $b$ 如何将 $C_B$ 和 $C_b$ 配对。黄色圆盘的边界是由 $a$ 和 $BAb$ 生成的模群的极限集。](/images/indra/fig-7.8.jpg){width=600 #fig-7.8}

:::{.simple}
We worked out the labels of the boundary circles $C_a, C_A, C_{BA}$ and $C_{Ba}$ in Figure 7.8 of the four-sided tile by going to part of the level-two Schottky chain for the gasket group. (You may find it easiest to check the arrangement in a picture like the left frame of Figure 7.4 without all the extra gasket tangencies first.) Notice the four tangency points of these circles are all on the boundary of the yellow disk. As you can see, the four circles form a new chain of tangent circles. As usual, $a$ pairs $C_A$ to $C_a$. In addition, $BAb$ pairs $C_{Ba}$ to $C_{BA}$ because:

$$BAb\left(C_{Ba}\right) = BAb\left(B\left(C_a\right)\right) = BA\left(C_a\right) = B\left(C_A\right) = C_{BA}.$$

Inside the gasket group we have found another mini-chain of four tangent circles, together with a pair of transformations which match them together in pairs!
:::

我们通过研究垫片群的二级 Schottky 链的局部结构，确定了 [图 7.8](#fig-7.8) 中四边形瓷砖的边界圆 $C_a,C_A,C_{BA}$ 和 $C_{Ba}$ 的标签。（建议首先参考 [图 7.4](#fig-7.4) 左图中圆的排列，暂时忽略所有额外的垫片切点，会更容易理解）。值得注意的是，这些圆的四个切点全部位于黄色圆盘的边界上。正如你所见，这四个圆形成了一个新的切圆链。按照惯例，变换 $a$ 将圆 $C_A$ 和 $C_a$ 配对。此外，变换 $BAb$ 将圆 $C_{Ba}$ 和 $C_{BA}$ 配对，原因如下：
$$BAb\left(C_{Ba}\right) = BAb\left(B\left(C_a\right)\right) = BA\left(C_a\right) = B\left(C_A\right) = C_{BA}.$$
在垫片群中，我们发现了一个由四个相切圆组成的迷你链，以及一对将它们成对匹配的变换！

:::{.simple}
This construction shows that the modular group is a new kind of ‘necklace group’, made by disregarding all the rest of the gasket and looking only at the disks produced by acting with $a$ and $BAb$ on the four circles which bound the new tile. The new group is generated by the transformations $a$ and $BAb$. Indeed in Figure 7.3, you can actually pick out chains of image disks nicely shrinking down onto the glowing limit circle through -1 and 0 . The only difference from the kissing Schottky groups we met in the last chapter is that the two generators pair not opposite circles but adjacent ones. As we shall explain in more detail on p. 213 ff., the image circles shrink because $a,BAb$ and their product $aBAb$ are all parabolic.
:::

这一构造表明，模群是一种新型的“项链群”，它是通过忽略垫片的其余部分，仅关注由变换 $a$ 和 $BAb$ 作用于新瓷砖边界的四个圆所产生的圆盘而形成的。这个新群由变换 $a$ 和 $BAb$ 生成。实际上，在 [图 7.3](#fig-7.3) 中，你可以清晰地看到一串映像圆盘，它们逐渐缩小并收敛到经过点 -1 和 0 的发光极限圆上。这与上一章讨论的“接吻式 Schottky 群”的唯一关键时，这两个生成元配对的不是相对的圆，而是相邻的圆。正如我们将在第 213 页及以后章节中详细解释的那样，这些像圆之所以缩小，是因为 $a,BAb$ 以及它们的乘积 $aBAb$ 都是抛物型变换。

:::{.simple}
The same pattern of pairing circles is repeated all over the gasket. Every pink disk is the image of the yellow one under some element in the gasket group, which conjugates our modular group to another ‘modular group’ acting in the new disk. The white disks are different from the pink ones, because you can never get from pink to white using transformations in the gasket group. However you can still find a chain of four tangent circles matched in the same pattern, as described in [Project 7.4](#proj-7.4).
:::

在垫片的每一个局部区域，都能观察到完全相同的圆配对模式。每个粉色圆盘均可视为黄色圆盘经垫片群中某个变换作用后的像——这个变换元素会将我们原本的模群共轭到一个新的"模群"，而新模群将作用在对应的粉色圆盘上。白色圆盘与粉色圆盘存在本质区别：垫片群中的任意变换都无法将粉色圆盘映射为白色圆盘。不过，我们仍能找到四个相切圆构成的配对链，其模式与前文所述完全一致（具体构造方法详见项目 7.4）。

:::{.simple}
You might well imagine that we should be set to repeat everything we did in the last chapter. By taking four tangent circles and pairing them in this new pattern we should presumably get a whole new lot of quasifuchsian groups. Not so! It turns out that the rigours imposed by specifying that the two generators and their product are all parabolic actually ‘freeze’ the group. Without any mention of circle chains, we prove in Note 7.1 the remarkable fact that all groups made with pairing conditions like this are, up to conjugation, ‘the same’. What this means in more detail is this. Suppose that $U$ and $V$ are any two parabolic Möbius transformations with the property that $UV$ is also parabolic, and such that the fixed points ${\rm Fix}\,U$ and ${\rm Fix}\,V$ of $U$ and $V$ are not the same. Then there is always a conjugating map $M$ such that:
$$
MUM^{-1} = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}, \quad MVM^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}.
$$
This explains why there are so many circles in the gasket group, and why you get an identical tiling pattern in each one.
:::

你或许会以为，我们接下来要做的就是重复上一章的研究过程。毕竟，如果我们选取四个相切圆并按照这种新模式进行配对，似乎理所当然会得到一大堆新的拟富克斯群。然而并非如此！事实证明，要求两个生成元及其乘积都是抛物型变换这一刚性条件，实际上"冻结"了群的结构。在 [注记 7.1](#note-7.1) 中，我们甚至无需提及圆链的概念，就证明了这样一个惊人的结论：所有满足这种配对条件的群，在共轭意义下其实都是“相同”的。具体而言，设 $U$ 和 $V$ 是任意两个抛物型莫比乌斯变换，满足 $UV$ 仍为抛物型，且两者的不动点 $\fix U$ 与 $\fix V$ 互异，那么，总存在一个共轭变换 $M$，使得：
$$
MUM^{-1} = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}, \quad MVM^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}.
$$
这也解释了为何在垫片群（gasket group）中会出现那么多的圆，以及为何每个圆内的镶嵌图案都一模一样。

:::{.note #note-7.1}
**Note 7.1: Uniqueness of the modular group** \

**注 7.1：模群的唯一性**

Suppose that $U$, $V$ and $UV$ are all parabolic (and therefore not the identity!) and the fixed point of $U$ is $z_U$ and the fixed point of $V$ is $z_V$. We are trying to conjugate $U$ and $V$ to the generators of the modular group. We have seen that we can find a Möbius transformation $M$ that maps $z_U$ to $0$ and $z_V$ to $\infty$. Conjugating our original transformations $U$ and $V$ by $M$ arranges that $MUM^{-1}(0)=0$ and $MVM^{-1}(\infty)=\infty$, and still the two transformations $MUM^{-1}$ and $MVM^{-1}$ are parabolic. Since we can simultaneously conjugate them in this way, we may just as well assume the original transformations $U$ and $V$ have fixed points $0$ and $\infty$, respectively.

A parabolic transformation that fixes $\infty$ is always conjugate to any other, up to a minus sign. (See Chapter 3.) Let's arrange by conjugation and possibly multiplying by -1 that $V$ corresponds to the matrix $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.　Now all that’s left is $U$. Since $U(0)=0$, after again possibly multiplying by -1, we can conclude that the matrix of $U$ is
$$
\begin{pmatrix} 1 & 0 \\ x & 1 \end{pmatrix}
$$
for some number $x$.

That brings us to the last hypothesis that $UV$ is parabolic. Let's multiply this out:

$$
\begin{pmatrix} 1 & 0 \\ x & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ x & 1+2x \end{pmatrix}.
$$

The trace of $UV$ under these assumptions is $2 + 2x$. This is $\pm 2$ for precisely two values of $x$, namely, $x = -2$ and $x = 0$. In the latter case, $U$ is the identity, which we are definitely excluding. That means $x = -2$, and we have shown that $U$ and $V$ are simultaneously conjugate to
$$
\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \text{ and } \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}.
$$
(We may have to multiply one or both matrices by -1 to arrange that they both have trace 2.)

假设 $U$, $V$ 和 $UV$ 均为抛物型变换（因此不是恒等变换！），且 $U$ 的不动点是 $z_U$，$V$ 的不动点是 $z_V$。我们的目标是将 $U$ 和 $V$ 共轭变换为模群的生成元。我们已经看到，可以找到一个莫比乌斯变换 $M$，它将 $z_U$ 映射到 $0$，$z_V$ 映射到 $\infty$。通过 $M$ 对原变换 $U$ 和 $V$ 进行共轭后，新变换 $MUM^{-1}$ 将保持 0 不变，$MVM^{-1}$ 将保持 $\infty$ 不变，且两者仍为抛物型变换。既然这种共轭可同步完成，我们不妨直接假设原变换 $U$ 和 $V$ 的不动点分别是 $0$ 和 $\infty$。

固定 $\infty$ 的抛物型变换在相差一个符号的意义下彼此共轭（参见第 3 章）。通过适当共轭及可能的符号调整，可以使 $V$ 对应于矩阵 $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$。此时仅需确定 $U$ 的形式。由于 $U(0) = 0$，经可能的符号调整后，$U$ 的矩阵必为：
$$
\begin{pmatrix} 1 & 0 \\ x & 1 \end{pmatrix}\quad (x\in\mathbb{C}).
$$
最后利用 $UV$ 是抛物型这一条件。计算乘积：
$$
UV=\begin{pmatrix} 1 & 0 \\ x & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ x & 1+2x \end{pmatrix}.
$$
此时 $UV$ 的迹是 $2 + 2x$。抛物型变换的迹需满足 $|\tr|=2$，这恰好对 $x$ 的两个值成立，即 $x = -2$ 和 $x = 0$。当 $x=0$ 时，$U$ 退化为恒等变换（已排除），因此必有 $x=−2$。由此可知 $U$ 和 $V$ 可共轭于矩阵：
$$
\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \text{ and } \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}
$$
（必要时可对其中一个或两个矩阵取负，以确保其迹均为 2）
:::

# The modular group of arithmetic

:::{.simple}
The result just discussed shows that the modular group is conjugate to a very famous group of great importance in number theory. It is made by arranging the four Schottky circles with their tangency points at $-1,0,1$ and $\infty$. You can see these, coloured red and green, in the left frame of Figure 7.9. Since one of the tangency points is the point at infinity, two of the circles show up as green vertical lines. These green lines are paired by $b=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, while the two red circles tangent at 0 are paired by $a=\begin{pmatrix}1&0\\-2&1\end{pmatrix}$. Notice how $a$ and $b$ match adjacent circles in the chain in exactly the pattern of the red and green arrows in Figure 7.8. In fact, as you can easily calculate, $ab$ is the parabolic transformation $\begin{pmatrix}1&2\\-2&-3\end{pmatrix}$.
:::

刚刚讨论的结果表明，模群与一个在数论中极为著名且重要的群是共轭的。这个群是通过排列四个肖特基圆生成的，其切点分别位于 $-1, 0, 1$ 和 $\infty$。在 [图 7.9](#fig-7.9) 的左图中，这些圆分别以红绿两色呈现。由于其中一个切点是无穷远点，因此有两个圆在图中呈现为绿色的垂直直线。这两条绿色直线由变换 $b=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ 配对，而在原点 0 处相切的两个红色圆则通过变换 $a=\begin{pmatrix}1&0\\-2&1\end{pmatrix}$ 配对。请注意，变换 $a$ 和 $b$ 对相邻圆的配对方式，恰好与 [图 7.8](#fig-7.8) 中红绿箭头所示的模式完全一致。事实上，通过简单的计算即可验证，$ab$ 是抛物型变换 $\begin{pmatrix}1&2\\-2&-3\end{pmatrix}$。

![Figure 7.9. The modular tessellation of the upper half plane. The left frame shows the tiling or tessellation of the upper half plane by ideal triangles belonging to the smaller modular group coming from pairing tangent circles, while the right frame shows the richer tessellation associated to the full modular group with its added symmetries. Each tile on the left is subdivided into twelve tiles on the right. \
图 7.9. 上半平面的模群密铺。左图展示了通过配对相切圆生成的子模群对应的理想三角形密铺结构；右图则展示具有完整模群对称性的更加精细的密铺。左侧的每个瓷砖在右侧被细分为十二个小瓷砖。](/images/indra/fig-7.9.jpg){width=600 #fig-7.9}

:::{.simple}
It is no coincidence that the entries of these three matrices are integers. The right frame of Figure 7.9 is a more complicated picture which shows all the symmetries of the tiling on the left. Each ideal triangle has been subdivided into three hatched and three unhatched sub-triangles. (The sub-triangles are not quite ideal, because only one of their angles is 0 .) The group of symmetries of this more complicated tiling is, from the point of view of Möbius maps, the simplest group of all: just the set of all $2\times 2$ matrices $\begin{pmatrix}p&q\\r&s\end{pmatrix}$ with integer entries $p,q,r$ and $s$ and determinant $ps-qr$ equal to 1. To distinguish from the group of the left frame, we sometimes call it the full modular group. The matrices in the (smaller) modular group of the left picture are just those matrices with integer entries for which $q$ and $r$ are even and $p$ and $s$ are odd.
:::

这三个矩阵的元素都是整数，此现象绝非偶然。[图 7.9](#fig-7.9) 右侧的复杂图像完整呈现了左侧密铺图案的所有对称性。每个理想三角形都被剖分为三个阴影子三角形和三个非阴影子三角形。（这些子三角形并不完全是理想的，因为它们只有一个角为 0）。从莫比乌斯变换的角度来看，这个更复杂的密铺结构的对称群是最简单的：即所有元素为整数且行列式 $ps-qr$ 等于 1 的 $2\times2$ 矩阵 $\begin{pmatrix}p&q\\r&s\end{pmatrix}$ 构成的集合。为了与左图的对称群区分开来，该群常被称为全模群。而左侧密铺对应的（较小）模群则由满足特殊同余条件的整数矩阵构成——其 $q$ 与 $r$ 元素都是偶数，$p$ 与 $s$ 元素都是奇数。

:::{.simple}
There is a very beautiful connection between the modular tessellation and fractions: the points where the ideal triangles meet the real axis are exactly the rational numbers. Although it is something of a digression here, we want to take the time to explain the pattern, which turns out to be indispensible when we come to map making in Chapter 9.
:::

模镶嵌与有理数之间有着极其美妙的联系：理想三角形与实轴交点恰恰是有理数。虽然这一内容在此略显偏离主题，但我们希望花些时间来阐明这个规律，因为它在第 9 章的制图过程中将变得至关重要。

![Figure 7.10. The modular tiling from our ancestral home. The tessellation generated by the full modular group, conjugated over to the unit disk. This beautiful rendition is Figure 35 in Vol. 1 of Vorlesungen äber elliptischen Modulfunctionen by Klein and Fricke. \
图 7.10. 来自我们老家的模密铺。这是一个由完整模群生成的镶嵌图案，经过共轭变换映射到单位圆盘上。这幅精美的图像出自克莱因与弗里克合著的《椭圆模函数讲义》第一卷中的第 35 图。](/images/indra/fig-7.10.jpg){width=600 #fig-7.10}

:::{.simple}
Figure 7.11 shows the first few levels in the modular tessellation. The basic tile is the four-sided region, called an ideal quadrilateral, which was bounded by the coloured lines in Figure 7.9. Images of this ideal quadrilateral are shown bounded by solid arcs. The dotted arcs divide them into the two ideal triangles which we saw, half hatched and half white, on the left in Figure 7.9. As the group acts on the basic tile, we get more and more smaller and smaller tiles nesting down to the real axis. The vertices of all these tiles meet the real axis in points which are all fractions. Several things can be read off from a careful examination of this intricate pattern:

+ All vertices of the tiles are rational numbers $p/q$.
+ If $r/s$ and $p/q$ are two vertices of the same tile, then $ps - rq = \pm 1$.
+ If $r/s < p/q$ are the outer two vertices of a tile, then the third vertex between them is $(r + p)/(s + q)$.

Check this out! For instance, between $2/3$ and $1/2$, we get $(2 + 1)/(3 + 2)$, that is $3/5$.
:::

[图 7.11](#fig-7.11) 展示了模镶嵌的前几个层级。基本瓷砖是一个四边形，称为理想四边形，它由 [图 7.9](#fig-7.9) 中的彩色线条围成。实线弧显示了这个理想四边形的图像，而虚线弧将其分割成两个理想三角形，这两个三角形可以在  [图 7.9](#fig-7.9) 的左侧看到，一半是阴影，一半是空白。随着群对基本瓷砖的作用，我们得到越来越多、越来越小的瓷砖，逐层嵌套，直至延伸到实轴。所有这些瓷砖的顶点都与实轴相交，这些交点都是分数。仔细观察这个复杂的图案，我们可以得出以下几个结论：

+ 所有瓷砖的顶点都是有理数 $p/q$。
+ 如果 $r/s$ 和 $p/q$ 是同一瓷砖的两个顶点，则 $ps - rq = \pm 1$。
+ 如果 $r/s < p/q$ 是同一瓷砖的两个外顶点，那么它们之间的第三个顶点是 $(r + p)/(s + q)$。

验证一下吧！比如，在 $2/3$ 和 $1/2$ 之间，我们得到 $(2 + 1)/(3 + 2)$，即 $3/5$。

:::{.simple}
It's easy to see why this happens. As we have seen, a typical matrix in the modular group will look like

$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$$

where $p, q, r$ and $s$ are integers and $ps - rq = 1$. If $M$ acts on the vertices of the initial triangle with vertices $0 = 0/1, 1 = 1/1$ and $\infty = 1/0$, then we get the new triangle with vertices $M(0) = r/s, M(\infty) = p/q$ and $M(1) = (p + r)/(q + s)$. Assuming all four entries are positive, we have $r/s < (p + r)/(q + s) < p/q$ (you can see this by multiplying out). This is just what we found in Figure 7.11. If $p, q, r, s$ are not all positive, there are half a dozen other cases in which the order of the points $M(0), M(1)$ and $M(\infty)$ is different but we get the same result. The same thing happens if we start from the other triangle $M(-1), M(0), M(\infty)$.
:::

这个现象不难理解。我们知道，模群中的一个典型矩阵可以表示为
$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix},$$
其中 $p, q, r$ 和 $s$ 是整数，且满足 $ps - rq = 1$。如果矩阵 $M$ 作用于初始三角形的顶点，该初始三角形的顶点分别是 $0 = 0/1, 1 = 1/1$ 和 $\infty = 1/0$，那么变换后的新三角形的顶点将变成 $M(0) = r/s, M(\infty) = p/q$ 和 $M(1) = (p + r)/(q + s)$。假设 $p,q,r,s$ 都是正数，我们可以验证不等式 $r/s < (p + r)/(q + s) < p/q$ 成立（通过乘法可轻松验证）。这正是 [图 7.11](#fig-7.11) 所示的情况。如果 $p, q, r, s$ 并非全为正数，还有几种不同的情形，此时点 $M(0), M(1), M(\infty)$ 的顺序可能会改变，但结果仍然一致。类似地，若从另一个三角形 $M(-1), M(0), M(\infty)$ 出发，也会得到相同的结论。


:::{.simple}
Any two fractions $r/s$ and $p/q$ such that $ps - qr = \pm 1$ are called neighbours. Thus any two vertices of an ideal triangle in the modular tessellation are neighbours. If $p/q$ is a fraction, then, as we explain in Project 7.5, the process of finding its neighbours is essentially Euclid’s two thousand year old algorithm for finding the highest common factor of two numbers, surely one of the most useful and clever algorithms of all time. The rule for finding the ‘next’ point $\frac{p+r}{q+s}$ between two neighbours is every student’s dream of what addition of fractions should be. This simple form of fraction ‘addition’ is sometimes called Farey addition’, which one might want to symbolise with a funny symbol like:

$$
\frac{p}{q} \oplus \frac{r}{s} = \frac{p + r}{q + s}
$$

Farey addition gives a neat way of organising the rational numbers. Instead of the usual way of arranging them in increasing order (which is difficult, because you never know which one should come ‘next’), fractions can be described by a sequence of left or right moves, reflecting the choice at each stage of whether we choose the new pair of neighbours to the right, or the pair of neighbours to the left.
:::

任何两个分数 $r/s$ 和 $p/q$，若满足 $ps - qr = \pm 1$，则称它们为邻居。因此，模群镶嵌中的理想三角形的任意两个顶点都是邻居。如果 $p/q$ 是一个分数，那么正如我们在项目 7.5 中所解释的那样，寻找其邻居的过程，本质上就是欧几里得两千年前发明的最大公约数算法——这无疑是人类历史上最实用、最巧妙的算法之一。计算两个邻居之间“下一个”点 $\frac{p+r}{q+s}$ 的规则，正是每个学生心目中理想的分数加法方式。这种简单的分数“加法”有时被称为“法雷加法”（Farey addition），人们或许会用一个有趣的符号来表示它，比如：
$$
\frac{p}{q} \oplus \frac{r}{s} = \frac{p + r}{q + s}
$$

法雷加法提供了一种巧妙的方式来组织有理数。不像按递增顺序排列那样麻烦（毕竟你很难确定下一个该是谁），分数可以通过一系列左移或右移的操作来描述，这正对应了我们在每一步中选择将新的邻居对放置在左边还是右边的决定。

:::{.simple}
For positive fractions, the starting point are the two fractions $0/1$ and $1/0$, which we can regard as special honourary neighbours because they are connected by a side of our initial triangle, the vertical imaginary axis. Farey addition gives the in-between fraction $0/1\oplus 1/0=1/1$.

Now we have a choice: go to the 'left' and look in the interval between 0 and 1, or go to the 'right' and look in the interval between 1 and $\infty$. Suppose we are aiming for the fraction $3/5$. Then we turn to the left and apply the Farey addition $0/1 \oplus 1/1 = 1/2$. At the next stage, we choose the right interval and Farey add to get $1/2 \oplus 1/1 = 2/3$. Finally, we choose the left interval and Farey add $1/2 \oplus 2/3 = 3/5$. An exactly similar procedure could be applied to home in on any fraction $p/q$. Our choice of left-right turns is a driving map: $3/5$ is given by the instructions 'left, right, left'. This arrangement of fractions and sequence of right-left moves is closely related to a way of writing fractions as what are called continued fractions, explained in Note 7.2.
:::

对于正分数，我们的起点是两个特殊的分数：$0/1$ 和 $1/0$。我们不妨将它们视作“荣誉邻居”，因为它们由初始三角形的一条边——垂直的虚轴——连接在一起。利用 Farey 加法，我们可以在它们之间找到一个中间分数：$0/1 \oplus 1/0 = 1/1$。

接下来，我们需要做出选择：向“左”走，查看 0 到 1 之间的区间；还是向“右”走，查看 1 到 $\infty$ 之间的区间。假设我们的目标是分数 $3/5$。那么我们选择向左，执行 Farey 加法：$0/1 \oplus 1/1 = 1/2$。在下一步，我们转向右侧区间，并执行 Farey 加法得到：$1/2 \oplus 1/1 = 2/3$。最后，我们再次选择左侧区间，进行 Farey 加法：$1/2 \oplus 2/3 = 3/5$。

通过完全相同的步骤，我们可以找到任意分数 $p/q$。我们每次选择向左或向右的决策就像一张“导航图”：例如，分数 $3/5$ 对应的指令是“左、右、左”。这种分数的排列方式和左右转向的序列，与将分数表示为连分数的写法密切相关，详见 [注记 7.2](#note-7.2)。

:::{.note #note-7.2}
**Note 7.2: Continued fractions**

**注记 7.2 连分数**

Expressions like
$$\frac{3}{10} = \frac{1}{3 + \frac{1}{3}}$$
and
$$\frac{2}{19} = \frac{1}{2 + \frac{1}{9}}$$
are called continued fractions. It turns out that every fraction $p/q$ can be written in a similar way. Assuming $p/q$ is between 0 and 1, then you can always write it in the form
$$\frac{p}{q} = \frac{1}{a + \frac{1}{b + \frac{1}{c + \frac{1}{\cdots}}}}$$
where $a$, $b$, $c$ and so on are positive integers. Actually you can do the same even for an irrational number. The difference is that if the original number is irrational, then the terms $a$, $b$, $c$ and so on continue without end. The sequence $a, b, c, \ldots$ always describes the number of left-right turns in the Farey algorithm we described in the text.

If we successively 'reduce' a continued fraction by decreasing its final entry by 1, down to the value 1, and then shrinking its length, we recover the Farey process for homing in on the fraction. For example, for the fraction $3/5$, we get:
$$\begin{aligned}
\frac{3}{5} &= \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}\\
\frac{2}{5} &= \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}\\
\frac{1}{3} &= \frac{1}{2 + \frac{1}{1}}\\
\frac{1}{2} &= \frac{1}{2}.
\end{aligned}
$$
The process of turning a fraction into a continued fraction is very closely related to Euclid’s algorithm. We give some hints in Project 7.5.

像下面这样的表达式
$$\frac{3}{10} = \frac{1}{3 + \frac{1}{3}}$$
和
$$\frac{2}{19} = \frac{1}{2 + \frac{1}{9}}$$
被称为连分数。事实上，任何分数 $p/q$ 都可以以类似的方式表示。假设 $p/q$ 介于 0 与 1 之间，那么你总能将其写成如下的形式

$$\frac{p}{q} = \frac{1}{a + \frac{1}{b + \frac{1}{c + \frac{1}{\cdots}}}}$$
其中 $a$，$b$，$c$ 等是正整数。实际上，即使是无理数，你也可以用同样的方式表示。区别在于，如果原始数字是无理数，那么项 $a$，$b$，$c$ 等将无限延续下去。序列 $a, b, c, \ldots$ 始终对应于我们在正文中提到的 Farey 算法中的左右转弯次数。

如果我们通过将连分数的最后一项逐步减 1，直到其值为 1，然后缩短其长度，连续地“简化”一个连分数，我们就能恢复用于逼近该分数的 Farey 过程。以分数 $3/5$ 为例，经过这一过程，我们得到：

$$\begin{aligned}
\frac{3}{5} &= \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}\\
\frac{2}{5} &= \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}\\
\frac{1}{3} &= \frac{1}{2 + \frac{1}{1}}\\
\frac{1}{2} &= \frac{1}{2}.
\end{aligned}
$$

将一个分数转换成连分数的过程与欧几里得算法密切相关。我们在项目 7.5 中提供了一些线索。
:::


# The pairing pattern of the modular group

:::{.simple}
The modular group is a new kind of ‘necklace group’. It is still made by pairing four tangent circles, and the only difference from the kissing Schottky groups we met in the last chapter is that the generators pair not opposite circles but adjacent ones. Whenever we have an arrangement of paired tangent circles like this, something like the necklace condition on p. 168 must still be true, but because we are pairing the circles in a different pattern, we can expect that different elements must be parabolic to cause the image circles to shrink.
:::

模群是一种新型的“项链群”。它同样由四个相切的圆配对构成，不同之处在于，生成元这次配对的不是相对的圆，而是相邻的圆。每当我们遇到这样的相切圆配对排列时，类似于第 168 页提到的“项链条件”仍然必须成立。不过，由于这次采用了不同的配对模式，我们可以预见，只有某些不同的元素变成抛物型时，像圆才会缩小。

:::{.simple}
With the notation of the figure beside Box 20, we have $a(P) = R$ and $b(R) = P$, so that the four tangency points of the circles are $S = \text{Fix}(a)$, $Q = \text{Fix}(b)$, $P = \text{Fix}(ba)$, and $R = \text{Fix}(ab)$. By similar reasoning to that in Chapter 6, in order for the image circles near $S$ and $Q$ to shrink, the generators $a$ and $b$ must be parabolic. Moreover, $ba$ must also be parabolic, to make the circles shrink at $P$. Notice that $ab$ and $ba$ are conjugate (since $b(ab)b^{-1} = ba$), so saying that $ab$ or $ba$ must be parabolic is really one and the same thing. The wonderful thing is, that as we proved in Note 7.1, all groups with these three elements parabolic are automatically conjugate. This is so important to us that we summarize it in Box 20.
:::

根据 [框 20](#box20) 旁的图示，我们有 $a(P) = R$ 且 $b(R) = P$，因此四个切点分别是：$S＝\fix(a)$, $Q =\fix(b)$, $P =\fix(ba)$ 和 $R=\fix(ab)$。类似于第 6 章的推理，为使靠近 $S$ 和 $Q$ 的像圆收缩，生成元 $a$ 和 $b$ 必须是抛物型变换。而且 $ba$ 也必须是抛物型的，以确保圆在 $P$ 处收缩。需要注意的是，$ab$ 和 $ba$ 是共轭的（因为 $b(ab)b^{-1} = ba$），所以要求 $ab$ 或 $ba$ 是抛物型本质上是一回事。奇妙的是，正如我们在 [注记 7.1](#note-7.1) 中所证明的，所有包含这三个抛物型元素的群自动共轭。这一点对我们来说非常重要，因此我们在 [框 20](#box20) 中专门进行了总结。

:::{.simple}
Because the pattern of pairing circles is different, so is the arrangement in which the labelled circles are laid down in the plane. The Schottky circles in Figure 7.11 are labelled according to our usual rules, so for example, $C_{ba}$ still means the image of circle $C_a$ under the map $b$. However, if you look carefully, you will see that the order of the circles along the line is not the same as our original order round the boundary of the word tree on p. 104. The labels can be read off in their correct order from the revised version in Figure 7.12. (To see this you will have to twiddle the diagram around so the arrows from the vertex you are interested in are pointing ‘down’ rather than ‘up’.) There is a subtle difference from our original word tree, because there the cyclic order round a vertex was $a,B,A,b$ while now it is $a,A,b,B$. The ramifications of this seemingly minor change propagate down the tree.
:::

由于圆的配对方式改变，标记圆在平面上的排列方式也随之改变。[图 7.11](#fig-7.11) 中的 Schottky 圆仍按照我们通常的规则标记，例如，$C_{ba}$ 依然表示圆 $C_a$ 在映射 $b$ 下的像。然而，如果你仔细观察，就会发现这些圆沿着直线的排列顺序与第 104 页单词树边界上的原始顺序不同。修订后的 [图 7.12](#fig-7.12) 显示了正确的标签顺序。（为了看清这一点，你需要稍微调整图形，使得你关注的顶点的箭头指向“下方”而非“上方”）。与原单词树相比，这里有一个微妙的差异，源于顶点周围的循环顺序变化：原单词树中的顺序是 $a, B, A, b$，而现在则是 $a, A, b, B$。这一看似微小的变化将沿树结构逐级向下传播。

:::{.simple #box20}
**Box 20. The modular necklace**

**盒子 20：模群项链**

![](/images/indra/box20.jpg){width=200 .fig}

A modular necklace is a tangent chain of four circles in which adjacent disks are paired by two transformations $a$ and $b$ as in the figure in the margin. The transformations $a, b$ and $ab$ are all
parabolic and $S = Fix(a), Q = Fix(fc), a(P) = K, b(R) = P$ so that $P = \fix(ba)$ and $R = \fix(ab)$. The group generated by $a$ and $b$ is always conjugate to the 'standard' modular group generated by
$$
\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \text{ and } \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}
$$

The four points $P, Q, R$ and $S$ always lie on a circle (or line) which is the limit set of the group. The limit circle is perpendicular to all circles in the chain. Both inner and outer tiles have their sides matched in the same way and the surfaces made by gluing up these tiles are each spheres with three punctures or cusps.

一个模群项链是由四个相切的圆组成的链条，其中相邻的圆盘通过两种变换 $a$ 和 $b$ 配对，正如旁边图中的所示。变换 $a$、$b$ 和 $ab$ 都是抛物型的，且有 $S=\fix(a)$, $Q = \fix(b)$, $a(P) = R$, $b(R) = P$，从而得到 $P = \fix(ba)$ 和 $R = \fix(ab)$。由 $a$ 和 $b$ 生成的群总是与由
$$
\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \text{ and } \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}
$$
生成的“标准”模群共轭。

四个点 $P,Q,R,S$ 总是位于一个圆（或直线）上，这个圆（或直线）是该群的极限集。极限圆与链条中的所有圆都垂直。无论是内层还是外层的瓷砖，它们的边缘都以相同的方式匹配，通过将这些瓷砖拼接在一起形成的曲面，都是具有三个孔或尖点的球面。
:::

![Figure 7.12. The tree of words rearranged in the pattern of the modular group. \
图 7.12. 以模群模式重新排列的词汇树。](/images/indra/fig-7.12.jpg){width=600 #fig-7.12}

:::{.simple}
Because some elements in the modular group are parabolic, the infinite endpoints of certain paths down the word tree merge. For example, the path which starts at $a$ and heads always as far as possible to the left (from the viewpoint of a person walking down the branch) is $aaa\cdots$, ending at the attracting fixed point ${\rm Fix}^+a$. On the other hand, starting from $A$ and always turning right gives the path $AAA\cdots$, ending at ${\rm Fix}^+A$. Since $a$ is parabolic, the end points of these two paths are the same. In a similar way, other coincidences of endpoints are caused by the merging of the fixed points of $b$ and $ab$. You should compare the details with Figure 6.13.
:::

由于模群中存在抛物型元素，这导致单词树中某些路径的无限端点会发生合并。例如，从 $a$ 出发并始终尽可能向左延伸的路径（从沿分支下行的视角来看）可表示为 $aaa\cdots$，最终到达 $a$ 的吸引不动点 $\fix^+a$。反之，从 $A$ 出发始终右转的路径则为 $AAA\cdots$，终止于 $\fix^+A$。由于 $a$ 是抛物型元素，这两条路径的终点完全重合。类似地，$b$ 与 $ab$ 的不动点合并也会导致其他端点重合的现象。建议读者将这些细节与 [图 6.13](#fig-6.13) 进行对照分析。

:::{.simple}
A similar phenomenon is repeated at all levels. For example, the extreme left and extreme right paths starting at $aB$ end at $aB\bar{a}=\fix aBabA$, and $aB\bar{A} = \fix aBAbA$. Notice that $(aBAbA)^{-1}=aBabA$ and that $aBabA$ must be parabolic because it can be written $(aB)a(aB)^{-1}$, so the two endpoints merge. Every tangency point of the many circles in Figure 7.9 comes about because of a similar conjugacy to one of the three basic parabolics $a$, $b$ or $ab$.
:::

类似的现象在各个层次上反复出现。例如，从 $aB$ 出发的极左和极右路径分别终止于 $aB\bar{a} = \fix^+ aBabA$ 和 $aB\bar{A} = \fix^+aBAbA$。注意，$(aBAbA)^{-1} = aBabA$，而且 $aBabA$ 必然是抛物型的，因为它可以写成 $(aB)a(aB)^{-1}$，因此这两个端点最终重合。[图 7.9](#fig-7.9) 中众多圆的切点的出现，本质上都源于群元素与三个基本抛物元 $a$、$b$ 或 $ab$ 之一类似的共轭关系。

:::{.simple}
Let’s mention one final difference from the kissing Schottky groups in Chapter 6. The chain of four initial circles still divides the Riemann sphere into two four-sided tiles. However, because the pairing is different, so is the result of glueing up the tiles. Dr. Stickler is puzzling this out in Figure 7.13. In contrast to the pair of once-punctured tori we got in Figure 6.16, the outcome is now a pair of triply-punctured spheres.
:::

让我们提到与第 6 章中亲吻 Schottky 群的最后一个不同之处。四个最初的圆依然将黎曼球面划分为两个四边形瓷砖。然而，由于配对方式的不同，拼接后的结果也发生了变化。Stickler 博士正在 [图 7.13](#fig-7.13) 中对此进行思考。与我们在 [图 6.16](#fig-6.16) 中得到的那一对单孔环面相比，这次的结果是两个三孔球面。

![Figure 7.13. The gluing construction for the modular group. We start from a chain of four kissing circles giving a tile with two pieces, each a rectangle with four cusps. After gluing according to the modular recipe, we get two spheres, each with three cuspidal ‘punctures’ where they are joined. \
图 7.13. 模群的粘合构造。我们从一串四个相切的圆开始，得到一个由两块矩形瓷砖组成的图案，每块瓷砖上都有四个尖点。按照模群的粘合法则将这些部分粘合后，最终得到两个球面，每个球面上都有三个尖点状的“穿孔”，它们通过这些穿孔相连。](/images/indra/fig-7.13.png){width=600 #fig-7.13}

# The problem of gaps

![Figure 7.14. The gaps in the gasket. 图 7.14. 垫片中的缝隙。](/images/indra/fig-7.14.jpg){width=500 #fig-7.14}

:::{.simple}
We end this chapter by returning to the gasket and programming, with the confession that we cheated slightly to make pictures like Figures 7.1 and 7.4. Figure 7.14 shows the same picture plotted with our current algorithm. It contains a slight but thoroughly annoying imperfection if you look closely, you will see that at many places where we allege the limit set is ‘pinched’, it does not actually quite meet itself, but contains what are in reality quite large gaps.
:::

本章的结尾，我们再次回到垫片和编程的话题，并坦白在绘制 [图 7.1](#fig-7.1) 和 [图 7.4](#fig-7.4) 这类图像时，我们稍微做了一点“取巧”。[图 7.14](#fig-7.14) 展示的是使用我们当前算法绘制的同一图像。仔细观察的话，你会发现它存在一个微小但颇为恼人的缺陷：在许多地方，我们宣称极限集已经“收缩”的地方，实际上并没有完全闭合，反而留下一些肉眼可见的较大空隙。

:::{.simple}
Gaps and other imperfections in scientific pictures are a common nuisance, but they sometimes have greater significance. Mandelbrot recounted that his first detailed pictures of what later came to be known as the Mandelbrot set seemed to be plagued by specks of dirt. He and his assistant made a complete inspection of their program, computer system and printer, only to find that the specks were indeed correct. Investigating the specks led to the discovery of the vast and complicated spider web of filaments connecting all the various parts of that stunningly beautiful and now famous icon of the fractal world.
:::

科学图像中的空隙和其他瑕疵往往令人烦恼，但有时它们却蕴藏着更深的含义。曼德勃罗回忆道，他第一次绘制的、后来被称为曼德勃罗集的精细图像，总是被一些看似污点的斑点困扰。于是，他和助手对程序、计算机系统和打印机进行了彻底检查，结果发现这些斑点竟然是正确的。深入探究这些斑点，他们最终发现了一个复杂而庞大的蜘蛛网般的细丝结构，连接着曼德勃罗集各个部分，揭示了这个令人震撼、现已声名赫赫的分形世界象征的奇妙之处。

:::{.simple}
What is happening in the present case is that our algorithm develops tremendous inertia as it approaches the fixed points of parabolic or nearly parabolic words. It’s as if it starts to run in slow motion, simply not having the energy to go all the way out to the end. For this particular picture, the plotting threshold was a reasonably small 0.005 and the word length crept up to more than 400 as the plot approached the gaps. Still the visible gaps are substantially larger than 0.005.
:::

在这个例子中，我们的算法在接近抛物型或近似抛物型词的固定点时，表现出极大的惯性。就像是进入了慢动作，似乎完全没有足够的能量继续前进，无法走到最后。对于这幅特定的图像，绘图的阈值被设置得相当小，仅为 0.005，而随着绘图接近空隙，词的长度悄然增加到了超过 400。然而，尽管如此，空隙的大小依然明显超过了 0.005。

:::{.simple}
We could make better plots if we modified the algorithm to take account of the fact that the words $a$ and $b$ are parabolic. The basic idea is that we should plot not only points with repetends which are cyclic permutations of the basic commutator abAB (itself parabolic), but in addition those whose repetends are any of $a, A, b$ or $B$. Pictures like Figure 7.4, plotted with the new algorithm, are the measure of our success.
:::

如果我们修改算法，使其考虑到单词 $a$ 和 $b$ 是抛物型的这一特点，就能绘制出更精确的图形。基本思路是，我们不仅要绘制那些循环节为基本换位子 $abAB$（本身是抛物型）及其循环排列的点，还要包括那些循环节为 $a, A, b$ 或 $B$ 的点。采用新算法绘制的图像。比如 [图 7.4](#fig-7.4)，正是我们取得成功的标志。

:::{.simple}
Here is a more detailed look at the modified algorithm. We start by telling the program that the three parabolic elements $a, b$ and $abAB$ are 'special'. For each generator, the program then determines the repetends it must consider when enumerating the infinite words. They are listed in Note 7.3.
:::

下面是对修改后算法的更详细说明。首先，我们告诉程序，三个抛物型元素 $a$、$b$ 和 $abAB$ 是“特殊的”。接下来，程序会为每个生成元确定在枚举无限词时需要考虑的循环节。这些循环节列在 [注记 7.3](#note-7.3) 中。

:::{.simple}
This chart is used in the following way. Suppose we are considering a word w which ends with the tag `gens[l] = a`, for example $w = BABaa$. We are trying to plot the part of the limit set corresponding to words with prefix $w$, so we want to look at those places where this segment of the limit curve unexpectedly gets stretched out. This section of limit set, the $w$-section as we may call it, consists of points corresponding to all the infinite words between $w\overline{bABa}$ and $w\overline{BAba}$.
:::
该图表的使用方法如下。假设我们正在考虑一个以标签 `gens[l] = a` 结尾的单词，比如 $w = BABaa$。我们希望绘制极限集中的一部分，这部分对应的是以 $w$ 为前缀的所有单词。因此，我们关注的是极限曲线中该段意外被拉伸的位置。这一段极限集，我们可以称之为 $w$-区段，包含了所有介于 $w\overline{bABa}$ 和 $w\overline{BAba}$ 之间的无限单词所对应的点。


:::{.simple}
Because $a$ is parabolic, the fixed points $\bar{a}$ and $\bar{A}$ are the same, and therefore, although the infinite words are different, the limit points corresponding to $w\bar{a}$ and $w\bar{A}$ are equal. Notice that the infinite word $w\bar{A}$ reduces slightly to
$$w\bar{A} = BABaaAAAAA\cdots = BABAAA\cdots = BAB\bar{A}.$$
These cancellations mean that, on the boundary of the word tree, $BAB\bar{A}$ is far outside the interval of infinite words which correspond to the $w$-section of the limit set. So the chances are that the point $w\hat{a}$ is going to be stretched way away from its expected position, and we had better check it out when we are making our plot. We explain in Note 7.3 why  it is only worth checking out the special repetends in the list and not, for example, words ending in $a$ followed by the repetend $b$.
:::

由于 $a$ 是抛物元素，$\bar{a}$ 和 $\bar{A}$ 的不动点重合，因此，尽管无限词 $w\bar{a}$ 和 $w\bar{A}$ 不同，它们对应的极限点却是相同的。请注意，无限词 $w\bar{A}$ 可以简化为：
$$w\bar{A} = BABaaAAAAA\cdots = BABAAA\cdots = BAB\bar{A}.$$
这种简化意味着，在词树的边界上，$BAB\bar{A}$ 超出了与 $w$-截面极限集对应的无限词区间的范围。因此，点 $w\hat{a}$ 很可能会被拉伸得远离预期位置，因此我们在绘制图形时需要特别留意这一点。在 [注记 7.3](#note-7.3) 中，我们解释了为何只需检查列表中的特定循环节，而不必关注像以 $a$ 结尾、后接循环节 $b$ 的词。

:::{.note #note-7.3}
**Note 7.3: Which repetends should be considered?** \

**注 7.3：应考虑哪些循环节？**

Here is the list of repetends the program must consider when enumerating infinite words:

$$
\begin{aligned}
\text{gens[1]}&=a \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[1,1]=bABa \\
\text{repet}[1,2]=a \\
\text{repet}[1,3]=BAba
\end{array}
\right. \\
\text{gens[2]}&=b \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[2,1]=ABab \\
\text{repet}[2,2]=b \\
\text{repet}[2,3]=aBAb
\end{array}
\right. \\
\text{gens[3]}&=A \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[3,1]=BabA \\
\text{repet}[3,2]=A \\
\text{repet}[3,3]=baBA
\end{array}
\right. \\
\text{gens[4]}&=B \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[4,1]=abAB \\
\text{repet}[4,2]=B \\
\text{repet}[4,3]=AbaB
\end{array}
\right.
\end{aligned}
$$

There are some obvious omissions. For example, the generator $b$ is also parabolic, so that $w\overline{b}$ is the same point as $w\overline{B}$. Should we perhaps check out $w\overline{b}$ as well? Well, since $w$ ends in $a$, neither of the infinite words $w\overline{b}$ and $w\overline{B}$ collapse at all, so both $w\overline{b}$ and $w\overline{B}$ are in the small stretch of infinite words which correspond to the wiggly $w$-section. There seems to be no special need to bother with these points, in fact looking at plots we learned by experience that they don't stick particularly far out at all. In other words, if $w$ ends with $a$, then there is no need to look at repetends $b$ or $B$. Similar reasoning leads to the pattern in the chart. The repetends which are important to consider after a word $w$ which ends in the tag $c$ (one of $a$, $b$, $A$ or $B$) are precisely those which themselves end in $c$. This is because the inverse of the repetend will begin with $C$ (letters in the inverse word, remember, appear in reverse order) so that there are cancellations in $wC$. This means that the point $w(\overline{C})$ is not in the part of the boundary of the word tree corresponding to infinite words with the prefix $w$. You can imagine that its presence pulls the point $w(\overline{c})$ (which is in the $w$-section) towards it, causing distortions which our program needs to check out.

程序枚举无限字时需考察的循环节列表如下：

$$
\begin{aligned}
\text{gens[1]}&=a \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[1,1]=bABa \\
\text{repet}[1,2]=a \\
\text{repet}[1,3]=BAba
\end{array}
\right. \\
\text{gens[2]}&=b \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[2,1]=ABab \\
\text{repet}[2,2]=b \\
\text{repet}[2,3]=aBAb
\end{array}
\right. \\
\text{gens[3]}&=A \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[3,1]=BabA \\
\text{repet}[3,2]=A \\
\text{repet}[3,3]=baBA
\end{array}
\right. \\
\text{gens[4]}&=B \quad \Rightarrow \quad \left\{
\begin{array}{l}
\text{repet}[4,1]=abAB \\
\text{repet}[4,2]=B \\
\text{repet}[4,3]=AbaB
\end{array}
\right.
\end{aligned}
$$

显然，当前列表存在一些遗漏。例如，生成元 $b$ 同样是抛物型的，因此 $w\overline{b}$ 和 $w\overline{B}$ 对应相同的点。那么，我们是否也应该检查 $w\overline{b}$ 呢？实际上，由于 $w$ 以 $a$ 结尾，$w\overline{b}$ 和 $w\overline{B}$ 都不会发生任何坍缩，因此二者均位于描述 $w$-区段波动形态的无限词集合中。根据绘图观察的经验，这类点并不会显著突出边界轮廓。换言之，如果 $w$ 以 $a$ 结尾，则无需考察以 $b$ 或 $B$ 结尾的循环节。通过类似推理可得图表中的模式规律：对于以标签 $c$（即 $a,b,A,B$ 之一）结尾的词 $w$，需重点考察的循环节恰是那些自身以 $c$ 结尾者。这是因为此类循环节的逆元将以 $C$ 开始（注意逆元中的字母顺序是反转的），从而在组合 $wC$ 时产生抵消效应。这意味着点 $w(\overline{C})$ 并不位于对应前缀 $w$ 的无限字所在词树边界区域。可以设想，该点的存在会将 $w(\overline{c})$（位于 $w$-区段内）拉向它，从而产生程序需要检查的扭曲效应。
:::

![Figure 7.15. Slow motion gasket. This is a piece of the Apollonian gasket plotted with `\epsilon=0.1`. The width and height of the frame are 0.4. We have started numbering the limit points at $1 = \overline{bABA}$ in the upper left corner. One has to run through quite a few limit points after number $20 = b\overline{A}$, before we return to that same point labelled by the different infinite word $b\overline{a}$ at number 128. The limit points through which the curve passes twice have repetends $a$, $A$, $b$ or $B$. \
图 7.15. 慢动作的阿波罗涡旋。这是一个阿波罗涡旋的片段，使用了 $\epsilon = 0.1$ 进行绘制。框架的宽度和高度都是 0.4。我们从左上角的点 $1 = \overline{bABA}$ 开始为极限点编号。直到编号为 $20 = b\overline{A}$ 的点之后，才需要通过若干个极限点，才能返回到那个用不同无限单词 $b\overline{a}$ 标记的同一点——这个点的编号是 128。曲线经过两次的极限点，其重复部分包括 $a$、$A$、$b$ 或 $B$。](/images/indra/fig-7.14.jpg){width=500 #fig-7.15}


:::{.simple}
At the beginning of the program, our routine computes the attractive fixed point ${\rm fp}[i,j]$ of each of the repetends ${\rm repet[i,j]\}$ listed in the chart. The only parts of the running algorithm which need to be changed are the termination and plotting subroutines. Suppose we are at the finite word ending in the generator $gens[i]$. Then we compute the three points

$$z_j = \text{word}({\rm fp}[i,j])$$

for $j = 1, 2, 3$. Given the plotting gap $\epsilon$, we require both $|z_2 - z_1| \leq \epsilon$ and $|z_3 - z_2| \leq \epsilon$ in order to terminate the forward enumeration along that particular branch of the word tree. If the criterion is met, we draw a line segment from $z_1$ to $z_2$, and a line segment from $z_2$ to $z_3$. That is all the modification we need.
:::

在程序开始时，我们的例行步骤会计算出图表中每个循环节（repetend）${\rm repet[i,j]}$ 的吸引不动点（attractive fixed point）${\rm fp}[i,j]$。原有算法中，唯一需要修改的部分是终止条件和绘图子程序。假设我们当前位于一个以生成元 $gens[i]$ 结尾的有限字（finite word）。此时，我们计算以下三个点：
zj=word(fp[i,j])zj​=word(fp[i,j])
其中 $j = 1, 2, 3$。

给定绘图精度 $\epsilon$，我们要求满足 $|z_2 - z_1| \leq \epsilon$ 且 $|z_3 - z_2| \leq \epsilon$，才能终止该分支在字树（word tree）上的正向枚举。若条件满足，我们依次绘制两条线段：一条从 $z_1$ 到 $z_2$，另一条从 $z_2$ 到 $z_3$。这就是我们所需的全部修改。

:::{.simple}
Figure 7.15 shows a slow motion execution of this special word algorithm for the gasket. As above, $a,b$
and the commutator have been listed as special words. A piece of the gasket has been plotted at the rather large gap size of `epsilon=0.1`. As you can see, all the contact points between far away parts of the limit set curve are completely filled in and the algorithm produces limit sets with no visible gaps. You will see better how the special word algorithm works if you follow through the description in Note 7.4.
:::

图 7.15 展示了这种针对垫片的特殊词算法的慢动作执行过程。和上文一样， 特殊词中包括 $a,b$ 和换位子。图中绘制了垫片的一部分，采用了较大的间隙尺寸 `epsilon=0.1`。正如你所见，极限集曲线中远处部分之间的所有接触点都已被完全填充，算法生成的极限集不再存在可见的间隙。如果你参照 [注记 7.4](#note-7.4) 中的描述，将能更清楚地理解特殊词算法的工作原理。

:::{.simple}
Many fractals are created through a process of iteration which is not terribly sensitive to the order of execution of the program. Seeing limit sets like the gasket drawn as curves is too wonderful to leave to such a procedure. When testing your program it is essential to scrutinize with excruciating care the order of infinite words and corresponding limit points. For lack of space (it's already a crowded picture), not all the limit points in Figure 7.15 have been labelled. If you really wish to test your understanding of the algorithm, you should try to fill in some missing labels, which can be done given the dictionary ordering and the desired special words.
:::

许多分形图形是通过迭代过程生成的，而这种过程对程序的执行顺序通常并不十分敏感。然而，像垫片（gasket）这样的极限集，如果仅仅以这种方式画成曲线，未免太过可惜——它的美妙远不止于此。

在测试程序时，务必仔细审查无限词的顺序及其对应的极限点，做到一丝不苟。由于空间有限（图 7.15 已经非常拥挤），并未对其中的所有极限点标注。如果你真的想检验自己对算法的理解，不妨尝试补全其中缺失的标注。只要参考字典序和那些特殊的目标词，这项工作是完全可行的。

:::{.note #note-7.4}
**Note 7.4: Tracing the gasket**

**注记 7.4：追踪垫片**

To understand the workings of our special word algorithm better, you may like to try following along segments of the curve in Figure 7.15 carefully as we describe here.

Let's focus on the segment of limit set between points 1 and 35. This is the segment corresponding to all words with prefix $bA$. As you can see by referring to our chart of repetends, $1 = bABabA$ and $35 = bAbaBA$. (In the figure, these points are written slightly differently, simply because we chose a different point starting point for cycling the repetend. So for example $bABabA$ is exactly the same sequence as $\overline{bABA}$.) As you can see by following the numbers closely, the segment of limit set between points $1 = bABabA$ and $35 = bAbaBA$ passes through the bad fixed point $20 = bAA$. At this scale the distortion is not too bad – in comparison to the distance between 1 and 35, the point 20 is not too far away. Things get worse when you go to the next level and study the subsegment corresponding to infinite words with prefix $bAA$. The initial point of this section of limit set is $15 = bAABabA$ and the final point is $25 = bAAbaBA$. The outlier is still 20, which can also be written as $bAAA$. See how 20 is pulled quite far out in comparison to the distance between 15 and 25. This is happening because in fact $20 = b\overline{A}$ is the same point as 128 = $b\overline{a}$, which is in quite a different section of the path round the boundary of the word tree. Our algorithm would only stop at this prefix if the distances from 15 to 20 and from 20 to 25 were both less than the cut-off value $\epsilon$. At the next stage, look at the interval between 17 = $bAAABabA$ and 23 = $bAAAbaBA$. The outlier is still 20 = $bAAAA$. Now the disproportion between the distances from 17 to 23, as opposed to the distances from 17 to 20 and 20 to 23, is really getting large. As you go further and further into the spike, the disproportion gets ever worse, so the finer you want to plot your pictures the more important it is to check out these outliers. If we weren't using the special words algorithm, the plot would terminate far too soon, chopping off the piece of limit set which sticks out into the spike.

为了更好地理解我们的特殊单词算法的工作原理，不妨按照我们在此描述的内容，仔细沿着图 7.15 中曲线的某些部分追踪观察。

让我们聚焦于点 1 和点 35 之间的极限集部分。这一部分对应于所有以 $bA$ 为前缀的单词。参照我们的循环节图表，可以看到 $1 = bABabA$，而 $35 = bAbaBA$。（图中这些点的表示稍有不同，仅仅是因为我们选择了一个不同的起始点来循环循环节。例如，$bABabA$ 与 $\overline{bABA}$ 实际上是完全相同的序列。）

仔细观察编号，可以发现，从点 $1 = bABabA$ 到点 $35 = bAbaBA$ 的极限集部分经过了那个糟糕的不动点 $20 = bAA$。在这个尺度下，尽管存在一定的畸变，但相较于点 1 和点 35 之间的距离，点 20 也并不算太远。然而，情况在进一步深入时变得更糟。当研究对应于以 $bAA$ 为前缀的无限单词的子区段时，情况就更明显了。这个区段的起始点是 $15 = bAABabA$，终点是 $25 = bAAbaBA$。

异常点依然是 20，它也可以写作 $bAAA$。注意点 20 在图中被拉出了相当远的距离，相较于点 15 到点 25 之间的距离，点 20 的偏离尤为显著。这种现象的根本原因在于，实际上 $20 = b\overline{A}$ 与 $128 = b\overline{a}$ 是同一个点，而该点在单词树边界路径的完全不同的部分。我们的算法仅在点 15 到点 20 以及点 20 到点 25 的距离都小于截断值 $\epsilon$ 时，才会在该前缀处停止。

再往下一层观察区间时，查看点 17 = $bAAABabA$ 和点 23 = $bAAAbaBA$ 之间的区段。异常点依然是点 20 = $bAAAA$。此时，点 17 到点 23 的距离，与点 17 到点 20 以及点 20 到点 23 的距离之间的失衡变得更加明显。随着你在这根尖刺中不断深入，这种失衡愈加严重。因此，越是要精细地绘制图形，检查这些异常点就越重要。如果我们没有使用特殊单词算法，绘图将会过早终止，从而截断伸入尖刺的那一部分极限集。
:::

# Projects

:::{.simple #proj-7.1}
**7.1: Uniqueness of ideal triangles**

**7.1：理想三角形的唯一性**

How many ideal triangles can you draw with given vertices $P$, $Q$ and $R$? If the vertices are $0$, $1$ and $\infty$, show that the sides must be the two ‘vertical’ lines through $0$ and $1$ and the circle with centre $1/2$, radius $1/2$. Thus there are exactly two ideal triangles with these vertices, but only in the ‘upper’ triangle are the vertices $0$, $1$ and $\infty$ in anticlockwise order round the edge. Sometimes this is called the standard ideal triangle. Find its incircle.

Suppose now you have another ideal triangle with vertices $P$, $Q$ and $R$ in anticlockwise order. Project 3.2 showed there is exactly one Möbius map $M$ which carries $0$, $1$ and $\infty$ to $P$, $Q$, $R$ in that order. What properties of Möbius maps show that $M$ carries the standard ideal triangle into the new one? If there were another other ideal triangle with the same vertices in the same order, what would happen when you applied $M^{-1}$? Why does any ideal triangle have exactly one incircle?

给定顶点 $P$、$Q$ 和 $R$，可以画出多少个理想三角形？如果顶点是 $0$、$1$ 和 $\infty$，可以证明它们的边必须是通过 $0$ 和 $1$ 的两条“垂直”直线，以及以 $1/2$ 为圆心、$1/2$ 为半径的圆。因此，具有这些顶点的理想三角形恰好有两个，但只有在“上方”的三角形中，顶点 $0$、$1$ 和 $\infty$ 按逆时针顺序排列在边界上。有时这个三角形被称为标准理想三角形。找出它的内切圆。

假设现在有另一个理想三角形，其顶点 $P$、$Q$ 和 $R$ 按逆时针顺序排列。项目 3.2 表明，存在唯一的莫比乌斯变换 $M$，将 $0$、$1$ 和 $\infty$ 依次映射到 $P$、$Q$、$R$。莫比乌斯变换的哪些性质表明 $M$ 将标准理想三角形映射到新的三角形？如果存在另一个具有相同顶点且按相同顺序排列的理想三角形，那么对其应用 $M^{-1}$ 会发生什么？为什么任何理想三角形都有且仅有一个内切圆？
:::


:::{.simple #proj-7.2}
7.2: An instance of Soddy's formula

**7.2：索迪公式的一个实例**

Calculate the radius of the incircle $C_A$ in the right frame of Figure 7.4 using Soddy's formula, and check your answer with a more conventional computation using Pythagoras' theorem. Be careful: one circle has infinite radius! Use your result to show that the points $S$ and $R$ in the figure are at $\pm 0.2 - 0.4i$, and then check the generators pair the tangency points properly.

使用索迪公式计算图 7.4 右侧框中的内切圆 $C_A$ 的半径，并通过应用勾股定理进行常规计算来验证你的结果。请小心：其中一个圆的半径是无限的！利用你的结果，证明图中的点 $S$ 和 $R$ 位于 $\pm 0.2 - 0.4i$，然后检查生成器是否正确地配对了切点。
:::


:::{.simple #proj-7.3}
**7.3: The Ford circles**

**7.3: 福特圆**

There is a remarkable pattern for the radii of the circles which touch the real axis in Figure 7.5, commonly credited to Lester Ford. The pattern is easiest to analyze if we shift and scale so that the largest pink circles are tangent to the real axis at integer points, so they have diameter $1$, and the strip is $1$ unit high. Then there is exactly one circle (pink or white) tangent at every rational point $p/q$. Find the pattern that describes which rationals $p/q$ are tangent to a white circle, and which to a pink one.

The formula for the radius of the circle tangent at $p/q$ is quite simple. It depends only on $q$. For example, at each integer point $n/1$ the denominator is $1$ and the radius is $1/2$. At each half-integer, $\pm 1/2, \pm 3/2$, etc., the denominator is $2$ and the radius is $1/8$. Those are all the hints we'll give.

如图 7.5 所示，与实轴相切的圆的半径呈现出一个显著的规律，通常归功于 Lester Ford。最容易分析这个规律的方法是通过平移和缩放，使得最大的粉色圆与实轴在整数点相切，直径为 $1$，并且该条带的高度为 $1$ 单位。这样，恰好每个有理数点 $p/q$ 上都会有一个圆（无论是粉色还是白色）与实轴相切。接下来，找出描述哪些有理数 $p/q$ 与白色圆相切，哪些与粉色圆相切的规律。

在 $p/q$ 处与实轴相切的圆的半径公式非常简单，它只与分母 $q$ 有关。例如，在每个整数点 $n/1$ 处，分母为 $1$，半径为 $1/2$；在每个半整数点 $\pm 1/2, \pm 3/2$ 等处，分母为 $2$，半径为 $1/8$。这些就是我们给出的所有提示。
:::


:::{.simple #proj-7.4}
**7.4: Another modular group in the gasket group**

**垫片群中的另一个模群**

In the text (see p. 213), we focussed on the modular group acting in what were the pink disks in Figure 7.4. (The tiling of these disks is shown in Figure 7.6.) The modular group acts in the white disks too. In the right frame of Figure 7.4, look at the lower blue circles $C_B$ and $C_b$. Their images $a(C_B)$ and $a(C_b)$ are also tangent circles, actually the reflections of the first two in the real axis. These four circles are tangent and cut the white exterior of the unit disk into four quarters. Twist yourself inside out to see that in this white exterior we also have the gluing pattern for the modular group: four tangent circles with neighbouring circles being paired. Show that the two tangency points correspond to the parabolic elements $b$ and $abA$, while the other two are the products $abAB$ and $BabA$, which are parabolic with fixed points at $1$ and $-1$ respectively. The limit set for this subgroup is the unit circle.

在文本中（见第 213 页），我们集中讨论了模群在图 7.4 中粉色圆盘上的作用。（这些圆盘的镶嵌方式见图 7.6。）模群同样作用于白色圆盘。在图 7.4 的右侧框架中，观察下方的蓝色圆圈 $C_B$ 和 $C_b$。它们的像 $a(C_B)$ 和 $a(C_b)$ 也是相切的圆，实际上是前两个圆关于实轴的对称映像。这四个圆相切，并且将单位圆的白色外部区域切割成四个部分。试着从另一个角度来理解，你会发现，在这片白色外部区域中，模群的拼接模式也显现出来：四个相切的圆，其中相邻的圆形成一对。证明这两个相切点对应于抛物线元 $b$ 和 $abA$，而另外两个则是乘积 $abAB$ 和 $BabA$，这两个也是抛物线元，分别在 $1$ 和 $-1$ 处有不动点。这个子群的极限集是单位圆。
:::


:::{.simple #proj-7.5}
**7.5: Farey fractions and Euclid's algorithm**

**7.5: 法雷分数与欧几里得算法**

To show that every rational number $p/q$ is a vertex of the modular tiling in Figure 7.9 we need to find two other integers $r$ and $s$ such that $ps - qr = \pm 1$. Why will this do what we want?

The procedure for finding $r$ and $s$ like this is exactly the famous Euclidean algorithm for finding the highest common factor of two numbers. In this case, we may as well suppose that $p/q$ is in its lowest terms so the highest common factor is 1. Let's suppose $p > q > 0$. The algorithm says we shall be able to find integers $a_1, r_1, a_2, r_2, \ldots$ and so on such that:

$$\begin{aligned}
& p = a_1 q + r_1, \quad 0 < r_1 < q, \\
& q = a_2 r_1 + r_2, \quad 0 < r_2 < r_1, \\
& r_1 = a_3 r_2 + r_3, \quad 0 < r_3 < r_2, \\
& \vdots \\
& r_{n-1} = a_{n+1} r_n + 1.
\end{aligned}
$$

Using these equations you can work backwards to find $r$ and $s$. For example, if $p = 14$, $q = 3$ then $14 = 4 \cdot 3 + 2$, $3 = 2 \cdot 1 + 1$ and so $14 - 4 \cdot 3 = 2 = 3 - 1$ giving $14 - 5 \cdot 3 = -1$. Now try to spot the connection with continued fractions:

$$\frac{14}{3} = 4 + \frac{2}{3} = 4 + \frac{1}{\frac{3}{2}} = 4 + \frac{1}{1 + \frac{1}{2}}.$$

要证明每个有理数 $p/q$ 都是图 7.9 中模群镶嵌的一个顶点，我们需要找到两个整数 $r$ 和 $s$，使得 $ps - qr = \pm 1$。为什么这能达到我们的目标？

这种寻找 $r$ 和 $s$ 的方法正是著名的欧几里得算法，用于求两个数的最大公因数。在这种情况下，我们可以假设 $p/q$ 已经化为最简分数，因此它们的最大公因数为 1。假设 $p > q > 0$。算法指出，我们可以找到整数 $a_1, r_1, a_2, r_2, \ldots$ 等，使得：

$$\begin{aligned}
& p = a_1 q + r_1, \quad 0 < r_1 < q, \\
& q = a_2 r_1 + r_2, \quad 0 < r_2 < r_1, \\
& r_1 = a_3 r_2 + r_3, \quad 0 < r_3 < r_2, \\
& \vdots \\
& r_{n-1} = a_{n+1} r_n + 1.
\end{aligned}
$$
利用这些等式可以回溯找到 $r$ 和 $s$。例如，如果 $p = 14$，$q = 3$，则 $14 = 4 \cdot 3 + 2$，$3 = 2 \cdot 1 + 1$，因此 $14 - 4 \cdot 3 = 2 = 3 - 1$，从而 $14 - 5 \cdot 3 = -1$。现在尝试找到与连分数的联系：
$$\frac{14}{3} = 4 + \frac{2}{3} = 4 + \frac{1}{\frac{3}{2}} = 4 + \frac{1}{1 + \frac{1}{2}}.$$
:::

:::{.simple #proj-7.6}
**7.6: The modular group and odd-even fractions**

**7.6：模群与奇偶分数**

Show that if $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is in the (small) modular group then $a$ and $d$ are odd and $b$ and $c$ are even. Why is a fraction in the orbit of $0$ under the (small) modular group exactly when it is ‘even/odd’? What can you say about odd/odd and odd/even? (Notice that in any triple of Farey neighbours you get one fraction of each kind.)

证明如果 $\begin{pmatrix} a & b \ c & d \end{pmatrix}$ 属于（小）模群，则 $a$ 和 $d$ 为奇数，$b$ 和 $c$ 为偶数。为什么当一个分数在（小）模群作用下的轨道中时，它恰好是“偶/奇”分数？关于奇/奇和奇/偶分数可以说些什么？（请注意，在任何一个 Farey 邻居三元组中，总会有一种类型的分数。）
:::

:::{.simple #proj-7.7}
**7.7: The modular group or not?**

**7.7：模群还是别的？**

It is interesting to compare the group which generated Figure 6.5 in the last chapter with the modular group. The group in Chapter 6 has generators

$$a = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix} \text{ and } b = \begin{pmatrix} \sqrt{2} & 1 \\ 1 & \sqrt{2} \end{pmatrix}.$$

The conjugated picture of this group in frame (v) of Figure 6.10 looks exactly the same as the basic tile for the modular group in Figure 7.9. Are these two groups the same up to conjugation or not?

将第 6 章中生成 [图 6.5](#fig-6.5) 的群与模群进行比较很有趣。第 6 章中的群的生成元为：
$$a = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix} \text{ and } b = \begin{pmatrix} \sqrt{2} & 1 \\ 1 & \sqrt{2} \end{pmatrix}.$$
在 [图 6.10](#fig-6.10) 的第 (v) 帧中，该群的共轭图看起来与 [图 7.9](#fig-7.9) 中模群的基本镶嵌完全相同。它们是否在共轭意义下相同？
:::


:::{.simple #proj-7.8}
**7.8: A special Schottky group**

**7.8：一个特殊的 Schottky 群**

In Project 4.1 we introduced a family of Schottky groups depending on 2 real numbers $s$ and $t$ which mapped the real axis to itself. These groups were designed so that the order of the Schottky circles along the real axis was the same as for the modular group. In fact, we organised things so that when $s = 0$ and $t = 1$, we get the modular group itself! Just as we did on p. $179 ff$. in the last chapter, we can use this family to see explicitly what happens as we bring the four disjoint circles together until they touch.

Check that if $s = 0$, then both generators are parabolic. Which of the four Schottky circles touch? Show that if $s = 0$ then $\text{Tr } ab = 2 - 4/t^2$ and the distance between its fixed points is $4\sqrt{1 - t^2}/t^2$. Hence verify directly that as $t$ tends to 1, $ab$ also becomes parabolic with trace $-2$ and fixed point at $-1$, the tangency point of $C_a$ and $C_b$. Which group element corresponds to the tangency point of $C_A$ and $C_b$? Why does it become parabolic at the same time as $ab$?

在项目 4.1 中，我们介绍了一个取决于两个实数 $s$ 和 $t$ 的 Schottky 群族，这些群将实轴映射到自身。我们特意设计这些群，使得沿实轴的 Schottky 圆的排列顺序与模群相同。事实上，我们特意安排使得当 $s = 0$ 且 $t = 1$ 时，该群就是模群本身！正如上一章第 179 页及后续部分所讨论的那样，我们可以利用这个群族来直观地观察，当四个互不相交的圆逐渐靠近直至相切时会发生什么。

验证当 $s = 0$ 时，这两个生成元都是抛物变换。此时，哪四个 Schottky 圆相切？证明如果 $s = 0$，则 $\tr{ab} = 2 - 4/t^2$，且其不动点之间的距离为 $4\sqrt{1 - t^2}/t^2$。从而可以直接验证，当 $t \to 1$ 时，$ab$ 也成为一个抛物变换，其迹为 $-2$，且不动点为 $-1$，即圆 $C_a$ 和 $C_b$ 的切点。哪个群元素与圆 $C_A$ 和 $C_b$ 的切点相关？为什么它会恰好在 $ab$ 变为抛物变换时同时成为抛物变换？
:::


:::{.simple #proj-7.9}
**7.9: Nesting circles which don't shrink!**

**7.9：不会收缩的嵌套圆！**

It is not quite easy to find an explicit group whose generators $a$ and $b$ pair opposite Schottky circles in a tangent chain in such a way that $abAB$ is not parabolic. If instead we use circles paired according to the modular group pattern, it is much simpler. The non-parabolic element will be the product $ab$.

We do it with a slight alteration to the modular group which is easiest to describe in terms of the vertices of the red and green ideal quadrilateral in Figure 7.9. Fix the vertices at $0$, $-1$ and $\infty$ but move the vertex $1$ to a point $r$ on the real axis slightly to its right (so $r > 1$). Check that

$$b = \begin{pmatrix} 1 & 1 + r \\ 0 & 1 \end{pmatrix} \text{ and } a = \begin{pmatrix} 1 & 0 \\ -1 - 1/r & 1 \end{pmatrix}$$

pair the new chain of tangent circles, matching tangency points correctly.

Verify that $a$ and $b$ are parabolic with fixed points at $\infty$ and $0$. Now calculate $ab$ and show it is hyperbolic whenever $r > 1$. Where are its fixed points? If you have a suitable program up and running, you may wish to draw some pictures to check that the diameters of the nested circles do not shrink properly near $-1$ and $r$.

要显式构造一个群，使其生成元 $a$ 和 $b$ 能将相切链中相对的 Schottky 圆配对，且使得 $abAB$ 不是抛物型变换，这并非易事。但若采用模群的圆配对方式，问题便大为简化——此时非抛物元素恰是乘积

我们通过对模群稍作调整来实现这一点，最简单的方法是借助图 7.9 中红色和绿色理想四边形的顶点：将三个顶点固定于 $0,-1,\infty$ 处，并将顶点 $1$ 沿实轴向右侧略微移动至 $r$（即 $r > 1$）。可验证矩阵
$$b = \begin{pmatrix} 1 & 1 + r \\ 0 & 1 \end{pmatrix} \text{ and } a = \begin{pmatrix} 1 & 0 \\ -1 - 1/r & 1 \end{pmatrix}$$

能正确配对新生成的相切圆链，并精确匹配切点。

验证这时 $a$ 和 $b$ 都是抛物型变换，其不动点分别位于 $\infty$ 和 $0$。然后计算 $ab$ 并证明当 $r > 1$ 时它是双曲变换。它的不动点在哪里？如果你有合适的程序运行，不妨绘制一些图像，检查靠近 $-1$ 和 $r$ 处的嵌套圆的直径是否未按预期缩小。
:::


[^1]: Reproduced from Nature, 137, 1936.
[^2]: The refinement has to do with ensuring that circles appear with the desired visual accuracy.
[^3]: That would have made high school geometry a lot simpler! Perhaps that’s why triangles like this are called ‘ideal’.

