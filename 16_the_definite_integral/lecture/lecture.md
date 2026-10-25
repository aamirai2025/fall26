# Calculus and Analytical Geometry

## The Definite Integral

### Dr. Aamir Alaud Din

# Objectives

After preparing this topic you must be able to
1. Define the definite integral as a limit of Riemann sums, interpret it as signed (net) area, understand the precise meaning and notation of the integral, and use right-endpoint sums to express limits as definite integrals.
2. Evaluate definite integrals by expressing them as limits of Riemann sums, applying formulas for sums of powers and properties of sums, and interpreting definite integrals geometrically as signed areas.
3. Use the Midpoint Rule to approximate definite integrals by partitioning an interval into equal subintervals, evaluating the integrand at each subinterval's midpoint, and interpreting the resulting approximation geometrically and numerically.
4. Apply the fundamental properties of definite integrals—including reversing or equating limits, linearity, additivity over adjacent intervals, and comparison bounds—to simplify and evaluate definite integrals and estimate their values.

# The Why Section

A definite integral provides a systematic way to accumulate a continuously varying quantity over an interval. In mechanical engineering, it can be used to estimate the net displacement of a moving component from its velocity, the work done by a variable force, or the accumulated effect of a changing load. In computer science and mechatronics, sensor measurements may vary continuously over time, and an integral can estimate the total accumulated signal or motion from those changing measurements.

For example, suppose a mechatronic positioning system records the velocity of a moving platform as a function of time. The velocity may be positive during forward motion and negative during reverse motion. Adding the signed contributions over a time interval gives the platform's net displacement. To understand how this accumulation is represented mathematically and how it can be calculated from increasingly fine subdivisions, we study the definite integral and Riemann sums.

A definite integral allows us to combine many small contributions into a single total quantity. In mechanical engineering, these contributions may represent small amounts of work along a displacement, the effect of a varying force, or the accumulated response of a system. In computer science and data science, the same mathematical idea appears when accumulating a continuously varying quantity or approximating a total from many small intervals.

For example, imagine a mechatronic actuator whose force varies with its position. The total work performed while the actuator moves from one position to another depends on the force throughout the motion, not just on its force at the starting or ending point. We can divide the interval into small pieces, approximate the work on each piece, add the contributions, and then take a limit as the pieces become increasingly narrow. The definite integral formalizes this process. In this lecture, we will learn how to evaluate definite integrals from their Riemann-sum definition and how to interpret their values geometrically.

A definite integral can represent an accumulated quantity, such as distance travelled, energy consumed, fluid volume, or the total effect of a changing force. In practical problems, an exact antiderivative may be difficult to find, or the available information may consist only of measurements taken at selected points. Numerical integration provides a way to estimate the accumulated quantity from a finite number of function values.

The Midpoint Rule is a numerical integration method that approximates the area over each subinterval by using a rectangle whose height is the function value at the midpoint of that subinterval. Compared with using only the left or right endpoint, a midpoint sample can provide a better approximation for many functions. The quality of an approximation still depends on the behavior of the function and the number of subintervals.

**Mechatronics scenario.** Imagine a mobile robot whose speed changes as it moves along a factory floor. Its controller records speed at the midpoint of each short time interval. By multiplying each midpoint speed by the corresponding time interval and adding the results, the controller can estimate the total distance travelled. Studying the Midpoint Rule gives us the numerical method needed to make this estimate.

A definite integral can represent accumulated change or the signed area between a graph and the horizontal axis. In engineering and computing, such quantities arise when estimating total displacement from a velocity profile, calculating accumulated energy, or adding a signal's contribution over successive time intervals. Once an integral has been defined, its properties let us combine simpler integrals, reverse an interval when necessary, and obtain useful bounds without evaluating every integral from first principles.

Consider a mechatronic actuator whose sensor records a time-dependent signal $f(t)$. The total signed contribution over a time interval can be represented by a definite integral. If the interval is divided into adjacent parts, we should be able to combine the contributions from those parts; if the signal is bounded above and below, we should also be able to estimate the total contribution. These are exactly the kinds of questions that can be handled by studying the properties of the definite integral.

# The Definite Integral

## From the Area Problem to a Limit

In the area problem, we approximated the area under a curve by dividing the interval into many small subintervals and adding the areas of the corresponding rectangles. As the number of subintervals increases, their widths become smaller and the rectangular approximation can approach the exact area.

For a function $f$ on $[a,b]$, divide the interval into $n$ equal subintervals. Each subinterval has width

$$
\Delta x=\frac{b-a}{n}
$$

Choose a sample point $x_i^*$ from the $i$th subinterval. The height of the corresponding rectangle is $f(x_i^*)$, so its signed contribution is $f(x_i^*)\Delta x$. Adding all the contributions gives the Riemann sum

$$
\sum_{i=1}^{n} f(x_i^*)\Delta x
$$

As $n$ increases and the widths of the subintervals approach zero, this sum approaches the definite integral, provided the function is integrable:

$$
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x
$$

The same limiting process can be used when some of the graph lies below the $x$-axis. In that case, the contributions below the axis are negative, so the integral represents signed or net area rather than the total geometric area.

## Definition: The Definite Integral {.blue}

If $f$ is defined on the interval $[a,b]$, divide the interval into $n$ equal subintervals, each of width

$$
\Delta x=\frac{b-a}{n}
$$

Let the endpoints be $x_0=a,x_1,\ldots,x_n=b$, and choose a sample point $x_i^*$ in each subinterval $[x_{i-1},x_i]$. The **definite integral** of $f$ from $a$ to $b$ is defined by

$$
\int_a^b f(x)\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x
$$

provided this limit exists and has the same value for every allowable choice of sample points. If the limit exists, $f$ is said to be integrable on $[a,b]$.

<div class="definition-end">$\blacksquare$</div>

## The Precise Meaning of the Limit

The statement

$$
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x
=
\int_a^b f(x)\,dx
$$

means that the Riemann sums can be made as close as desired to the definite integral by choosing a sufficiently large number of subintervals. More precisely, for every $\epsilon>0$, there is an integer $N$ such that

$$
\left|\int_a^b f(x)\,dx-\sum_{i=1}^{n}f(x_i^*)\Delta x\right|<\epsilon
$$

whenever $n>N$ and the sample points are chosen in their respective subintervals.

Here, $\epsilon$ is any prescribed positive error tolerance. The condition says that once the partition is sufficiently fine, every permitted Riemann sum is within $\epsilon$ of the integral. The same value must be approached regardless of the sample points selected.

## Notes on Integral Notation

