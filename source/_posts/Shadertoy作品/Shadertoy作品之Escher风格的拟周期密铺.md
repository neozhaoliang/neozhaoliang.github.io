---
title: "Shadertoy 作品：Escher 风格的拟周期密铺动画"
date: 2020-12-06
categories: [Shadertoy 作品]
tags:
  - Shadertoy
  - de Bruijn
  - Penrose tiling
  - Aperiodic tiling
  - Escher
  - Rhombus
url: "debruijn-rhombus-tiling"
---

周末刚完成了一个有点烧脑的 Shadertoy 项目，Escher 风格的[拟周期密铺](https://en.wikipedia.org/wiki/Aperiodic_tiling)，请欣赏：

<!-- more -->

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/wsKBW1?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

> 小屏的时候有锯齿现象，全屏效果更好，你可以点击窗口左上角的 "Impossible aperiodic tiling" 标题前往 Shadertoy 网站查看源代码。

你能看出这个动画的奥妙之处在哪里吗？

直观上看，这个动画由一些错落有致，但又无缝拼接在一起的房间组成，每个房间有三个面可见，这三个面上各自绘制了一些“窗户”，房间的颜色、窗户的开闭、朝向都是不断变化的，但是仔细一看，诶，好像一些房间的窗口的朝向是“矛盾”的哎？这种整体布局和谐但是局部细节与真实世界矛盾的艺术风格由[埃舍尔](https://en.wikipedia.org/wiki/M._C._Escher) (1898-1972) 所创立，所以这个作品也可以叫做 Escher 风格的不可能密铺。

实际上在这个动画里面基本的几何元素只有菱形，这些菱形分为两种：胖菱形和瘦菱形。在代码中我是对每一个像素，首先确定其所属的菱形，然后计算它到各个装饰元素 (菱形边界、窗户、窗台) 的 signed distance field 函数 $d$，根据 $d$ 的值来混合颜色，特别还根据菱形的类型和方向加上了阴影的效果，使得整个画面看起来有立体感。

生成动画中菱形排列的算法非常奇妙，它来自 de Bruijn 1981 年的发现，是所谓构造拟周期密铺的网格法 [^1] (aperiodic tiling)，而添加窗户的点缀则是受到了 Greg Egan 的 [Javascript 动画](http://gregegan.net/APPLETS/02/02.html)启发。我很久之前就知道 de Bruijn 的方法，并且也写过[一些代码](https://github.com/neozhaoliang/pywonderland/tree/master/src/aperiodic-tilings)绘制这样的图案 (比如这个博客的背景图片)，但是看到 Greg Egan 的动画以后还是萌发了在 shader 里面做出一个更漂亮的 3D 效果来的想法。这个念头憋了好久，终于前几天利用晚上业余时间动手折腾了一番，捣鼓出了上面的效果，当然只是一个伪 3D 的效果。我的动画与 Greg Egan 不同的地方在于 Greg Egan 是精心选择了每一个菱形的窗户的开口方向，使得所有的房间的窗户看起来都是矛盾的；而我这里为了让窗户也能动起来只是随机选择了其开口的方向，所以只有部分房间的窗户是矛盾的。

代码中窗户的绘制方法参考了 Greg Egan 的代码和注释，特别致谢。

[^1]: N.G. de Bruijn. Algebraic theory of Penrose's non-periodic tilings of the plane.