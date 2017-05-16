---
layout: post
title: Discovering the Coefficients of a Projection Matrix
comments: true
---

Suppose you have a set of correlated 3-D and 2-D coordinates, $\vec{x}_i$ and $\vec{b}_i$ related by some *unknown, linear* transformation matrix, $A$. That is 

$$
\begin{equation}
Ax_i=b_i
\end{equation}
$$

where

$$
A = 
\left(\begin{matrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}
\end{matrix}\right)
$$

$$
x_i = (x_{i_1},x_{i_2},x_{i_3})^T
$$

$$
b_i = (b_{i_1},b_{i_2})^T
$$

for $i = 1 \ldots N$. We want a way to find the 'best' $A$ in this situation. Once we have $A$ we can then use the [pseudo-inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_pseudoinverse) to find the transformation from 2-D to 3-D (up to some vector in the null space of $A$). Here we will define 'best' as minimizing the $L^2$ norm. 

We start by multiplying the left side of (1).

$$
Ax_i = \left( 
\begin{matrix}a_{11}x_{i_1} + a_{12}x_{i_2} + a{13}x_{i_3}\\
a_{21}x_{i_1} + a_{22}x_{i_2} + a{23}x_{i_3}
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{i_1}\\
 b_{i_2}
\end{matrix}
\right)
$$

Using our $N$ measurements, we can form the following set of equations

$$
\begin{matrix}
Ax_1 = \left( 
\begin{matrix}a_{11}x_{1_1} + a_{12}x_{1_2} + a{13}x_{1_3}\\
a_{21}x_{1_1} + a_{22}x_{1_2} + a_{23}x_{1_3}
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{1_1}\\
 b_{1_2}
\end{matrix}
\right)\\
Ax_2 = \left( 
\begin{matrix}a_{11}x_{2_1} + a_{12}x_{2_2} + a{13}x_{2_3}\\
a_{21}x_{2_1} + a_{22}x_{2_2} + a{23}x_{2_3}
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{2_1}\\
 b_{2_2}
\end{matrix}
\right)\\
\vdots\\
Ax_N = \left( 
\begin{matrix}a_{11}x_{N_1} + a_{12}x_{N_2} + a{13}x_{N_3}\\
a_{21}x_{N_1} + a_{22}x_{N_2} + a{23}x_{N_3}
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{N_1}\\
 b_{N_2}
\end{matrix}
\right)
\end{matrix}
$$

Since all of these equations are satisfied simultaneously, we can group them in the following way

$$
\begin{equation}
\left( 
\begin{matrix}a_{11}x_{1_1} + a_{12}x_{1_2} + a{13}x_{1_3}\\
a_{11}x_{2_1} + a_{12}x_{2_2} + a{13}x_{2_3}\\
\vdots\\
a_{11}x_{N_1} + a_{12}x_{N_2} + a{13}x_{N_3}\\
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{1_1}\\
 b_{2_1}\\
 \vdots\\
 b_{N_1}
\end{matrix}
\right)\\
\end{equation}
$$

and

$$
\begin{equation}
\left( 
\begin{matrix}a_{21}x_{1_1} + a_{22}x_{1_2} + a{23}x_{1_3}\\
a_{21}x_{2_1} + a_{22}x_{2_2} + a{23}x_{2_3}\\
\vdots\\
a_{21}x_{N_1} + a_{22}x_{N_2} + a{23}x_{N_3}\\
\end{matrix}
\right) = 
\left( 
\begin{matrix}b_{1_2}\\
 b_{2_2}\\
 \vdots\\
 b_{N_2}
\end{matrix}
\right)\\
\end{equation}
$$

which can be re-written as 

$$
\begin{align}
Ra_1 &= c_1\\
Ra_2 &= c_2
\end{align}
$$

where 

$$
R = 
\left( 
\begin{matrix}
x_{1_1} & x_{1_2} & x_{1_3}\\
x_{2_1} & x_{2_2} &x_{2_3}\\
& \vdots & \\
x_{N_1} & x_{N_2} & x_{N_3}\\
\end{matrix}
\right) 
$$

$$
\begin{align*}
a_1 &= \left(\begin{matrix} a_{11} & a_{12} & a_{13} \end{matrix} \right)^T\\
a_2 &= \left( \begin{matrix} a_{21} & a_{22}&  a_{23} \end{matrix}\right)^T
\end{align*}
$$

$$
c_1 =
\left( 
\begin{matrix}b_{1_1}\\
 b_{2_1}\\
 \vdots\\
 b_{N_1}
\end{matrix}
\right)
$$

$$
c_2 = 
\left( 
\begin{matrix}b_{1_2}\\
 b_{2_2}\\
 \vdots\\
 b_{N_2}
\end{matrix}
\right)
$$

These equations can be solved using the [principle of least squares]({% post_url  2014-12-19-gateaux-derivative %}).
Together, equations (2) and (3) give us the coefficients of our original matrix $A$. With this matrix, we can project a point from 3-D to 2-D. Using the pseudo-inverse, we can 'invert' $A$ to get the position of a 2-D point in 3-space. Remember, this was done without any knowledge of the camera or 3-D point cloud sensor other than the fact that there exists a linear transformation between the two. It must be stated that this is *not* always (often?) the case.