**Note 1: The integral sign and terminology.** The symbol $\int$ is an elongated letter $S$, chosen to recall a limit of sums. In $\int_a^b f(x)\,dx$, the expression $f(x)$ is the **integrand**, $a$ is the **lower limit of integration**, and $b$ is the **upper limit of integration**. The symbol $dx$ indicates the variable of integration; in this definition it corresponds to the small widths $\Delta x$. The process of calculating an integral is called **integration**.

**Note 2: The value does not depend on the variable's name.** A definite integral is a number, so the integration variable can be renamed without changing its value:

$$
\int_a^b f(x)\,dx
=
\int_a^b f(t)\,dt
=
\int_a^b f(r)\,dr
$$

**Note 3: The Riemann sum.** The sum

$$
\sum_{i=1}^{n}f(x_i^*)\Delta x
$$

is called a **Riemann sum**, named after the mathematician Bernhard Riemann. It approximates the definite integral and can be interpreted geometrically through the signed areas of rectangles.

## Riemann Sums and Area Under a Curve

When $f(x)\geq 0$ on $[a,b]$, each rectangle's contribution is nonnegative. The Riemann sum adds the areas of the rectangles, and in the limit the definite integral gives the area under the curve from $a$ to $b.

Location of Figure 1. Riemann rectangles approximating the area under a nonnegative curve; the Riemann sum is the sum of the rectangle areas.

Location of Figure 2. The region under the curve $y=f(x)$ from $a$ to $b$, representing the definite integral when $f(x)\geq 0$.

The figures illustrate the transition from a rectangular approximation to the exact area. As the widths shrink, the Riemann sum approaches the area beneath the curve.

## Definite Integrals as Net Area

A function need not be positive throughout the interval. If the graph lies below the $x$-axis, the corresponding function values are negative, so the associated terms $f(x_i^*)\Delta x$ are negative. The Riemann sum therefore adds areas above the axis and subtracts areas below it.

Location of Figure 3. Riemann rectangles for a function that crosses the $x$-axis, with contributions above the axis positive and contributions below the axis negative.

Location of Figure 4. The signed or net area between the curve and the $x$-axis, showing positive and negative regions.

Let $A_1$ denote the geometric area above the $x$-axis and below the curve, and let $A_2$ denote the geometric area below the $x$-axis and above the curve. Then the definite integral is the **net area**:

$$
\int_a^b f(x)\,dx=A_1-A_2
$$

Thus, a definite integral is not always the total geometric area. If the graph lies entirely above the axis, the integral is the area; if some of the graph lies below the axis, those regions contribute negatively.

## Example 1 {.green}

Evaluate the Riemann sum for $f(x)=x^3-6x$ on $[0,3]$, using $n=6$ equal subintervals and right endpoints.

## Solution {.green}

The interval is $[0,3]$ and the number of subintervals is $n=6$. Therefore, the width of each subinterval is

$$
\Delta x=\frac{3-0}{6}=\frac12
$$

Using right endpoints, the sample points are

$$
x_1=0.5,\quad x_2=1,\quad x_3=1.5,\quad x_4=2,\quad x_5=2.5,\quad x_6=3
$$

The Riemann sum is

$$
R_6=\sum_{i=1}^{6}f(x_i)\Delta x
$$

Substitute $f(x)=x^3-6x$ and $\Delta x=\frac12$:

$$
R_6=\frac12\left[f(0.5)+f(1)+f(1.5)+f(2)+f(2.5)+f(3)\right]
$$

Evaluate the function at each right endpoint:

$$
\begin{aligned}
f(0.5)&=(0.5)^3-6(0.5)=-2.875\\
f(1)&=1^3-6(1)=-5\\
f(1.5)&=(1.5)^3-6(1.5)=-5.625\\
f(2)&=2^3-6(2)=-4\\
f(2.5)&=(2.5)^3-6(2.5)=0.625\\
f(3)&=3^3-6(3)=9
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
R_6
&=\frac12(-2.875-5-5.625-4+0.625+9)\\
&=-3.9375
\end{aligned}
$$

Location of Figure 5. Graph of $y=x^3-6x$ on $[0,3]$ with six right-endpoint rectangles; rectangles above the $x$-axis contribute positively and those below it negatively.

The result is negative because the total signed contribution from the rectangles below the $x$-axis exceeds the contribution from the rectangle above the axis. The Riemann sum is an approximation using six rectangles; it is not yet the exact definite integral.

<div class="example-end">$\blacksquare$</div>

## Unequal Subintervals and the General Limit

**Note 4: Unequal widths.** Equal-width subdivisions are convenient, but some applications provide data at unequally spaced times or require subdivisions of different sizes. Riemann sums can also be defined for unequal subintervals. If the widths are $\Delta x_1,\Delta x_2,\ldots,\Delta x_n$, the sum is

$$
\sum_{i=1}^{n} f(x_i^*)\Delta x_i
$$

The limiting process requires the largest subinterval width to approach zero. Writing $\max \Delta x_i$ for the largest width, the general definition is

$$
\int_a^b f(x)\,dx
=
\lim_{\max\Delta x_i\to0}
\sum_{i=1}^{n}f(x_i^*)\Delta x_i
$$

This form is useful when the observations or sampling times are not equally spaced. The essential condition is that the widths of all subintervals become arbitrarily small.

## Theorem {.orange}

If $f$ is continuous on $[a,b]$, or if it has only a finite number of jump discontinuities on $[a,b]$, then $f$ is integrable on $[a,b]$. In other words, the definite integral

$$
\int_a^b f(x)\,dx
$$

exists.

<div class="theorem-end">$\blacksquare$</div>

## Theorem: Definite Integral as a Limit of Right-Endpoint Sums {.orange}

If $f$ is integrable on $[a,b]$, then

$$
\int_a^b f(x)\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x
$$

where

$$
\Delta x=\frac{b-a}{n}
\qquad\text{and}\qquad
x_i=a+i\Delta x
$$

Here, $x_i$ is the right endpoint of the $i$th subinterval. This theorem lets us express a limit of sums as a definite integral by identifying the function, the interval, and the subinterval width.

<div class="theorem-end">$\blacksquare$</div>

## Example 2 {.green}

Express the following limit as a definite integral on the interval $[0,\pi]$:

$$
\lim_{n\to\infty}\sum_{i=1}^{n}(x_i^3+x_i\sin x_i)\Delta x
$$

## Solution {.green}

Compare the given limit with the right-endpoint sum formula

$$
\int_a^b f(x)\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x
$$

The expression being evaluated at each sample point is $x_i^3+x_i\sin x_i$. Therefore, the corresponding function is

$$
f(x)=x^3+x\sin x
$$

The interval is $[0,\pi]$, so $a=0$ and $b=\pi$. The subinterval width is $\Delta x=\frac{\pi}{n}$, and the right endpoints are $x_i=0+i\Delta x$.

