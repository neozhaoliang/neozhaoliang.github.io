---
title: Coxeter groups, automata and uniform tilings
date: 2019-12-19
url: uniform-tilings
---

This program can draw 2d and 3d uniform tilings in Euclidean, spherical and hyperbolic spaces by treating them in an uniform approach: word processing in Coxeter groups. The code is on [github](https://github.com/neozhaoliang/pywonderland/tree/master/src/uniform-tilings).

I learned most of the math stuff from [Casselman](https://www.math.ubc.ca/~cass/)'s essays, he's Java implementation (unpublished) of the minimal roots algorithm was also very helpful.

# Examples


+ Below is the 2d Euclidean tiling omnitruncated (4, 2, 4):

    <img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-4-2-4.png" width="600"/>

+ Below is the 2d hyperbolic tiling regular (2, 3, 13) in Poincaré's disk model:
  
    <img style="margin:0px auto;display:block" src="/images/coxeter/2-3-13.png" width="500"/>

+ Below is the 2d hyperbolic tiling omnitruncated (4, 3, 3) in upper half plane model:

    <img style="margin:0px auto;display:block" src="/images/coxeter/uhp-4-3-3.png" width="600"/>

+ Below is the 3d hyperbolic tiling regular (3, 5, 3) in Poincaré's ball model:

    <img style="margin:0px auto;display:block" src="/images/coxeter/3-5-3.png" width="600"/>

+ Below is the 3d hyperbolic tiling regular (5, 3, 5) in Poincaré's ball model:

    <img style="margin:0px auto;display:block" src="/images/coxeter/5-3-5.png" width="600"/>

+ Below is the 3d hyperbolic tiling regular (5, 3, 4) in Poincaré's ball model:

    <img style="margin:0px auto;display:block" src="/images/coxeter/5-3-4.png" width="600"/>

+ Below is the 3d hyperbolic tiling regular (4, 3, 5) in Poincaré's ball model:

    <img style="margin:0px auto;display:block" src="/images/coxeter/4-3-5.png" width="600"/>

+ The above four regular tilings are the only regular ones with compact cells. If we drop the restriction on compactness and requires the cells must have finite volume, then we have ten more regular tilings, with each has a Euclidean vertex configure. For example (6, 3, 3)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/6-3-3.png" width="600"/>

    You can see the cells have ideal vertices, i.e. vertices at the infinity. These tilings are called "paracompact".

+ If we drop the restriction on being "regular" then we have lots more examples, like rectified (3, 5, 3) and rectified (5, 3, 4)：

    <img style="margin:0px auto;display:block" src="/images/coxeter/rectified-3-5-3.png" width="600"/>

    <img style="margin:0px auto;display:block" src="/images/coxeter/rectified-5-3-4.png" width="600"/>

    and the [cantic order-5 cubic](https://en.wikipedia.org/wiki/Uniform_honeycombs_in_hyperbolic_space#[5,31,1]_family) tiling from the [5, 3<sup>1,1</sup>] family:
    
    <img style="margin:0px auto;display:block" src="/images/coxeter/cantic-order-5-cubic.png" width="600"/>

+ Below is a 2d spherical tiling rendered in 3d:

    <img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-5-2-3.png" width="500"/>

+ Finally a shader program exported from Matt Zucker's excellent work on [shadertoy](https://www.shadertoy.com/view/3tsSzM):

    <img style="margin:0px auto;display:block" src="/images/coxeter/wythoff_shader.png" width="800"/>

For 2d tilings the program computes the coordinates of each vertex, the indices of each edge/face and then export the data to svg/POV-Ray for rendering. For 3d hyperbolic tilings the program only computes the coordinates of the cells and exports the data of the edges to POV-Ray (because it's too slow to compute all exact information in this case). It usually takes ten minutes to generate 1.5M edges in Python and two hours to render a scene as above on a machine with 16G memory. I usually run the Python part on a machine in my office after work, start the rendering process before I go home and check the result the next morning.


# Wythoff construction


All these tilings can be generated via Wythoff construction. The principal of this construction is the same as how a kaleidoscope works, as illustrated in the video below. We align some reflection mirrors in the space where the dihedral angles between them are carefully chosen, then choose an initial point in the space and iteratively compute the virtual images of this point in the mirrors, the virtual images of virtual images, ..., and so on. The resulting kaleidoscopic pattern is exactly the tiling we want.

<video src="/images/coxeter/wythoff.mp4" width="600" controls></video>

The key step in building the tiling is to efficiently compute the set of virtual images and extract edge/face information between them. This is where this program differs with most of other open-source tiling-generation programs: most of the computations are done in a symbolic computational manner using only integer arithmetics: it knows all exact information required to construct the tiling like how many vertices are there, how these vertices are transformed from the initial point, which pairs of them form the edges, ..., etc, without knowing the coordinates of any vertex!

Sounds interesting? I'll give an example to illustrate the procedure.

# Example: omnitruncated (7, 2, 3) tiling

The Coxeter-Dynkin diagram for the omnitruncated (7, 2, 3) tiling is:

<img style="margin:0px auto;display:block" src="/images/coxeter/coxeter723.svg" width="250"/>

This is a hyperbolic tiling, its symmetry group $G$ is the Coxeter group determined by Coxeter matrix

$$M=\begin{pmatrix} 1 & 7 & 2 \\ 7 &1 &3\\ 2 & 3 &1\end{pmatrix}$$

and has presentation

$$G = \langle s_0,s_1, s_2\ |\ s_0^2=s_1^2=s_2^2=(s_0s_1)^7=(s_1s_2)^3=(s_0s_2)^2=1\rangle.$$

The initial vertex $v_0$ is not on any of the three mirrors, so its stabilizing subgroup is $\langle 1\rangle$, by [orbit-stabilizer theorem](https://en.wikipedia.org/wiki/Group_action_(mathematics)#Orbit-stabilizer_theorem) each element $g$ of $G$ maps $v_0$ to a distinct vertex in the tiling.

We know that $g$ can be represented as a word in the generators $\{s_0,s_1,s_2\}$ and such a representation is not unique. For example from the relations given above we can easily verify that $s_0s_2=s_2s_0$, $s_1s_2s_1=s_2s_1s_2$, etc. We can choose a well-defined "normal form" for $g$ by firstly defining the alphabetical order of $s_0,s_1,s_2$ as $s_0<s_1<s_2$ and then extend this ordering to the set of all words:

{% blockquote %}
**Shortlex ordering**: Let $w_1=s_{i_1}s_{i_2}\cdots s_{i_n}$ and $w_2=s_{j_1}s_{j_2}\cdots s_{j_m}$ be two different words, their ordering is determined as follows:

1. Compare their lengths first. If $n<m$ then $w_1<w_2$, if $n>m$ then $w_1>w_2$.
2. Else $n=m$ and we compare them element-wise from left to right: let $k$ be the smallest index such that for all $l<k$ it holds $s_{i_l}=s_{j_l}$ and $s_{i_k}\ne s_{j_k}$, the ordering of $w_1,w_2$ is the same with the ordering of $s_{i_k},s_{j_k}$.
{% endblockquote %}

Since shortlex ordering is a total ordering on the set of all words, each $g\in G$ has an unique normal form in this ordering. We define the length of any $g\in G$ to be the length of its normal form and define the ordering of any two group elements $g,g'$ to be the samw with the shortlex ordering of their normal forms.

Let $\mathcal{SL}(G)$ be the set of normal forms for all $g\in G$, all the 37 elements in $\mathcal{SL}(G)$ with length <= 5 are listed below (row first):

$$
\begin{array}{lllll}e&s_{0}&s_{1}&s_{2}&s_{0}s_{1}\\s_{0}s_{2}&s_{1}s_{0}&s_{1}s_{2}&s_{2}s_{1}&s_{0}s_{1}s_{0}\\s_{0}s_{1}s_{2}&s_{0}s_{2}s_{1}&s_{1}s_{0}s_{1}&s_{1}s_{0}s_{2}&s_{1}s_{2}s_{1}\\s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{1}&s_{0}s_{1}s_{0}s_{2}&s_{0}s_{1}s_{2}s_{1}&s_{0}s_{2}s_{1}s_{0}\\s_{1}s_{0}s_{1}s_{0}&s_{1}s_{0}s_{1}s_{2}&s_{1}s_{0}s_{2}s_{1}&s_{1}s_{2}s_{1}s_{0}&s_{2}s_{1}s_{0}s_{1}\\s_{0}s_{1}s_{0}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{1}s_{2}&s_{0}s_{1}s_{0}s_{2}s_{1}&s_{0}s_{1}s_{2}s_{1}s_{0}&s_{0}s_{2}s_{1}s_{0}s_{1}\\s_{1}s_{0}s_{1}s_{0}s_{1}&s_{1}s_{0}s_{1}s_{0}s_{2}&s_{1}s_{0}s_{1}s_{2}s_{1}&s_{1}s_{0}s_{2}s_{1}s_{0}&s_{1}s_{2}s_{1}s_{0}s_{1}\\s_{2}s_{1}s_{0}s_{1}s_{0}&s_{2}s_{1}s_{0}s_{1}s_{2}&\end{array}
$$

Note the number of all words in $s_0,s_1,s_2$ with length less or equal than five is $1+3+\cdots+3^5=364$, the list above tells us that they indeed contain only 37 different ones, the remaining 364 - 37 = 327 ones are duplicates. A further computation shows that the number of all words with length no more than six is 1093 but they contain only 53 different ones. So we can gain a great improvement in efficiency if we only use words in $\mathcal{SL}(G)$ instead of traversing all possible combinations of the generators.

How can we generate those words that are precisely in $\mathcal{SL}(G)$? This leads us to a very important theorem on Coxeter groups:

{% blockquote %}
**Theorem [Brigitte Brink & Robert B. Howlett, 1993]**: If $G$ is a finitely generated Coxeter group then $\mathcal{SL}(G)$ is a regular language.
{% endblockquote %}

The term "regular language" comes from computer science, a basic fact about a regular language over a finite alphabetical set is that this language can always be recognized by a definite finite automaton (DFA), such DFA may not be unique but there is a "minimal one" with the least number of states and this minimal one is unique if we don't distinct relabellings of the states.

Below is the automaton recognizes $\mathcal{SL}(G)$ for the (7, 2, 3) group:

<img style="margin:0px auto;display:block" src="/images/coxeter/dfa_723.svg" width="600"/>

You can see there are 19 nodes (i.e. states) in the automaton. The labels of the states are irrevalent because renumbering the states of an automaton does not change the language it recognizes.

The red node is the initial state.

The directed edges in the graph tell us the transition rule between the states. The edges are labelled by the generators of the group, i.e. $i$ for $s_i$. If we start from the initial state and keep on moving to a next state along an edge up to a finite number of steps, then the path we travelled gives a word in $\mathcal{SL}(G)$. All words in $\mathcal{SL}(G)$ can be generated in this way.

{% blockquote %}
**Example**:

1. The only path of length 0 correspondes to the identidy 1.
2. The three paths of length 1 $0\xrightarrow{\ s_0\ }1$, $0\xrightarrow{\ s_1\ }2$, $0\xrightarrow{\ s_2\ }8$ corresponde to the three generators $s_0,s_1,s_2$ in $\mathcal{SL}(G)$.
3. The five paths $0\xrightarrow{\ s_0\ }1\xrightarrow{\ s_1\ }2$, $0\xrightarrow{\ s_0\ }1\xrightarrow{\ s_2\ }8$, $0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_0\ }3$, $0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_2\ }8$, $0\xrightarrow{\ s_2\ }8\xrightarrow{\ s_1\ }9$ corresponde to the five elements of length 2 in $\mathcal{SL}(G)$: $s_0s_1,s_0s_2,s_1s_0,s_1s_2,s_2s_1$.
{% endblockquote %}

Using breadth-first search we can easily generate all words in $\mathcal{SL}(G)$ up to any given depth.

Note for an infinite Coxeter group the automaton must have cycles, but for a finite Coxeter group the automaton must be a directed tree, for example the symmetry group $S_4$ of tetrahedron:

<img style="margin:0px auto;display:block" src="/images/coxeter/tetrahedron.svg" width="600"/>

The 24 different paths corresponde to the 24 group elements of $S_4$:

$$
\begin{array}{llll}e&s_{0}&s_{1}&s_{2}\\s_{0}s_{1}&s_{0}s_{2}&s_{1}s_{0}&s_{1}s_{2}\\s_{2}s_{1}&s_{0}s_{1}s_{0}&s_{0}s_{1}s_{2}&s_{0}s_{2}s_{1}\\s_{1}s_{0}s_{2}&s_{1}s_{2}s_{1}&s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{2}\\s_{0}s_{1}s_{2}s_{1}&s_{0}s_{2}s_{1}s_{0}&s_{1}s_{0}s_{2}s_{1}&s_{1}s_{2}s_{1}s_{0}\\s_{0}s_{1}s_{0}s_{2}s_{1}&s_{0}s_{1}s_{2}s_{1}s_{0}&s_{1}s_{0}s_{2}s_{1}s_{0}&s_{0}s_{1}s_{0}s_{2}s_{1}s_{0}\end{array}
$$

Now the big question:

{% blockquote %}
**Question 1**: How to compute $\mathcal{SL}(G)$?
{% endblockquote %}

The answer to this question is too complicated to be covered in this article, a simple sketch of the main thread is appended at the end. When I was developing this program I mainly referred to Casselman's notes [^1] [^2] [^3] and the textbook by Humphreys [^4]. These should be enough for a reader with a solid background in undergradute abstract algebra.


Once we have the normal forms of the group elements, we can easily use them to map the initial vertex $v_0$ to other vertices in the tiling:

Let $w=s_{i_0}s_{i_1}\cdots s_{i_n}$, we adopt the convention that the action of $w$ on $v_0$ is to successively apply each generator in $w$ from right to left:
$$w\cdot v_0 = s_{i_0}(s_{i_1}(\cdots s_{i_n}(v_0)).$$
Since $G$ is infinite we can only generate words up to a given depth. Suppose we have the 37 words listed above stored in a list $L$, they map $v_0$ to 37 different vertices in the tiling. To draw the edges between them we need to compute which of them are adjacent. How can we do this?

Firstly we need a multiplicaiton table $T$ for the words in $L$. $T$ is a 2d array with its $i$-th row correspondes to the $i$-th word $w_i$ in $L$ and its $j$-th column correspondes to the $j$-th generator $s_j$. The entry $T[i][j]$ records the index of $s_jw_j$ in $L$ (note this multiplication may not be a normal form). If $s_jw_i$ does not exist in $L$ we simply return `None`. The usage of $T$ is, for any given word $w$, we can quickly find the index of $w$ in $L$ by using $T$ as a lookup table.

In our example $T$ is listed below, the words in $L$ are put into the second column:

<details>
<summary><font color="#D00">**Click to expand $T$**</font></summary>
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

Hence for any word $w=s_{i_0}s_{i_1}\cdots s_{i_n}$, we can start from the first row of $T$, find the index of $s_{i_n}$ in $L$, say $k$, then jump to the $k$-th row and find the index of $s_{i_{n-1}}s_{i_n}$ in $L$, ..., and finally get the index of $w$ (or `None`).

Suppose the reflection of the initial vertex $v_0$ about the $i$-th mirror gives a virtual image $v_1=s_i(v_0)$, then $e=(v_0,v_1)$ is an edge of type $i$. By the orbit-stabilizer theorem all edges of type $i$ can be obtained by applying the coset representatives in $G/H$ to $e$, where $H=\langle i\rangle$ is the stabilizing subgroup of $e$ ($H$ is called a standard parabolic subgroup). It's easy to see the words of the two ends of $e$ are $1$ and $s_i$ respectively. We then compute the coset representatives of the words in $L$ for the subgroup $H$, use a set to remove duplicates, apply each resulting coset representative $w$ to the two ends of $e$. The words of the two ends of $w\cdot e$ are $w$ and $ws_i$ respectively. We can find the indices of $w$ and $ws_i$ as shown above to get $w\cdot e$.

The edges between the 37 vertices in $L$ are drawn below:

<img style="margin:0px auto;display:block" src="/images/coxeter/723_edges.png" width="500"/>

0 is the initial vertex, the number of white strips in an edge indices the type of it (no white strips for $s_0$, one for $s_1$ and two for $s_2$).

It's worth noting that one can easily read the shortlex word representation of any vertex $v$ from the above image, just start from vertex 0, trace a shortest path from 0 to $v$ (if there are more than one shortest path then always choose the smaller vertex at bifurcaton points) and record the edges along the way. For example there are two paths with shortest length from vetex 0 to vertex 33:
$$
\begin{align*}&0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_0\ }6\xrightarrow{\ s_2\ }13\xrightarrow{\ s_1\ }22\xrightarrow{\ s_0\ }33.\\
&0\xrightarrow{\ s_1\ }2\xrightarrow{\ s_2\ }7\xrightarrow{\ s_0\ }13\xrightarrow{\ s_1\ }22\xrightarrow{\ s_0\ }33.
\end{align*}$$
By concatenating edge labels from left to right we have two words that both map vertex 0 to vertex 33: $s_1s_0s_2s_1s_0$ and $s_1s_2s_0s_1s_0$. The first is the shortlex one.

{% blockquote %}
**Question 2**: How to compute the normal form of the multiplicaiton of two words? How to compute the coset representative of a word for a standard parabolic subgroup?
{% endblockquote %}

Again the answer is too long to be included here. A short sketch of the procedure is attached below.

The procedure for computing faces is very similar with the case of edges. The reflections about the $i$-th and $j$-th mirrors generate a polygon $f_0$ centered at a vertex of the fundamental triangle. The stabilizing subgroup of $f_0$ is the standard parabolic subgroup $\langle i,j\rangle$. Again we find a word representation for each vertex in $f_0$, apply the words in $L$ to $f_0$, and use $T$ to get the indices of the transformed face.

The final image is shown below, it contains 30517 vertices, 42057 edges and 11541 polygons.

<img style="margin:0px auto;display:block" src="/images/coxeter/omnitruncated-7-2-3.png" width="500"/>


# About the code

The core part of the code is the `CoxeterGroup` class which is initialized by a Coxeter matrix and is responsible for computing the reflection table of minimal roots, doing multiplications in this group, computing coset representatives and drawing the automaton. I have delegated most of the drawing stuff to a 3rd party lib [hyperbolic](https://github.com/cduck/hyperbolic/) and POV-Ray.


# More explainations on the math stuff

In this section I'll give a short sketch of the core part of the math stuff. This requires you know some basic concepts like geometric realizations of Coxeter groups, Tit's cone, root systems. These are fairly standard materials and can be found in Humphreys's book.

Almost everything relies upon a 2d table called **reflection table of minimal roots**. Again we use group (7, 2, 3) as example:

<img style="margin:0px auto;display:block" src="/images/coxeter/roots.png" width="800"/>

This image is the same with the last one except that it has 12 labelled mirrors, these mirror have particular importance among all roots in the root system: they are the set of minimal roots in the root system.

You can think the root system of $G$ as the mirrors in the image which are colored in white. Each mirror is a geodesic line and intersects the boundary at two points. It also cuts the space into two disjoint halfspaces, one for a positive root and the other for its negative counterpart. The halfspace contains the fundamental triangle $\Delta ABC$ correspondes to the positive root.

Intuitively speaking, a minimal root $r$ is a mirror such that if one stands inside the fundamental domain $\Delta ABC$ and looks outwards, there is no other mirror $r'\ne r$ can completely screen off $r$ from being seen. Simple roots are always minimal since they are the "walls" of the fundamental domain. The most important fact about minimal root is:

{% blockquote %}
**Theorem**: The set of minimal roots is finite.
{% endblockquote %}

This theorem is the key step in Brink and Howlett's proof that Coxeter groups are automatic groups.

The reflection table of minimal roots `reftable` is defined as follows: it's a 2d array with its $i$-th row correspondes to the $i$-th minimal root $\alpha_i$ and $j$-th column correspondes to the $j$-th generator $s_j$. The $(i,j)$-entry records the action of $s_j$ on $\alpha_i$. Let $\beta=s_j(\alpha_i)$:

1. If $\beta=\alpha_k$ is the $k$-th minimal root then set this entry to $k$.
2. If $\beta$ is a negative root then set this entry to $-1$.
3. Else $\beta$ is a positive root but not minimal, set this entry to `None`.

The `reftable` of the (7, 2, 3) group is listed below:

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

Let $\Sigma$ be the set of minimal roots of $G$, all states in the automaton are subsets of $\Sigma$, the transition rule between the subsets is:

$$S\xrightarrow{\ s_i\ } \{s_i\} \cup (s_i(S)\cup\{ s_i(\alpha_j),j<i\})\cap\Sigma.$$

One can use breadth-first search to build this automaton and use [Hopcroft's algorithm](https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft's_algorithm) to get a minimized version of it.

The image below shows the subsets of minimal roots for each state in the automaton:

<img style="margin:0px auto;display:block" src="/images/coxeter/723_dfa_subsets.png" width="800"/>

The code for computing the multiplication of a generator and a word is given below:

``` python
def left_mul_invshortlex(reftable, s, w):
    w = tuple(w)
    t = s
    k = -1
    mu = s
    for i, s_i in enumerate(w):
        if mu is None:
            return w[:k+1] + (t,) + w[k+1:]
        elif mu < 0:
            return w[:i] + w[i+1:]
        elif mu < s_i:
            t = mu
            k = i
        else:
            continue
    return w[:k+1] + (t,) + w[k+1:]
```
Here $s$ is a generator and $w$ is a word in the normal form of the *inverse shortlex ordering* (invshortlex). The function returns the normal form of $s\cdot w$ also in the invshortlex ordering. The computations in shortlex can be obtained by doing computations in invshortlex first and then reverse the result back.

{% blockquote %}
The intermedian step of doing computations in invshortlex ordering is mainly for keeping consistent with Casselman's paper.
{% endblockquote %}

Finding the coset representative of a given word for a standard parabolic subgroup is quite straight-forward: let $T$ be the set of generators of this standard parabolic subgroup, the pseudocode for the procedure is given below:

```
x := w
u := 1
while l(xt) < l(x) for some t in T
    x := xt
    u := t
end

return x
```
Where $l(\cdot)$ is the length function.

For finite Coxeter groups all positive roots are minimal. For affine Coxeter groups the root system consists of families of parallel affine hyperplanes. In each family there is a pair of minimal roots such that the fundamental domain lies between them and all other mirrors in this family are completely screened off by them hence are not minimal. See the image for (6, 2, 3) (affine $\widetilde{G}_2$) for an example:

<img style="margin:0px auto;display:block" src="/images/coxeter/roots_623.png" width="800"/>


[^1]: [Automata to perform basic calculations in Coxeter groups, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/banff.pdf).

[^2]: [Computation in Coxeter groups I. Multiplication, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/cm.pdf).

[^3]: [Computation in Coxeter groups II. Constructing minimal roots, by Bill Casselman](https://www.math.ubc.ca/~cass/research/pdf/roots.pdf).

[^4]: Reflection Groups and Coxeter Groups, by James E. Humphreys.
