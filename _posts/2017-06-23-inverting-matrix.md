---
layout: post
title: Matrix Inversion as a Change of Basis
comments: true
---

My schooling was in [pure math](https://mathwithbaddrawings.com/2015/02/24/why-do-we-pay-mathematicians/).  However, the language and way of thinking of the applied mathematician is significantly different than that of the theorist. It has been a slow process for me as I change my way of thinking. Along the way I have found two books that have helped a lot. The first, which I have mentioned [previously]({% post_url 2014-12-31-differentiation-by-integration %}) is [Applied Analysis](https://www.amazon.com/Applied-Analysis-Dover-Books-Mathematics/dp/048665656X) by Cornelius Lanczos. The second is one I just came across, [Numerical Linear Algebra](https://www.amazon.com/Numerical-Linear-Algebra-Lloyd-Trefethen/dp/0898713617) by Trefethen and Bau. These two books provide insight into the "right way" to think about problems as an applied mathematician. I will often turn to Lanzcos when faced with a problem where a better approximation is necessary. Here, we are going to talk about a way of thinking about matrix multiplication and inversion that is more useful than what is normally taught in the undergraduate math curriculum. (Throughout this post, we consider matrices whose entries are from $\mathbb{C}$.)

### Multiplying a Matrix by a Vector ###

Before we get to matrix inversion, we will briefly discuss a way of thinking about matrix multiplication that is more useful to the applied mathematician. First, we look at multiplying a matrix by a vector. When students are first introduced to matrices, they are taught the following formula for multiplying an $m \times n$ matrix, $A$ and $n \times 1$ vector, $x$.

$$
\begin{equation}
b_i = \left(Ax\right)_i = \sum_{j = 1}^n a_{ij}x_j
\end{equation}
$$

for $i = 1, \ldots, m$. By $\left(Ax\right)_i = b_i$, I mean the $i^{\text{th}}$ component of the vector $Ax$ (which I have labelled $b$). This definition is sufficient for computing matrix-vector products in an introductory course and is perhaps easier to comprehend for the novice. However, it hides a useful way of thinking about what is going on. 

Rather than thinking about matrix-vector multiplication as an operator acting on a vector, we can think of $Ax$ as *a linear combination of the columns of $A$ in the components of $x$*. 

$$
\begin{equation}
b = Ax = \sum_{j = 1}^n a_{j}x_j
\end{equation}
$$

In a longer form, equation (2) looks like

$$
\begin{align}
b &= Ax = \left(
\begin{matrix}  &  &  & \\
 a_1  & a_2 & a_3\\
 & &  & \\
\end{matrix}\right)x\\
&= 
\left(\begin{matrix}  \\
 a_1 \\
  \\
\end{matrix}\right)x_1 + \left(\begin{matrix}  \\
 a_2 \\
  \\
\end{matrix}\right)x_2 + \cdots 
+ \left(\begin{matrix}  \\
 a_n \\
  \\
\end{matrix}\right)x_n
\end{align}
$$

where now, $a_j$ is the $j^{\text{th}}$ column of $A$.

Now, at first, the difference doesn't look like much. In fact, the only differences symbolically between (1) and (2) are subscript $i\text{'s}$ on the $b$ and $a\text{'s}$. However, if we can move past just thinking about the symbols and look at what is happening we will see that this way of thinking helps our understanding of what is going on. Now we are solving for the entire $b$ vector in one "swoop".

### Matrix Multiplication ###

Now matrix multiplication becomes a combination of matrix-vector multiplications. Given matrices $A$ and $B$ of sizes $m \times n$ and $n \times p$ respectively, the $j^{\text{th}}$ column of the product $AB$ is 

$$
\left(AB\right)_j = \left(\begin{matrix}  \\
 a_1 \\
  \\
\end{matrix}\right)b_{1j} + \left(\begin{matrix}  \\
 a_2 \\
  \\
\end{matrix}\right)b_{2j} + \cdots 
+ \left(\begin{matrix}  \\
 a_n \\
  \\
\end{matrix}\right)b_{nj}
$$

for $j = 1 \ldots p$. That is, each column of the product $AB$ is just a multiplication of the matrix $A$ by a column vector in $B$.

### Inverting a Matrix ###

For the sake of completeness, we mention that the inverse of a square $m \times m$ matrix $A$ is a square matrix $Z$ (necessarily of the same size) such that 

$$
AZ=I
$$

where 

$$
I = \left( \begin{matrix}  1 & 0  &\cdots &&& 0 \\
0  & 1 & 0 & && \vdots \\
\vdots & 0 & \ddots&&\\
 & \vdots & &&&0\\
0 & 0 & 0 & \cdots &&1\\
\end{matrix}\right)
$$ 

is the identity matrix. Then, without going into all the details of the [equivalent conditions](http://mathworld.wolfram.com/InvertibleMatrixTheorem.html) that a matrix being invertible implies we just state that if $A$ is invertible than the columns of $A$ span the space $\mathbb{C}^m$. That is, we can represent *any* vector in $\mathbb{C}^m$ as a linear combination of the columns of $A$. Specifically, if we identify the $j^{\text{th}}$ standard basis vector (i.e a one in the $j^{\text{th}}$ entry and zero elsewhere) by $e_j$. Then we can write

$$
e_j = \sum_{j = 1}^m a_{j}z_j
$$

Since we can do this for all $j = 1,\ldots, m$ we see that the coefficients $z_j$ taken together form an expansion of the $e_j$ in the basis formed by the columns of $A$.

This is the key of this section (indeed the entire post). **Solving the system $Ax=b$ gives the expansion of the vector $b$ in the basis formed by the columns of $A$.**

$$
\begin{array}{ccc}
Ax=b \text{}& \iff & x = A^{-1}b \\
\text{$b$ expanded in the standard basis}&&\text{The expansion of $b$}\\
&&\text{in the basis formed by the columns of $A$}
\end{array}
$$

This mode of thinking also helps when we generalize to singular matrices. For instance, in [least squares]({% post_url 2014-12-19-gateaux-derivative %}) problems, you can pick a basis, with polynomial or Fourier terms say and compose your matrix $A$ with these columns. Then, given a vector $b$, when we solve $Ax=b$ we are finding the coefficients that best approximate that signal in your basis of choice. 

#### Note ####
To end, I can mention that I have seen this type of thinking explained in [Strang's](http://www-math.mit.edu/~gs/) [Introductory Linear Algebra book](http://math.mit.edu/~gs/linearalgebra/) but I have not read it in depth. However, based on my knowledge of some of his other work, I'm confident that this book (with the corresponding [class on MIT OCW](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/index.htm))  would be a great introduction to the subject from an applied point of view.