Applying the theorem gives

$$
\boxed{
\lim_{n\to\infty}\sum_{i=1}^{n}(x_i^3+x_i\sin x_i)\Delta x
=
\int_0^\pi (x^3+x\sin x)\,dx
}
$$

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

A function is divided into $n=8$ equal subintervals on $[2,10]$. Find the width $\Delta x$.

## Answer {.red}

$$
\Delta x=\frac{10-2}{8}=1
$$

<div class="question-end">$\blacksquare$</div>

## Question 2 {.red}

A graph has geometric area $A_1=12$ above the $x$-axis and area $A_2=5$ below the $x$-axis. Find the definite integral over that interval.

## Answer {.red}

The definite integral gives net area:

$$
\int_a^b f(x)\,dx=A_1-A_2=12-5=7
$$

<div class="question-end">$\blacksquare$</div>

# Scenario Problem

## Problem {.green}

A mechatronic cart moves along a straight track. Its velocity, in metres per second, is modeled over the time interval $0\leq t\leq3$ by

$$
v(t)=t-2
$$

The cart initially moves in the negative direction and later moves in the positive direction. Use the interpretation of the definite integral as net area to determine its net displacement over the three-second interval.

## Solution {.green}

The net displacement is the definite integral of velocity over time:

$$
\text{Net displacement}=\int_0^3 v(t)\,dt=\int_0^3(t-2)\,dt
$$

The velocity is negative on $0\leq t<2$ and positive on $2<t\leq3$. Thus, the region below the time axis contributes negatively and the region above it contributes positively.

The geometric area below the axis from $t=0$ to $t=2$ is a triangle with base $2$ and height $2$:

$$
A_1=\frac12(2)(2)=2
$$

The geometric area above the axis from $t=2$ to $t=3$ is a triangle with base $1$ and height $1$:

$$
A_2=\frac12(1)(1)=\frac12
$$

The signed area, and hence the net displacement, is

$$
\int_0^3(t-2)\,dt=-2+\frac12=-\frac32\text{ m}
$$

Therefore, the cart's net displacement is $-1.5$ m. The negative sign indicates that its final position is 1.5 m in the negative direction relative to its initial position.

<div class="example-end">$\blacksquare$</div>

# Evaluating Definite Integrals

## The Definite Integral as a Limit of Sums

Suppose that $f$ is integrable on the interval $[a,b]$. Divide the interval into $n$ equal subintervals, each of width

$$
\Delta x=\frac{b-a}{n}
$$

Using right endpoints, the sample point in the $i$th subinterval is

$$
x_i=a+i\Delta x
$$

The corresponding Riemann sum is

$$
\sum_{i=1}^{n} f(x_i)\Delta x
$$

As $n$ increases, the widths of the subintervals approach zero. The limit of these sums gives the definite integral:

$$
\int_a^b f(x)\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x
$$

where $\Delta x=(b-a)/n$ and $x_i=a+i\Delta x$. This definition is the basis for the calculations in this lecture.

## Sums of Powers

When we use the definition of a definite integral, we often need to simplify a sum involving powers of the integers $1,2,\ldots,n$. The following formulas make it possible to evaluate the sums that arise from polynomial functions.

$$
\sum_{i=1}^{n}1=n
$$

$$
\sum_{i=1}^{n}i=\frac{n(n+1)}{2}
$$

$$
\sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}{6}
$$

$$
\sum_{i=1}^{n}i^3=\left[\frac{n(n+1)}{2}\right]^2
$$

## Properties of Sums

We will also use the following properties to separate sums and take constant factors outside the summation sign.

$$
\sum_{i=1}^{n}ca_i=c\sum_{i=1}^{n}a_i
$$

$$
\sum_{i=1}^{n}(a_i+b_i)=\sum_{i=1}^{n}a_i+\sum_{i=1}^{n}b_i
$$

$$
\sum_{i=1}^{n}(a_i-b_i)=\sum_{i=1}^{n}a_i-\sum_{i=1}^{n}b_i
$$

These formulas allow us to rewrite a Riemann sum as a combination of simpler sums, evaluate each sum, and then calculate the limit.

## Example 3 {.green}

Evaluate $\displaystyle\int_0^3(x^3-6x)\,dx$.

## Solution {.green}

We use the definition of the definite integral. Here, $f(x)=x^3-6x$, $a=0$, and $b=3$. Therefore,

$$
\Delta x=\frac{b-a}{n}=\frac{3}{n}
$$

The right endpoints of the subintervals are

$$
x_i=a+i\Delta x=\frac{3i}{n}
$$

By the definition,

$$
\int_0^3(x^3-6x)\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}
\left[\left(\frac{3i}{n}\right)^3-6\left(\frac{3i}{n}\right)\right]\frac{3}{n}
$$

Simplify the expression inside the summation:

$$
\begin{aligned}
&\left[\left(\frac{3i}{n}\right)^3-6\left(\frac{3i}{n}\right)\right]\frac{3}{n}\\
&=\left(\frac{27i^3}{n^3}-\frac{18i}{n}\right)\frac{3}{n}\\
&=\frac{81i^3}{n^4}-\frac{54i}{n^2}
\end{aligned}
$$

Thus,

$$
\int_0^3(x^3-6x)\,dx
=
\lim_{n\to\infty}
\left[
\frac{81}{n^4}\sum_{i=1}^{n}i^3
-
\frac{54}{n^2}\sum_{i=1}^{n}i
\right]
$$

Apply the formulas for the sums of cubes and integers:

$$
=
\lim_{n\to\infty}
\left[
\frac{81}{n^4}\left(\frac{n(n+1)}{2}\right)^2
-
\frac{54}{n^2}\frac{n(n+1)}{2}
\right]
$$

Simplifying gives

$$
=
\lim_{n\to\infty}
\left[
\frac{81}{4}\left(1+\frac{1}{n}\right)^2
-
27\left(1+\frac{1}{n}\right)
\right]
$$

As $n\to\infty$, we have $1/n\to0$. Therefore,

$$
\begin{aligned}
\int_0^3(x^3-6x)\,dx
&=\frac{81}{4}-27\\
&=-\frac{27}{4}\\
&=-6.75
\end{aligned}
$$

The graph of $y=x^3-6x$ crosses the $x$-axis within the interval. The definite integral is therefore the area above the axis minus the area below it. In Figure 6, the positive area $A_1$ is smaller than the negative-area magnitude $A_2$, so the signed result $A_1-A_2$ is negative.

Location of Figure 6. Graph of $y=x^3-6x$ on $[0,3]$, illustrating the positive area $A_1$ and negative area $A_2$ and the signed integral $A_1-A_2=-6.75$.

