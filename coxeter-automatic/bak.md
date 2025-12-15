---
title: "Coxeter 群语言正则的证明"
---
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
若 $\alpha,\beta\in\Phi$ 满足 $|(\alpha,\beta)|<1$，则必然有 $(\alpha,\beta)=\cos(p\pi/q)$，其中 $p,q$ 是互素的正整数，而且反射 $\ra,\rb$ 生成的子群是有限群。
:::

**证明**：若 $|(\alpha,\beta)|<1$，则内积 $\inn$ 限制在 $\alpha,\beta$ 张成的二维子空间 $U=\span{\{\alpha,\beta\}}$ 上是正定的。

我们可以不妨假定 $\alpha$ 是正根，以及 $\beta=\alpha_s$ 是单根。设
$$\alpha = c_s\alpha_s + \sum_{t\ne s }c_t\alpha_t.$$
由于 $\alpha$ 不可能是 $\alpha_s$ 的正倍数，所以 $\gamma=\alpha - c_s\alpha_s\ne0$。

注意到如果 $a,b\in\bbR$ 使得 $a\gamma+b\alpha_s\in\Phi$，则 $a,b$ 必须同时非负，或者同时非正。如果 $\alpha,\beta$ 所夹的角度是 $\pi$ 的无理数倍，那么 $(\ra s)$ 是 $U$ 上角度为 $\pi$ 的无理数倍的旋转，它的各次幂 $\{(\ra s)^n,n=0,1,\ldots,\}$ 会将 $\alpha$ 映射为 $U$ 中单位圆周上稠密的集合，特别地必然有某个 $k$ 使得 $(\ra s)^k\alpha$ 位于区域 $\{a\gamma+b\alpha_s\mid a > 0, b<0\}$ 中，这与此区域不包含任何根矛盾。所以 $\alpha,\beta$ 所夹的角度必须是 $\pi$ 的有理数倍，形如 $p\pi/q$，从而 $\ra,\rb$ 生成的子群 $D$ 在 $U$ 上的作用是一个二面体群。另一方面 $\inn$ 限制在 $U$ 上是正定的，所以 $V=U\oplus U^\bot$。而 $D$ 作用在 $U^\bot$ 上是平凡的，所以 $D$ 在全空间上的作用也是二面体群。

:::{.definition}
对任何正根 $\alpha\in\Phi^+$，定义其深度为
$$\dp{\alpha}=\min\{\,l(w) \mid w\alpha\in\Phi^-\,\}.$$
对两个正根 $\alpha,\beta$，定义 $\alpha\preceq\beta$ 当且仅当存在 $w\in W$ 使得 $\beta=w\alpha$ 并且
$$\dp{\beta}=\dp{\alpha}+l(w).$$
如果 $\alpha\preceq\beta$ 且 $\alpha\ne\beta$ 我们记为 $\alpha\prec\beta$。
:::

:::{.lemma}
$\preceq$ 是 $\Phi^+$ 上的偏序。
:::

**证明**：若 $\alpha,\beta\in\Phi^+$ 使得 $\alpha\prec\beta$，则必然有 $\dp{\beta}>\dp{\alpha}$，即 $\preceq$ 是反对称的。我们只要再证明 $\preceq$ 是传递的。

设 $\alpha,\beta,\gamma\in\Phi^+$ 满足 $\alpha\preceq\beta$ 和 $\beta\preceq\gamma$，我们来证明 $\alpha\preceq\gamma$。为此我们设
$$\begin{aligned}
\beta &= u\alpha, &\dp{\beta} - \dp{\alpha} = l(u).\\
\gamma &= v\beta, &\dp{\gamma} - \dp{\beta} = l(v).\\
\end{aligned}
$$
显然 $\gamma=vu\alpha$ 且 $\dp{\gamma}-\dp{\alpha}= l(u)+l(v)$。只要再证明 $l(uv)=l(u)+l(v)$ 即可。

