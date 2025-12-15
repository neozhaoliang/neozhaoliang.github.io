---
title: TODO List
url: todo
---

# 写作

- 关于 SO3 的表示的文章，与球谐函数、有限群的不变量、Shephard-Todd 定理的关系。配一个 shadertoy demo。
- S_n 和 GL(n) 的表示论，Schur-Weyl 对偶。
- 六顶点模型，Yang-Baxter 方程和 ASM 的证明。
- 对称平面分拆的 Macdonald 猜想，Hall 多项式，SL(n) 表示在计数中的应用。
- 永不回到原点的二维随机游动，介绍 Doob h-变换、调和测度。
- 扭结与动力系统
- Lie 代数的 Minuscule 表示与对称平面分拆
- GTM A course in enumeration 中剩余的 highlight 问题。
- 二维码与 Reed-Solomon 编码算法介绍
- 图的环空间与割空间，顶点膨胀技巧
- Hilbert 曲线算法与 Golay 码
- Aztec diamond arctic circle 现象的解释
- Random walk, circle packing and conformal mapping.
- Billiard ball，测度论，Poncelet 定理
- Durrett 概率论 Brownian 运动部分改写
- Raymarching 中 sdf 函数与各种变换的数学证明
- 正的 Hausdoff 维数意味常返性 http://www.cmat.edu.uy/~lessa/resource/randomwalknotes.pdf
- 准晶，Faraday 驻波。
- 连分数，圆堆，Fary。
- Fulton algebraic curves, Poncelet porism 的代数几何证明和 Jacobi 椭圆函数证明。
- Mobius gear 和 Quaternion 是啥关系，flockaroo 的 shadertoy
- 蜂巢和 Gauss 整数的关系：https://twitter.com/roice713/status/1497252225785204738?s=20&t=WN0vB5s3eU_riCbC37nWiA
- stable diffusion 学习
- 互锁的折纸 origami 正十二面体 | Interlock 多面体
- 局部中心极限定理 | 电流与同调 | 改写随机游动
- quaternions and polytopes
- 整理概率论的常用结论？单调类、Dynkin...
- 双曲内积
- Thurston 圆堆算法，常返与暂态
- 可裂八元数，G2 与复合代数
- 多连通空间上群作用怎么给出表现
- John Baez 李群和四元数讲义, G2 and the rolling ball, Kepler 问题的四维对称性
- 二维随机游动常返，如双曲、Penrose 等的判断。
- [Weyl 特征公式](http://math.soimeme.org/~arunram/Resources/KacMoodyLieAlgebrasChapterIII.html) 以及基于 BGG resolution 的证明

# Shadertoy

- 3D icosahedral quasicrystal
- Sphere and lattice gears and SO3 representation
- 加速到光速演示相对论
- doyle spiral
- Stange + sl2c 的 shader 研究实现
- 分形反射盒子
- Dirac belt trick
- Bruhat-Tits tree
- Escher circle limit
- Klein quartic 曲面上打台球
- seascape 详解
- 笛沙格定理
- 算术 Coxeter 群
- 三维 Kleinian 群
- 模群面上的测地流和 horocycle 流
- Thurston 的圆堆算法
- Clebsch 曲面上的 27 lines
- [极小曲面](http://bugman123.com/MinimalSurfaces/index.html) 上面跑车


# Python

- Python + cairo 实现 hyperbolic tiling 矢量绘图库。
- 继续可视化项目系列，可视化复分析 + indra's pearls，可视化 circle packings，可视化双曲空间 (Hee Oh)。
- Faraday 驻波模拟
- Conway's Topograph
- magicavoxel and magicaCSG
- mitsuba
- Voxel Turtle
- 纸壳制作多面体?
- sl3 shdertoy?
- epstein 说的扫描线，gifmaze 能画？
- Knuth-Bendix 约化，模群和 indra's pearls
- shadertoy Jigsaw 版本的 monotile


# Indra's pearls 问题

- 为什么 $\mu(p/q)=\pm2$ 分别只有一个解使得群离散？
- 连分式，Farey word 和 cutting sequence 的关系
- 为什么单尖群的普通集，一侧仍然是单穿孔环面，另一侧是一些圆盘，每个圆盘是一个三孔球面？
- 怎么从核心圆链里面读出连分式
- 为什么 Punctured torus 上只能 pinch 一条曲线 ？(交数 > 0，collar 引理导致另一条测地线的长度必然趋于穷)
- 单/双退化群怎么构造的？为什么非周期的无理字单侧和双侧对称分别给出单双退化群？通过袜子戏法，把捏紧 $(1/0,\gamma)$ 曲线变成捏紧 $(\gamma,-1/\gamma)$ ？
- 为什么一侧的常域塌陷，另一侧没事？
- 双尖群总是给出一个circle packing, 这个 circle packing 由两部分组成。这是为什么？


# 概率论常用结论

- Doob-Dynkin 引理
- 单调类定理（两个版本）
- 无穷乘积测度中，任何可测集可以被有限柱集逼近。无限多个随机变量生成的 sigma 域，可以被有限维时间逼近。