<div style="text-align: center;">
<img src="../images/0506.png" style="width: 650px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 6.</strong> The signed area for $\int_0^3(x^3-6x)\,dx$.</span>
</div>

### Riemann-sum approximation using $n=40$

The right Riemann sum for $f(x)=x^3-6x$ on $[0,3]$ is

$$
R_n=\sum_{i=1}^{n}f\left(\frac{3i}{n}\right)\frac{3}{n}
$$

For $n=40$, the interval is divided into 40 narrow subintervals. The rectangles below the $x$-axis contribute negatively, while rectangles above the axis contribute positively. Their signed total approximates the definite integral.

Location of Figure 7. Right-endpoint rectangles for $y=x^3-6x$ on $[0,3]$ with $n=40$ subintervals.

<div style="text-align: center;">
<img src="../images/0507.png" style="width: 650px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 7.</strong> Right Riemann sum with $n=40$ for $y=x^3-6x$ on $[0,3]$.</span>
</div>

The table below shows that the right Riemann sums approach the exact value $-6.75$ as $n$ increases.

| Number of subintervals $n$ | Right Riemann sum $R_n$ |
|---:|---:|
| 40 | -6.3998 |
| 100 | -6.6130 |
| 500 | -6.7229 |
| 1000 | -6.7365 |
| 5000 | -6.7473 |

<div style="text-align: center;">
<span><strong>Table 1.</strong> Effect of the number of subintervals on the right Riemann sum for $\int_0^3(x^3-6x)\,dx$.</span>
</div>

As the number of rectangles increases, the approximation gets closer to $-6.75$. This illustrates the defining limit of the definite integral. Notice that the integral is not the total unsigned area: it is the difference between the area above the $x$-axis and the area below it.

<div class="example-end">$\blacksquare$</div>

## Example 4 {.green}

**(a)** Set up an expression for $\displaystyle\int_1^3 e^x\,dx$ as a limit of sums.

**(b)** Use a computer algebra system to evaluate the expression.

## Solution {.green}

### Part (a)

Here, $f(x)=e^x$, $a=1$, and $b=3$. The width of each subinterval is

$$
\Delta x=\frac{b-a}{n}=\frac{2}{n}
$$

Using right endpoints, the sample points are

$$
x_i=a+i\Delta x=1+\frac{2i}{n}
$$

By the definition of a definite integral,

$$
\int_1^3 e^x\,dx
=
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x
$$

Substitute $f(x)=e^x$, $x_i=1+2i/n$, and $\Delta x=2/n$:

$$
\boxed{
\int_1^3e^x\,dx
=
\lim_{n\to\infty}\frac{2}{n}
\sum_{i=1}^{n}e^{1+2i/n}
}
$$

This is the required expression as a limit of Riemann sums.

### Part (b)

A computer algebra system can simplify the finite geometric sum and evaluate its limit. The resulting exact value is

$$
\int_1^3e^x\,dx=e^3-e
$$

Numerically, this is approximately $17.3673$. The graph of $y=e^x$ is above the $x$-axis on $[1,3]$, so the definite integral is the positive area under the curve between $x=1$ and $x=3$.

Location of Figure 8. The region under $y=e^x$ and above the $x$-axis from $x=1$ to $x=3$.

<div style="text-align: center;">
<img src="../images/0508.png" style="width: 550px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 8.</strong> The area represented by $\int_1^3e^x\,dx$.</span>
</div>

<div class="example-end">$\blacksquare$</div>

## Example 5 {.green}

Evaluate the following integrals by interpreting each in terms of areas.

**(a)** $\displaystyle\int_0^1\sqrt{1-x^2}\,dx$

**(b)** $\displaystyle\int_0^3(x-1)\,dx$

## Solution {.green}

### Part (a)

The integrand is $y=\sqrt{1-x^2}$, which is nonnegative on $[0,1]$. Squaring both sides gives

$$
y^2=1-x^2
$$

or

$$
x^2+y^2=1
$$

This is the equation of a circle of radius $1$ centered at the origin. In the first quadrant, the curve is a quarter-circle. Therefore, the integral equals the area of a quarter-circle of radius $1$:

$$
\int_0^1\sqrt{1-x^2}\,dx
=
\frac14\pi(1)^2
$$

Hence,

$$
\boxed{\int_0^1\sqrt{1-x^2}\,dx=\frac{\pi}{4}}
$$

Location of Figure 9. The quarter-circle $y=\sqrt{1-x^2}$ in the first quadrant, bounded by the coordinate axes and the curve.

<div style="text-align: center;">
<img src="../images/0509.png" style="width: 430px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 9.</strong> The quarter-circle region for $\int_0^1\sqrt{1-x^2}\,dx$.</span>
</div>

### Part (b)

The graph of $y=x-1$ is a straight line. It crosses the $x$-axis at $x=1$ and passes through $(3,2)$. The integral from $0$ to $3$ is the signed area: the region above the axis from $x=1$ to $x=3$ contributes positively, and the region below the axis from $x=0$ to $x=1$ contributes negatively.

The positive region is a triangle with base $2$ and height $2$, so

$$
A_1=\frac12(2)(2)=2
$$

The negative region has base $1$ and height $1$, so its area magnitude is

$$
A_2=\frac12(1)(1)=\frac12
$$

Therefore,

$$
\begin{aligned}
\int_0^3(x-1)\,dx
&=A_1-A_2\\
&=2-\frac12\\
&=\frac32
\end{aligned}
$$

Hence,

$$
\boxed{\int_0^3(x-1)\,dx=\frac32=1.5}
$$

Location of Figure 10. The line $y=x-1$ from $x=0$ to $x=3$, showing the triangular regions below and above the $x$-axis.

<div style="text-align: center;">
<img src="../images/0510.png" style="width: 520px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 10.</strong> Signed triangular areas for $\int_0^3(x-1)\,dx$.</span>
</div>

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

Evaluate $\displaystyle\sum_{i=1}^{n}i$ using the formula for the sum of the first $n$ positive integers.

## Answer {.red}

$$
\boxed{\sum_{i=1}^{n}i=\frac{n(n+1)}{2}}
$$

## Question 2 {.red}

If a graph lies entirely below the $x$-axis on an interval, is its definite integral positive or negative?

## Answer {.red}

The definite integral is negative because it represents signed area, with regions below the $x$-axis contributing negatively.

<div class="question-end">$\blacksquare$</div>

# Scenario Problem

## Problem {.green}

A mechatronic actuator moves along a straight track from position $x=0$ to $x=3$ meters. Its force, in newtons, varies with position according to $F(x)=x^3-6x$. The work performed by a variable force along this path is represented by the definite integral

