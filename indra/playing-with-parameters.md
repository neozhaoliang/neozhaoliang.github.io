---
title: "Playing with parameters"
subtitle: "The vision of Felix Klein"
date: 2025-01-23
url: "playing-with-parameters"
---
\DeclareMathOperator{\tr}{Tr}
\newcommand{\fix}{\mathrm{Fix}\,}


:::{.simple}
I could spin a web if I tried.' said Wilbur, boasting. 'Ive just never tried.'

‘Let’s see you do it,’ said Charlotte…

‘OK.’ replied Wilhur. ‘You coach me and I’t’ spin one. It must be a lot of fun to spill a web. How do I start?


“要是我愿意，我也能织网。”威尔伯吹嘘道，“只是我从来没试过。”

“那你来织一个给我们看看吧。”夏洛特说。

“好啊。”威尔伯答道，“你来指导我，我就织一个。织网一定很好玩。我该怎么开始呢？”
:::


:::{.simple}
As any mathematician who has revealed his (or her) occupation to a neighbour on a plane flight has discovered, most people associate mathematics with something akin to the more agonizing forms of medieval torture. It seems indeed unlikely that mathematics would be done at all, were it not that a few people discover the play that lies at its heart. Most published mathematics appears long after the play is done, cloaked in lengthy technicalities which obscure the original fun. The book in hand is unfortunately scarcely an exception. Never mind; after a fairly detailed introduction to the art of creating tilings and fractal limit sets out of two very carefully chosen Möbius maps, we are finally set to embark on some serious mathematical play. The greatest rewards will be reaped by those who invest the time to set up their own programs and join us charting mathematical territory which is still only partially explored.
:::

正如任何一位曾在飞机上向邻座透露自己职业的数学家都会发现的那样，大多数人对数学的印象，似乎与某种中世纪酷刑的痛苦体验无异。倘若不是有少数人发现了数学的核心妙趣，数学恐怕早已无人问津。大多数已发表的数学成果，往往是在趣味探索结束许久之后才浮出水面的，而那些冗长繁复的技术细节，往往掩盖了最初的乐趣。遗憾的是，手头的这本书也未能完全例外。不过，别担心——在颇为详尽地介绍了如何用两个精心挑选的莫比乌斯变换来构造密铺图案和分形极限集之后，我们终于可以开始一场真正的数学探险了。那些愿意投入时间亲手编写程序、与我们一道探索这片尚未完全揭示的数学版图的读者，定将收获最丰厚的回报。

:::{.simple}
All the limit sets we have constructed thus far began from a special arrangement of four circles, the Schottky circles, grouped into two pairs. For each pair, we found a Möbius map which moved the inside of one circle to the outside of the other. Our initial tile was the region outside these four circles. By iterating, we produced a tiling which covered the the plane minus the limit set, near which the tiles shrank to minute size. Depending on how we chose the initial Schottky circles, the limit set was either fractal dust, a very crinkled fractal loop we called a quasicircle or, in certain very special cases, a true circle.
:::

迄今为止，我们构造的所有极限集都源自四个圆的独特排列，这些圆被称为肖特基圆，分为两对。对于每一对圆，我们找到一个莫比乌斯映射，将一个圆的内部映射到另一个圆的外部。我们的初始瓷砖是这四个圆外部的区域。通过反复迭代，我们生成了一种密铺，覆盖了平面上除了极限集以外的区域，在极限集附近，瓷砖逐渐缩小至微不可察的尺寸。根据我们选择的初始肖特基圆的不同，极限集可能呈现为分形尘埃，或者是我们称之为拟圆的极度扭曲的分形环，亦或在某些极其特殊的情况下，成为一个完美的圆。

:::{.simple}
The problem with this approach is that it is just too time-consuming to set up the circles and maps which pair them. Free-spirited play shouldn’t be ruined by too much preparation. Why not throw the Schottky circles away, take any pair of $2\times 2$ matrices for our generators $a$ and $b$, run our limit point plotting program, and see what we get?

Hold on though - how exactly will this work? The shrinking disks were so reassuring, and the limit set was so comfortably nestled within them, that it is hard to see why we won’t get chaos in their absence. No matter, the worst that is likely to happen is that the hard disk crashes, so why not give it a try? Luckily, on p. 182 ff. we already upgraded the DFS code to remove the calculation of Schottky disks from the branch termination procedure. All we need do is take the plunge and run the very same algorithm for any pair of transformations $a$ and $b$.
:::

这个方法的弊端在于，设置这些圆及其配对映射实在太耗时了。自由随性的探索不应该被繁琐的准备工作束缚住手脚。为什么不干脆抛开 Schottky 圆，随便挑一对 $2 \times 2$ 矩阵作为我们的生成元 $a$ 和 $b$，然后直接运行极限点绘图程序，看看会蹦出什么结果呢？

慢着，这真的行得通吗？那些嵌套收缩的圆盘让人倍感安心，极限集恰如其分地安居其中。没有了它们的庇护，系统难道不会陷入混沌？不过没关系，大不了就是硬盘崩了呗，那为什么不试试看呢？

幸运的是，在第 182 页及后续章节中，我们已经对 DFS 算法进行改良，去掉了分支终止判定中对 Schottky 圆盘的计算。我们所需要的，只是鼓起勇气，运行同样的算法，随便选一对变换 $a$ 和 $b$，放手一试就好。

:::{.simple}
The reward is the glorious Figure 8.1! See intricate dance of spirals of two loxodromic transformations. This is a quasifuchsian group very different from the circle groups we met in Chapter 6. As usual, once  a certain feature appears, the Mobius transformations in the group transport it around. Theoretical knowledge is one thing, but it wasn't until we got our programs up and running that the first ever pictures of exploding spirals brought the reality home. The authors, and later the participants in 1980  Thurston Theory Conference at Bowdoin College, could not suppress their awe at the eerie glowing image  of the limit curve snaking its way across an old Tektronix terminal.
:::

