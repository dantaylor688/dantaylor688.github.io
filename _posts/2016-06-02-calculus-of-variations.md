---
layout: post
title: An Overview of The Calculus of Variations
comments: true
---

Given two points in the plane $M_1=(x_1,y_1)$ and $M_2=(x_2,y_2)$, what is the fastest path from $M_1$ to $M_2$? This is a standard question that can be answered by the calculus of variations. Motivated by the question above, this post will show the basic method for solving problems of this type. At the end we will also show how this method naturally extends to higher dimensional problems. The ideas that will be developed here were previously written about in this [post]({% post_url  2014-12-19-gateaux-derivative %}) but with less detail.

For the problem above, our task is to find the path giving the minimum amount of time necessary to travel from $M_1$ to $M_2$. Without loss of generality, we set the coordinate axis such that the origin goes through the point $M_1$ and $M_2$ lies in the fourth quadrant. 

Denote by $y=y(x)$ the desired path. An infinitesimal step along $y$ has arc-length

 $$\begin{align*}
 ds &= \sqrt{dx^2 + dy^2}\\
 &= \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx\\
 &= \sqrt{1 + y'^2}\,dx
 \end{align*}
 $$

Then we make use of the basic formula from physics relating velocity, distance, and time 

$$\begin{align*}
&ds = vdt\\
\implies&\frac{ds}{v} = dt
\end{align*} 
$$

The conservation of energy principle tells us that the potential energy at the beginning of the path must equal the kinetic energy at the end.

$$
\frac{1}{2}mv^2 = mgy
$$

So that

$$
v = \sqrt{2gy}
$$

Substituting this and our earlier result for $ds$ into the expression above we obtain

$$
\frac{\sqrt{1 + y'^2}}{\sqrt{2gy}}\,dx = dt
$$

Integrating yields

$$\begin{equation}
T = \frac{1}{\sqrt{2g}} \int_{0}^{x_2}\frac{\sqrt{1 + y'^2}}{\sqrt{y}}\,dx
\end{equation}
$$

This is the expression that we want to minimize in our pursuit of finding the fastest path from $M_1$ to $M_2$. Specifically, we want the function $y$ that minimizes $T$ over all functions $f = f(x)$ such that $f(0)=0$ and $f(x_2) = y_2$. In terms of the calculus of variations, the integral $T$ in (1) is an example of a **functional**. A functional is an expression whose inputs are themselves functions. Finding the extreme values of a functional is the subject of the calculus of variations. The study of general properties of functionals themselves is the subject matter of functional analysis.

### General Solution for Expressions Involving a Single Function ###

The functional $T$ in (1) is of the type

$$\begin{equation}
I(y) = \int_{x_1}^{x_2}{F(x,y,y')\,dx}
\end{equation}
$$

This is the most basic functional of the calculus of variations and will provide us a good example of the techniques. The function $F$ takes three arguments: $x,y$ and $y'$. We also assume it is twice differentiable with respect to all its arguments. We also consider functions defined on the closed interval $[x_1,x_2]$.

The set, $M$ of **admissible** functions is the set of functions, $y=y(x)$ which we will consider as possible solutions to our problem (2). The set of admissible functions here will have two requirements:

1. $y(x)$ is smooth (that is continuously differentiable) on the segment $[x_1,x_2]$.
2. $y(x)$ meets the given boundary conditions

$$
y(x_1)=y_1, \qquad y(x_2) = y_2
$$

Otherwise, the function $y(x)$ can be completely arbitrary. We will assume the function giving the minimum value of the integral exists and we will denote it by $y(x)$. 

The following argument is common in the calculus of variations. (This is similar to the argument used [here]({% post_url  2014-12-19-gateaux-derivative %}).) 

Consider the family of functions

$$
\bar{y} = y(x) + \alpha \eta(x)
$$

with parameter $\alpha$. The function $\eta$ can be any continuously differentiable function that is zero on the end points of the interval $[x_1,x_2]$.

$$
\eta(x_1) = \eta(x_2) = 0
$$

With these conditions on $\eta$, $\bar{y}$ is an admissible function. The integral $I$ computed for $\bar{y}$ becomes

$$
I = \int_{x_1}^{x_2}{F(x,y+\alpha \eta,y' + \alpha \eta')\,dx} = \Phi(\alpha)
$$

Since $\bar{y}$ corresponds with $y$ when $\alpha = 0$ the function $\Phi$ must have a minimum at $\alpha=0$ (since we assumed $y$ is the function causing the minimum of $I$). So we know that the derivative of $\Phi$ must be zero at $\alpha = 0$

$$
\Phi'(0) = 0 
$$

We compute $\Phi'(\alpha)$ as follows

$$\begin{align*}
\Phi'(\alpha) &= \frac{d}{d \alpha}\int_{x_1}^{x_2}{F(x,y+\alpha \eta,y' + \alpha \eta')\,dx}\\
&=\int_{x_1}^{x_2}{\frac{d}{d \alpha} F(x,y+\alpha \eta,y' + \alpha \eta')\,dx}\\
\end{align*}
$$

The derivative inside the last integral can be worked out using the [multi-variable chain rule]({% post_url  2016-04-24-harmonic-functions %}) 

$$\begin{align*}
\frac{d}{d \alpha} F(x,y+\alpha \eta,y' + \alpha \eta') &= \frac{\partial F}{\partial x} \frac{\partial x}{\partial \alpha} + \frac{\partial F}{\partial (y +\alpha \eta)} \frac{\partial (y +\alpha \eta)}{\partial \alpha} + \frac{\partial F}{\partial (y' +\alpha \eta')} \frac{\partial (y' +\alpha \eta')}{\partial \alpha}\\
&= 0 + \frac{\partial F}{\partial (y +\alpha \eta)}\eta + \frac{\partial F}{\partial (y' +\alpha \eta')}  \eta'
\end{align*}
$$

So that 

$$\begin{align*}
\Phi'(\alpha) =\int_{x_1}^{x_2}{\frac{\partial F}{\partial (y +\alpha \eta)}\eta + \frac{\partial F}{\partial (y' +\alpha \eta')}  \eta'\,dx}\\
\end{align*}
$$

Letting $\alpha \rightarrow 0$ 

$$
\Phi'(0) =\int_{x_1}^{x_2}{\frac{\partial F}{\partial y }\eta + \frac{\partial F}{\partial y'}  \eta'\,dx}
$$

Then integration by parts allows us to switch the differential in the second term inside the integral (paying the price of a minus sign). After factoring out the common $\eta$ we get

$$\begin{equation}
\Phi'(0) = \int_{x_1}^{x_2}{\left(\frac{\partial F}{\partial y } - \frac{d}{dx}\frac{\partial F}{\partial y'}\right)  \eta \,dx} = 0\\
\end{equation}
$$

We pause for a brief lemma

**Lemma**

>If
>
>$$
\int_{a}^{b} f(x)\xi(x) \,dx = 0 
$$
>
> for all functions $\xi$, then $f(x) = 0$ on the interval $[a,b]$. 

**Proof**

Suppose to the contrary that for some $c \in [a,b]$ $f(c) \neq 0$. Then since $f$ is continuous, there exists an interval $[\alpha,\beta]$ on which $f$ is not identically zero and has the same sign as $f(c)$. 

We can then construct a continuously differentiable function, $\xi$ that will cause the integral to be non-zero over $[\alpha,\beta]$. For instance,

$$
\xi(x) = \begin{cases}
0 & a < x < \alpha\\
(x-\alpha)^2(x-\beta)^2 & \alpha < x < \beta \\
0 & \beta < x < b
\end{cases}
$$   

Then,

$$
\int_{a}^{b} f(x)\xi(x) \,dx =  \int_{\alpha}^{\beta} f(x)\xi(x) \,dx.
$$

The last integral cannot be zero since $f\xi$ is non-zero over $[\alpha,\beta]$ and never changes sign. So $f=0$ over $[a,b]$. $\Box$

Applying this lemma to (3), we immediately see that 

 $$\begin{equation}
 \frac{\partial F}{\partial y } - \frac{d}{dx}\frac{\partial F}{\partial y'} = 0
 \end{equation}
 $$

Using the [multi-variable chain rule]({% post_url  2016-04-24-harmonic-functions %}), we can compute the last derivative in (4) and write **Euler's Equation**

$$\begin{equation}
F_y - F_{xy} - F_{yy'}y' - F_{y'y'} y'' = 0
\end{equation}
$$

where we have adopted the notation $F_y = \frac{\partial F}{\partial y}$.

If a function, $y(x)$ minimizes the integral $I(y)$ it must satisfy the differential equation (5). This is analogous to searching for critical points in a first semester calculus course by finding points such that $df = 0$. This reduces our work from looking at any arbitrary function to those that solve (5) while satisfying the boundary conditions

$$
y(x_1) = y_1 \qquad y(x_2) = y_2
$$

We have thus transformed a statement about minimizing an integral to that of solving a boundary value problem for differential equations.

#### Example ####

Going back to our example at the beginning of the post, we already saw that in order to find the fastest path between two points we must find the minimum of the integral (1).

$$
T = \frac{1}{\sqrt{2g}} \int_{0}^{x_2}\frac{\sqrt{1 + y'^2}}{\sqrt{y}}\,dx
$$

Following the notation in (2), 

$$
F(y) =  \frac{\sqrt{1 + y'^2}}{\sqrt{y}}.
$$

Then using (5) we can find the function that minimizes (1). First note the partial derivatives

$$
F_y = -\frac{1}{2}\frac{\sqrt{1+y'^2}}{y^{3/2}} \qquad F_{y'} = \frac{y'}{\sqrt{y} \sqrt{(1+y')^2}}
$$

and the second partials 

$$
F_{yy'} = -\frac{1}{2}\frac{y'}{y^{3/2}\sqrt{(1+y')^2}} \qquad F_{y'y'} = \frac{1}{ \sqrt{y}(1+y'^2)}
$$

$$
F_{xy'} = 0.
$$

So that (5) becomes

$$
-\frac{1}{2}\frac{\sqrt{1+y'^2}}{y^{3/2}} - 0 + \frac{1}{2}\frac{y'^2}{y^{3/2}\sqrt{(1+y')^2}} - \frac{1}{ \sqrt{y}(1+y'^2)}y'' = 0
$$

$$
\implies \frac{-1}{2y^{3/2}\sqrt{1+y'^2}} - \frac{y''}{\sqrt{y}(1+y'^2)^{3/2}} = 0
$$

which after rearranging becomes

$$
\frac{-1}{y} = \frac{2y''}{1+y'^2}
$$

We solve this differential equation by multiplying by  $y'$ and integrating.

$$
\int\frac{-y'}{y}\,dx = \int\frac{2y''y'}{1+y'^2}\,dx
$$

So that

$$
-\log y + \log k = \log (1+ y'^2)
$$

(Where we have written the additive constant as a logarithm for simplicity as will be made clear next). This last equation can be manipulated to become

$$\begin{align*}
y'^2 &= \frac{k}{y} - 1 \\
\implies y' &= \pm \sqrt{\frac{k-y}{y}}
\end{align*}
$$

$$\begin{equation}
\implies \sqrt{\frac{y}{k-y}}\,dy = \pm \, dx
\end{equation}
$$

Now we make the substitution

$$
y = \frac{k}{2}(1-\cos u) \qquad dy = \frac{k}{2} \sin u \,du
$$

Then the left side of (6) becomes

$$\begin{align*}
\sqrt{\frac{1 - \cos u}{1+\cos u}}\frac{k}{2} \sin u \,du &= \sqrt{\frac{(1 - \cos u)^2}{1- \cos^2 u}}\frac{k}{2} \sin u \,du \\
&=\sqrt{\left( \frac{1 - \cos u}{\sin u} \right)^2}\frac{k}{2} \sin u \,du \\
&= \frac{k}{2}(1-\cos u) \,du
\end{align*}
$$

So

$$
\frac{k}{2}(1-\cos u) \,du = \pm \,dx
$$

and upon integrating

$$
x = \frac{k}{2}(u-\sin u) + C
$$

Since the curve goes through the origin (where we placed $M_1$), it follows that $C=0$. So the solution to our initial question of finding the fastest path between two points is given by the cycloid

$$\begin{equation}
x = \frac{k}{2}(u-\sin u) \qquad y = \frac{k}{2}(1-\cos u) 
\end{equation}
$$

### Functionals Depending on Several Functions ###

Next, we consider a functional that depends on several functions.  The technique is the same as the case above. For simplicity, we consider a functional that depends on two functions. Higher dimensional problems will be follow similarly.

We consider the functional 

$$\begin{equation}
I(y,z) = \int_{t_1}^{t_2}F(t,y,z,y',z')\,dt
\end{equation}
$$

where $y=y(t)$ and $z=z(t)$. The admissible functions here meet the following two criteria:

1. $y(t)$ and $z(t)$ are continuously differentiable over the interval $[t_1,t_2]$.
2. They also meet the boundary conditions

$$\begin{matrix}
y(t_1) = y_1 & y(t_2) = y_2\\
z(t_1) = z_1 & z(t_2) = z_2
\end{matrix}
$$ 

We denote by $y$ and $z$ those functions which minimize the functional $I$.

Similar to above, we define

$$
\bar{y} = y+\alpha \zeta \qquad \bar{z} = z + \alpha \eta
$$

for continuously differentiable functions $\zeta$ and $\eta$ which themselves depend on $t$ and are zero at the ends of the interval  $[t_1,t_2]$. With these definitions, we see that 

$$
I(\bar{y},\bar{z}) = \int_{t_1}^{t_2}F(t,y+\alpha \zeta ,z+ \alpha \eta ,y'+\alpha \zeta ',z'+ \alpha \eta')\,dt = \Phi(\alpha)
$$

Then when $\alpha = 0$, $\bar{y}$ and $\bar{z}$ correspond with $y$ and $z$ respectively, hence $\Phi'(0)=0$.

$$
\Phi'(0) = \int_{t_1}^{t_2} \frac{\partial F}{\partial y}\zeta + \frac{\partial F}{\partial z} \eta + \frac{\partial F}{\partial y'}\zeta ' + \frac{\partial F}{\partial z'} \eta ' \,dt  =0
$$

We can rewrite the last integral as

$$\begin{equation}
\Phi'(0) = \int_{t_1}^{t_2} \frac{\partial F}{\partial y}\zeta + \frac{\partial F}{\partial y'}\zeta ' + \frac{\partial F}{\partial z} \eta + \frac{\partial F}{\partial z'} \eta ' \,dt  =0
\end{equation}
$$

From which we readily see that integration by parts gives us

$$\begin{equation}
\Phi'(0) = \int_{t_1}^{t_2} \left(\frac{\partial F}{\partial y} - \frac{d}{dt}\frac{\partial F}{\partial y'}\right)\zeta + \left(\frac{\partial F}{\partial z} - \frac{d}{dt} \frac{\partial F}{\partial z'}\right) \eta \,dt  =0
\end{equation}
$$

Since (10) holds for all $\zeta$ and $\eta$ that are continuously differentiable and zero on the endpoints of the interval, by the lemma proved above we must have

$$\begin{align*}
\frac{\partial F}{\partial y} - \frac{d}{dt}\frac{\partial F}{\partial y'} &= 0\\
\frac{\partial F}{\partial z} - \frac{d}{dt} \frac{\partial F}{\partial z'} &= 0
\end{align*}
$$

So in this case, our problem of finding the minimum of functional (8) amounts to finding a solution for the boundary-value problem for this last [system of differential equations]({% post_url  2015-11-03-decoupling-differential-equations %}).

I will not work out the details here, but as an example one may work out Newton's laws of motion from minimizing the integral of "total engery" of a particle.

### Multiple Integrals ###

The last functional we will consider here is a multiple integral. For simplicity, we will just consider the case of a double integral. Again, the process is no different for higher dimensional problems. 

Let $B$ be a domain in the plane bounded by the contour $l$. Now the set of admissible functions will be those that meet the criteria

1. $u(x,y)$ is continuously differentiable on $B$.
2. On $l$ the function $u$ takes the given values

$$
u|_l=f(M)
$$

We want to minimize the double integral

$$\begin{equation}
I(u) = \iint_B F(x,y,u,u_x,u_y)\,dx\,dy
\end{equation}
$$

Again, define

$$
\bar{u} = u + \alpha \eta(x,y)
$$

where $\eta(x,y)$ is continuously differentiable on $B$ and zero on $l$. Then just as above, we must have

$$
I(\bar{u}) = \iint_B F(x,y,u+ \alpha \eta, u_x + \alpha \eta_x, u_y+ \alpha \eta_y)\,dx\,dy = \Phi(\alpha)
$$

and

$$
\Phi'(0) = \iint_B \frac{\partial F}{\partial u}\eta + \frac{\partial F}{\partial u_x}\eta_x + \frac{\partial F}{\partial u_y}\eta_y \,dx \,dy = 0 
$$

By the product rule we can rewrite the integrand as

$$
\frac{\partial F}{\partial u}\eta + \frac{\partial F}{\partial u_x}\eta_x + \frac{\partial F}{\partial u_y}\eta_y = \frac{\partial F}{\partial u}\eta + \frac{\partial}{\partial x}\left(F_{u_x}\eta\right) - \frac{\partial F_{u_x}}{\partial x}\eta + \frac{\partial}{\partial y}\left(F_{u_y}\eta\right) - \frac{\partial F_{u_y}}{\partial y}\eta
$$

This allows us to rewrite the integral as

$$
\iint_B \left(\frac{\partial}{\partial x}\left(F_{u_x}\eta\right) + \frac{\partial}{\partial y}\left(F_{u_y}\eta\right)\right) \,dx\,dy + \iint_B \left(\frac{\partial F}{\partial u} - \frac{\partial F_{u_x}}{\partial x} - \frac{\partial F_{u_y}}{\partial y}\right)\eta\,dx\,dy
$$

By [Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem), the first integral can be rewritten as a contour integral over $l$.

$$
\iint_B \left(\frac{\partial}{\partial x}\left(F_{u_x}\eta\right) + \frac{\partial}{\partial y}\left(F_{u_y}\eta\right) \right) \,dx\,dy = \oint_l -F_{u_y} \eta \,dx + F_{u_x}\eta \, dy
$$

This contour integral over $l$ must vanish since $\eta$ vanishes on $l$. This makes our above equation

$$\begin{equation}
\Phi'(0) = \iint_B \left(\frac{\partial F}{\partial u} - \frac{\partial F_{u_x}}{\partial x} - \frac{\partial F_{u_y}}{\partial y}\right)\eta\,dx\,dy = 0
\end{equation}
$$

Which holds for all contiously differentiable functions $\eta$ that vanish on $l$, so 

$$\begin{equation}
\frac{\partial F}{\partial u} - \frac{\partial F_{u_x}}{\partial x} - \frac{\partial F_{u_y}}{\partial y} = 0
\end{equation}
$$

We have again reduced the problem of finding the minimum of a integral to that of finding a solution to a boundary problem of a (partial) differential equation. If $u$ is to be a solution to the problem (11) it must be a solution to the equation (13) and meet the boundary conditions (1) and (2) mentioned at the beginning of this section.

#### Example ####

To find the displacement of points on a membrane streched over a region $B$ with boundary values $\phi$ we minimize the potential energy

$$
\frac{\mu}{2}\iint_B u_x^2 + u_y^2 \,dx\,dy
$$

Ignoring the constant term $\mu$

$$
F = \frac{1}{2}\left(u_x^2 + u_y^2\right)
$$


So that (13) becomes 

$$
-\frac{\partial}{\partial x} u_x - \frac{\partial}{\partial y} u_y = 0
$$

or 

$$\begin{equation}
\Delta u = \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0
\end{equation}
$$

That is, the problem of finding the displacement of points of a membrane is reduced to finding a [harmonic function]({% post_url  2016-04-24-harmonic-functions %}) that meets the specified boundary conditions.
