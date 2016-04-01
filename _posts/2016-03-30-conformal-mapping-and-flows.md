---
layout: post
title: Conformal Mapping and Flows
comments: true
---

If $f$ is a [sourcless and irrotational flow]({% post_url 2016-02-13-analytic-function-geometry %}) on a domain $D$ then there exists an analytic function $G$ such that

$$
G'(z) = \overline{f(z)} \qquad z \in D
$$

$G$ is known as the **complex potential** of the flow. In this post, we will see that the level curves $\text{Im }G = c_0$ where $c_0$ is a constant are the paths followed by a particle in the flow. That is, these level curves are the [streamlines](https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines) of the flow.

Let $z_0$ be a point in $D$ such that $G(z_0) \ne 0$. Then $G'(z_0) = \overline{f(z_0)} \ne 0$ so $G$ is one-to-one in $\left\{ z : \|z-z_0\| \lt \delta \right\}$ that is some disc centered at $z_0$ (see the discussion [here]({% post_url 2015-12-30-learning-laurent-series %})). Since $G$ is one-to-one, it is invertible. Denote its inverse by $H$ so that $H(G(z)) = z$ at least for all $z$ in $|z-z_0| \lt \delta$. Then, $H(w)$ is an analytic function for $w \in \Omega = \left\{G(z) : |z - z_0 | \lt \delta\right\}$. 

Now the level curve

$$
\Gamma_0 = \left\{z: \text{Im }G(z) = \text{Im }G(z_0), |z-z_0| \lt \delta \right\}
$$

can be written as

$$\begin{align*}
\Gamma_0 &= \left\{z: \text{Im }G(z) = \text{Im }G(z_0), |z-z_0| \lt \delta \right\}\\
&= \left\{H(w): \text{Im }w = \text{Im }G(z_0), w \in \Omega\right\}\\
&=  \left\{H(\tau + ic_0): c_0 = \text{Im }G(z_0), \tau + ic_0 \in \Omega\right\}
\end{align*}
$$

The tangent vector of $\Gamma_0$ is the derivative of $H(\tau + ic_0)$ with respect to $\tau$ which is also the derivative of $H$ with respect to $w$ because $H$ is analytic. Then, by the chain rule

$$
1 = \frac{d}{dz}z = \frac{d}{dz}H(G(z)) = H'(G(z))G'(z) = H'(w)\overline{f(z)}
$$

So

$$\begin{equation}
\frac{1}{H'(w)} = \overline{f(z)} 
\end{equation}
$$

and consequently,

$$
\frac{H'(w)}{|H'(w)|} = \frac{|f(z)|}{f(z)} = \frac{\overline{f(z)}}{|f(z)|} 
$$

So the unit tangent vector of $\Gamma_0$ is parallel to that of $f(z)$ for all $z$ in $\Gamma_0$. 

Now if $u(t)$, $a \lt t \lt b$ is a continuously differentiable function with values on the line $$L = \left\{ \tau + ic_0: \tau + ic_0 \in \Omega, c_0 = \text{Im }G(z_0) \right\}$$ such that

$$
u'(t) = \left|H'(u(t))\right|^{-2}, \qquad a \lt t \lt b
$$

and define $\gamma (t) = H(u(t))$, $a \lt t \lt b$. Then the range of the curve $\gamma$ is 

$$\begin{align*}
\gamma(t) &= \left\{H(u(t)): \text{Im }G(z) = \text{Im }G(z_0), |z-z_0| \lt \delta \right\}\\
&= \left\{H(\tau + ic_0): c_0 = \text{Im }G(z_0), \tau + ic_0 \in \Omega\right\}\\
&= \left\{\tau + ic_0:  \tau + ic_0 \in \Omega, c_0 =  \text{Im }G(z_0)\right\}\\
&=  \left\{z:  c_0 =  \text{Im }G(z_0)\right\}
\end{align*}
$$

Which is precisely $\Gamma_0$. Then using (1) from above, the derivative of $\gamma$ is given by

$$\begin{align*}
\gamma'(t) &= H'(u(t))u'(t)\\
&= \frac{H'(u(t))}{|H'(u(t))|^{2}}\\
&= \frac{1}{\overline{H'(u(t))}}\\
&= f(H(u(t))\\
&= f(\gamma(t))
\end{align*}
$$

for $a \lt t \lt b$. So the tangent vectors of $\gamma$ are precisely the paths that a particle in the flow will follow. That is, the level curves given by $\Gamma_0$ are exactly the streamlines of $f$. 

This observation serves to motivate the [Riemann Mapping theorem](https://en.wikipedia.org/wiki/Riemann_mapping_theorem) and  [Schwarz-Christoffel Transformations](https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping) because it shows us why we might care to find specific conformal maps. Perhaps there will be a follow up post on these results.