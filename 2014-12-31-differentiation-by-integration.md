---
layout: post
title: Differentiation by Integration
comments: true
---
Consider the scenario where we have samples of a function, \\(f\\).We want a way to estimate its derivative. The noise on the measurements makes a simple difference unreliable. We would like to find the derivative of a smooth function that fits **all** the data points, \\((x_i, y_i)\\).

To this end, we first look at the Taylor series expansion of \\(f\\) about \\(x\\)

$$f(x + t) = f(x) + tf'(x) + \frac{t^2}{2}f''(x) + \frac{t^3}{6}f'''(x) + \cdots$$

Now, if we multiply the above expression by \\(t\\) and integrate we get the following

\\[\begin{equation} \label{ri}
\int_{-\varepsilon}^{\varepsilon}tf(x + t)  \, dt = \frac{2 \varepsilon^3}{3}f'(x) + \frac{\varepsilon^5}{15}f'''(x) + \cdots 
\end{equation}\\]

It is easy to see now that if we solve \\(\ref{ri}\\) for \\(f'(x)\\) (while ignoring higher order derivatives) we get the approximation

\\[\begin{equation}\label{rr}
f'(x) = \frac{3}{2 \varepsilon^3} \int_{-\varepsilon}^{\varepsilon}tf(x + t)  ~ dt. 
\end{equation}\\]

The approximation holds as long as \\(\varepsilon\\) is small. Since \\(\varepsilon\\) is in the limits of integration in \\(\eqref{ri}\\); \\(\varepsilon\\) being small corresponds to having samples of our function densely packed together. Indeed, the error in the approximation is \\(\sim \varepsilon^2\\), so when our samples are very close together (\\(\Delta x \ll 1 \\)) the error becomes very small.

The formula \\(\eqref{rr}\\) is attributed to [Cornelius Lanczos](http://en.wikipedia.org/wiki/Cornelius_Lanczos). His work, [Applied Analysis](http://www.amazon.com/Applied-Analysis-Dover-Books-Mathematics/dp/048665656X) is a surprisingly delightful read. It seems Lanczos had several results that were not fully appreciated at the time, including his work on an [FFT algorithm](http://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm#cite_ref-7) over 20 years before Cooley and Tukey.