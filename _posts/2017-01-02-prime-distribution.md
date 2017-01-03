---
layout: post
title: A Brief Look at the Distribution of the Primes
comments: true
---

With the holiday break at hand, I wanted to read up on something different from my typical day-to-day areas of concentration. I decided to read a little about prime numbers, because who wouldn't want to spend some of their vacation time studying primes? 

Here we will look at some of the work [P.L. Chebyshev](https://en.wikipedia.org/wiki/Pafnuty_Chebyshev) produced related to the distribution of the primes within the natural numbers.

We denote by $\pi (x)$, the number of primes less than or equal to $x$. For example $\pi(10) = 4$ and $\pi(\pi) = 2$.  The question, what is the law of growth of $\pi(x)$? That is, is there some well known function that approximates the size of $\pi(x)$?

It was [Legendre](https://en.wikipedia.org/wiki/Adrien-Marie_Legendre) who first proposed the following function as such a law of growth of the prime numbers 

$$
\frac{x}{\ln x - A}
$$

where $A=1.08\ldots$. He did not prove the proposition. Gauss later came along and proposed that the distribution of primes differs little from the function

$$
\int_2^x\frac{dt}{\ln t}
$$

Actually, these two results are "the same" in the sense that 

$$\begin{equation}
\lim_{x \to \infty}\frac{\int_2^x\frac{dt}{\ln t}}{\frac{x}{\ln x}} = 1.
\end{equation}
$$

As we can see by integrating the numerator by parts

$$\begin{align*}
\int_2^x\frac{dt}{\ln t} &= \frac{t}{\ln t} |_2^x + \int_2^x\frac{dt}{(\ln t)^2}\\
&= \frac{x}{\ln x} - \frac{2}{\ln 2} + \int_2^x\frac{dt}{(\ln t)^2}
\end{align*}
$$

and then for the final integral, we make the following comparisons

$$
\begin{equation}
\int_2^x\frac{dt}{(\ln t)^2} > \int_2^x\frac{dt}{t(\ln t)^2} = -\frac{1}{\ln x} +\frac{1}{\ln 2}
\end{equation}
$$

and 

$$
\begin{equation}
\int_2^x\frac{dt}{(\ln t)^2} < \int_2^x\frac{dt}{(\ln t)^{\frac{3}{2}}} = \frac{2}{5} \left(\frac{x}{(\ln x)^{\frac{3}{2}}} - \frac{2}{(\ln 2)^{\frac{3}{2}}}\right)
\end{equation}
$$

Then (1) becomes

$$\begin{align*}
\lim_{x \to \infty}\frac{\int_2^x\frac{dt}{\ln t}}{\frac{x}{\ln x}} &= \lim_{x \to \infty}\frac{\frac{x}{\ln x} - \frac{2}{\ln 2} + \int_2^x\frac{dt}{(\ln t)^2}}{\frac{x}{\ln x}}\\
&= 1 + \lim_{x \to \infty}\frac{\int_2^x\frac{dt}{(\ln t)^2}}{\frac{x}{\ln x}}
\end{align*}
$$

Using (2) and (3) we get the following estimates for the last limit above

$$\begin{align*}
\lim_{x \to \infty}\frac{\int_2^x\frac{dt}{(\ln t)^2}}{\frac{x}{\ln x}} &\ge \lim_{x \to \infty} \frac{-\frac{1}{\ln x} +\frac{1}{\ln 2}}{\frac{x}{\ln x}}\\
&= \lim_{x \to \infty}-\frac{1}{x} + \frac{1}{x\ln 2}\\
&=0
\end{align*}
$$

and 

$$\begin{align*}
\lim_{x \to \infty}\frac{\int_2^x\frac{dt}{(\ln t)^2}}{\frac{x}{\ln x}}
&\le \lim_{x \to \infty} \frac{\frac{2}{5} \left(\frac{x}{(\ln x)^{\frac{3}{2}}} - \frac{2}{(\ln 2)^{\frac{3}{2}}}\right)}{\frac{x}{\ln x}}\\
&=\frac{2}{5} \lim_{x \to \infty}\frac{1}{\sqrt{\ln x}}\\
&=0
\end{align*}
$$

So that (1) is established.

### Chebyshev's Method ###

This is a simplified version of the method Chebyshev used for computing the number of primes in a given interval. As such, our results will not be as precise as his. Here is the first problem statement

>Let $p$ be a prime, and $n$ a natural number. What is the largest power $a$ of the prime $p$ that divides $n! = 1\cdot2\cdot3 \cdots \cdot n$ with no remainder?

We use the notation $[x]$ to mean the largest integer *less than* $x$. E.g. $[2.1] = 2,$ $[e] = 2,$ and $[-1.5] = -2.$ 

Among the numbers, $1, 2, 3, \ldots,n$, there will be $[\frac{n}{p}]$ that are divisible by $p$, $[\frac{n}{p^2}]$ of these will be divisible by $p^2$, $[\frac{n}{p^3}]$ of these will be divisible by $p^3$, etc. Hence, since each of the numbers $1, \ldots, n$ are in the product $n!$ the number $a$ must be

$$
a = \left[\frac{n}{p}\right] + \left[\frac{n}{p^2}\right] + \left[\frac{n}{p^3}\right] + \cdots
$$

where the sum eventually terminates because $n$ and $p^m$ are both positive and so their quotient (and thus the integral part) can't be less than zero. 

Based on the answer to the above question, and the [Fundamental Theorem of Arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic), it follows that the number $n!$ will be the product of primes with powers of the form

$$
p^{\left[\frac{n}{p}\right] + \left[\frac{n}{p^2}\right] + \left[\frac{n}{p^3}\right] + \cdots}
$$

over all primes $p \le n$. Thus the log of this product will turn into the sum of the logarithms of these powers

$$
\begin{equation}
\ln n! = \sum_{p \le n} \left( \left[\frac{n}{p}\right] + \left[\frac{n}{p^2}\right] + \left[\frac{n}{p^3}\right] + \cdots\right) \ln p
\end{equation}
$$

In what follows, we will make use of the following string of inequalities which follows from the fact that $y= \ln x$ is an increasing function

$$
\ln m! = \ln m \int_m^{m+1} \,dx \lt \int_m^{m+1} \ln x \,dx \lt \ln(m+1) \int_m^{m+1}\,dx = \ln(m+1)
$$

Thus

$$
\begin{align*}
\ln n! &= \ln 1 + \ln 2 + \cdots + \ln n! \\
&\lt \int_1^2 \ln x \,dx + \int_2^3 \ln x \,dx + \cdots + \int_{n-1}^n \ln x \,dx + \ln n \\
&= \int_1^n \ln x \,dx + \ln n
\end{align*}
$$

and similarly


$$
\begin{align*}
\ln n! &= \ln 1 + \ln 2 + \cdots + \ln n! \\
&\gt \ln 1 + \int_1^2 \ln x \,dx + \cdots\ + \int_{n-2}^{n-1} \ln x \,dx + \int_{n-1}^n \ln x \,dx \\
&= \int_1^n \ln x \,dx
\end{align*}
$$

The last integral in both equations can be evaluated by parts

$$
\int_1^n \ln x \,dx = n\ln n - \int_1^n\,dx = n \ln n - n + 1
$$
Then based on the two inequalities immediately preceding we have the following estimates

$$
n\ln n -n + 1 \lt \ln n! \lt n\ln n - n +1 + \ln n
$$

So that we can write

$$
\begin{equation}
\ln n! = n\ln n + O(n)
\end{equation}
$$

Note that  $\ln n = O(n)$ because for any positive power $\alpha$

$$
\begin{equation}
\lim_{n \to \infty} \frac{\ln n}{n^{\alpha}} = 0.
\end{equation}
$$

We want a way to rewrite (4). So we further observe that

$$
\begin{align*}
\sum_{ p \le n} \left( \left[\frac{n}{p^2}\right] + \left[\frac{n}{p^3}\right] + \cdots \right) \ln p &\le \sum_{ p \le n} \left( \frac{n}{p^2}+ \frac{n}{p^3} + \cdots \right) \ln p\\
& = \sum_{ p \le n} \frac{n \ln p}{p^2\left(1 - \frac{1}{p}\right)} \\
& \lt 2n \sum_{ p \le n} \frac{\ln p}{p^2} \\
& \lt \sum_{m=1}^\infty \frac{\ln m}{m^2} \\
& = 2n C_0\\
&= O(n)
\end{align*}
$$

where we used the fact that $1 + \frac{1}{p} + \frac{1}{p^2} + \cdots$ is a geometric series and $C_0$ is the sum of the convergent series  $\sum_{m=1}^\infty \frac{\ln m}{m^2}.$ This result, paired with the (5) gives

$$
\begin{equation}
\sum_{p \le n} \left[\frac{n}{p}\right] \ln p = n \ln n +O(n)
\end{equation}
$$

Next, we consider the function introduced by Chebyshev

$$
\begin{equation}
\Theta(n) = \sum_{p \le n} \ln p
\end{equation}
$$

That is the logarithm of the product of primes less than or equal to $n$. With this notation, equation (7) can be rewritten as 

$$
\begin{equation}
\Theta\left(\frac{n}{1}\right) + \Theta\left(\frac{n}{2}\right) + \Theta\left(\frac{n}{3}\right) + \cdots =n \ln n + O(n)
\end{equation}
$$

Each $\ln p$ enters into the sums $\Theta \left(\frac{n}{s}\right)$ when $p \le \frac{n}{s}$ and there are $\left[\frac{n}{p}\right]$ such sums. I suggest trying it for yourself with a small $n$ (say $n=6$) if you still need convincing.

This last equation is also valid for non-integers, $n$. It is sufficient to show that the equation is true for any $x$ in the interval $n \lt x \lt n+1$. It is obvious that the left side is unchanged by replacing $n$ by $x$ since the number of primes less than $x$ can only increase if $n$ is incremented by 1. (Obviously, the left side does not decrease.)To see that the right side is unchanged, recall the increment of a function 

$$
f(x) - f(a) = (x-a)f'(c) \qquad a \lt c \lt x
$$

then we have 

$$
\begin{align*}
x \ln x - n\ln n &= (x - n)(\ln c + 1 ) \quad n \lt c \lt x\\
&\lt \ln(n+1) +1\\
&= O(n) \qquad (\text{since } 0 \lt x-n \lt 1)
\end{align*}
$$

Since (8) holds for non-integers, we can subtract from it twice the equation derived from replacing $n$ by $\frac{n}{2}$.

$$
\begin{align*}
\Theta\left(\frac{n}{1}\right) &+ \Theta\left(\frac{n}{2}\right) + \Theta\left(\frac{n}{3}\right) + \cdots = n \ln n + O(n)\\
- \qquad &2\left( \Theta\left(\frac{n}{2}\right) + \Theta\left(\frac{n}{4}\right) + \Theta\left(\frac{n}{6}\right) + \cdots\right) = 2\frac{n}{2} \ln \frac{n}{2} + O(n)
\end{align*}
$$ 

Giving us

$$
\Theta\left(\frac{n}{1}\right) - \Theta\left(\frac{n}{2}\right) + \Theta\left(\frac{n}{3}\right) - \Theta\left(\frac{n}{4}\right) + \cdots = n \ln 2 + O(n) < C_1n
$$

where $C_1 > 0$ is constant. From this and the fact that the first two terms can't be bigger than the entire rest of the sum (since each of the $\Theta\left(\frac{n}{b}\right) - \Theta\left(\frac{n}{b+1}\right)$ are positive) it follows that 

$$
\Theta\left(\frac{n}{1}\right) - \Theta\left(\frac{n}{2}\right) \lt C_1n
$$

Similarly

$$
\begin{align*}
\Theta\left(\frac{n}{2}\right) - \Theta\left(\frac{n}{4}\right) &\lt C_1\frac{n}{2}\\
\Theta\left(\frac{n}{4}\right) - \Theta\left(\frac{n}{8}\right) &\lt C_1\frac{n}{4}\\
&\vdots
\end{align*}
$$

so that 

$$
\Theta(n) \lt C_1\left(n + \frac{n}{2} + \frac{n}{4} + \cdots \right) = 2C_1n
$$

Then 

$$
0 \lt \sum_{p \le n} \frac{n}{p} \ln p - \sum_{p \le n} \left[\frac{n}{p}\right] \ln p \le \sum_{p \le n} \ln p = \Theta (n) \le 2C_1n = O(n)
$$

and with (7) we get 

$$
\sum_{p \le n} \frac{n}{p}\ln p = n \ln n + O(n)
$$

$$
\begin{equation}
\sum_{p \le n} \frac{\ln p}{p} = \ln n + \theta C
\end{equation}
$$

where $C>0$ is a constant and $\theta$ depends on $n$ such that $\|\theta \| \le 1.$

Now we come to the point of the post. *For a given constant $M$, we will establish inequalities for the number of primes, $T$ in the interval  $[n,Mn].$* We first note that 

$$
\sum_{n \le p \le Mn} \frac{\ln p}{p} = \sum_{p \le Mn} \frac{\ln p}{p} - \sum_{p \le n} \frac{\ln p}{p}
$$

Replacing $n$ with $Mn$ in (9), we get

$$
\sum_{p \le Mn} \frac{\ln p}{p} = \ln (Mn) + \theta' C = \ln M + \ln n + \theta ' C
$$

where $\theta'$ is defined analogously to $\theta$ in (9). This equation with the two preceding it gives

$$
\sum_{n \le p \le Mn} \frac{\ln p}{p} = \ln M + \theta 'C - \theta C = \ln M + 2\theta_0C
$$

where $\|\theta_0\| \le 1$. So the following inequality holds

$$
\ln M - 2C \le \sum_{n \le p \le Mn} \frac{\ln p}{p} \le \ln M + 2C
$$

On the other hand, since $y=\frac{\ln x}{x}$ is a decreasing function of $x$ for $x>e$, it follows that for $n\ge 3$ 

$$
T \frac{\ln (Mn)}{Mn} \le \sum_{n \le p \le Mn} \frac{\ln p}{p} \le T \frac{\ln n}{n}
$$

and thus 

$$
\begin{equation}
T \frac{\ln n}{n} \gt \ln M - 2C
\end{equation}
$$ 

 and 
 
$$
\begin{equation}
T \frac{\ln (Mn)}{Mn} \gt \ln M + 2C.
\end{equation}
$$ 

All that is left is to choose $M$ such that the right side of (11) is equal to 1

$$
\begin{align*}
\ln M &-2C = 1\\
M &= e^{2C + 1}
\end{align*}
$$

and set 

$$
L = M(\ln M + 2C).
$$

Then for the number of primes, $T$ lying between $n$ and $Mn$, we get 

$$
\begin{equation}
\frac{n}{\ln n} < T < L\frac{n}{\ln n}
\end{equation}
$$

which is what we set out to show in this quick look at the distribution of the prime numbers. Much more has been studied related to the primes, but this was just some Christmas break fun. Happy New Year.