---
layout: post
title: Transcritical Bifurcations
comments: true
---

In my [last post]({% post_url  2016-09-03-saddle-node-bifurcation%}), we discussed the simplest type of bifurcation, the saddle-node bifurcation. Next, we look at a different type of bifurcation. The transcritical bifurcation has the normal form

$$
\begin{equation}
\dot{x} = rx - x^2
\end{equation}
$$

In this type of bifurcation, instead of both fixed points annihilating each other, the fixed points "swap" stability. Let's look at the normal form (1) to see what this means.

![plane]({{ site.url }}/assets/transcritical/phase.png "r varries")

Notice that $x=0$ is a fixed point for a $r$.  For $r<0$, $x = 0$ is stable and $x = r$ is unstable.  For $r>0$ the fixed points "swap" stability and $x=0$ becomes unstable while $x=r$ is now stable. The bifurcation diagram is given next

![plane]({{ site.url }}/assets/transcritical/bif.png "bifurcation")

### Example ###
Next, we consider the example 

$$
\begin{equation}
\dot{x} = rx - \log(1+x)
\end{equation}
$$

We will handle this in two different ways. First, we look at the phase diagram of (2) for several values of $r$.

![plane]({{ site.url }}/assets/transcritical/log-bif.png "log phase diagram")

Notice that $x=1$ is a fixed point for all $r$. We can employ the same method as in the [previous post]({% post_url  2016-09-03-saddle-node-bifurcation%}) and solve for $r$ in terms of $x$ and then just invert the axes. For a fixed point, 

$$
\begin{align*}
0 &= rx-\log(1+x)\\
r &= \frac{\log(1+x)}{x}
\end{align*}
$$

When we invert the axes (making the plot of $x$ as a function of $r$) we get

![plane]({{ site.url }}/assets/transcritical/log.png "x*")

Another strategy is to make use of the Taylor expansion of $\log(1+x)$ about the point $x=1$.

$$
\log(1+x) = x - \frac{x^2}{2} + O(x^3)
$$

The the system (2) becomes

$$
\begin{align*}
\dot{x} &= rx - x + \frac{x^2}{2} + O(x^3)\\
&= (r-1)x + \frac{x^2}{2} + O(x^3)
\end{align*}
$$

So 

$$
\begin{align}
\dot{x} &\approx (r-1)x + \frac{x^2}{2}\\
\implies \dot{x} &\approx -2 (r-1)x - x^2
\end{align}
$$

Then again, the system has a trans-critical bifurcation at $r = 1$ and now a linear approximation of the bifurcation diagram (good for $x \approx 0$) is 

![plane]({{ site.url }}/assets/transcritical/lin-approx.png "linear approximation")

And here are the two plots together to get a better feel for how good the approximation is.

![plane]({{ site.url }}/assets/transcritical/log-lin.png "comparison")

We have yet to discuss pitchfork bifurcations. It was my intention for that to be the topic of my next post. However, I recently started a new job working on the [autonomous car](http://media.gm.com/media/us/en/gm/news.detail.html/content/Pages/news/us/en/2016/mar/0311-cruise.html) at [GM](http://www.gm.com/index.html). Because of this, my area of focus will be shifting, so I don't know if my current study of nonlinear dynamics will continue nor do I know what the topic of my next post will be. We shall see.