$$
W=\int_0^3F(x)\,dx
$$

Use the Riemann-sum definition to determine the work represented by this model.

## Solution {.green}

Substituting the force function gives

$$
W=\int_0^3(x^3-6x)\,dx
$$

From Example 3, the Riemann-sum calculation gives

$$
W=-\frac{27}{4}\text{ J}
$$

Thus, the signed work represented by this model is $-6.75$ joules. The negative value indicates that the force's contribution below the $x$-axis outweighs the positive contribution above the axis over the specified interval.

<div class="example-end">$\blacksquare$</div>

# The Midpoint Rule

## From Riemann Sums to the Midpoint Rule

A Riemann sum approximates the definite integral of a function by adding the areas of rectangles. Divide the interval $[a,b]$ into $n$ equal subintervals. The width of each subinterval is

$$
\Delta x=\frac{b-a}{n}
$$

The partition points are

$$
x_i=a+i\Delta x,\qquad i=0,1,\ldots,n
$$

For the Midpoint Rule, we choose the sample point at the centre of each subinterval $[x_{i-1},x_i]$. Its midpoint is

$$
\bar{x}_i=\frac{x_{i-1}+x_i}{2}
$$

The height of the rectangle over that subinterval is $f(\bar{x}_i)$, so its signed area is approximately $f(\bar{x}_i)\Delta x$. Adding the contributions from all $n$ subintervals gives the Midpoint Rule.

## Definition: Midpoint Rule {.blue}

For a function $f$ on the interval $[a,b]$, divide $[a,b]$ into $n$ equal subintervals, each of width

$$
\Delta x=\frac{b-a}{n}
$$

Let $\bar{x}_i$ be the midpoint of the $i$th subinterval:

$$
\bar{x}_i=\frac{x_{i-1}+x_i}{2}
$$

The Midpoint Rule approximates the definite integral by

$$
\int_a^b f(x)\,dx\approx M_n
=\sum_{i=1}^{n}f(\bar{x}_i)\Delta x
$$

Equivalently,

$$
M_n=\Delta x\left[f(\bar{x}_1)+f(\bar{x}_2)+\cdots+f(\bar{x}_n)\right]
$$

The midpoint of each subinterval is used as the sample point, and the sum of the corresponding rectangle areas gives the approximation.

<div class="definition-end">$\blacksquare$</div>

## How to Apply the Midpoint Rule

1. Identify the integrand $f(x)$ and the integration interval $[a,b]$.
2. Determine the number of subintervals $n$.
3. Calculate the common width $\Delta x=(b-a)/n$.
4. Find the midpoint of every subinterval.
5. Evaluate $f$ at each midpoint.
6. Add the function values and multiply their sum by $\Delta x$.

When $f(\bar{x}_i)$ is positive, the corresponding rectangle contributes positively to the approximation; when it is negative, it contributes negatively. Thus, the Midpoint Rule approximates the **signed** area represented by the definite integral, not necessarily the total geometric area between the curve and the $x$-axis.

## Example 6 {.green}

Use the Midpoint Rule with $n=5$ equal subintervals to approximate

$$
\int_1^2\frac{1}{x}\,dx
$$

## Solution {.green}

**Step 1: Identify the function and interval.**

Here,

$$
f(x)=\frac{1}{x},\qquad a=1,\qquad b=2,\qquad n=5
$$

**Step 2: Calculate the width of each subinterval.**

$$
\Delta x=\frac{b-a}{n}=\frac{2-1}{5}=\frac15=0.2
$$

The six partition points are

$$
1,\ 1.2,\ 1.4,\ 1.6,\ 1.8,\ 2
$$

Therefore, the five subintervals are $[1,1.2]$, $[1.2,1.4]$, $[1.4,1.6]$, $[1.6,1.8]$, and $[1.8,2]$.

**Step 3: Find the midpoint of each subinterval.**

Using $\bar{x}_i=(x_{i-1}+x_i)/2$, the five midpoints are

$$
\begin{aligned}
\bar{x}_1&=\frac{1+1.2}{2}=1.1\\
\bar{x}_2&=\frac{1.2+1.4}{2}=1.3\\
\bar{x}_3&=\frac{1.4+1.6}{2}=1.5\\
\bar{x}_4&=\frac{1.6+1.8}{2}=1.7\\
\bar{x}_5&=\frac{1.8+2}{2}=1.9
\end{aligned}
$$

Location of Figure 11: The five equal subintervals on $[1,2]$, each of width $\Delta x=0.2$, with midpoints $1.1$, $1.3$, $1.5$, $1.7$, and $1.9$ marked.

**Step 4: Evaluate the function at each midpoint.**

Since $f(x)=1/x$,

$$
\begin{aligned}
f(1.1)&=\frac{1}{1.1}\\
f(1.3)&=\frac{1}{1.3}\\
f(1.5)&=\frac{1}{1.5}\\
f(1.7)&=\frac{1}{1.7}\\
f(1.9)&=\frac{1}{1.9}
\end{aligned}
$$

**Step 5: Apply the Midpoint Rule.**

For five subintervals,

$$
M_5=\Delta x\left[f(1.1)+f(1.3)+f(1.5)+f(1.7)+f(1.9)\right]
$$

Substituting $\Delta x=1/5$ gives

$$
M_5=\frac15\left(
\frac1{1.1}+\frac1{1.3}+\frac1{1.5}+\frac1{1.7}+\frac1{1.9}
\right)
$$

Evaluating the sum,

$$
M_5\approx 0.691908
$$

Therefore, the Midpoint Rule approximation is

$$
\boxed{\int_1^2\frac1x\,dx\approx 0.691908}
$$

Location of Figure 12: The graph of $y=1/x$ on $[1,2]$ with five midpoint rectangles illustrating the area approximation $M_5\approx0.691908$.

**Interpreting the result.** The function $1/x$ is positive on $[1,2]$, so the integral represents the area under the curve and above the $x$-axis. The five rectangles approximate this area. Their heights are taken from the function values at the midpoints, rather than at the left or right endpoints.

<div class="example-end">$\blacksquare$</div>

## Comparing the Midpoint Rule with a Right-Endpoint Approximation

The sample point used in a Riemann sum affects the approximation. For a given partition, the right-endpoint rule uses the right endpoint of every subinterval, while the Midpoint Rule uses its centre. For some functions, the midpoint rectangles track the curve more effectively and produce a more accurate result. This is not a guarantee for every individual function and partition, but it is an important practical advantage of the method.

The book's earlier Example 3 considers the integral of $f(x)=x^3-6x$ from $0$ to $3$. Its exact value is

