---
layout: post
title: Why L1 Works, Simply
comments: true
---
The problem of finding a sparse vector solution to an underdetermined system:
\\[\min \|\|x\|\|_1 s.t. Ax = f\\]
is known as the Basis Pursuit problem. This is also what is used in the extremely popular field of
compressive sensing. Here \\(A\\) is an \\(m \times n\\) matrix with \\(m \lt n\\) (and usually \\(m \lt\lt n\\)). 
When we say that the vector \\(x\\) is sparse, we mean it has few non-zero entries.

We have a sparse vector in \\(L^2\\):
![plane]({{ site.url }}/assets/L1-fig0.png "Vector on the y-axis")
We also have a set of equations (just one equation since we are only working in two dimensions).
![plane]({{ site.url }}/assets/L1-fig1.png "Vector on the y-axis with Ax=b")
If we look at the \\(L^2\\) ball we can more easily see the point on the line that has minimum 
\\(L^2\\)-norm. This point is the one closest to the circle.
![plane]({{ site.url }}/assets/L1-fig2.png "L2 ball")
You can see there is a bit of a discrepency between the goal vector \\(\vec x\\) and the vector with 
minimum \\(L^2\\)-norm. Though the vectors look close, the difference is substantial when we start 
working in higher dimensions. This phenomenon is known as the curse of dimensionality. A good explanation
of the problem with distance functions in high dimensions is found near the beginning of [this paper](http://www-users.cs.umn.edu/~kumar/papers/siam_hd_snn_cluster.pdf).

Now, if we look at the \\(L^1\\) ball:
![plane]({{ site.url }}/assets/L1-fig4.png "L1 ball")

we notice that we get exact recovery (we get precisely the target vector \\(\vec x\\) when we take the 
vector on the line with minimum \\(L^1\\)-norm.
![plane]({{ site.url }}/assets/L1-fig5.png "Exact recovery")

There is more to say about incoherence and taking a few extra samples to prevent trouble when we are in a less friendly situation.
 