设 $w\in W$ 满足 $w\alpha\in\Phi^-$ 且 $l(w)=\dp{\alpha}$。于是
$$\gamma=vu\alpha\Rightarrow u^{-1}v^{-1}\gamma=\alpha \Rightarrow wu^{-1}v^{-1}\gamma\in\Phi^-.$$
从而 $l(wu^{-1}v^{-1})\geq\dp{\gamma}$。

另一方面
$$l(wu^{-1}v^{-1})\leq l(w)+(l(u)+l(v))=\dp{\alpha}+(\dp{\gamma}-\dp{\alpha})=\dp{\gamma}.$$
所以 $l(wu^{-1}v^{-1})=\dp{\gamma}$，特别地上式中所有的不等号都是等号，于是 $l(wu^{-1}v^{-1})= l(w)+l(u)+l(v)$，从而必然有 $l(uv)=l(u)+l(v)$。$\blacksquare$。

:::{.lemma}
设 $\alpha_s$ 是单根，$\alpha\ne\alpha_s$ 是正根，则
$$\dp{s\alpha}=\begin{cases}\dp{\alpha}-1 & \text{if } (\alpha,\alpha_s)>0,\\\dp{\alpha} & \text{if } (\alpha,\alpha_s)=0.\\\dp{\alpha}+1 & \text{if } (\alpha,\alpha_s)<0.\end{cases}$$
:::

第二条是显然的，而第三条可以由第一条得出：只要对 $s\alpha$ 应用第一条的结论即可。所以我们只需要证明第一条。

首先取 $w\in W$ 使得 $l(w)=\dp{\alpha}$ 且 $w\alpha\in\Phi^-$。

1. 如果 $w\alpha_s\in\Phi^-$，则 $l(ws)<l(w)$，并且 $ws$ 满足 $(ws)(s\alpha)<0$，所以 $\dp{s\alpha}\leq l(ws)=l(w)-1$，从而 $\dp{s\alpha}=l(w)-1$。

2. 如果 $w\alpha_s\in\Phi^+$，则 $w(s\alpha)$ 是负根，并且
$$\begin{align*}
w(s\alpha)&=w(\alpha - 2(\alpha,\alpha_s)\alpha_s)\\
&=w\alpha-cw\alpha_s (c>0)
\end{align*}$$
由于 $\alpha\ne\alpha_s$ 是不同的正根，所以它们不共线，从而 $w\alpha$ 和 $w\alpha_s$ 也不共线，于是上式是两个不共线的负根的和，所以任何单反射不能将 $w(s\alpha)$ 变成正根。取 $t\in S$ 使得 $l(tw)<l(w)$，则 $(tw)(s\alpha)$ 仍然是负根，所以 $\dp{s\alpha}\leq l(tw)=l(w)-1$，结论仍然得证。

:::{.corollary}
若 $\alpha\preceq\beta$，则存在序列
$$\alpha=\alpha_0\preceq\alpha_1\preceq\cdots\preceq\alpha_k=\beta$$
使得对每个 $i$ 有 $\dp{\alpha_{i+1}}=\dp{\alpha_i}+1$。
:::

**证明**：设 $w=s_k\cdots s_1$ 满足 $\beta=w\alpha$ 且 $l(w)=\dpb-\dpa$，考虑 $\alpha_i=s_i\cdots s_1\alpha$，其中 $\alpha_0=\alpha$，$\alpha_k=\beta$。从 $\alpha_0$ 到 $\alpha_k$ 经过了 $k=l(w)$ 次单反射，depth 增加了 $l(w)$，但上面的引理告诉我们每次单反射 depth 至多增加 1，所以只能是每一项的 depth 都比前一项增加了 1，即得结论。

:::{.corollary}
若 $\alpha\preceq\beta$，且 $\alpha=\sum c_s\alpha_s,\, \beta=\sum d_s\alpha_s$，则对每个 $s$ 有 $c_s\leq d_s$。
:::

