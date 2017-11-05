---
layout: post
title: Projectors and Least Squares
comments: true
---

Here, we will take a look at projection matrices and finish up with looking again at the principle of least squares. 

## Projectors ##
A square matrix $P$ such that 

$$
\begin{equation}
P^2 = P
\end{equation}
$$

is said to be a projection matrix. The projection need not be orthogonal, if $P$ is indeed *not* orthogonal, we may call it *oblique*. 

Projectors are named such since they can be thought of as the result of shining a light on $\text{range}(P)$ from just the right direction. So that $Pv$ is the shadow of $v$. 

But from what direction does the light shine? To answer that question first consider if $v \in \text{range}(P)$. Then it lies in it's own shadow. That is if $v=Px$ for some $x$ then 

$$
Pv=P^2x = Px = v.
$$

If $v \notin \text{range}(P)$, then $v \neq Pv$ and we can consider the vector $Pv - v$. This is the vector from $v$ to $Pv$. Applying $P$ to *this* vector **will** give us $0$:

$$
P(Pv - v) = P^2v - Pv = 0.
$$

So $Pv - v \in \text{null}(P)$. So for any $v$, the direction that the light is shining from may be different, but it will be a vector in $\text{null}(P)$.

## Complementary Projectors ##

If $P$ is a projector, so is the matrix $I-P$, since

$$
(I-P)^2 = (I - P)(I - P) = I - 2P + P^2 = I - P.
$$

The projector $I-P$ is the complementary projector of $P$. 

But what is the range of the projector $(I-P)$? It is the nullspace of $P$! To see this notice that if $Pv = 0$, then $(I-P)v=v$ so $\text{range}(I-P) \supseteq \text{null}(P)$. But we also have that for any $v$, $(I-P)v = v - Pv \in \text{null}(P)$, so $\text{range}(I-P) \subseteq \text{null}(P)$ and thus 

$$
\text{range}(I-P) = \text{null}(P).
$$

By the exact same argument (but making the substitution $P=I-P$) we get that

$$
\text{range}(P) = \text{null}(I-P).
$$

So, $P$ and $I-P$ split the space $\mathbb{C}^m$ into two subspaces, $S_1$ and $S_2$ whose intersection is the singleton ${0}$. If $\text{range}(P)=S_1$ and $\text{null}(P)=S_2$, we say that the projector $P$ projects onto the space $S_1$ along the space $S_2$. 

## Orthogonal Projectors ##

An *orthogonal projector* is one that projects onto one subspace, $S_1$ along another space, $S_2$ such that $S_1$ and $S_2$ are orthogonal to each other (that is if $x \in S_1$ and $y \in S_2$, then $x^* y = 0$). Another useful definition is that in addition to the criterion for projection matrices above in (1), an orthogonal projection matrix is also Hermitian with $P^*=P$.

>**Theorem:** A projector $P$ is orthogonal if and only if $P = P^*$.

**Proof** If $P^* =P$ then the inner product between a vector $Px \in S_1$ and $(I-P)y\in S_2$ is zero:

$$
\begin{align}
(Px)^*(I-P)y &= x^*P^*(I-P)y\\
 & = x^*(P^*-P^*P)y\\
 & = x^*(P -P^2)y \\
 & = 0.
\end{align}
$$

So the projector is orthogonal.

For the other direction we can use the [SVD]({% post_url 2017-08-19-svd-geometry %}). Suppose $P$ projects onto $S_1$ along $S_2$ and $S_1 \perp S_2$ and that $S_1$ has dimension $n$. The we can form the SVD of $P$ as follows. Let ${q_1,\ldots,q_m}$ be an orthonormal basis for $\mathbb{C}^m$ where ${q_1,\ldots,q_n}$ is a basis for $S_1$ and ${q_{n+1},\ldots,q_m}$ is a basis for $S_2$. For $j \leq n$ we have $Pq_j = q_j$ and for $j>n$ we have $Pq_j = 0$. Now, let $Q$ be the unitary matrix whose $j^{\text{th}}$ column is $q_j$. Then clearly,

$$
PQ = \left( 
\begin{matrix} 
\lvert & & \lvert & \lvert & \\
q_1 & \cdots& q_n & 0 & \cdots \\
\lvert & & \lvert & \lvert & \\
\end{matrix}
\right)
$$

and 

$$
Q^*PQ = \left( 
\begin{matrix} 
1 & & & & \\
& \ddots& && \\
 & & 1 & & \\
 & & & 0& \\
& & & & \ddots\\
\end{matrix}
\right) = \Sigma
$$

is a diagonal matrix with ones along the first $n$ entries and zeros in the remaining $m-n$ diagonal entries. Thus we have the following SVD of $P$:

$$
P = Q\Sigma Q^*.
$$

Then to see that $P$ is hermitian we simply look at the conjugate transpose:

$$
P^* = \left(Q\Sigma Q^*\right)^* = Q\Sigma^* Q^* = Q\Sigma Q^* = P \qquad \Box
$$

## Projection with an Arbitrary Basis (and Least Squares)##

An orthogonal projector can be constructed from an arbitrary set set $n$ linearly independent vectors in $\mathbb{C}^m$ (not necessarily orthogonal). Suppose that the $n$-dimensional space is spanned by the linearly independent set of vectors $\left{ a_1, \ldots, a_n \right}$ and let $A$ be the $m \times n$ matrix whose $j^{\text{th}}$ column is $a_j$.

If $A$ is orthogonal, then in passing from the vector $v$ to it's orthogonal projection $y \in \text{range}(A)$, we must have that the difference $y-v$ is orthogonal to $\text{range}(A)$. This is equivalent to saying that $a_j^* (y-v) = 0$ for all $j$. Since this is true for all $j$, we can write $A^* (Ax - v)=0$ or 

$$
A^*Ax =A^*v
$$

which is the [normal equation]({% post_url 2014-12-19-gateaux-derivative %}). Since $A$ has full rank $A^* A$ is invertible and 

$$
x =\left(A^*A\right)^{-1}A^*v
$$

Then the projection $y$ of the vector $v$, $y=Ax$ in the space spanned by the columns of $A$, is given by $y=A\left(A^* A\right)^{-1}A^* v$. So the orthogonal projector, $P$ onto $\text{range}(A)$ is given by

$$
P = A\left(A^*A\right)^{-1}A^*.
$$

*Note* 
While this is yet again looking at the principle of least squares, I am convinced that it is better to be the master of a few fundamental ideas than it is to have a dabbling knowledge of many different techniques. I don't claim that this is true for me (the mastery part I mean) but am simply striving to emphasize the importance of returning to familiar ideas to increase the depth of understanding. 