$$
\begin{aligned}
\int_0^3(x^3-6x)\,dx
&=\left[\frac{x^4}{4}-3x^2\right]_0^3\\
&=\frac{81}{4}-27\\
&=-6.75
\end{aligned}
$$

Using $40$ subintervals, the midpoint approximation is approximately $M_{40}=-6.7563$, whereas the right-endpoint approximation is approximately $R_{40}=-6.3998$.

Location of Figure 13: The graph of $y=x^3-6x$ on $[0,3]$ with the region represented by the definite integral and the midpoint approximation labelled $M_{40}\approx-6.7563$.

The absolute error of the midpoint approximation is approximately

$$
|M_{40}-(-6.75)|=|-6.7563+6.75|=0.0063
$$

The absolute error of the right-endpoint approximation is approximately

$$
|R_{40}-(-6.75)|=|-6.3998+6.75|=0.3502
$$

Thus, for this example, $M_{40}$ is much closer to the exact value than $R_{40}$. The example illustrates how choosing midpoints can substantially improve an approximation for a particular function and partition.

# Quick Check

## Question 1 {.red}

Use the Midpoint Rule with $n=2$ to approximate

$$
\int_0^2 x^2\,dx
$$

## Answer {.red}

The width is

$$
\Delta x=\frac{2-0}{2}=1
$$

The two subintervals are $[0,1]$ and $[1,2]$, with midpoints $0.5$ and $1.5$. Therefore,

$$
\begin{aligned}
M_2&=1\left[f(0.5)+f(1.5)\right]\\
&=(0.5)^2+(1.5)^2\\
&=0.25+2.25\\
&=2.5
\end{aligned}
$$

$$
\boxed{M_2=2.5}
$$

## Question 2 {.red}

A student divides $[0,4]$ into $4$ equal subintervals. What is the width $\Delta x$, and what sample point should be used in the second subinterval?

## Answer {.red}

The width is

$$
\Delta x=\frac{4-0}{4}=1
$$

The second subinterval is $[1,2]$, so its midpoint is

$$
\bar{x}_2=\frac{1+2}{2}=1.5
$$

$$
\boxed{\Delta x=1,\qquad \bar{x}_2=1.5}
$$

<div class="question-end">$\blacksquare$</div>

# Scenario Problem

## Problem {.green}

A mobile robot moves along a straight factory aisle. Its speed changes over a time interval of $0$ to $4$ seconds and is modelled by

$$
v(t)=2+t^2\quad\text{m/s}
$$

The robot's controller estimates the distance travelled by sampling the speed at the midpoint of each of four equal time intervals. Use the Midpoint Rule to estimate the distance travelled during the four seconds.

## Solution {.green}

The distance is approximated by the integral of speed over time:

$$
D=\int_0^4 v(t)\,dt
$$

For $n=4$ subintervals, the width is

$$
\Delta t=\frac{4-0}{4}=1\text{ s}
$$

The subintervals are $[0,1]$, $[1,2]$, $[2,3]$, and $[3,4]$. Their midpoints are

$$
0.5,\quad 1.5,\quad 2.5,\quad 3.5
$$

Evaluate the speed at each midpoint:

$$
\begin{aligned}
v(0.5)&=2+(0.5)^2=2.25\\
v(1.5)&=2+(1.5)^2=4.25\\
v(2.5)&=2+(2.5)^2=8.25\\
v(3.5)&=2+(3.5)^2=14.25
\end{aligned}
$$

Applying the Midpoint Rule,

$$
\begin{aligned}
D&\approx M_4\\
&=\Delta t\left[v(0.5)+v(1.5)+v(2.5)+v(3.5)\right]\\
&=1(2.25+4.25+8.25+14.25)\\
&=29\text{ m}
\end{aligned}
$$

Therefore, the estimated distance travelled is

$$
\boxed{D\approx29\text{ m}}
$$

The controller approximates the distance by treating the speed as constant at each interval's midpoint value. This is a numerical estimate; increasing the number of subintervals can improve the approximation in many practical applications.

<div class="example-end">$\blacksquare$</div>

# Properties of the Definite Integral

## Reversing the Limits of Integration

The definite integral is defined using a limit of Riemann sums. The interval's orientation matters: interchanging the limits changes the sign of the integral.

$$
\int_b^a f(x)\,dx=-\int_a^b f(x)\,dx
$$

This means that the integral from $a$ to $b$ and the integral from $b$ to $a$ have equal magnitudes but opposite signs, provided the integrals exist. When the graph lies above the $x$-axis, the integral from left to right is positive, while reversing the direction makes it negative. The same sign-reversal rule holds when the function takes both positive and negative values.

## Equal Limits of Integration

When the upper and lower limits are equal, the interval has zero width. Therefore, the definite integral is zero:

$$
\int_a^a f(x)\,dx=0
$$

There is no interval over which to accumulate area or signed change, so the result is zero.

## Four Fundamental Properties of the Definite Integral

Assume the functions involved are integrable on $[a,b]$, and let $c$ be a constant.

1. **Integral of a constant**

   $$
   \int_a^b c\,dx=c(b-a)
   $$

2. **Integral of a sum**

   $$
   \int_a^b [f(x)+g(x)]\,dx
   =
   \int_a^b f(x)\,dx+\int_a^b g(x)\,dx
   $$

3. **Constant multiple rule**

   $$
   \int_a^b cf(x)\,dx
   =
   c\int_a^b f(x)\,dx
   $$

4. **Integral of a difference**

   $$
   \int_a^b [f(x)-g(x)]\,dx
   =
   \int_a^b f(x)\,dx-\int_a^b g(x)\,dx
   $$

These rules allow us to split a complicated integrand into simpler parts and evaluate each part separately.

## Property 1: Integral of a Constant

For a constant function $f(x)=c$, the graph is the horizontal line $y=c$. Over the interval $[a,b]$, the region is a rectangle with height $c$ and width $b-a$. When $c>0$, its area is $c(b-a)$, which gives

$$
\int_a^b c\,dx=c(b-a)
$$

The formula also works for negative $c$, with the integral representing signed area.

Location of Figure 14: The graph of the constant function $y=c$ over $[a,b]$, showing a rectangle of width $b-a$, height $c$, and area $c(b-a)$.

## Property 2: Integral of a Sum

The integral of a sum equals the sum of the integrals:

$$
\int_a^b [f(x)+g(x)]\,dx
=
\int_a^b f(x)\,dx+\int_a^b g(x)\,dx
$$

### Geometric explanation using Figure 15

When $f$ and $g$ are nonnegative, the graph of $f+g$ is obtained by adding their heights at each $x$-value. The area under $f+g$ therefore combines the area under $f$ with the area under $g$. Figure 15 illustrates this relationship: the vertical heights of the two functions add, so their accumulated areas add as well.