**证明**：若 $\beta=s\alpha$ 则 $\alpha,\beta$ 只有在 $\alpha_s$ 项的系数不同。又 $(\alpha,\alpha_s)<0$ 所以 $d_s>c_s$ 得证。

:::{.definition}
对 $\alpha,\beta\in\Phi^+$，如果对任何 $w\in W$ 都有 $w\alpha\in\Phi^-\Rightarrow w\beta\in\Phi^-$，我们就称 $\alpha$ 支配 $\beta$，记作 $\alpha\dom\beta$。
:::

:::{.lemma}
设 $\alpha,\beta\in\Phi^+$ 且 $\alpha\dom\beta$，则：

1. $(\alpha,\beta)>0$。
2. 若 $w\in W$ 使得 $w\beta$ 是正根，则 $w\alpha\dom w\beta$。
3. 若 $\alpha\prec\alpha'$ 则 $\alpha'$ 不是极小根。换句话说，若一个根是极小根，则在偏序 $\preceq$ 下小于它的根也都是极小根。
4. $\dp{\alpha}\geq\dp{\beta}$，等号当且仅当 $\alpha=\beta$ 时成立。
:::

**证明**：

1. $\ra$ 满足 $\ra \alpha=-\alpha\in\Phi^-$，所以 $\ra\beta=\beta-2(\alpha,\beta)\alpha<0$，这必须 $(\alpha,\beta)>0$ 才行。

2. 显然。

