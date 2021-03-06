---
layout: post
title: QR Factorization
comments: true
---

In this post, we move on to the topic of matrix factorization. While we've already looked at the [SVD]({% post_url 2017-08-19-svd-geometry %}), we now study the QR factorization.

The idea behind $QR$ factorization is to find a series of orthogonal vectors, $q_1, q_2, \ldots $ that span the same (successive) spaces as their counterparts in the columns of $A$, $a_1, a_2, \ldots$. It isn't too hard to see that if $A \in \mathbb{C}^{m \times n}, m \ge n$ has full rank then this implies that the following system holds

$$
\left( 
\begin{matrix} 
\lvert & & \lvert &  \\
a_1 & \cdots& a_n &\\
\lvert & & \lvert &  \\
\end{matrix}
\right) = \left( 
\begin{matrix} 
\lvert & & \lvert \\
q_1 & \cdots& q_n \\
\lvert & & \lvert  \\
\end{matrix}
\right) \left( 
\begin{matrix} 
r_{11} & r_{12} & \cdots & r_{1n} \\
0 & r_{22} & \cdots& r_{2n} \\
\vdots & 0 & \ddots & &   \\
 & \vdots & &  r_{nn}  \\
\end{matrix}
\right)
$$

As a matrix formula we can write

$$
\begin{equation}
A = \hat{Q}\hat{R}
\end{equation}
$$

and we refer to (1) as the reduced $QR$ factorization of the matrix $A$.

To get the full $QR$ factorization, we continue picking orthogonal vectors, $q_i$ and append these as columns of $\hat{Q}$ until we have a unitary $m \times m$ matrix $Q$. We then simply append rows of zeros to $\hat{R}$ that correspond with our new columns of $Q$ to form the $m \times n$ matrix $R.$ Note that $R$ is still upper triangular.

$$
\begin{align}
A &= QR\\
&= \left( 
\begin{matrix} 
 & \lvert & &\lvert \\
\hat{Q} & q_{n+1}& \cdots & q_{m}\\
 & \lvert & & \lvert \\
\end{matrix}
\right)\left( 
\begin{matrix} 
& \hat{R} & \\
 \cdots & 0 & \cdots  \\
  & \vdots &   \\
   \cdots & 0 & \cdots  \\
\end{matrix}
\right)
\end{align}
$$

## Gram-Schmidt Orthogonalization

How can we go about picking such orthogonal (orthonormal) vectors, $q1,q_2,\ldots$ and their counterparts $r_{ij}$? One method is to form the vectors by successive orthogonalization. This technique is known as Gram-Schmidt Orthogonalization.

The process is as follows. At step $j$, we want to find a unit vector $q$ that is in the span of the columns $a_1, \ldots, a_j$ that is also orthogonal to $q_1, \ldots, q_{j-1}$ (from now on, we denote the space spanned by vectors $a_1, \ldots, a_j$ as $\langle a_1, \ldots, a_j \rangle$ ). Then, the vector 

$$
v_j = a_j - (q_1^*a_j)q_1 - (q_2^*a_j)q_2 - \cdots - (q_{j-1}^*a_j)q_{j-1}
$$

is one that meets the orthogonality requirements. If we normalize it by $\|v_j\|_2$ then the result is our vector $q_j$. Then we have

$$
\begin{align}
q_1 &= \frac{a_1}{r_{11}}\\
q_2 &= \frac{a_2 - (q_1^*a_2)q_1}{r_{22}}\\
q_3 &= \frac{a_3 - (q_1^*a_3)q_1 - (q_2^*a_3)q_2}{r_{33}}\\
&\vdots \\
q_n &= \frac{a_n - \sum_{i=i}^{n-1}(q_i^*a_n)q_i}{r_{nn}}\\
\end{align}
$$

For matrix $R$, we can write

$$
r_{ij} = (q_i^*a_j) \qquad (i \neq j)
$$

and 

$$
r_{jj} = \| a_j - \sum_{i=i}^{j-1}r_{ij}q_i\|_2
$$

## Rank of $A = QR$ 

As a quick application, we can gain the following insight into the rank of $A$ based on the QR factorization:

1. $A$ has rank $n$ if and only if all the diagonal entries of $\hat{R}$ are nonzero.
2. More generally, if $\hat{R}$ has $k$ nonzero diagonal entries for some $k$ with $0 \le k \lt n$, the rank of $A$ is $k$.

**Proof (1)**
If $A$ has rank n, then any non-trivial linear combination of the $a_j$, $j=1,\ldots,n$ must be nonzero. But then the $r_{jj}$ are chosen such that 

$$
\|r_{jj}\| = \|a_{j} - \sum_{i=1}^{j-1}r_{ij}q_i\| \neq 0
$$

Conversely, if all the diagonal entries in $\hat{R}$ are nonzero, then 

$$
0 \neq \|r_{jj}\| = \|a_{j} - \sum_{i=1}^{j-1}r_{ij}q_i\| 
$$

so

$$
a_{j} - \sum_{i=1}^{j-1}r_{ij}q_i \neq 0.
$$

Since this holds for all $j$, $1 \le j \le n$ all the columns of $A$ are linearly independent and thus $A$ has rank $n$. $\Box$

**Proof (2)**
If $\hat{R}$ has $k$ nonzero diagonal entries, then we can write the QR factorization of $A$ as

$$
A = QR = [Q_1 \, Q_2]\left[ \begin{matrix}R_1\\
0\end{matrix}\right]
$$

Where $Q_1$ has $k$ linearly independent columns. So 

$$\text{rank}(A) = \text{rank}\left(Q_1R_1\right) = k \qquad \Box$$