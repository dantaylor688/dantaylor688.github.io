---
layout: post
title: A Short Note on Using the G#x00E2;teaux Derivative
comments: true
---
Here is a small set of notes demonstrating how to use the G#x00E2;teaux derivative. For the sake of this brief exposition, we will go through a derivation of the least squares method for solving an overdetermined set of equations \\(Ax=b\\); that is, \\(A\\) is an \\(m \times n\\) matrix with \\(m \gt n\\).

The G#x00E2;teaux derivative of a function, \\(f\\), denoted \\(D_u(f)\\) is defined by the limit

$$\begin{align*}
D_u(f) &= \lim_{\varepsilon \to 0} \frac{f(x + \varepsilon u) - f(x)}{\varepsilon} \\
& = \frac{d}{d \varepsilon} \left. f(x + \varepsilon u)\right|_{\varepsilon = 0} 
\end{align*}$$

Before we begin the actual derivation, we recall a few properties of the inner product of two vectors. The inner product is defined on a vector space \\(V\\) over a field of scalars \\(F\\) as a map 

\\[\left< \cdot,\cdot\right>: V \times V \rightarrow F \\]

that satisfies the following properties for all \\(x,y,z \in V\\) and \\(\alpha \in F \\):

+	Conjugate symmetry: 
	\\[\left< x,y \right> = \overline{\left< y,x \right>} \\]
	
+	Linearity in the first argument
	+	\\[\left< \alpha x,y \right> = \alpha \left< x,y \right>\\]
	+	\\[\left< x,z \right> +  \left< y,z \right> = \left< x+y,z \right>\\]

+	Positive-definiteness
	+	\\[\left< x,x \right> \ge 0\\]
	+	\\[\left< x,x \right> = 0 \implies x = 0\\]

Additionally, the inner product of a vector \\(x \\) with itself is the squared norm of \\(x\\):

\\[ \left\lVert x\right\rVert^2 = \left< x,x \right>.\\]

For the remainder of this post, we will assume **all of our vectors are real**. With this assumption, we get that the inner product is linear in both arguments.

The last piece we need before we are ready to begin our derivation is the G#x00E2;teaux derivative of the inner product of two real-valued functions \\(f\\) and \\(g\\). To this end, observe that 

$$\begin{align*}
\frac{1}{\varepsilon} &\left[\left< f(x+ \varepsilon u),g(x+ \varepsilon u) \right> - \left< f,g \right> \right] \\
&=  \frac{1}{\varepsilon} \left[\left< f(x+ \varepsilon u),g(x+ \varepsilon u) \right> 
- \left< f(x+ \varepsilon u),g(x) \right> + \left< f(x+ \varepsilon u),g(x) \right> - \left< f,g \right> \right]\\
&= \frac{1}{\varepsilon} \left[\left< f(x+ \varepsilon u),g(x+ \varepsilon u) -g(x)\right> + \left< f(x+ \varepsilon u) - f(x),g(x) \right> \right]\\
&= \left<f(x+ \varepsilon u), \frac{g(x+ \varepsilon u) -g(x)}{\varepsilon}\right> + \left<  \frac{f(x+ \varepsilon u) - f(x)}{\varepsilon},g(x) \right>.
\end{align*}$$

Taking $\varepsilon \to 0$ we arrive at the formula analogous to the product rule you learn in your first semester calculus course:

\\[D\_u \left< f,g \right> = \left< f,D\_u g \right> + \left< D\_u f,g \right>.\\]

Now we are ready to tackle the problem at hand: find the least-square solution to the overdetermined system of equations \\(Ax=b\\). Consider the functional

$$\begin{align*}
J(x) &= \frac{1}{2} \left\lVert Ax - b\right\rVert^2 \\
&= \frac{1}{2} \left<Ax - b,Ax-b\right> 
\end{align*}$$

We want to minimize \\(J\\). This happens when \\(D_uJ = 0\\).

$$\begin{align*}
D_u J &= \frac{1}{2} D_u \left< Ax - b,Ax-b \right> \\
&= \frac{1}{2} \left[ \left< Ax-b,D_{u} \left(Ax-b\right) \right> + \left< D_{u}\left(Ax-b\right),Ax-b \right>\right]\\
&= \frac{1}{2} \left[ \left< Ax-b,\frac{d}{d \varepsilon} \left. \left(A(x + \varepsilon u)-b\right)\right|_{\varepsilon = 0} \right> + \left< \frac{d}{d \varepsilon} \left.\left(A(x + \varepsilon u)-b\right)\right|_{\varepsilon = 0},Ax-b \right>\right]\\
&= \frac{1}{2} \left[ \left< Ax-b,Au \right> + \left< Au,Ax-b \right>\right]\\
&= \left< Ax-b,Au \right>\\
&=\left< A^T(Ax-b),u \right>
\end{align*}$$

We set this final expression to zero:

\\[\left< A^T(Ax-b),u \right> = 0\\]

and note that this equation holds for all \\(u\\), therefore 

\\[A^T(Ax-b) = 0\\]
or
\\[A^TAx=A^Tb,\\]

which is the formula we are familiar with. Of course, since \\(A^T A\\) is invertible,

\\[x = \left( A^T A\right)^{-1} A^T b.\\]