3. 只要对 $\dp{\alpha'}=\dp{\alpha}+1$ 进行证明即可。这时存在单反射 $s$ 使得 $\alpha'=s\alpha$，并且 $(\alpha_s,\alpha)<0$。根据 $\alpha\dom\beta$ 和 $(\alpha,\beta)>0$ 说明 $\beta\ne\alpha_s$，从而 $s\beta$ 是正根，从而 $\alpha'=s\alpha\dom s\beta$ 不是极小根。

4. $\alpha\dom\beta$ 显然意味着 $\dpa\geq\dp{\beta}$。设 $w\in W$ 使得 $w\alpha=-\alpha_s$ 是某个负的单根，则 $w\beta\in\Phi^-$。注意这时 $w^{-1}\alpha_s=-\alpha<0$，所以 $l(sw)<l(w)$。

    + 若 $sw\beta\in\Phi^+$，则由 $w\beta<0$ 可知 $w\beta=-\alpha_s$，再结合 $w\alpha=-\alpha_s$ 可得 $\alpha=\beta$。

    + 若 $sw\beta\in\Phi^-$，则 $\dpb\leq l(sw)<\dpa$。

:::{.corollary}
在有限 Coxeter 群中，所有根都是极小根。
:::

**证明**：设 $w_0$ 是最长元，则 $\alpha\to -w_0(\alpha)$ 置换 $\Phi^+$。我们来验证这个置换保持每个正根的深度不变：若 $w\alpha<0$，则 $w_0w\alpha>0$，从而 $(w_0ww_0)-w_0\alpha<0$，这说明 $\dp{-w_0\alpha}\geq l(w_0ww_0)=l(w)$。对 $-w_0\alpha$ 应用此结论可得 $\dpa\geq\dp{-w_0\alpha}$。从而二者相等。

另一方面我们来验证它翻转 $\dom$ 这个偏序：若 $\alpha\dom\beta$，则
$$\begin{align*}
w\alpha<0&\Rightarrow w\beta<0\\
&\Downarrow\\
w\beta > 0&\Rightarrow w\alpha>0\\
&\Downarrow\\
ww_0\beta > 0&\Rightarrow ww_0\alpha>0\\
&\Downarrow\\
w(-w_0\beta) < 0&\Rightarrow w(-w_0\alpha)<0\\
\end{align*}$$
即确实有 $-w_0\beta\dom -w_0\alpha$。

:::{.proposition}
$\alpha\dom\beta$ 的充要条件是 $\dpa\geq\dpb$ 且 $(\alpha,\beta)\geq1$。
:::

**证明**：我们只考虑 $\alpha\ne\beta$ 的情形即可。

$\Rightarrow$：只要再证明 $(\alpha,\beta)\geq1$。用反证法，若不然，则 $0<(\alpha,\beta)<1$，从而 $\ra,\rb$ 生成一个有限二面体群 $D$。由于在有限群中没有支配关系，所以存在 $w\in D$ 使得 $w\alpha\in\Phi^-,\,w\beta\in\Phi^+$。这与 $\alpha\dom\beta$ 矛盾。

$\Leftarrow$：我们先考虑 $\beta=\alpha_s$ 是一个单根的情形。由于 $\alpha\ne\beta$ 所以 $s\alpha$ 仍然是正根。我们发现
$$(\alpha,s\alpha)=(\alpha,\alpha-2(\alpha,\alpha_s)\alpha_s)=1-2(\alpha,\alpha_s)^2\leq -1.$$
所以有无穷多个形如 $a\alpha+b\alpha_s$ 的正根，其中 $a,b>0$。

用反证法，如果 $\alpha$ 不支配 $\beta=\alpha_s$，则存在 $w\in W$ 使得 $w\alpha\in\Phi^-$ 但 $w\alpha_s\in\Phi^+$。由于
$$w(s\alpha)=w\alpha - 2(\alpha,\alpha_s)w\alpha_s$$
是负根 $w\alpha$ 减去正根 $w\alpha_s$ 的一个正倍数，必然仍然是负根。于是 $\{\alpha,s\alpha\}\subset N(w)$，从而所有形如 $\{a\alpha+bs\alpha\mid a,b>0\}$ 的根都在 $N(w)$ 中，这与 $|N(w)|=l(w)<\infty$ 矛盾。

对 $\beta$ 是一般正根的情形，取 $w\in W$ 使得 $w\beta\in\Delta$，$l(w)=\dpb-1$。由于 $\dpa\geq\dpb$ 所以 $w\alpha$ 仍然是正根，当然就有 $\dp{w\alpha}\geq\dp{w\beta}=1$ 和 $(w\alpha,w\beta)=(\alpha,\beta)\geq1$。根据上面的证明，$w\alpha\dom w\beta$，所以 $\alpha\dom\beta$。

:::{.proposition}
设 $\lambda,\mu$ 是正根，且 $s_\lambda,s_\mu$ 生成一个无限群，则下面三种情况必居其一：

1. $\lambda\dom\mu$.
2. $\mu\dom\lambda$.
3. $s_\mu\lambda\dom\mu$ 且 $s_\lambda\mu\dom\lambda$.
:::

**证明**：$s_\lambda,s_\mu$ 生成一个无限群说明 $|(\lambda,\mu)|\geq1$。如果 $(\lambda,\mu)\geq1$ 那么 $\lambda,\mu$ 中 depth 更大的那一个支配另一个。

如果 $(\lambda,\mu)\leq-1$ 我们来证明 $s_\mu\lambda\dom\mu$，$s_\lambda\mu\dom\lambda$ 的论证是一样的。注意到这时 $(s_\mu\lambda, \mu)=-(\lambda,\mu)\geq1$，所以只要再证明 $\dp{s_\mu\lambda}\geq \dp{\mu}$ 即可。

设 $w\in W$ 使得 $w(s_\mu\lambda)<0$ 且 $l(w)=\dp{s_\mu\lambda}$，我们来证明必有一个长度 $l(w')\leq l(w)$ 的元素 $w'$ 使得 $w'\mu<0$，从而 $\dp{s_\mu\lambda}\geq \dp{\mu}$。

首先若 $w\mu<0$ 则可以取 $w'=w$。否则若 $w\mu>0$，我们来计算
$$w(s_\mu\lambda)=w\lambda-2(\mu,\lambda)w\mu.$$
我们知道这是一个负根，而且它是 $w\lambda$ 加上正根 $w\mu$ 的正倍数，所以必须 $w\lambda<0$，从而 $l(ws_\lambda)<l(w)$。

进一步我们计算
$$(ws_\lambda)\mu=w\mu-2(\mu,\lambda)w\lambda.$$
我们来证明 $(ws_\lambda)\mu$ 是一个负根，从而 $\dp{\mu}\leq l(ws_\lambda)<l(w)=\dp{s_\mu\lambda}$。

若不然，记 $c=-2(\mu,\lambda)\geq2$，若 $(ws_\lambda)\mu=w\mu+cw\lambda>0$，乘以 $c$ 得到 $cw\mu+c^2w\lambda$ 是正根的非负线性组合（未必还是根），根据上面 $w\lambda+cw\mu<0$，减去后者得到
$(c^2-1)w\lambda$ 是正根的非负线性组合，但 $c^2-1\geq 3$，这与 $w\lambda<0$ 矛盾。

:::{.proposition}
设 $\alpha,\beta\in\Phi^+$ 满足 $\beta\preceq\alpha$，并且 $\alpha$ 是极小根。进一步设 $\alpha_s\in\Delta$ 满足 $(\beta,\alpha_s)\leq-1$，则 $\alpha$ 和 $\beta$ 的 $\alpha_s$ 项的系数相等。
:::

**证明**：设 $\beta\preceq\gamma\preceq\alpha$ 使得 $\gamma$ 是偏序 $\preceq$ 下最大的与 $\beta$ 有相同的 $\alpha_s$ 项系数。如果 $\gamma\ne\alpha$，则存在 $t$ 使得 $\gamma\prec t\gamma\preceq\alpha$。由 $\gamma$ 的极大性可得 $s=t$。

但是 $\gamma-\beta=\sum_{t\ne s}c_t\alpha_t$，且每个 $c_t\geq0$。因此
$$(s\gamma, \alpha_s)=(\gamma,-\alpha_s)=-(\beta,\alpha_s)-\sum_{t\ne r}c_t(\alpha_t,\alpha_s)\geq1.$$
于是 $s\gamma\dom\alpha_s$ 不是极小根，从而 $\alpha\succeq s\gamma$ 也不是极小根。矛盾！所以 $\gamma=\alpha$，从而命题得证。

:::{.proposition}
设 $\alpha,\beta\in\Phi$ 满足 $|(\alpha,\beta)|\leq 1$，则这样的 $(\alpha,\beta)$ 只有有限多个值。
:::

**证明**：若 $|(\alpha,\beta)|<1$ 则 $\ra,\rb$ 生成的子群 $D$ 是有限的，所以存在 $w\in W$ 使得 $wDw^{-1}$ 属于某个有限的标准椭圆子群 $W_J$，特别地，$\ra\rb$ 的阶 $m$ 应该整除 $W_J$ 的阶，从而 $(\alpha,\beta)$ 形如 $\cos(a\pi/m)$，其中 $0\leq a\leq 2m$ 而且 $m$ 是某个有限标准椭圆子群的阶的因子。由于这样的子群是有限的，所以这样的 $\cos$ 值也是有限的。

:::{.lemma}
设 $\alpha=\sum a_s\alpha_s$ 和 $\beta=\sum b_s\alpha_s$ 都是正根。进一步设 $S=I\cup J$ 使得

1. 对任何 $t\in I$ 有 $(\alpha,\alpha_t)=(\beta,\beta_t)$。
2. $c_t=b_t$ 对任何 $t\in J$ 成立。

则 $(\alpha,\beta)=1$。
:::

注意这里 $I$ 或者 $J$ 允许有一个是空集。

**证明**：我们有 $\alpha-\beta=\sum_{s\in I}(a_s-b_s)\alpha_s$，所以
$$(\alpha,\alpha-\beta)=\sum_{s\in I}(a_s-b_s)(\alpha,\alpha_s)=\sum_{s\in I}(a_s-b_s)(\beta,\alpha_s)=(\beta,\alpha-\beta).$$
即 $(\alpha,\beta)=1$。

:::{.theorem}
极小根集合是有限的。
:::

**证明**：我们来证明极小根的深度是有上界的。设 $\beta$ 是一个深度为 $d$ 的极小根，$\beta_1\prec\cdots\prec\beta_d=\beta$ 是一个序列满足 $\dp{\beta_i}=i$，则每个 $\beta_i$ 都是极小根。

记 $J_i=\{\gamma\in\Delta \mid (\gamma, \beta_i)\geq-1\}$。我们来证明 $\{J_i,1\leq i\leq d\}$ 是递降的，并且最终会降为空集。

对 $1\leq i\leq d$，若 $\gamma\notin J_i$，则 $\gamma$ 在所有 $\beta_j(j\geq i)$ 中的系数都相同。

设 $\beta_i=\sum c_s\alpha_s,\, \beta_j=\sum d_s\alpha_s$，则 $0\leq c_s\leq d_s$ 且 $c_\gamma=d_\gamma$。注意到 $(\beta_j,\gamma)=\sum_{s\in\Delta}d_s(\alpha_s, \gamma)\leq \sum_{s\in\Delta}c_s(\alpha_s, \gamma)=(\beta_i, \gamma)<-1$。所以 $\gamma\not\in J_j$。即 $\{J_i\}$ 确实是递降的。

设 $J_i=\cdots=J_i=J$ 对某个 $i<j$ 成立。对任何 $\gamma\in J$ 和 $i\leq k\leq j$，由于 $\beta_k$ 不能支配 $\gamma$，所以 $-1\leq (\beta,\gamma)\leq 1$，等于 1 当且仅当 $\beta=\gamma$。于是 $(\beta_k,\gamma)\in\mathcal{C}(S)$。于是如果 $j-i>|\mathcal{C}(S)|^{|S|}$ 那么必然存在 $i\leq m < n\leq j$ 使得 $(\beta_m, J)=(\beta_n, J)$。（鸽笼原理，$\beta$ 和一个单根的内积有 $|c|$ 种不同的可能值，和所有单根的内积共有 $c^{|S|}$ 种不同的可能值）。

但是如果 $\gamma\not\in J$，则 $\gamma$ 在 $\beta_m,\beta_n$ 中的系数相同，所以根据前面的引理 $(\beta_m,\beta_n)=1$，但这导致 $\beta_n \dom \beta_m$，所以如果 $j-i>c^{|S|}$ 时 $J_j$ 必须比 $J_i$ 严格地小，所以整个链的长度有限，即 $d$ 有限。


> **引理**：设 $\gamma$ 不是极小根，$u,v\in W$ 使得 $u\gamma, v^{-1}\gamma$ 都是单根，则 $l(uv)\ne l(u)+l(v)$。

证明：设 $u\gamma=\alpha_s,v^{-1}\gamma=\alpha_t$，则 $\gamma\in N(su)\cap N(tv^{-1})$。又设 $\gamma\dom \beta$，则 $\beta\in N(su)\cap N(tv^{-1})$。但是 $u\beta\ne u\gamma=\alpha_s$，所以 $su\beta\in\Phi^-$ 说明 $u\beta\in\Phi^-$。同理 $v^{-1}\beta\in\Phi^-$，所以 $N(u)\cap N(v^{-1})$ 非空，所以引理得证。

---

设 $\Sigma$ 是所有极小根组成的集合，则 $|\Sigma|<\infty$ 是有限集。

定义状态机如下：

一个状态 $S_i\subset\Sigma$ 是极小根的子集。转移 $S_i\xrightarrow{s}S_{i+1}$ 为：

1. 如果 $s\in S_i$ 则 $S_i\xrightarrow{s}\no$。
2. 如果 $s\notin S_i$ 则 $S_i\xrightarrow{s} (sS_i\cup \{\alpha_s\}\cup \{s\alpha_t,t<s\})\cap\Sigma$。

我们来证明这个状态机识别语言 $\shlex$。

为方便我们记 $\low_i=\{\alpha_s\in\Delta, s<i\}$ 是那些字典序下小于 $\alpha_i$ 的单根组成的集合。

假设 $s_1\cdots s_l\in \shlex$，但是 $s_1\cdots s_{l+1}\notin \shlex$ 当且仅当 $\alpha_{l+1}\in S_l$。其中 $S_i\subset\Sigma$ 是状态机读入 $s_i$ 以后的状态。

我们来证明对任何 $k\leq l$ 有
$$S_k\subset\{(s_k\cdots s_{i+1})\alpha_i\mid 1\leq i\leq l\}\cup\cup_{i=1}^{k}(s_k\cdots s_i)\cdot\low_i.$$
首先 $k=1$ 时 $S_1=\{\alpha_1\}$，

由于下一步读入 $s_{l+1}$ 的时候是拒绝态，所以 $\alpha_{l+1}$ 也属于上面的集合。

+ 如果 $\alpha_{l+1}\in \{(s_l\cdots s_{i+1})\alpha_i\mid 1\leq i\leq l\}$，则 $s_1\cdots s_ls_{l+1}$ 不是既约的，所以不在 $\shlex$ 中。

+ 如果 $\alpha_{l+1}\notin \{(s_l\cdots s_{i+1})\alpha_i\mid 1\leq i\leq l\}$，则 $s_1\cdots s_ls_{l+1}$ 是既约的，但是 $\alpha_{l+1}$ 形如 $s_l\cdots s_{i}\alpha_r(r<i)$，所以 $s_1\cdots s_{l+1}\notin\shlex$。

反之，我们要证明如果 $\shlex$ 拒绝一个字 $w=s_1\cdots s_n$，设 $l$ 是使得 $\shlex$ 接受 $w$ 的最大位置，则必有 $\alpha_{l+1}\in S_l$。用反证法，设 $\alpha_{l+1}\notin S_l$。

+ 如果 $s_1\cdots s_{l+1}$ 不是既约的，则存在 $1\leq i\leq l$ 使得 $\alpha_{l+1}=s_l\cdots s_{i+1}\alpha_i$。于是 $l$ 在集合 $\{i\leq k\leq l \mid (s_k\cdots s_{i+1})\alpha_i\notin S_k\}$ 中。设 $j$ 是此集合的最小元素，$\beta=s_j\cdots s_{i+1}\alpha_i$。由于 $\alpha_i\in S_i$，所以 $j>i$。于是 $s_{j-1}\cdots s_{i+1}\alpha_i\in S_{j-1}$，$\beta\in s_jS_{j-1}$。由于 $s_j\cdot S_{j-1}\cap\Sigma\subset S_j$ 这说明 $\beta$ 不是极小根。注意到 $(s_{i+1}\cdots s_j)\beta=\alpha_i$ 和 $(s_{j+1}\cdots s_l)^{-1}\beta=\alpha_{l+1}$，根据上面的引理 $l(s_{r+1}\cdots s_l)\ne l-i$，这与 $s_1\cdots s_l\in\shlex$ 矛盾，所以 $\alpha_{l+1}\in S_l$。

+ 如果 $s_1\cdots s_{l+1}$ 既约但不属于 $\shlex$，则 $\alpha_{l+1}=(s_l\cdots s_{i+1})\alpha_s(s<i)$。设 $i\leq j\leq l$ 使得 $\beta=(s_js_{j-1}\cdots s_i)\alpha_s\notin S_j$。如果 $j\ne i$，则由于 $\{s_i\alpha_r\mid r<i\}\cap\Sigma\subset S_i$ 这说明 $\beta$ 不是极小根。若 $j>i$ 同样可得 $\beta$ 不是极小根。于是根据上面同样的论证得出矛盾。