奖励是辉煌的 [图 8.1](#fig-8.1)！看看两个斜驶变换螺旋的复杂舞蹈。这是一个与我们在第 6 章遇到的圆群截然不同的拟 Fuchs 群。像往常一样，一旦某个特征出现，群中的莫比乌斯变换便会将其传递开来。理论知识是一回事，但直到我们的程序启动并运行，第一张爆炸螺旋的图片才让人真正感受到其中的魅力。作者们，以及后来参加 1980 年鲍登学院 Thurston 理论会议的与会者，无法抑制对极限曲线在老式 Tektronix 显示器上蜿蜒而出的那张诡异发光图像的敬畏。

:::{.simple}
There's one question here you may be asking: how did we choose $a$ and $b$? The answer is, we built a machine. When engineers design a new sports car, do you really think they first test it by creeping down
the driveway carefully at 5 miles per hour, then 10 miles per hour, and so on? Of course not; they push it madly through its paces to see how it drives. In order to carry out our explorations, we needed an  easy-to-use program so we could quickly test out all sorts of possible matrices. In the next section, we shall explain a recipe which allows us to easily make as many variants of pictures like this as we please. The recipe depends on just two complex numbers, the traces of $a$ and $b$. These will be our parameters; just feed them in and let the program fly.
:::

接下来，你可能会有一个问题：我们是如何选择 $a$ 和 $b$ 的？答案是，我们构建了一台机器。当工程师设计一辆新跑车时，你真的认为他们会先以每小时 5 英里的速度小心翼翼地沿着车道缓慢测试，然后是每小时 10 英里，依此类推吗？当然不是；他们会毫不犹豫地将它推向极限，以各种速度行驶，观察它的驾驶表现如何。为了进行我们的探索，我们需要一个易于使用的程序，能够快速测试各种可能的矩阵。在下一节中，我们将解释一种方法，让我们轻松地制作出任意数量的此类图片变体。这个方法仅依赖于两个复数—— $a$ 和 $b$ 的迹。它们将作为我们的参数；只需输入它们，启动程序即可。

:::{.simple}
Actually you may get even greater satisfaction by varying the parameters continuously and watching the limit set writhing in response. For that, you will have to write another small program which plots a sequence of frames of limit sets whose parameters are just slightly changed step-by-step. Several people have done this, but stills are the best we can offer in a book. Jeff Brock offers some films of crawling limit bugs on his web page www.math.uchicago.edu/~brock. For the Macintosh, we recommend a program by Masaaki Wada called *OPTi*, available at vivaldi.ics.nara-wu.ac.jp/~wada.
:::

其实，如果你尝试连续调整参数，并观察极限集在这种变化中不断扭动、变形，你可能会感受到更大的乐趣。为此，你需要编写一个小程序，绘制一系列极限集的动画帧，每一帧的参数都稍稍有所变化。虽然已经有人做过这类工作，但在书中我们只能展示静态图像。Jeff Brock 在他的网站 www.math.uchicago.edu/~brock 上提供了一些关于“爬行的极限虫”的短片。对于 Macintosh 用户，我们推荐 Masaaki Wada 开发的 OPTi 程序，可在 vivaldi.ics.nara-wu.ac.jp/~wada 下载。

![Figure 8.1. Mating snails? The limit set of a group generated by two maps $a$ and $b$ with complex conjugate traces $t_a=1.87+0.1i$ and $t_b=1.87-0.1i$. This group is quasifuchsian because its limit set is a continuous loop which never crosses or meets itself. Curves like this are called Jordan curves: the celebrated Jordan Curve Theorem innocently states that every Jordan curve divides the plane into two parts, an ‘inside’ (gray) and an ‘outside’ (white). The proof of this seemingly obvious result is not easy. and this picture gives some idea of just how complicated a Jordan curve can be. We had to devise a handerafted algorithm to colour the inside. \
**图 8.1 交配的蜗牛？** 这是由两个映射 $a$ 和 $b$ 所生成的群的极限集，它们的迹互为复共轭，分别为 $t_a = 1.87 + 0.1i$ 和 $t_b = 1.87 - 0.1i$。该群是拟 Fuchsian 群，因为它的极限集是一条既不交叉也不自交的连续闭曲线。这样的曲线被称为 Jordan 曲线。著名的 Jordan 曲线定理看似简单：每一条 Jordan 曲线都将平面分成两个部分，一个“内部”（灰色）和一个“外部”（白色）。尽管这个结果听起来显而易见，证明它却并不容易。而这幅图正好展示了 Jordan 曲线可以复杂到什么程度。为了给内部区域上色，我们不得不专门设计一个手工打造的算法。](/images/indra/fig-8.1.jpg){width=500 #fig-8.1 .fig}


# Grandma's recipe

:::{.simple}
To make pictures, we need two Möbius maps $a$ and $b$, given by matrices
$$
a = \begin{pmatrix} a_1 & a_2 \\ a_3 & a_4 \end{pmatrix} \quad \text{and} \quad b = \begin{pmatrix} b_1 & b_2 \\ b_3 & b_4 \end{pmatrix}.
$$
Numerical inputs to a device or program are often called parameters. On the face of it, two matrices means eight complex numbers which means sixteen real numbers: that's quite a few! To build our ‘easy-to-use’ program, we need reduce the parameters to a minimum. We can get the number down to six by assuming that each matrix has determinant 1. We can further reduce the number by remembering that the interesting thing is to study groups up to conjugation. In practice this means that after we have studied one particular group $G$, we no longer need study any of the conjugate groups $hGh^{-1}$ for any conjugating Möbius map $h$ (apart of course from the fun of getting a quite different ‘view’ of the limit set). A definite choice among all the conjugate groups $hGh^{-1}$ is called a normalization for $G$.
:::

为了绘制图形，我们需要两个莫比乌斯映射 $a$ 和 $b$，它们分别由以下矩阵给出：
$$
a = \begin{pmatrix} a_1 & a_2 \\ a_3 & a_4 \end{pmatrix} \quad \text{and} \quad b = \begin{pmatrix} b_1 & b_2 \\ b_3 & b_4 \end{pmatrix}.
$$
设备或程序的数值输入通常被称为参数。从表面上看，两个矩阵意味着八个复数，即十六个实数：这可真不少！为为了让我们的程序“好用”，我们需要尽量减少参数的数量。通过假设每个矩阵的行列式为 1，我们可以将参数数减少到六个。我们还可以通过记住，研究群的共轭类才是关键，进一步减少参数数量。实际上，这意味着一旦我们研究了某个特定的群 $G$，我们就不再需要研究任何共轭群 $hGh^{-1}$，其中 $h$ 是任何共轭的莫比乌斯映射（当然，除非你想体验一下从完全不同的角度观察极限集的乐趣）。在所有共轭群 $hGh^{-1}$ 中，选定一个特定的群作为代表，这个选择就称为对 $G$ 的归一化。

:::{.simple}
Choosing a particular normalization allows you to eliminate three further parameters, because there is always exactly one Möbius map which carries any three points to any other three. This means that you can prespecify the position of three points; for example, you might specify that the attracting fixed points of $a$, $A$ and $b$ are $0$, $1$, and $\infty$ respectively. This is exactly what we did on p. 207 when we proved that, up to conjugation, the modular group is unique. The upshot is that up to conjugacy, we should be able to reduce the number of complex parameters necessary to describe a two-generator group from eight to just three. The question is, which three? From our experience in the last two chapters, a good guess might be the three traces $\tr{a}$, $\tr{b}$ and $\tr{ab}$. These numbers don't change when you conjugate, moreover we have already seen in some special cases that, up to conjugation, they completely determine the group.
:::

选择特定的归一化方式，可以进一步消去三个参数。原因是，总存在一个莫比乌斯映射，能够将任意三个点映射到另一个任意的三点组合。这意味着，你可以预先指定这三个点的位置。例如，你可以规定映射 $a$、$A$ 和 $b$ 的吸引不动点分别为 $0$、$1$ 和 $\infty$。事实上，这正是我们在第 207 页中证明模群在共轭意义下唯一时所采用的方法。

由此可见，在共轭等价的条件下，我们应该能够将描述一个双生成元群所需的复数参数数量，从八个减少到仅三个。问题是，这三个参数该如何选取？根据我们在前两章中的经验，一个合理的猜测是：选取 $\tr{a},\tr{b}$ 和 $\tr{ab}$ 作为参数。这三个数在共轭下保持不变，而且我们已经在一些特殊情形中见过，单凭它们（在共轭意义下）就足以完全确定该群。

:::{.simple}
Our upgraded algorithm is going to work by moving systematically round the boundary of the word tree, plotting limit points in order when it detects they are close. This means that for the program to work reasonably efficiently, it will be best if the limit set is still, at least roughly speaking, a connected loop. In the situation of pairing opposite Schottky circles this happens provided all four basic commutators are parabolic with traces equal $-2$. As we saw on p. 189, we can arrange this by choosing $\tr{ab}$ to satisfy the Markov identity
$$
(\tr{a})^2 + (\tr{b})^2 + (\tr{ab})^2 = \tr{a} \tr{b} \tr{ ab}.
$$
:::

我们升级后的算法将通过沿着单词树的边界系统地移动，在发现极限点接近时按顺序将其标出。为了让程序尽可能高效地运行，极限集最好仍然是一个连通的环，或者至少大致如此。

在配对相对的 Schottky 圆时，只要四个基本交换子都是迹为 $-2$ 的抛物型元素，这种情况就会成立。正如我们在第 189 页所看到的，可以通过选择 $\tr{ab}$ 满足马尔可夫恒等式来实现这一点：
$$(\tr{a})^2 + (\tr{b})^2 + (\tr{ab})^2 = \tr{a} \tr{b} \tr{ ab}.$$

:::{.simple}
So for most of this chapter, we shall insist that $\tr{abAB} = -2$, or equivalently that our three parameters $t_a$, $t_b$ and $t_{ab}$ satisfy the Markov equation. Give or take some trouble with square roots, this reduces our parameter count from 3 to 2, namely $t_a$ and $t_b$. We shall give the name **parabolic commutator groups** to those groups in which $\tr{abAB} = -2$. They are also sometimes known as **once-punctured torus groups**, because of the topological picture on p. 190.
:::

因此，在本章的大部分内容中，我们将始终假设 $\tr{abAB} = -2$。换句话说，我们的三个参数 $t_a$、$t_b$ 和 $t_{ab}$ 满足马尔可夫方程。撇开一些与平方根有关的麻烦不谈，这一假设将参数的数量从 3 个降至 2 个，即 $t_a$ 和 $t_b$。我们将把满足 $\tr{abAB} = -2$ 的群称为抛物交换子群（parabolic commutator groups）。它们有时也被称为一次穿孔环面群（once-punctured torus groups），这是因为在第 190 页的拓扑图景中可以看到它们的相关性。

:::{.simple}
In Box 21 we have revealed Grandma's treasured family recipe for the specially normalized two-parameter family which we used for most of our own explorations.^1 The matrix entries of the two generators $a$ and $b$ are written down entirely in terms of the parameters $t_a$ and $t_b$, which you can set equal to any two complex numbers you care to choose. As you can see, the recipe is designed so that these numbers are the traces of $a$ and $b$. Among all possible normalizations and hence many different possible recipes she might equally well have tried, Grandma selected this one mixed with some special spices to make the pictures come out really nice. If you put in real values for $t_a$ and $t_b$, you get the group which pairs Schottky circles arranged in the pattern in frame (vi) on p. 176. The same formula gave us the generators for the Apollonian gasket on p. 201. There are some hints on how to verify that just knowing $t_a$ and $t_b$ really does fix the group in Project 8.4.
:::

在框 21 中，我们揭示了奶奶传下来的秘制家族配方，这是一种特定归一化的双参数族，我们的大部分探索都采用了这种方法。两个生成元 $a$ 和 $b$ 的矩阵元素完全由参数 $t_a$ 和 $t_b$ 表示，你可以任意选择这两个参数为任何复数。正如你所见，这份配方经过奶奶亲手调配，加上了一些独家秘制香料，使得这两个数恰好是 $a$ 和 $b$ 的迹。

归一化的方法有很多种，奶奶特意选择了这一份，加上她的独门手法，调出了让图像变得格外出彩的效果。如果你将 $t_a$ 和 $t_b$ 设为实数值，就会得到与第 176 页图 (vi) 中排列的 Schottky 圆相配对的群。同样的公式还为我们提供了第 201 页阿波罗尼奥斯垫片的生成元。项目 8.4 提供了一些提示，教你如何验证仅凭 $t_a$ 和 $t_b$ 确实足以确定该群。

:::{.simple}
Gosh, it's so easy; why is there any need to explain? As you can see, in the second step of her recipe Grandma arranged that $t_{ab}$ satisfies the Markov identity, thereby ensuring that $\tr{abAB} = -2$. We had better check that multiplying $a$ and $b$ gives the formula we have written down for $ab$, and that the determinants of $a$ and $b$ are both 1. You may wish to resort to your favourite symbolic algebra program, or, for the traditionalists, we recommend beginning with a good pile of blank scratch paper, copying the two matrices $a$ and $b$ carefully, and multiplying them out very slowly indeed.
:::

天哪，这也太简单了，还需要解释吗？正如你所见，在她的食谱第二步中，奶奶巧妙地安排了 $t_{ab}$ 满足马尔可夫恒等式，从而确保 $\tr{abAB} = -2$。不过，我们还是最好核对一下：把 $a$ 和 $b$ 相乘，是否确实得到了我们写下的 $ab$ 公式？还有，$a$ 和 $b$ 的行列式是否真的都是 1？你可能想借助自己喜欢的符号代数程序，或者，如果你更喜欢传统方法，我们建议你备上一大堆干净的草稿纸，把矩阵 $a$ 和 $b$ 仔细抄下来，然后一步一步、慢吞吞地把它们算出来。


:::{.simple #box21}
**Box 21: Grandma’s special parabolic commutator groups**

**框 21：外婆的特殊抛物线换位子群**

1. Choose any complex numbers $t_a$ and $t_b$.
2. Choose one of the solutions $x$ of the quadratic equation
   $$x^2 - t_a t_b x + t_a^2 + t_b^2 = 0$$
    and set $t_{ab} = x$.
3. Compute
    $$z_0 = \frac{(t_{ab} - 2) t_b}{t_b t_{ab} - 2 t_a + 2 i t_{ab}}.$$
4. Compute the generator matrices:
   $$a = \begin{pmatrix}
   \frac{t_a}{2} & \frac{t_a t_{ab} - 2 t_b + 4i}{(2 t_{ab} + 4) z_0} \\
   \frac{(t_a t_{ab} - 2 t_b - 4i) z_0}{2 t_{ab} - 4} & \frac{t_a}{2}
   \end{pmatrix}$$
    $$b = \begin{pmatrix}
    \frac{t_b - 2i}{2} & \frac{t_b}{2} \\
    \frac{t_b}{2} & \frac{t_b + 2i}{2}
    \end{pmatrix}.$$
5. It’s worth noting that the product $ab$ is also quite simple:
    $$ab = \begin{pmatrix}
    \frac{t_{ab}}{2} & \frac{t_{ab} - 2}{2 z_0} \\
    \frac{(t_{ab} + 2) z_0}{2} & \frac{t_{ab}}{2}
    \end{pmatrix}.$$

One could compute $b$ and $ab$ first, and then find $a$ by multiplying $ab$ on the right by the inverse of $b$, that is, $a = (ab)B$.


1. 选取任意复数 $t_a$ 和 $t_b$。  
2. 解以下二次方程，取其中一个解为 $x$：
$$x^2 - t_a t_b x + t_a^2 + t_b^2 = 0.$$  
然后令 $t_{ab} = x$。  
3. 计算
$$z_0 = \frac{(t_{ab} - 2) t_b}{t_b t_{ab} - 2 t_a + 2 i t_{ab}}.$$  
4. 计算生成元矩阵：
$$a = \begin{pmatrix}
\frac{t_a}{2} & \frac{t_a t_{ab} - 2 t_b + 4i}{(2 t_{ab} + 4) z_0} \\
\frac{(t_a t_{ab} - 2 t_b - 4i) z_0}{2 t_{ab} - 4} & \frac{t_a}{2}
\end{pmatrix}$$  
$$b = \begin{pmatrix}
\frac{t_b - 2i}{2} & \frac{t_b}{2} \\
\frac{t_b}{2} & \frac{t_b + 2i}{2}
\end{pmatrix}.$$  
5. 值得注意的是，矩阵 $ab$ 也有一个相对简单的形式：  
$$ab = \begin{pmatrix}
\frac{t_{ab}}{2} & \frac{t_{ab} - 2}{2 z_0} \\
\frac{(t_{ab} + 2) z_0}{2} & \frac{t_{ab}}{2}
\end{pmatrix}.$$  

我们也可以先计算 $b$ 和 $ab$，然后通过将 $ab$ 右乘以 $b$ 的逆矩阵来求得 $a$，即 $a = (ab) B$。
:::

:::{.simple}
All the groups made using Grandma's recipe have a rather beautiful symmetry, which Grandma felt was a very flavourful ingredient in her groups. You may notice that the diagonal entries in both $a$ and $ab$ are the same. This has the consequence, immediately noticeable in all our pictures, that the limit set of any group made using her recipe is symmetrical under the 180° rotation about the origin $O$. How this works is explained in Note 8.1.

Lastly, what about that mysterious number $z_0$ in the off-diagonal entries of $a$ and $ab$? Grandma could just have left it out of her recipes altogether, and then $z_0$ would have been none other than the fixed point of the commutator $abAB$. By conjugating by a map that moves $z_0$ to 1, Grandma has added a little extra style to her pictures. To get the hang of her recipe, you may like to work through Projects 8.1 and 8.2.
:::

所有按照祖母配方制作的群都具有相当美丽的对称性，祖母认为这是她的群中一个非常独特且富有风味的“成分”。你可能会注意到，矩阵 $a$ 和 $ab$ 的对角线元素是相同的。这个特性直接导致了一个显而易见的结果：在我们所有的图像中，使用她配方制作的群的极限集在关于原点 $O$ 的 $180^\circ$ 旋转下是对称的。这个现象的原理在注释 8.1 中已经做了详细说明。

最后，再来谈谈矩阵 $a$ 和 $ab$ 非对角线元素中的那个神秘数字 $z_0$。祖母本可以完全省略它，这样，$z_0$ 就会成为交换子 $abAB$ 的不动点。通过使用一个将 $z_0$ 移动到 1 的映射进行共轭，祖母为她的图像增添了一点额外的风格。如果你想更好地理解她的配方，不妨尝试完成项目 8.1 和 8.2。


# Let's play (gently at first)

![Figure 8.2. Varying parameters: from $t_a = t_b = 3$ to $t_a = t_b = 2$. We wrote down the generators for the group in frame (iii) in Project 6.5, and frame (vi) is the Apollonian gasket. \
图 8.2. 参数变化：从 $t_a = t_b = 3$ 到 $t_a = t_b = 2$。我们在项目 6.5 的框架 (iii) 中写下了该群的生成元，而框架 (vi) 则是阿波罗尼亚垫片。](/images/indra/fig-8.2.jpg){width=500 #fig-8.2}

:::{.simple}
To ensure all is working smoothly and to gain familiarity with what to expect from Grandma's recipe, we are going start our play rather gently with groups in which the traces of the generators $a$ and $b$ are both real.

Figure 8.2 shows the outcome of our first experiment. We made it by running the program many times, keeping the two traces $t_a$ and $t_b$ equal and real-valued, sliding down from the initial value 3 to the final value 2. These groups can be made by pairing tangent circles, and we have shown the Schottky circles. In the first three frames, the limit set is just the unit circle and the group is Fuchsian. The arcs rotate as the traces decrease until they reach the symmetrical position in frame (iii). You may recognize this picture - it is exactly the group in frame (vi) on p. 176. As we move past the symmetric position, something dramatic happens. The limit set crinkles up and the group has become quasifuchsian. As we keep moving, the lowermost limit points (these are actually the fixed points $\overline{b},\overline{B}$) become corners with evermore pronounced angles, until finally they come together like a crab's pincers, chopping the region enclosed by the limit set into a myriad of tiny disks. This last frame should look familiar too - we have arrived at our old friend the Apollonian gasket from Chapter 7!
:::

为了确保一切顺利，并且熟悉祖母食谱的“味道”，我们打算从轻松的开始，先从那些生成元 $a$ 和 $b$ 的迹都是实数的群开始。

图 8.2 展示了我们第一次实验的结果。我们通过多次运行程序获得了这个结果，始终保持两个迹 $t_a$ 和 $t_b$ 相等且为实数值，并让它们从初始值 3 缓慢滑动至最终值 2。这样的群体可以通过配对相切的圆来构造，而我们标出了 Schottky 圆。

在最初的三个画面中，极限集仅仅是单位圆，群是 Fuchsian 群。随着迹的减小，弧线缓慢旋转，直到它们在画面 (iii) 中达到了对称位置。你可能会觉得这幅图有些眼熟——它正是第 176 页画面 (vi) 中的那个群。

当我们越过对称位置时，戏剧性的变化发生了。极限集皱缩起来，群变成了拟 Fuchsian 群。继续移动时，最下方的极限点（实际上是不动点 $\overline{b}$ 和 $\overline{B}$）逐渐变得越来越尖锐，最终它们像螃蟹的钳子一样夹拢在一起，将极限集所围成的区域切割成无数个微小的圆盘。

这最后一帧你一定也觉得眼熟——我们回到了第七章中那个熟悉的老朋友——阿波罗尼奥斯垫片！

:::{.note #note-8.1}
**Note 8.1: Grandma’s symmetry**

**注解 8.1：外婆的对称性**

Suppose $M$ is a matrix whose diagonal entries are equal, in other words with the special form
$$M = \begin{pmatrix} r & s \\ t & r \end{pmatrix}.$$
Such transformations have a special symmetry, encoded in the equation
$$-M(-z) = \frac{r(-z) + s}{t(-z) + r} = \frac{rz - s}{-tz + r} = M^{-1}(z).$$
To interpret this equation, write $j$ for the 180° rotation $z \mapsto -z$. Using the relation $j^{-1} = j$, this equation says that $jMj^{-1} = M^{-1}$. In other words, conjugating the transformation $M$ by 180° rotation about $O$ carries $M$ to $M^{-1}$.

In Grandma’s recipe, both $a$ and $ab$ have this property, which means $jaj = A$ and $jabj = BA$. Since $j$ is its own inverse, these imply $jAj = a$ and $jBAj = ab$. By combining these relations, we can show that any word in $a$, $b$, $A$ and $B$ is conjugated by $j$ into some other word in $a$, $b$, $A$ and $B$. That is, conjugation by $j$ does not change the group $G$ generated by $a$ and $b$, nor does it change the complete collection of infinite words in the generators. That is enough to tell us that the limit set of $G$ is unchanged by the transformation $j$. As an example, consider applying $j$ to the infinite word $abaBA \cdots$:

$$jabaBA \cdots = jabj jaj jBAj \cdots = BA A ab \cdots.$$

设 $M$ 是一个对角元素相等的矩阵，具体形式为
$$M=\begin{pmatrix} r & s \\ t & r \end{pmatrix}.$$
这种变换具有一种特殊的对称性，它可以通过以下等式来描述：
$$-M(-z) = \frac{r(-z) + s}{t(-z) + r} = \frac{rz - s}{-tz + r} = M^{-1}(z).$$

要理解这个等式，设 $j$ 表示将 $z$ 映射到 $-z$ 的 180° 旋转。利用 $j^{-1} = j$ 这一性质，上述等式表明 $jMj^{-1} = M^{-1}$。换句话说，对变换 $M$ 施加以原点为中心的 180° 旋转，其结果是将 $M$ 变为其逆变换 $M^{-1}$。

在外婆的配方中，$a$ 和 $ab$ 都具有这一性质，这意味着 $jaj = A$，$jabj = BA$。由于 $j$ 是它自身的逆映射，这些关系进一步推出 $jAj = a$，以及 $jBAj = ab$。

通过结合这些关系，我们可以证明，任何由 $a,b,A,B$ 组成的词在经过 $j$ 的共轭后，仍然是由 $a,b,A,B$ 构成的某个词。也就是说，$j$ 的共轭不会改变由 $a$ 和 $b$ 生成的群 $G$，也不会改变由这些生成元构成的所有无限词的完整集合。这足以说明，群 $G$ 的极限集在变换 $j$ 作用下保持不变。

举个例子，考虑将 $j$ 作用于无限词 $abaBA\cdots$：
$$jabaBA \cdots = jabj jaj jBAj \cdots = BA A ab \cdots.$$
:::

![Figure 8.3. The program hits chaos. The left side is the result of running the DFS algorithm for just a short length of time; on the right we had slightly more patience. The picture resulting from running the program forever (that is, without the safety cut-off lev_max) is slightly less interesting. Groups whose limit set look like this are called non-discrete. \
图 8.3 程序进入混沌状态。左侧是 DFS 算法运行短短一段时间的结果；右侧则是我们稍作耐心等待后得到的成果。如果让程序一直运行下（即不设安全上限 lev_max），得到的图像就会显得略微单调。那些极限集呈现这种形态的群体，被称为非离散群。](/images/indra/fig-8.3.jpg){width=500 #fig-8.3}


:::{.simple}
What happens if we decrease the traces just a little bit further and try $t_a = t_b = 1.9$? *Warning, warning, danger, danger*! The Schottky circles will start to overlap, and it becomes not at all clear what to expect. You can see what we are worried about in Figure 8.3. In this picture, we chose a pretty large cut-off value `epsilon = 0.1` in comparison to the frame size, 2.2 by 2.2. In contrast to the previous pictures, you can actually see the line segments drawn by the DFS program. Some of them are actually much larger than `epsilon`. That is because no matter how far we go down the branch, limit points which are supposed to be neighbours never get truly close. The branch is terminated only by the built-in maximum depth levjnax. It is lucky we built in this safeguard; otherwise our program would be stuck running a never ending loop. The truth is, Figure 8.3 should be a solid black square.
:::

如果我们将迹的值再稍微减少一些，并尝试设定 $t_a = t_b = 1.9$，会发生什么呢？警告，警告，危险，危险！肖特基圆开始重叠，情况变得完全不可预测。你可以在图 8.3 中看到我们担心的情况。

在这幅图中，我们选择了一个相对于帧尺寸（2.2×2.2）来说相当大的阈值 `epsilon = 0.1`。与之前的图像不同，你现在可以看到 DFS 程序绘制的线段。其中一些线段的长度实际上远远超过了 `\epsilon`。这是因为无论我们沿着分支向下走多远，原本应相邻的极限点始终无法真正靠近。分支的终止仅由内置的最大深度 `lev_max` 控制。

幸运的是，我们设置了这个保护机制，否则程序将陷入永无止境的循环。事实上，图 8.3 本应是一块实心的黑色方块。

:::{.simple}
The groups in Figure 8.2 are actually conjugates of the groups made from our original circle pairing recipe on p.170 in Chapter 6. To seethis, let $x = u = t_a/2$. The connection between the two constructions is shown in Figure 8.4 which was drawn using Grandma's recipe for the quasifuchsian group with $t_a = t_b = 2.2$. Our original recipe gave roughly equal weight to each of the four generators $a$, $A$, $b$ and $B$. By contrast, Grandma's recipe emphasizes symmetry relative to the alternative generators $a$ and $ab$. The word tree comes out distorted so that words beginning with $a$ occupy half the picture, the other half being divided among words beginning with the other three letters $A$, $b$ and $B$. The basic tile in Figure 8.4 is the one which has one side of each colour. The red side is part of the circle $C_a$, the blue side of $C_b$, and so on. Its vertices are the fixed points of the four commutators $abAB$, $bABA$, $ABab$ and $BabA$. As you can see, the red part is exactly half the limit set. The other half can be obtained by reflecting through the origin, using the map $j : z \mapsto -z$. (This trick was in part the original motivation for Grandma's normalization: we had only to plot a quarter of the limit points, and by reflecting got the rest of the picture for free.)
:::

图 8.2 中的群实际上是我们在第 6 章第 170 页使用原始圆配对方法构造的群的共轭群。为了理解这一点，设 $x = u = t_a / 2$。两种构造之间的联系如图 8.4 所示，该图是按照祖母的拟富克斯群配方绘制的，其中 $t_a = t_b = 2.2$。

我们的原始配方对四个生成元 $a$、$A$、$b$ 和 $B$ 赋予了大致相等的权重。而与此不同，祖母的配方则更加强调相对于替代生成元 $a$ 和 $ab$ 的对称性。结果，单词树出现了扭曲，导致以字母 $a$ 开头的单词占据了图像的一半，另一半则被以字母 $A$、$b$ 和 $B$ 开头的单词所瓜分。

图 8.4 中的基本瓷砖是每条边各具一种颜色的那一块。红色边属于圆 $C_a$ 的一部分，蓝色边属于圆 $C_b$ 的一部分，依此类推。该瓷砖的顶点是四个交换子 $abAB$、$bABA$、$ABab$ 和 $BabA$ 的不动点。如你所见，红色部分恰好是极限集的一半。另一半可以通过使用映射 $j : z \mapsto -z$ 对原点进行反射得到。（这一技巧在某种程度上正是 Grandma 归一化的原始动机：我们只需绘制四分之一的极限点，然后通过反射即可免费获得图像的其余部分。）

![Figure 8.4. The anatomy of the limit set for the group specified by Grandma’s recipe with $t_a = t_b = 2.2$. The different colours show the pieces of the limit set that begin with different one letter prefixes: red for those beginning with $a$, green for $A$, blue for $b$, and yellow for $B$. We have marked certain limit points by their infinite words, for example $\overline{a}$ marks the attracting fixed point of $a$. Since it is represented by the infinite word $aaaa\cdots$, it appears in the red section. This section also contains the fixed point of $aba^{-1}$ whose infinite word is $a\overline{b} = abbbb\cdots$, and $aBa^{-1}$ with infinite word $a\overline{B} = aBBBB\cdots$. Notice the various fixed points which seem to be coming together as the traces $t_a$ and $t_b$ get near 2. \
图 8.4. 按照“奶奶的配方”中设定的群（参数 $t_a = t_b = 2.2$）生成的极限集的剖析图。不同颜色表示以不同单字母前缀开头的极限集部分：红色对应以 $a$ 开头的部分，绿色对应以 $A$ 开头的部分，蓝色对应以 $b$ 开头的部分，黄色对应以 $B$ 开头的部分。我们用它们的无穷字标出了某些极限点。例如，$\overline{a}$ 表示 $a$ 的吸引不动点。由于它的无穷字是 $aaaa\cdots$，因此出现在红色区域内。该区域还包含 $aba^{-1}$ 的不动点，其无穷字为 $a\overline{b} = abbbb\cdots$，以及 $aBa^{-1}$ 的不动点，其无穷字为 $a\overline{B} = aBBBB\cdots$。请注意，随着迹数 $t_a$ 和 $t_b$ 接近 2，某些不动点似乎逐渐聚集在一起。
](/images/indra/fig-8.4.jpg){width=500 #fig-8.4}


# The fun begins: traces go complex

![Figure 8.5. Testing some complex values of the traces. For comparison we have made the viewing window the same in all four frames. \
图 8.5 测试一些复杂值的轨迹。为了便于比较，我们在所有四个帧中设置了相同的观察窗口。](/images/indra/fig-8.5.jpg){width=500 #fig-8.5}

:::{.simple}
Our play has been kept artificially gentle by restricting to examples in which $t_a$ and $t_b$ are both real. Such groups always come equipped with a chain of four tangent Schottky circles, so plotting their limit sets is really nothing new. The real fun starts when ta and tb go properly complex. Figure 8.5 shows the results of gingerly testing the waters. What were the Schottky circles appear to have gone haywire, but at least the limit sets are still loops.
:::

为了保持温和的氛围，我们仅选取了 $t_a$ 和 $t_b$ 都为实数的例子。这样的群总是配备有一条由四个切线 Schottky 圆组成的链条，因此，绘制它们的极限集实际上并不算什么新鲜事。真正有趣的部分出现在当 $t_a$ 和 $t_b$ 变为复数时。图 8.5 展示了我们小心翼翼地试水的结果。原本是 Schottky 圆的部分似乎已经乱成一团，但至少极限集仍然是环状的。

:::{.simple}
The curling and twisting you can see in these limit sets is caused by tiny spiralling motions of loxodromic transformations. Transformations with non-real traces are always loxodromic, so as soon as we make $t_a$ and $t_b$ complex, we can expect curling to occur. The amount of curling of a transformation depends not so much on the imaginary part of its trace as on the tightness of the spiral motion near its fixed points. Referring back to Chapter 3, you will see the spiral is tightly coiled if the multiplier is near 1, so the trace is near 2, and if in addition the imaginary part is comparatively small. You can see this in evidence in the substantial curling in the last two frames in Figure 8.5, where $t_a$ and $t_b$ are near 2 and only slightly complex. There are no Schottky circles, but on the `inside`, we have drawn red circular arcs meeting at the fixed points of the four basic commutators. (We made the first arc perpendicular to the direction of the parabolic at the fixed point.) You can tell they are no longer pieces of Schottky circles, because Schottky circles never intersect. You might wonder if the same group might be constructed as a Schottky group starting from a different set of circles, and with different generators doing the pairings. Whether or not this is possible, we don't know.
:::

你在这些极限集上看到的弯曲和扭曲，是由斜航型变换的小螺旋运动引起的。具有非实迹的变换总是斜航型变换，因此，只要我们将 $t_a$ 和 $t_b$ 设为复数，就可以预见到弯曲现象的出现。变换的弯曲程度不仅仅取决于迹的虚部，更依赖于其不动点附近螺旋运动的紧密程度。回到第三章，你会发现当乘数接近 1 时，螺旋会紧密盘绕，此时迹接近 2，且如果虚部相对较小，这种情况更加明显。你可以在图 8.5 的最后两帧中看到这一现象，这里 $t_a$ 和 $t_b$ 接近 2 且仅稍微为复数。没有 Schottky 圆，但在“内部”，我们画出了红色的圆弧，它们在四个基本交换子点的固定点相交。（我们使第一条圆弧垂直于固定点的抛物线方向。）你可以判断它们不再是 Schottky 圆的部分，因为 Schottky 圆是永远不会相交的。你可能会好奇，是否可以从一组不同的圆出发，构造出一个 Schottky 群，并使用不同的生成元来完成配对。我们不知道这是否可能。


![Figure 8.6. Dr. Stickler blown about inside the limit set of a quasifuchsian group with $t_a=t_b=1.91+0.05i$. . You can see a full view of this limit set in Figure 8.1. We made this picture by implementing a tiling type plot with the prostrate Dr. Stickler as the initial seed. \
图 8.6. 斯蒂克勒博士在一个拟福克斯群的极限集内被吹动，参数 $t_a=t_b=1.91+0.05i$。你可以在图 8.1 中看到这个极限集的完整视图。我们通过实现一种镶嵌类型的图形，并以斯蒂克勒博士躺倒的形象作为初始种子，制作了这张图片。](/images/indra/fig-8.6.jpg){width=500 #fig-8.6}

:::{.simple}
As you can see, all these groups are still quasifuchsian, meaning that the limit set is a connected curve which doesn't cross itself and which divides the plane into an inside' and 'outside'. These are the first  groups whose limit sets we genuinely could not have drawn using our old Schottky circle algorithm. It would be nice to explore the region inside the limit set, but since there are no Schottky circles to work with, it can become a very tricky problem to find suitable tiles. Undeterred, we blew up a small part of a nice limit set with $t_a = t_b= 1.91 + 0.05i$ and set Dr. Stickler lying flat on his back in red on the righthand side. You can see him in Figure 8.6 spinning around, carried into every nook
and cranny, so that there is exactly one Dr. Stickler for every word in the group.
:::

正如你所看到的，这些群仍然是准福克群（quasifuchsian），意味着其极限集是一个连通曲线，既不交叉自身，也将平面分成了“内部”和“外部”两部分。这些是我们通过旧的 Schottky 圆算法，确实无法画出的第一个群体极限集。虽然我们很想探索极限集内部的区域，但由于没有 Schottky 圆可以使用，找到合适的瓷砖就变成了一个非常棘手的问题。尽管如此，我们依然不气馁，放大了一个漂亮的极限集的一小部分，设定了 $t_a = t_b = 1.91 + 0.05i$，并让斯蒂克勒博士躺在右侧的平面上，用红色标出。你可以在 图 8.6 中看到他旋转的样子，他被带入每一个角落与缝隙中，所以每一个群体中的每个词语都对应着一个斯蒂克勒博士。


![Figure 8.7. All the tiles are obtained from the red one by applying words in the group. What is the red tile? In Figure 8.6, note that the red Dr. Stickler is larger than all his copies. We could try putting a miniscule Dr. Stickler anywhere and see if he is larger than his copies. The places where this happens are the points of the red tile. \
图 8.7 中，所有瓷砖都是通过对红色瓷砖应用群中的词语得到的。红色瓷砖是什么？在图 8.6 中，注意红色的 Dr. Stickler 比所有复制品都要大。我们可以尝试在任何地方放置一个微小的 Dr. Stickler，看看他是否比他的复制品大。这种情况发生的地方就是红色瓷砖的点。](/images/indra/fig-8.7.jpg){width=500 #fig-8.7}

:::{.simple}
In Figure 8.7 we have actually found a tiling for a quasifuchsian group with $t_a = 2 + 0.1i, t_b = 3$. Notice that the tiles are no longer four- but six-sided. As ever, the different tiles are carried onto each other by the transformations in the group. They get exceedingly skinny in the middle: if we varied our parameters just a little bit each of these tiles would fall apart into two halves. We found this particular tiling by a completely different method explained briefly in the caption.
:::

在图 8.7 中，我们实际上为一个准福克斯群找到了一个铺砖，参数为 $t_a = 2 + 0.1i$，$t_b = 3$。注意，这些瓷砖不再是四边形，而是六边形。正如往常一样，不同的瓷砖通过群中的变换相互映射。它们在中间变得异常狭长：如果我们稍微调整一下参数，每一块瓷砖都会裂成两半。我们通过一种完全不同的方法找到了这个特殊的铺砖，简要的解释见图注。

![Figure 8.8. Our first probe. In this sequence, $t_b=3$ and $t_a=x+0.05i$ with $x$ varying from 3 down to 1.9. \
图 8.8. 我们的第一次探测。在这个序列中，$t_b = 3$，$t_a = x + 0.05i$，其中 $x$ 从 3 变化到 1.9。
](/images/indra/fig-8.8.jpg){width=500 #fig-8.8}

:::{.simple}
The curling in the last two frames of Figure 8.5 piqued our interest, hinting at directions which might be interesting to explore. Just how much curling is possible? The interest seems to centre on traces near 2, but ever so slightly complex. To investigate, we shall run an experiment in which we fix the trace $t_b$ safely equal 3, and then let $t_a$ run through values $x + 0.05i$, where $x$ is a real number which starts at 3 and slowly decreases to some dangerous transitional value, as yet unknown.  Figure 8.8 shows the preliminary results. The first frame is just a slightly wobbly circle. The second and third frames show some bumps forming, with the first hints of spiralling in the third frame at $x = 2$. From the chaotic fourth frame we deduce that somewhere between $x = 2.0$ and $x = 1.9$, we stepped over the boundary. The live version of the last frame is more interesting: the DFS algorithm frantically criss-crosses the picture trying to draw a solid black square. To locate the transition point more exactly, in Figure 8.9 we decrease $x$ by finer increments from 2.0 to 1.9. From 1.97 to 1.94 to 1.91, you can see the bumps on the limit set developing into pronounced and ever more tightly whirling spirals. We know from our earlier probe that the boundary lies above $x = 1.90$; when we ever-so-carefully stepped to 1.905, the DFS plot tried to fake sanity for a while, until its turbulent
behaviour at last manifested and we terminated the program, allowing us at least to see some of the spirals that are still evident. We have pinned down the transition to madness somewhere between $x = 1.91$ and 1.905.
:::

图 8.5 的最后两帧中出现的弯曲引起了我们的兴趣，暗示了一些可能值得探索的方向。那么，究竟有多少弯曲是可能的呢？兴趣似乎集中在接近 2 的轨迹上，但又略微带有复数特性。为了探讨这一点，我们进行了一次实验，将轨迹 $t_b$ 固定为安全的 3，然后让 $t_a$ 通过值 $x + 0.05i$ 变化，其中 $x$ 是一个实数，起始值为 3，并逐渐减小到某个尚未确定的危险过渡值。图 8.8 展示了初步结果。第一帧只是一个略微晃动的圆形。第二帧和第三帧显示出一些隆起的形成，第 3 帧在 $x = 2$ 时出现了螺旋的初步迹象。从混乱的第四帧中，我们推断出在 $x = 2.0$ 到 $x = 1.9$ 之间的某个位置，我们跨越了边界。最后一帧的实时版本更加有趣：DFS 算法疯狂地交叉扫描图像，试图绘制一个实心的黑色正方形。为了更精确地定位过渡点，在图 8.9 中，我们将 $x$ 从 2.0 到 1.9 以更小的增量减少。从 1.97 到 1.94 再到 1.91，你可以看到极限集上的隆起逐渐发展成明显且越来越紧密旋转的螺旋。我们从早前的探索中知道，边界位于 $x = 1.90$ 之上；当我们小心翼翼地走到 1.905 时，DFS 图尝试保持“理智”了一段时间，直到它的动荡行为最终显现出来，我们终止了程序，至少让我们看到了仍然明显存在的一些螺旋。我们已经将过渡到混乱的边界定位在 $x = 1.91$ 和 1.905 之间。

![Figure 8.9. In this refined probe, $t_b = 3$ and $t_a = x + 0.05i$ with $x$ varying from 1.97 down to 1.905. In (iv), the program was terminated prematurely, when the erratic nature of the plot became clear. \
图 8.9. 在这个改进的探针中，$t_b = 3$，$t_a = x + 0.05i$，其中 $x$ 从 1.97 变化到 1.905。在 (iv) 中，当图像的不规则性变得明显时，程序被提前终止。](/images/indra/fig-8.9.jpg){width=500 #fig-8.9}

# Transition to madness

:::{.simple}
We have now three times bumped into places where our limit set plot has gone wild. What is going on? As we warned at the outset, there is no reason to expect that our limit set plot, bereft of the Schottky circles, will produce anything reasonable at all. The greater miracle, perhaps, is that it ever does! What is happening here is this. If you multiply a large number of matrices together, then you would expect that the resulting matrix product would automatically get 'large'. In the groups which produce reasonable limit sets this is certainly the case. What is going wrong when the limit set goes haywire is that a word in the group which is a long matrix product of many generators unexpectedly turns out to be actually very 'small'. The matrices cancel in a mysterious way, so the manner in which this particular group element moves points around in the plane is not at all what you might expect. Of course, not all entries can be near 0 because the determinant of any matrix in our group is always to equal to 1. So what we mean by saying that a matrix is 'small' is that it is very near the identity matrix $I$. From this point of view, $I$ is the 'smallest' matrix and we measure how large a matrix is by measuring the distance of its entries from those of $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. Groups for which large products stay away from $I$ are called discrete.
:::

我们现在已经遇到三次极限集图形异常的情况。这是怎么回事呢？正如我们一开始所警告的，完全没有理由期望没有 Schottky 圆的极限集图形会产生任何合理的结果。也许更大的奇迹是，它居然偶尔会产生一些合理的东西！现在发生的情况是这样的。如果你将大量矩阵相乘，那么你会期望结果矩阵的乘积会自动变得“很大”。在那些能够产生合理极限集的群体中，这种情况无疑是成立的。而当极限集出现异常时，问题出在某个群中的一个词，它是许多生成元的长矩阵积，结果竟然变得非常“小”。这些矩阵以一种神秘的方式相互抵消，因此这个特定群元素在平面上移动点的方式与你预期的完全不同。当然，并非所有的元素都可以接近 0，因为我们群中任何矩阵的行列式总是等于 1。那么，当我们说一个矩阵是“小”的时候，指的是它非常接近单位矩阵 $I$。从这个角度来看，$I$ 是“最小”的矩阵，我们通过测量矩阵的元素与 $\begin{pmatrix} 1 & 0 \ 0 & 1 \end{pmatrix}$ 的元素之间的距离来衡量矩阵的大小。那些大乘积远离 $I$ 的群称为离散群。

:::{.simple}
You can look for discreteness in our plots by seeing how close $M(z)$ can get to $z$, for any point $z$ in the plane. In the groups we have studied so far, you can always find tiles which cover all of the ordinary set, that is, all parts of the plane not occupied by the limit set itself. If you sit at a point $z$ in the middle of one tile, no points in any other tile can be too close, because no point can be nearer to you than the edges of your tile. But if $M$ was very near to $I$, then $M(z)$ would be very near to $I(z) = z$. This shows that very nasty cancellations can never occur as long as there are some 'limit set free' regions in the plane which can be covered by tiles.
:::

可以通过观察我们图表中的离散性，来查看平面上任意点 $z$ 能有多接近 $M(z)$。在我们目前研究的群组中，你总能找到一些瓷砖，覆盖整个普通集，即覆盖平面上那些没有被极限集本身占据的部分。如果你坐在某个瓷砖中间的点 $z$，那么其他瓷砖上的任何点都不会离你太近，因为没有点能比你的瓷砖边缘更接近你。但如果 $M$ 非常接近 $I$，那么 $M(z)$ 就会非常接近 $I(z) = z$。这表明，只要平面上存在一些可以被瓷砖覆盖的“无极限集”区域，就永远不会发生非常糟糕的抵消现象。

:::{.simple}
It turns out that there is yet another layer of complication because there are groups for which there is no ordinary set at all but which are still discrete. We will look at these in Chapter 10 where we shall be meeting some amazing pictures of groups which are discrete in the strict sense that they contain no matrices too close to $I$, but for which the limit set plot fills out the whole plane, in a magically organised and yet extremely complicated way. For now, though, looking at whether or not the computer plot goes wild and seems to be filling up the page will not lead you far wrong. If you can find a tiling, then it shows you visually that the group is discrete, and if there is no tiling, you had better watch out!
:::

事实证明，还有另一层复杂性存在，因为有些群体根本没有普通集，但它们仍然是离散的。我们将在第 10 章中讨论这些群体，届时我们将看到一些令人惊叹的群体图像，这些群体在严格意义上是离散的，因为它们不包含过于接近 $I$ 的矩阵，但它们的极限集却以一种神奇且极其复杂的方式填满了整个平面。不过，暂时而言，观察计算机绘图是否失控并看起来似乎填满整个页面，通常不会让你走错方向。如果你能找到密铺图案，那么它直观地向你展示了该群体是离散的；如果没有密铺图案，那你最好小心了！