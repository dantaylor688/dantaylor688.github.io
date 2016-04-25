---
layout: post
title: Harmonic Functions and Some Calc III
comments: true
---
A function $u = u(x,y)$ is harmonic if it satisfies **Laplace's Equation**

$$
\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0
$$

Harmonic functions come up in several physical problems and are of immense value in applications. In addition to showing the connection between harmonic functions and analytic functions in the complex plane, this post will also serve as a good refresher of some results learned in a multi-variable calculus course. 

### Harmonic and Analytic Functions ###
If a function $f$ is analytic then we can write $f = u + iv$. Since $f$ is analytic, it satisfies the Cauchy-Riemann equations

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

So

$$\begin{align*}
\Delta u &= \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2u}{\partial y^2}\\
&= \frac{\partial }{\partial x} \frac{\partial v}{\partial y}- \frac{\partial }{\partial y}\frac{\partial v}{\partial x}\\
&= \frac{\partial^2 v}{\partial x\partial y}- \frac{\partial^2 v}{\partial x\partial y}\\
&=0
\end{align*}
$$

Similarly $\Delta v = 0$. So both the real and imaginary parts of $f$ are harmonic. 

Conversely, if $u$ is harmonic then define $f$ to be

$$
f = u - i \int_{x_0}^x \frac{\partial u}{\partial y}(t,y)\,dt + i \int_{y_0}^y \frac{\partial u}{\partial x}(x_0,s)\,ds
$$

Then by the Fundamental Theorem of Calculus 

$$
\frac{\partial f}{\partial x} = \frac{\partial u}{\partial x} - i \frac{\partial u}{\partial y}
$$

and

$$\begin{align*}
\frac{\partial f}{\partial y} &= \frac{\partial u}{\partial y} - i \int_{x_0}^x \frac{\partial^2 u}{\partial y^2}(t,y)\,dt + i \frac{\partial u}{\partial x}\\
&= \frac{\partial u}{\partial y} + i \int_{x_0}^x \frac{\partial^2 u}{\partial x^2}(t,y)\,dt + i \frac{\partial u}{\partial x}\\
&= \frac{\partial u}{\partial y} + i\left(\frac{\partial u}{\partial x}(x,y) - \frac{\partial u}{\partial x}(x_0,y) \right) + i \frac{\partial u}{\partial x}\\
&=\frac{\partial u}{\partial y} + i \frac{\partial u}{\partial x}\\
&=i\frac{\partial f}{\partial x}
\end{align*}
$$

Then if we write $f=u+iv$ (where $v$ is the term with integrals above), then

$$\begin{align*}
i\frac{\partial f}{\partial x} &= \frac{\partial f}{\partial y}\\
i \left(\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} \right) &= \frac{\partial u}{\partial y} + i \frac{\partial v}{\partial y}\\
- \frac{\partial v}{\partial x}  + i\frac{\partial u}{\partial x} &= \frac{\partial u}{\partial y} + i \frac{\partial v}{\partial y}
 \end{align*}
$$

So that

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

but these are the Cauchy-Riemann equations. So $f$ is analytic, and thus $u$ is the real part of an analytic function.

Therefore, we have shown that *a function is harmonic if and only if it is the real part of some analytic function.*

### Maximum and Mean Values ###

With the conclusion of the last section under our belts, we can quickly conclude based on results discussed in [this post]({% post_url 2016-02-13-analytic-function-geometry %}) that:

>If a function $u$ is harmonic on a domain $D$ and continuous on $D \cup B$ (where $B$ is the boundary of $D$), then $u$ does not attain a maximum on $D$ and its maximum is on $B$.

Furthermore, we have a **Mean-Value Theorem for harmonic functions**. Let $u$ be a (possibly complex) harmonic function. Then we can write it as a sum of two real valued harmonic functions 

$$
u = u_1 + iu_2
$$

Define $f_1$ and $f_2$ to be the corresponding analytic functions for which $u_1$ and $u_2$ are the real part respectively. If we let $z_0 \in D$, and $R$ be the largest radius that can be drawn around $z_0$ and still have all the points, $z \in \|z-z_0\| <R$ lie within $D$ then for any $r$, $0 \lt r \lt R$ the following holds

