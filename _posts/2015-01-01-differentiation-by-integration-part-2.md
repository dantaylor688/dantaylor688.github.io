---
layout: post
title: Differentiation by Integration part II
comments: true
---
*This post is an attempt to further motivate, and expand upon the content of my [previous post]({% post_url 2014-12-31-differentiation-by-integration %}).*

By the end of this post we will be tackling a problem similar to that discussed in my [previous post]({% post_url 2014-12-31-differentiation-by-integration %}): finding the derivative of an empirical function. 

Before we talk about finding the derivative though, we will first discuss one way to find a smooth approximation to our data. Throughout the post, we assume that the data is such that the second derivative does not change much between a few neighboring points. This assumption means that for each point in our data set, we can fit a parabola

\\[\begin{equation}
y = ax^2 +bx + c
\end{equation}\\]

centered on the point using the \\(k=2\\) closest neighbors to the left and to its right. In all, we are fitting a parabola to five points. Since this cannot be done perfectly in general we need to use the principle of [least squares]({% post_url 2014-12-19-gateaux-derivative %}). We need to minimize

$$ \begin{align}
\lVert y - y_k\rVert_2^2 &= \sum_{k=-2}^{2}(y-y_k)^2\\
&= \sum_{k=-2}^{2}(a x_k^2 + bx_k + c -y_k)^2.\tag{2}
\end{align}$$

over \\(a,b,\\) and \\(c\\). Just to clarify, we will only be looking at \\(x\_k=-2,-1,0,1,2\\), so that \\(x\_{-2} = -2\\) and \\(x_0 = 0\\) corresponds with our data point. 

When we minimize (2) with respect to \\(a,b,\\) and \\(c\\) we get the following normal equations

$$ \begin{align}
\sum_{k=-2}^{2}2(ax_k^2 + bx_k + c - y_k)x_k^2 &= 0\tag{a}\\
\sum_{k=-2}^{2}2(ax_k^2 + bx_k + c - y_k)x_k&= 0\tag{b}\\
\sum_{k=-2}^{2}2(ax_k^2 + bx_k + c - y_k)&=0\tag{c}
\end{align}$$

Expanding and simplifying (a) we get 

\\[\begin{align}(4a&-2b+c-y\_{-2})\times4 \\
&+(a - b + c -y\_{-1})\times 1\\
&+(c-y_0)\times0\\
&+(a+b+c-y_1)\times1\\
&+(4a+2b+c-y_2)\times4 \\
&= 0
\end{align}\\]

$$\begin{equation}
\implies 34a + 10c - \sum\_{k=-2}^2 k^2y_k = 0\tag{a1}
\end{equation}$$

The same process with (c) yields

\\[\begin{equation}
10a + 5c - \sum\_{k=-2}^2y_k = 0\tag{c1}
\end{equation}\\]

We first care about the value at \\(x=0\\) (our data point), the theoretical value of which is given to us by our model (1): \\(y=c\\). So we solve the system of equations (a1) and (c1) for \\(c\\).

\\[\begin{align}
35c &=\sum\_{k=-2}^2(17y_k - 5k^2)\\
&= -3y\_{-2} + 12y\_{-1} + 17y_0 + 12y_1 - 3y_2\\
\implies  70c &= -6y\_{-2} + 24y\_{-1} + 34y_0 + 24y_1 - 6y_2\\
&= 70y_0 - 6(y\_{-2} + 4y\_{-1} + 6y_0 + 4y_1 + y_2)
\end{align}\\]

so that 

\\[c = y_0 - \frac{3}{35}(y\_{-2} + 4y\_{-1} + 6y_0 + 4y_1 + y_2)\\]

The final expression in parentheses is the fourth difference at \\(y_0\\). If we denote this by \\(\delta^4y_0\\) we get a succinct formula for our smoothed value

\\[c = y_0 - 6 \delta^4y_0.\\]

It's using a similar argument that we can arrive at the value of the **derivative** of \\(f\\) at \\(y_0\\). From our model (1) we know the derivative at \\(x=0\\) is simply \\(b\\). Making the necessary substitutions into (a), (b), and (c) and solving for \\(b\\) (as we did for \\(c\\) above) we come to

\\[10b = -2y\_{-2} - y\_{-1} + y_1 + 2y_2\\]

or 
\\[b = \frac{-2y\_{-2} - y\_{-1} + y_1 + 2y_2}{10}.\\]

If instead of being one, the interval between our data points is \\(h\\) we divide our difference by \\(h\\) and arrive at the formula

\\[b = \frac{-2f(x-2h) - f(x-h) + f(x+h) + 2f(x+2h)}{10h}.\\]

If we don't want to limit ourselves to just the two closest neighbors, but rather \\(k\\) neighbors to our point of interest we get

\\[\begin{equation}
b = \frac{\sum\_{\alpha=-k}^k\alpha f(x+\alpha h)}{2 \sum\_{\alpha = -k}^k \alpha^2h}
\end{equation}.\\]

This is very similar to the formula in the [previous post]({% post_url 2014-12-31-differentiation-by-integration %}). In fact, the results in my earlier post can be seen as the limit as the data points get close. However, this is not an exact formulation. That is, the results from the previous post are not obtained  by taking the limit as \\(h \to 0\\).

As an aside, the methods discussed here exclude the first and last couple of data points (where there are not enough neighbors before/after the data). We will not discuss now ways to handle this issue.

Perhaps in the future I will include examples to help illustrate the concepts in these posts.