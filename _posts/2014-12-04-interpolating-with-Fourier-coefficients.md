---
layout: post
title: Interpolating a Function with Its Fourier Coefficients
comments: true
---
It is often convenient to choose to work with a Fourier basis when modeling your data.
If we write the Discrete Fourier Transform (DFT) as 

\\[F_k = \sum_{n=0}^{N-1} f_n e^{-2 \pi i k \frac{n}{N}}\\]

for \\(k = 1 \ldots N\\). Then we can get our original function back using the inverse DFT formula. 
\\[f_n = \frac{1}{N} \sum_{k=0}^{N-1} F_k e^{2 \pi i k \frac{n}{N}}\\]

However this formula doesn't allow us to interpolate our model between the timestamps of our measurements, 
\\(t_n = \frac{n}{N}\\) for \\(n \in 0, \ldots , N-1\\).

So the question is, using the given \\(F_k\\)'s which we may have computed using a simple 
call to [Numpy's fft function](http://docs.scipy.org/doc/numpy/reference/routines.fft.html), say, 
how can we estimate \\(f(t)\\) where \\(t_0 \lt t \lt t_{N-1}\\)?

The solution is to use negative frequencies instead of the higher frequencies.

\\[f_n = \frac{1}{N} \left[ \sum_{k=0}^{N/2-1}{F_k e^{2 \pi i k t}} +  \sum_{k= N/2 }^{ N-1 }{F_k e^{-2 \pi i (N-k) t}} \right] \\].
