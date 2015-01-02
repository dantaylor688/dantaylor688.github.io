---
layout: post
title: Differentiation by Integration
comments: true
---
*Edit: I have provided additional background and motivation for this post [here]({% post_url 2015-01-01-differentiation-by-integration-part-2 %}). This post concerns a general formula for approximating the derivative of any analytic function. My follow up post describes how to go about computing the derivative of an empirical function.*

Consider the scenario where we have samples of a function, \\(f\\). We want a way to estimate its derivative. The presence of noise on the measurements is a nonanalytical phenomenon. We would like a way to find the derivative that overcomes this obstacle. To this end, we first look at the Taylor series expansion of \\(f\\) about \\(x\\)

$$f(x + t) = f(x) + tf'(x) + \frac{t^2}{2}f''(x) + \frac{t^3}{6}f'''(x) + \cdots$$

Now, if we multiply the above expression by \\(t\\) and integrate we get the following

\\[\begin{equation}
\int_{-\varepsilon}^{\varepsilon}tf(x + t)  \, dt = \frac{2 \varepsilon^3}{3}f'(x) + \frac{\varepsilon^5}{15}f''' (x) + \cdots 
\end{equation}\\]

It is easy to see now that if we solve (1) for \\(f'(x)\\) (while ignoring higher order derivatives) we get the approximation

\\[\begin{equation}
f'(x) = \frac{3}{2 \varepsilon^3} \int_{-\varepsilon}^{\varepsilon}tf(x + t)  ~ dt. 
\end{equation}\\]

The approximation holds as long as \\(\varepsilon\\) is small. Since \\(\varepsilon\\) is in the limits of integration in (1); \\(\varepsilon\\) being small corresponds to having samples of our function densely packed together. Indeed, the error in the approximation is \\(\sim \varepsilon^2\\), so when our samples are very close together (\\(\Delta x \ll 1 \\)) the error becomes very small.

*We emphasize the fact that (2) establishes a formula for the derivative for a function even when one does not exist in the ordinary sense. This can be especially helpful in the presence of noisy measurements which ruin the smooth nature of the true function, \\(f\\).*

The formula (2) is attributed to [Cornelius Lanczos](http://en.wikipedia.org/wiki/Cornelius_Lanczos). His work, [Applied Analysis](http://www.amazon.com/Applied-Analysis-Dover-Books-Mathematics/dp/048665656X) is a surprisingly delightful read. It seems Lanczos had several results that were not fully appreciated at the time, including his work on an [FFT algorithm](http://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm#cite_ref-7) over 20 years before Cooley and Tukey.