Location of Figure 15: Graphs of $f$, $g$, and $f+g$ over $[a,b]$, illustrating that the area under $f+g$ is the sum of the areas under $f$ and $g$.

### Mathematical proof using Riemann sums

Divide $[a,b]$ into $n$ subintervals of width $\Delta x$, and choose a sample point $x_i^*$ in each subinterval. The Riemann sum for $f+g$ is

$$
\sum_{i=1}^{n}[f(x_i^*)+g(x_i^*)]\Delta x
$$

Distributing the sum gives

$$
\sum_{i=1}^{n}f(x_i^*)\Delta x
+
\sum_{i=1}^{n}g(x_i^*)\Delta x
$$

Taking the limit as the largest subinterval width approaches zero, each Riemann sum approaches its corresponding definite integral. Hence,

$$
\begin{aligned}
\int_a^b [f(x)+g(x)]\,dx
&=\lim_{n\to\infty}\sum_{i=1}^{n}[f(x_i^*)+g(x_i^*)]\Delta x\\
&=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x
+\lim_{n\to\infty}\sum_{i=1}^{n}g(x_i^*)\Delta x\\
&=\int_a^b f(x)\,dx+\int_a^b g(x)\,dx
\end{aligned}
$$

This proves Property 2.

## Property 3: Constant Multiple Rule

For any constant $c$,

$$
\int_a^b cf(x)\,dx=c\int_a^b f(x)\,dx
$$

Multiplying a function by a positive constant scales every height by that constant. The corresponding signed area is scaled by the same factor. A negative constant also reverses the sign of the function, so the signed integral changes sign accordingly.

## Property 4: Integral of a Difference

The difference rule is

$$
\int_a^b [f(x)-g(x)]\,dx
=
\int_a^b f(x)\,dx-\int_a^b g(x)\,dx
$$

It follows from Property 2 by writing $f-g=f+(-g)$, then applying Property 3 with the constant $c=-1$:

$$
\begin{aligned}
\int_a^b [f(x)-g(x)]\,dx
&=\int_a^b [f(x)+(-g(x))]\,dx\\
&=\int_a^b f(x)\,dx+\int_a^b [-g(x)]\,dx\\
&=\int_a^b f(x)\,dx-\int_a^b g(x)\,dx
\end{aligned}
$$

## Example 7 {.green}

Use the properties of integrals to evaluate $\int_0^1 (4+3x^2)\,dx$.

## Solution {.green}

Using the sum rule and constant multiple rule,

$$
\begin{aligned}
\int_0^1(4+3x^2)\,dx
&=\int_0^1 4\,dx+\int_0^1 3x^2\,dx\\
&=\int_0^1 4\,dx+3\int_0^1 x^2\,dx
\end{aligned}
$$

By the integral-of-a-constant property,

$$
\int_0^1 4\,dx=4(1-0)=4
$$

Also, using the known result $\int_0^1 x^2\,dx=\frac13$,

$$
\begin{aligned}
\int_0^1(4+3x^2)\,dx
&=4+3\left(\frac13\right)\\
&=4+1\\
&=5
\end{aligned}
$$

Therefore,

$$
\boxed{\int_0^1(4+3x^2)\,dx=5}
$$

<div class="example-end">$\blacksquare$</div>

## Property 5: Combining Integrals over Adjacent Intervals

If $a<c<b$, then

$$
\int_a^c f(x)\,dx+\int_c^b f(x)\,dx
=
\int_a^b f(x)\,dx
$$

The interval $[a,b]$ is divided into two adjacent intervals, $[a,c]$ and $[c,b]$. The total signed area over the whole interval is the sum of the signed areas over its two parts. This property allows an integral over one interval to be found by subtracting the integral over an adjacent interval from a known total.

Location of Figure 16: The graph of $y=f(x)$ over $[a,b]$, divided at $x=c$ into the adjacent intervals $[a,c]$ and $[c,b]$.

## Example 8 {.green}

If it is known that $\int_0^{10} f(x)\,dx=17$ and $\int_0^8 f(x)\,dx=12$, find $\int_8^{10} f(x)\,dx$.

## Solution {.green}

By Property 5,

$$
\int_0^8 f(x)\,dx+\int_8^{10} f(x)\,dx
=
\int_0^{10} f(x)\,dx
$$

Substitute the given values:

$$
12+\int_8^{10} f(x)\,dx=17
$$

Subtract $12$ from both sides:

$$
\int_8^{10} f(x)\,dx=17-12=5
$$

Therefore,

$$
\boxed{\int_8^{10} f(x)\,dx=5}
$$

<div class="example-end">$\blacksquare$</div>

## Comparison Properties of the Integral

The next properties compare the value of an integral with zero, with another integral, or with bounds based on the minimum and maximum values of a function. For these comparison properties, assume $a\leq b$.

### Property 6: Nonnegative Functions

If $f(x)\geq0$ for all $x$ in $[a,b]$, then

$$
\int_a^b f(x)\,dx\geq0
$$

When a function is nonnegative, its graph lies on or above the $x$-axis. Its signed area is therefore nonnegative.

### Property 7: Comparing Two Functions

If $f(x)\geq g(x)$ for all $x$ in $[a,b]$, then

$$
\int_a^b f(x)\,dx\geq\int_a^b g(x)\,dx
$$

The function that is greater at every point has an integral at least as large as the integral of the lower function over the same interval. This follows because $f(x)-g(x)\geq0$, so Property 6 gives

$$
\int_a^b [f(x)-g(x)]\,dx\geq0
$$

Using the difference rule,

$$
\int_a^b f(x)\,dx-\int_a^b g(x)\,dx\geq0
$$

which yields the comparison.

### Property 8: Bounds from Minimum and Maximum Values

If $m\leq f(x)\leq M$ for all $x$ in $[a,b]$, then

$$
m(b-a)\leq\int_a^b f(x)\,dx\leq M(b-a)
$$

The function stays between the horizontal lines $y=m$ and $y=M$. Therefore, its integral is bounded by the areas of the rectangles with heights $m$ and $M$ and width $b-a$.

Location of Figure 17: A graph of $y=f(x)$ bounded between the horizontal lines $y=m$ and $y=M$ over $[a,b]$, together with the lower and upper rectangles.

### Proof of Property 8 {.orange}

Since $m\leq f(x)\leq M$ on $[a,b]$, the comparison property gives

$$
\int_a^b m\,dx\leq\int_a^b f(x)\,dx\leq\int_a^b M\,dx
$$

Evaluating the two constant integrals using Property 1,

$$
m(b-a)\leq\int_a^b f(x)\,dx\leq M(b-a)
$$

Thus, Property 8 is proved.

<div class="theorem-end">$\blacksquare$</div>