$$\begin{align*}
u(z_0) &= u_1(z_0) + iu_2(z_0)\\
&= \text{Re}f_1(z_0) + i\text{Re}f_2(z_0)\\
&=\text{Re}\int_0^{2\pi}f_1(z_0 + re^{it})\,dt + i\text{Re}\int_0^{2\pi}f_2(z_0 + re^{it})\,dt \\
&=  \int_0^{2\pi}\text{Re}f_1(z_0 + re^{it})\,dt + \int_0^{2\pi}i\text{Re}f_2(z_0 + re^{it})\,dt\\
&=\int_0^{2\pi}\text{Re}f_1(z_0 + re^{it}) + i\text{Re}f_2(z_0 + re^{it})\,dt\\ 
&= \int_0^{2\pi}u_1(z_0 + re^{it}) + iu_2(z_0 + re^{it}) \,dt \\
&= \int_0^{2\pi}u(z_0 + re^{it})\,dt
\end{align*}
$$

To reiterate

> The **Mean-Value Theorem for harmonic functions** is
>
>$$
u(z_0)   =\int_0^{2\pi}u(z_0 + re^{it})\,dt
$$


### Multi-variable Chain Rule ###
We digress for a moment to review a result from your multi-variable calculus class. 

>If $f = f(x(t),y(t))$ is continuous with continuous partial derivatives, and its components $x=x(t)$ and $y=y(t)$ are also continuous and smooth, then 
>
>$$
\frac{\partial f}{\partial t} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial t} 
$$

**Proof**
We use the definition of the derivative

$$\begin{align*}
\frac{\partial f}{\partial t} &= \lim_{h \rightarrow 0} \frac{f(x(t+h),y(t+h)) - f(x(t),y(t))}{h}\\
&= \lim_{h \rightarrow 0} \frac{f(x(t+h),y(t+h)) - f(x(t),y(t+h))}{h} + \frac{f(x(t),y(t+h)) - f(x(t),y(t))}{h}\\
\end{align*}
$$

By the [Mean Value Theorem](https://en.wikipedia.org/wiki/Mean_value_theorem) the limit of the first term in the last equation is equal to $\frac{\partial f(x(c_x),y)}{\partial x}\frac{\partial x(c_x)}{\partial t}$ for some $c_x$ with $t \lt c_x \lt t+h$. An analogous argument can be made for the second term in the last equation, leading us to 

$$\begin{align*}
\frac{\partial f}{\partial t} &= \lim_{h \rightarrow 0} \frac{f(x(t+h),y(t+h)) - f(x(t),y(t))}{h}\\
&= \lim_{h \rightarrow 0} \frac{f(x(t+h),y(t+h)) - f(x(t),y(t+h))}{h} + \frac{f(x(t),y(t+h)) - f(x(t),y(t))}{h}\\
&= \frac{\partial }{\partial x}f(x(c_x),y)\frac{\partial x(c_x)}{\partial t} + \frac{\partial }{\partial y}f(x(t),y(c_y))\frac{\partial y(c_y)}{\partial t} 
\end{align*}
$$

Hence,

$$
\frac{\partial f}{\partial t} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial t} 
$$

as desired. $\Box$ 

### Laplace's Equation in Polar Coordinates ###

We will now use the chain rule to derive the Laplace operator in polar coordinates. Recall that the relationship between polar coordinates $(r,\theta)$ and the Cartesian system is given by

$$\begin{cases}
x = r\cos(\theta)\\
y = r\sin(\theta)
\end{cases}
$$

To begin our derivation, we use the above definitions to note the following partial derivatives:

* $$
\frac{\partial x}{\partial r} = \cos(\theta)
$$
* $$
\frac{\partial x}{\partial \theta} = -r\sin(\theta)
$$
* $$
\frac{\partial y}{\partial r} = \sin(\theta)
$$
* $$
\frac{\partial y}{\partial \theta} = r\cos(\theta)
$$

Now, we compute the partial derivative $\frac{\partial u}{\partial r}$. As above, we use $u = u(x,y)$ and emphasize that $x$ and $y$ themselves are functions of $r$ and $\theta$. Then, using the chain rule 

$$\begin{align*}
\frac{\partial u}{\partial r} &= \frac{\partial u}{\partial x} \frac{\partial x}{\partial r} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial r} \\
&= \frac{\partial u}{\partial x} \cos(\theta) + \frac{\partial u}{\partial y} \sin(\theta)
\end{align*}
$$

Similarly,

$$\begin{align*}
\frac{\partial u}{\partial \theta} &= \frac{\partial u}{\partial x} \frac{\partial x}{\partial \theta} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial \theta} \\
&= \frac{\partial u}{\partial x} (-r\sin(\theta)) + \frac{\partial u}{\partial y} r\cos(\theta)
\end{align*}
$$

