---
layout: post
title: A Tip on Learning Mathematics
comments: true
---
As I have mentioned in a [previous post]({% post_url 2015-05-26-Invervting-constant-line %}), I am reading through Fisher's Complex Analysis during my lunch break at work. I am currently nearing the end of chapter two and reading about isolated singularities and a function's Laurent series.

My first exposure to these topics came while I was [preparing for the GRE mathematics subject test](https://www.quora.com/How-does-one-prepare-for-the-GRE-Mathematics-Subject-test/answers/2928285). Then, I just skimmed over the material with an eye toward simply being able to solve problems I would encounter on the test. I didn't focus very hard on digesting the theory nor try to understand the motivation behind each definition and theorem.

This time however, I have the freedom to spend as much time as necessary on each section. On a couple of occasions, this has allowed me to spend days focusing on a single problem or proof. 

As I mentioned above, I just finished the section on isolated singularities and Laurent series. While I could see *how* to calculate the residue of a function over a domain, for instance I couldn't see *why* you would want to. I also wasn't very comfortable with the definitions introduced in the section. 

This changed when I worked through the proof of the theorem below. I thought this would be a good way to highlight how to work toward understanding mathematics. In what follows, I will provide the relevant definitions as presented in my text and then proceed to prove the theorem stating the equivalence of these definitions to those I have seen in other texts. I take for granted the fact that a function that is analytic on a domain, $D$ has a power series expansion valid on $D$. 

## Isolated Singularities
An analytic function $f$ has an **isolated singularity** at a point $z_0$ if $f$ is analytic in the punctured disc $0 \lt \left\|z-z_0\right\| \lt r$, for some $r \gt 0$.  There are three possibilities for the behavior of $\left\|f\right\|$ when $0 \lt \left\|z-z_0\right\| \lt r$,

$$
\begin{equation}
\left\|f(z)\right\| \text{remains bounded as} z \rightarrow z_0.
\end{equation}
$$

$$
\begin{equation}
\lim_{z \rightarrow z_0} \left\|f(z)\right\| = \infty
\end{equation}
$$


\begin{equation}
\text{Neither 1 nor 2 holds.}
\end{equation}
$$


If the first case holds, define

$$
g(z) =
 \begin{cases}
\left( z - z_0\right)^2f(z),  & \text{if  $z \neq z_0$} \\
0, & \text{if $z=z_0$}
\end{cases}
$$

Then, $g$ is analytic and $g(z_0) = 0$ furthermore it is differentiable at $z_0$ and $g'\left(z_0\right)=0$ since

$$\begin{align*}
g'\left(z_0\right) &= \lim_{z \rightarrow z_0}\frac{g(z) - g\left(z_0\right)}{z-z_0}\\
&= \lim_{z \rightarrow z_0} \left(z-z_0\right)f(z)\\
&= 0
\end{align*}
$$

The final equality holds because $\left\|f(z)\right\|$$ is bounded as $z \rightarrow z_0$. Because of this and the fact that $g$ is analytic we know it has a power series valid in $D$ of the form

$$\begin{align*}
g(z) &= \frac{g''\left(z_0\right)}{2}\left(z-z_0\right)^2 +  \frac{g'''\left(z_0\right)}{3!} \left(z-z_0\right)^3+\cdots\\
&=b_2\left(z-z_0\right)^2 + b_3\left(z-z_0\right)^3 + \cdots
\end{align*}
$$

Set $$f\left(z_0\right) = b_2$$, then the power series expansion for $g$ can also work for $f$ after dividing out the $$\left(z-z_0\right)^2$$ term. Thus we have shown that under the condition (1) we can extend $f$ to be analytic on the disc $$\left\|z-z_0\right\| \lt r$$. In this case, we say $f$ has a **removable singularity** at $z_0$.

If the behavior of $$\left\|f\right\|$$ as $z \rightarrow z_0$ is as in (2), there is no harm in assuming $r$ is so small that $$\left\|f\right\| \gt 1$$ for $$\left\|z-z_0\right\| \lt r$$. Now define

$$
g(z) = \frac{1}{f}
$$ 

Then clearly $g$ is analytic in $$0\lt \left\|z-z_0\right\| \lt r$$. But since $$\left\|g\right\|$$ is bounded in that region ($$\left\|g\right\| \lt 1$$), then by (1) $g$ can be extended to be analytic in the disc $$\left\|z-z_0\right\| < r$$. Further, $g\left(z_0\right) = 0$ since (2) holds. 

We digress for a moment for a definition and a comment. 
 
> If a function $f$ is analytic on a domain $D$ and such that $f^{(k)} = 0$ for $k = 0, \ldots, m-1$, but $f^m\left(z_0\right) \neq 0$, then we say that **$f$ has a zero of order $m$ at $z_0$**.

A useful result we will simply state here is the following: 

 >*If $f$ has a zero of order $m$ at $z_0$, then $f(z) = \left(z-z_0\right)^mg(z)$, where $g$ is analytic in $D$ and $g\left(z_0\right) \neq 0$.*

Let $m$ be the order of the zero of $g$ at $z_0$. Write

$$
g(z) = \left(z-z_0\right)^mh(z)
$$

where $h$ is analytic in $$\left\|z-z_0\right\| \lt r$$ and $h\left(z_0\right) \neq 0$. Finally,  we know that $H(z) = \frac{1}{h}$ is analytic in $$\left\|z-z_0\right\| \lt r$$ and $H\left(z_0\right) \neq 0$ so that

$$
\begin{equation}
f = \frac{1}{g} = \frac{1}{\left(z-z_0\right)^mh(z)} = \frac{H(z)}{\left(z-z_0\right)^m}
\end{equation}
$$

Then as $z \rightarrow z_0$, $f \rightarrow \infty$ as a power of $\frac{1}{z}$. In this case, we say a function $f$ has a **pole of order $m$**. That is, if the function $\frac{1}{f}$ has a zero of order $m$ at $z_0$, then $f$ has a pole of order $m$.

If neither (1) nor (2) hold, then $f$ has an **essential singularity** at $z_0$.

## Laurent Series
If $f$ is analytic over the domain $\left\|z-z_0\right\| < r$, then we know it has a power series expansion valid over that domain. If, however it is only analytic over the punctured disc $0 < \left\|z-z_0\right\| < r$ or worse yet, the annulus $0 \le r \lt \left\|z-z_0\right\| \lt R$, there is still a series representation that is nearly as nice. First we need another result:

>Proposition: If $F$ is analytic in $\left\|z-z_0\right\| \gt R$, then it has a "power series" valid in that domain of the form
>$$
F(z) = \sum_0^\infty{c_k\left(\frac{1}{z}\right)^k}
$$

To see this, note that $G(z) = F\left(\frac{1}{z}\right)$ is analytic in $$\left\|z-z_0\right\| \lt \frac{1}{R}$$. Hence $G$ has a power series valid in that region

$$
G(z) = \sum_0^\infty{c_kz^k}
$$

Make the substitution $z = \frac{1}{w}$. Then we have

$$
F(w) = G(z)  = \sum_0^\infty{c_kz^k = \sum_0^\infty{c_k\left(\frac{1}{w}\right)^k}}
$$

And if 

$$
c_k =  \frac{1}{2\pi i }\int_{\left\|\varepsilon\right\|=r} \frac{G(\varepsilon)}{\varepsilon^{k+1}}\,d\varepsilon
$$

we can make the substitution

$$\begin{align}
\varepsilon &= \frac{1}{\zeta}\\
d\varepsilon &= \frac{-1}{\zeta^2}d\zeta
\end{align}
$$

We are integrating over the circle $$\left\|\zeta\right\|=s=\frac{1}{r}>R$$, so if $-\zeta$ is on the circle so is $\zeta$. Then

$$\begin{align}
c_k &=  \frac{1}{2\pi i }\int_{\left\|\varepsilon\right\|=r} \frac{G(\varepsilon)}{\varepsilon^{k+1}}\,d\varepsilon\\
&= \frac{1}{2\pi i }\int_{\left\|\zeta\right\|=s}F\left(\zeta\right)\zeta^{k-1}\,d\zeta
\end{align}
$$

are the coefficients of this series in terms of values of $F$.

So we can write any function, $f$ that is analytic on the annulus  $$0 \le r \lt \left\|z-z_0\right\| \lt R$$ as a combination of a power series valid on the disc $$\left\|z-z_0\right\| \lt R$$ and the "power series" just developed over $$\left\|z-z_0\right\| \gt r$$. So that

$$\begin{align}
f(z) &= f_1(z) + f_2(z)\\
&= \sum_0^\infty{a_k\left(z-z_0\right)^k} + \sum_0^\infty{b_k\frac{1}{\left(z-z_0\right)^k}}\\
&= \sum_{-\infty}^\infty{c_k\left(z-z_0\right)^k}
\end{align}
$$

where $c_k = a_k$, $k \ge 0$ and $c_{-k} = b_k$, $k=1,2,3,\ldots$

In applications, we often care about a function with a pole of order $m$. We start with equation (1) above

$$
f(z) = \frac{H(z)}{\left(z-z_0\right)^m}
$$

Since $H$ is analytic in $$\left\|z-z_0\right\| \lt r$$, it has a power series expansion.

$$
H(z) = \sum_{k=0}^{\infty}c_k\left(z-z_0\right)^k
$$

Performing the division yields:

$$
f(z) = \frac{c_0}{\left(z-z_0\right)^m} + \cdots +  \frac{c_{m-1}}{z-z_0} +  c_m + c_{m+1}\left(z-z_0\right) + \cdots
$$

Valid over the punctured disc $$0 \lt \left\|z-z_0\right\| \lt r$$.

## Gaining Understanding
As I read the above definitions, for whatever reason their meaning and motivation alluded me. This was until I worked through the following mini-theorem.

>**Theorem** Let $f $ be analytic in $$0 \lt \left\|z - z_0 \right\| \lt r$$, and let
>
>$$
f(z) = \sum_{n= - \infty}^{\infty} a_n\left(z-z_0\right)^n
$$
>
>be its Laurent series. Show that
>
>* $z_0 $ is a removable singularity for $f$ if and only if $a_n = 0 $ for $n=0,1,\ldots$.
* $z_0 $ is a pole of order $m \geq 1 $ for $f$ if and only if $a_{-m} \neq 0 $ but $a_{-n} = 0$ for all $n \geq m+1$.
* $z_0 $ is an essential singularity for $f$ if and only if there are infinitely many $a_{-n}$, $n \gt 0$, that are *not* zero. 

Indeed, I have seen the above statements about the Laurent series of $f$ as the definition of removable singularities, poles, and essential singularities from sources such as [here](http://mathfaculty.fullerton.edu/mathews/c2003/SingularityZeroPoleMod.html). We now prove the theorem.

**Proof**

* For the first part, if $z_0$ is a removable singularity that $f$ can be extended to be analytic throughout $$\left\|z-z_0\right\| \lt r$$. So it has a power series valid in that region

	$$
f(z) = \sum_{n=0}^{\infty} a_n \left(z-z_0\right)^n
$$
	So the conclusion follows.
	If $a_n = 0$ for $n\lt 0$, then the Laurent series for $f$ can be written
	
	$$
	f(z) = \sum_{n=0}^{\infty} a_n \left(z-z_0\right)^n
$$

	So $f$ has a power series expansion and is therefore analytic. 
* For the second part, if $z_0$ is a pole of order $m$ then
	
	$$
	f(z) = \frac{H(z)}{\left(z-z_0\right)^m}
$$

	where $H$ is analytic in $\left\|z-z_0\right\| \lt r$ and $H(z_0) \neq 0$. $H(z)$ has a power series expansion
	
	$$
	H(z) = \sum_{n=0}^{\infty}a_n\left(z-z_0\right)^n
	$$
	
	Dividing this series by $\left(z-z_0\right)^m$ yields the result.
	Now if $a_{-n}=0$ for all $n\geq m+1$ then
	
	$$
	f(z) = \frac{a_{-m}}{\left(z-z_0\right)^m} + \frac{a_{-m+1}}{\left(z-z_0\right)^{m-1}} + \cdots + a_0 + a_1z + \cdots
	$$
	
	and 
	
	$$
	g(z) = \left(z-z_0\right)^mf(z)
	$$
	
	is analytic in $\left\|z-z_0\right\| \lt r$ and $g(z_0) \neq 0$.
	Then we can write
	
	$$
	f(z) = \frac{g(z)}{\left(z-z_0\right)^m}
	$$
	
	Thus $f$ has a pole of order $m$.


	$$
	f(z) = \sum_{n=0}^{\infty} a_n \left(z-z_0\right)^n
	$$
	
	(if there are no $a_{-n} \neq 0$) in which case we know by the first part of this theorem that $f$ has a removable singularity at $z_0$. The other scenario is that we can write
	
	$$
	f(z) = \frac{a_{-m}}{\left(z-z_0\right)^m} + \frac{a_{-m+1}}{\left(z-z_0\right)^{m-1}} + \cdots + a_0 + a_1z + \cdots
	$$  
	
where $a_{-m} \neq 0$ for some fixed $m >0$. But then by the second part of the theorem, $f$ has a pole of order $m$. In either case, $z_0$ is not an essential singularity.

* For the reverse implication, if $z_0$ is not an essential singularity then it is either a removable singularity or $f$ has a pole of order $m$ at $z_0$. In either case, there are not infinitely many $a_{-n}$, $n \gt0$ not zero by the first two parts of this theorem.
	
	For the forward implication, if there are infinitely many $a_{-n}$, $n \gt0$ that are zero, then the hypothesis of neither of the previous two parts of this theorem are satisfied. Thus $f$ does not have a pole of order $m$ nor does it have a removable singularity. Therefore, it must have an essential singularity at $z_0$. $\Box$


Proving a theorem like this requires a lot of moving back and forth between the definitions. In the example above, for each proof, you are forced to look at the definition of the type of singularity and what you can say either about the function's power series or Laurent series. While the proofs in and of themselves are simple, they provide a doorway to more difficult tackling more difficult problems. When you get stuck in your own reading, working through a proof like this may be all it takes for you to be able to catch the subtleties of the material and thus attain a deeper understanding.