## Example 9 {.green}

Use Property 8 to estimate $\int_0^1 e^{-x^2}\,dx$.

## Solution {.green}

Let $f(x)=e^{-x^2}$ on $[0,1]$. This function is decreasing on the interval, so its maximum value is

$$
M=f(0)=e^0=1
$$

and its minimum value is

$$
m=f(1)=e^{-1}
$$

Property 8 gives

$$
m(1-0)\leq\int_0^1 e^{-x^2}\,dx\leq M(1-0)
$$

Substituting $m=e^{-1}$ and $M=1$,

$$
e^{-1}\leq\int_0^1 e^{-x^2}\,dx\leq1
$$

Since $e^{-1}\approx0.3679$, a numerical version of the estimate is

$$
\boxed{0.367\leq\int_0^1 e^{-x^2}\,dx\leq1}
$$

The integral is greater than or equal to the area of the lower rectangle and less than or equal to the area of the upper rectangle.

Location of Figure 18: The graph of $y=e^{-x^2}$ on $[0,1]$, bounded above by $y=1$ and below by $y=1/e$, showing the corresponding rectangular area bounds.

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

Given that $\int_2^5 f(x)\,dx=9$, evaluate $\int_5^2 f(x)\,dx$.

## Answer {.red}

Reversing the limits changes the sign:

$$
\boxed{\int_5^2 f(x)\,dx=-9}
$$

## Question 2 {.red}

Suppose $2\leq f(x)\leq6$ on $[1,4]$. Give lower and upper bounds for $\int_1^4 f(x)\,dx$.

## Answer {.red}

Using Property 8 with $m=2$, $M=6$, and $b-a=4-1=3$,

$$
2(3)\leq\int_1^4 f(x)\,dx\leq6(3)
$$

Therefore,

$$
\boxed{6\leq\int_1^4 f(x)\,dx\leq18}
$$

<div class="question-end">$\blacksquare$</div>

# Scenario Problem

## Problem {.green}

A mechatronic system records a nonnegative sensor signal $f(t)$ over the interval $0\leq t\leq4$ seconds. Calibration establishes that the signal always remains between $2$ and $5$ units. Without knowing the exact formula for the signal, estimate bounds for its total accumulated signal $\int_0^4 f(t)\,dt$.

## Solution {.green}

The signal satisfies

$$
2\leq f(t)\leq5
$$

for every $t$ in $[0,4]$. Thus, the minimum bound is $m=2$, the maximum bound is $M=5$, and the interval width is $4-0=4$.

By Property 8,

$$
m(b-a)\leq\int_a^b f(t)\,dt\leq M(b-a)
$$

Substitute the values:

$$
2(4)\leq\int_0^4 f(t)\,dt\leq5(4)
$$

Therefore,

$$
\boxed{8\leq\int_0^4 f(t)\,dt\leq20}
$$

The accumulated signal lies between $8$ and $20$ unit-seconds. These bounds can be obtained from the known signal range without calculating the integral exactly.

<div class="example-end">$\blacksquare$</div>

# Summary

The definite integral is defined as the limit of Riemann sums as the subinterval widths approach zero. For a nonnegative function, it represents the area under the curve; when a graph lies both above and below the $x$-axis, the integral represents net area, with regions below the axis counted negatively. The integral notation identifies the integrand, the lower and upper limits, and the variable of integration. The precise meaning of the limit states that for every positive error tolerance $\epsilon$, sufficiently fine subdivisions make the Riemann sum differ from the integral by less than $\epsilon$.

Continuous functions and functions with only finitely many jump discontinuities are integrable on a closed interval. For an integrable function, the definite integral can be expressed as the limit of right-endpoint Riemann sums, with $\Delta x=(b-a)/n$ and $x_i=a+i\Delta x$. This connection allows limits of sums to be written as definite integrals and gives the integral its role as a mathematical tool for accumulating continuously varying quantities.

A definite integral can be defined as the limit of Riemann sums, $\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x$, where $\Delta x=(b-a)/n$ and the right endpoints are $x_i=a+i\Delta x$. To evaluate these limits, we use the formulas for sums of powers and the properties of sums to simplify the summation before taking the limit. Examples show how this definition yields exact integral values and how numerical Riemann sums approach those values as the number of subintervals increases.

A definite integral also represents signed area: regions above the $x$-axis contribute positively, while regions below it contribute negatively. This interpretation allows us to evaluate integrals geometrically, as with a quarter-circle or the difference between two triangular areas. Both the limit-of-sums definition and the signed-area interpretation connect definite integrals to accumulated quantities in engineering and computing.

The Midpoint Rule is a numerical method for approximating a definite integral using rectangles whose heights are determined by the integrand at the midpoints of equal subintervals. For $n$ subintervals, the width is $\Delta x=(b-a)/n$, each midpoint is $\bar{x}_i=(x_{i-1}+x_i)/2$, and the approximation is $M_n=\Delta x\sum_{i=1}^{n}f(\bar{x}_i)$. In the worked example, using five subintervals to approximate $\int_1^2(1/x)\,dx$ gives $M_5\approx0.691908$. The accompanying figures show the subinterval midpoints and the rectangles used to approximate the area.

The comparison with the integral of $x^3-6x$ on $[0,3]$ illustrates that $M_{40}\approx-6.7563$ is much closer to the exact value $-6.75$ than the right-endpoint estimate $R_{40}\approx-6.3998$. The Midpoint Rule is useful for estimating accumulated quantities such as distance from sampled velocity data, but its result remains an approximation whose accuracy depends on the function and the partition.

The definite integral changes sign when its limits are exchanged and equals zero when its limits are the same. Its fundamental properties state that the integral of a constant is the constant multiplied by the interval width, the integral of a sum or difference is the corresponding sum or difference of integrals, and a constant factor can be taken outside the integral. Integrals over adjacent intervals combine to give the integral over the full interval.

Comparison properties state that a nonnegative function has a nonnegative integral, that ordering two functions orders their integrals over the same interval, and that if $m\leq f(x)\leq M$ on $[a,b]$, then $m(b-a)\leq\int_a^b f(x)\,dx\leq M(b-a)$. These properties simplify calculations and provide estimates even when an exact integral is difficult to evaluate.

# Exercises

Exercises help in transforming theoretical concepts into practical understanding. Mathematics is learned by doing and solving exercises which train you to analyze problems, select appropriate methods, and construct logical solutions. Attempting problems sometimes leads to mistakes which provide opportunities for learning and improvement. Regular practice increases speed, accuracy, and confidence. Exercises are given in the recommended book which has also been provided to you and you are expected to solve them on your own.

## Exercises

Solve the odd number exercises from exercise 1 to 82.
