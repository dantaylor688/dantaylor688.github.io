---
layout: post
title: Derivative of the Real Part of an Analytic Function
comments: true
---
I was helping someone recently with a homework question that required them to show that the real and imaginary parts of a complex polynomial are both individually [harmonic]({% post_url 2016-04-24-harmonic-functions %}). That is if 

$$
f(z) = a_nz^n + a_{n-1}z^{n-1} + \cdots + a_1z + a_0
$$

where the $a_i \in \mathbb{C}$, $i = 1, \ldots, n$ show that the real and imaginary part of $f = u + iv$ ($u$ and $v$ real) individually satisfy Laplace's equation

$$
\begin{align*}
\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} &= 0\\
\Delta v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2v}{\partial y^2} &= 0
\end{align*}
$$

when $f$ is considered a function of the real variables $z = x + iy$. 

The student was not familiar with complex analysis or the concept of an analytic function, so we couldn't simply make use of the [Cauchy-Riemann equations]({% post_url 2016-04-24-harmonic-functions %}).

I realized that if we just take the double derivatives we could get to the answer. 

$$
\begin{align}
\frac{\partial^2 f(x,y)}{\partial x^2} &= n(n-1)a_n(x+iy)^{n-1} + (n-1)(n-2) a_{n-1}(x+iy)^{n-3} + \cdots + a_2\\
\frac{\partial^2 f(x,y)}{\partial y^2}  &= -n(n-1)a_n(x+iy)^{n-1} - (n-1)(n-2) a_{n-1}(x+iy)^{n-3} - \cdots - a_2\\
\end{align}
$$
 
 So

$$
\Delta f(x,y) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2f}{\partial y^2} = 0
$$

and since a complex value is zero, both the real part and imaginary part must be zero. 

The problem is, that we assumed that the derivative of the real part was the same as the real part of the derivative. Now we will prove this statement.

> The derivative of the real (imaginary) part of an analytic function is the same as the real (imaginary) part of the derivative of that function.

**Proof** 
We will use the definition of the derivative with respect to the variable $x$. We will continue using the notation $f = u + iv$ so that $u = \text{Re} f.$ Then the derivative at $x_0$ is

$$
\frac{\partial }{\partial x} \text{Re}(f) = \frac{\partial u}{\partial x} = \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,y) - u(x,y)}{\Delta x}
$$

Similarly,

$$
\begin{align*}
\text{Re} \left( \frac{\partial f}{\partial x} \right) &= \text{Re} \left( \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,y) + iv(x + \Delta x,y)- u(x,y) - iv(x + \Delta x,y)}{\Delta x} \right)\\
&= \text{Re} \left(\lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,y) - u(x,y)}{\Delta x} + i \frac{ v(x + \Delta x,y) - v(x + \Delta x,y)}{\Delta x}\right)\\
&= \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,y) - u(x,y)}{\Delta x}
\end{align*}
$$


So

$$
\begin{equation}
\frac{\partial }{\partial x} \text{Re}(f) = \text{Re}\left( \frac{\partial f}{\partial x}\right)
\end{equation}
$$
 by the exact same argument
$$
\begin{equation}
\frac{\partial }{\partial x} \text{Im}(f) = \text{Im}\left( \frac{\partial f}{\partial x}\right)
\end{equation}
\qquad \Box
$$