Another application of the chain rule gives the second partials (remember that $\frac{\partial u}{\partial x}$ and $\frac{\partial u}{\partial y}$ are also functions of $x=x(r,\theta)$ and $y=y(r,\theta)$)

$$\begin{align*}
\frac{\partial^2 u}{\partial r^2} &= \frac{\partial}{\partial r} \frac{\partial u}{\partial r} \\
&= \frac{\partial}{\partial r}\left(\frac{\partial u}{\partial x} \cos(\theta) + \frac{\partial u}{\partial y} \sin(\theta)\right)\\
&=\frac{\partial}{\partial r}\frac{\partial u}{\partial x} \cdot\cos(\theta) + \frac{\partial}{\partial r}\frac{\partial u}{\partial y}\cdot \sin(\theta) \\ 
&= \left( \frac{\partial}{\partial x}\frac{\partial u} {\partial x} \cdot\frac{\partial x}{\partial r} + \frac{\partial}{\partial y}\frac{\partial u} {\partial x} \cdot\frac{\partial y}{\partial r}\right)\cos(\theta) \\
 & \qquad + \left( \frac{\partial}{\partial x}\frac{\partial u} {\partial y} \cdot\frac{\partial x}{\partial r} + \frac{\partial}{\partial y}\frac{\partial u} {\partial y} \cdot\frac{\partial y}{\partial r}\right)\sin(\theta)\\
 &= \left( \frac{\partial^2 u} {\partial x^2} \cos(\theta) + \frac{\partial^2 u} {\partial y \partial x} \sin(\theta)\right)\cos(\theta) + \left( \frac{\partial^2 u} {\partial x \partial y} \cos(\theta)+ \frac{\partial^2 u} {\partial y^2} \sin(\theta)\right)\sin(\theta)
\end{align*}
$$

Assuming that $u$ and all its components are sufficiently well behaved so that $\frac{\partial^2 u}{\partial x \partial y} = \frac{\partial^2 u}{\partial y \partial x}$, we can write

$$\begin{equation}
\frac{\partial^2 u}{\partial r^2} = \frac{\partial^2 u} {\partial x^2} \cos^2(\theta) + 2\frac{\partial^2 u} {\partial x \partial y} \sin(\theta)\cos(\theta) + \frac{\partial^2 u} {\partial y^2} \sin^2(\theta)
\end{equation}
$$

In a similar fashion,

$$\begin{equation}
\frac{\partial^2 u}{\partial \theta^2} = -r\left(\frac{\partial u}{\partial x}\cos(\theta) + \frac{\partial u}{\partial y}\sin(\theta)\right) + r^2\left(\frac{\partial^2 u} {\partial x^2} \sin^2(\theta) - 2\frac{\partial^2 u} {\partial x \partial y} \sin(\theta)\cos(\theta) + \frac{\partial^2 u} {\partial y^2} \cos^2(\theta) \right)
\end{equation}
$$

Observing that the first term of equation (2) is $\frac{\partial u}{\partial r}$ from above, we divide (2) by $r^2$ and then add the resulting equation to (1) yielding

$$\begin{align*}
\frac{\partial^2 u}{\partial r^2} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} =& \frac{\partial^2 u} {\partial x^2} \cos^2(\theta) + 2\frac{\partial^2 u} {\partial x \partial y} \sin(\theta)\cos(\theta) + \frac{\partial^2 u} {\partial y^2} \sin^2(\theta)\\ 
&-\frac{1}{r}\frac{\partial u}{\partial r} + \frac{\partial^2 u} {\partial x^2} \sin^2(\theta) - 2\frac{\partial^2 u} {\partial x \partial y} \sin(\theta)\cos(\theta) + \frac{\partial^2 u} {\partial y^2} \cos^2(\theta) 
\end{align*}
$$

Simplifying, we find the Laplace operator in polar coordinates

$$
\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = \frac{\partial^2 u}{\partial r^2} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} + \frac{1}{r}\frac{\partial u}{\partial r}
$$

With this form, we can quickly see that if a harmonic function depends on $\theta$ alone it must satisfy

$$
\frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} = 0
$$

So $u$ must be linear

$$
u(r,\theta) = A + B\theta.
$$

Similarly, if $u=u(r)$ is a function of $r$ only then for $u$ to be harmonic it must satisfy


$$
 \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} = 0
$$

and

$$
u(r,\theta) = A + B\log(r) \qquad 0 \lt r \lt \infty
$$