# Calculus and Analytical Geometry

## The Fundamental Theorem of Calculus, Part 2

### Dr. Aamir Alaud Din

### October 27, 2026

# Objectives

To apply the second part of the Fundamental Theorem of Calculus to evaluate definite integrals using antiderivatives, interpret definite integrals as net changes in quantities such as position, and understand how differentiation and integration are inverse processes.

# The Why Section

A definite integral can represent accumulated change. For example, if the velocity of a robot arm is known throughout a time interval, repeatedly adding tiny displacements would be a lengthy way to calculate its total change in position. The second part of the Fundamental Theorem of Calculus provides a much simpler method: find an antiderivative of the velocity and evaluate it at the endpoints.

The theorem is useful in mechanical engineering when calculating displacement from velocity, work-related accumulation, or the area under a curve. It is also useful in computer science and mechatronics, where software integrates sensor measurements or a modeled rate of change to estimate a system's accumulated output. Instead of approximating the accumulation with many small pieces, the theorem can give an exact result when a suitable antiderivative is available.

Consider a mechatronic positioning system whose velocity is described by a continuous function \(v(t)\). If the system is at position \(s(a)\) at time \(a\), we want to determine its position at time \(b\). Studying the second part of the Fundamental Theorem of Calculus will show how the accumulated velocity determines the change in position and how the final position can be calculated.

# The Fundamental Theorem of Calculus, Part 2

## Why Is the Second Part Important?

The first part of the Fundamental Theorem of Calculus connects accumulation and differentiation: if a function is defined by an integral with a variable upper limit, differentiating it recovers the integrand under the theorem's continuity condition. The second part gives a practical method for evaluating a definite integral.

Earlier, a definite integral was interpreted as the limit of Riemann sums. Although this definition is fundamental, calculating a limit of sums can be long and difficult. The second part of the theorem replaces that procedure with a simpler calculation: find an antiderivative and subtract its values at the endpoints.

## Theorem {.orange}

**The Fundamental Theorem of Calculus, Part 2.** If \(f\) is continuous on \([a,b]\), then

$$
\int_a^b f(x)\,dx=F(b)-F(a)
$$

where \(F\) is any antiderivative of \(f\), that is, a function satisfying \(F'(x)=f(x)\).

## Proof {.orange}

Define

$$
g(x)=\int_a^x f(t)\,dt
$$

Since \(f\) is continuous on \([a,b]\), the first part of the Fundamental Theorem of Calculus gives

$$
g'(x)=f(x)
$$

Thus, \(g\) is an antiderivative of \(f\) on the interval.

Let \(F\) be any other antiderivative of \(f\). Then

$$
F'(x)=f(x)
$$

and

$$
g'(x)=f(x)
$$

Therefore,

$$
F'(x)=g'(x)
$$

It follows that the derivative of \(F-g\) is zero:

$$
\frac{d}{dx}[F(x)-g(x)]=0
$$

A function whose derivative is zero on an interval is constant there. Hence, for some constant \(C\),

$$
F(x)-g(x)=C
$$

or

$$
F(x)=g(x)+C
$$

This equality holds throughout the interval, including its endpoints by continuity.

Now set \(x=a\). From the definition of \(g\),

$$
g(a)=\int_a^a f(t)\,dt=0
$$

Consequently,

$$
F(a)=g(a)+C=C
$$

Next, set \(x=b\):

$$
F(b)=g(b)+C
$$

Subtracting \(F(a)=C\) from \(F(b)=g(b)+C\) gives

$$
F(b)-F(a)=g(b)
$$

Using the definition of \(g\), we obtain

$$
F(b)-F(a)=\int_a^b f(t)\,dt
$$

Therefore,

$$
\boxed{\int_a^b f(x)\,dx=F(b)-F(a)}
$$

This proves the second part of the Fundamental Theorem of Calculus.

<div class="theorem-end">$\blacksquare$</div>

## Interpreting the Theorem as Net Change

Suppose \(s(t)\) denotes the position of a moving object and \(v(t)\) its velocity. Since velocity is the derivative of position,

$$
s'(t)=v(t)
$$

Therefore, \(s\) is an antiderivative of \(v\). Applying the theorem gives

$$
\int_a^b v(t)\,dt=s(b)-s(a)
$$

The integral of velocity over a time interval is the **net change in position**, or displacement, over that interval. It is not necessarily the total distance travelled: if the object reverses direction, positive and negative parts of velocity can cancel in the integral.

The same reasoning applies to other rates of change. If \(Q'(t)=r(t)\), then

$$
\int_a^b r(t)\,dt=Q(b)-Q(a)
$$

Thus, integrating a rate over an interval gives the net change in the quantity whose derivative is that rate.

## Example 5 {.green}

Evaluate the integral

$$
\int_1^3 e^x\,dx
$$

## Solution {.green}

The integrand is \(f(x)=e^x\). An antiderivative is

$$
F(x)=e^x
$$

because \(F'(x)=e^x\). By the second part of the Fundamental Theorem of Calculus,

$$
\begin{aligned}
\int_1^3 e^x\,dx
&=F(3)-F(1)\\
&=e^3-e
\end{aligned}
$$

Therefore,

$$
\boxed{\int_1^3 e^x\,dx=e^3-e}
$$

Notice that any antiderivative \(e^x+C\) would give the same result, because the constant cancels when the endpoint values are subtracted. It is therefore convenient to use the simplest antiderivative, \(F(x)=e^x\).

<div class="example-end">$\blacksquare$</div>

## Another Notation for the Theorem

The endpoint evaluation is often written using bracket notation:

$$
\left.F(x)\right|_a^b=F(b)-F(a)
$$

Therefore, the theorem can also be written as

$$
\int_a^b f(x)\,dx=\left.F(x)\right|_a^b
$$

where \(F'=f\). The notation means: evaluate \(F\) at the upper endpoint \(b\), evaluate it at the lower endpoint \(a\), and subtract the second value from the first.

## Example 6 {.green}

Find the area under the parabola \(y=x^2\) from \(0\) to \(1\).

## Solution {.green}

The required area is

$$
A=\int_0^1 x^2\,dx
$$

An antiderivative of \(x^2\) is

$$
F(x)=\frac{x^3}{3}
$$

Applying the Fundamental Theorem of Calculus gives

$$
\begin{aligned}
A
&=\left.\frac{x^3}{3}\right|_0^1\\
&=\frac{1^3}{3}-\frac{0^3}{3}\\
&=\frac13
\end{aligned}
$$

Therefore, the area is

$$
\boxed{A=\frac13}
$$

This calculation is much shorter than evaluating the area by taking a limit of Riemann sums.

<div class="example-end">$\blacksquare$</div>

## Example 7 {.green}

Evaluate

$$
\int_3^6 \frac{dx}{x}
$$

## Solution {.green}

We can write the integral as

$$
\int_3^6 \frac{1}{x}\,dx
$$

An antiderivative of \(1/x\), for \(x>0\), is \(\ln x\). Since the interval \([3,6]\) lies entirely in the positive real numbers, we can use \(F(x)=\ln x\).

By the Fundamental Theorem of Calculus,

$$
\begin{aligned}
\int_3^6 \frac{1}{x}\,dx
&=\left.\ln x\right|_3^6\\
&=\ln 6-\ln 3\\
&=\ln\left(\frac63\right)\\
&=\ln 2
\end{aligned}
$$

Hence,

$$
\boxed{\int_3^6 \frac{1}{x}\,dx=\ln 2}
$$

<div class="example-end">$\blacksquare$</div>

## Example 8 {.green}

Find the area under the cosine curve from \(0\) to \(b\), where \(0\leq b\leq \pi/2\).

## Solution {.green}

On the interval \(0\leq x\leq b\leq\pi/2\), the cosine function is nonnegative. Therefore, the area under the curve \(y=\cos x\) from \(x=0\) to \(x=b\) is

$$
A=\int_0^b \cos x\,dx
$$

An antiderivative of \(\cos x\) is \(\sin x\). Applying the Fundamental Theorem of Calculus,

$$
\begin{aligned}
A
&=\left.\sin x\right|_0^b\\
&=\sin b-\sin 0\\
&=\sin b
\end{aligned}
$$

Thus,

$$
\boxed{A=\sin b}
$$

In particular, if \(b=\pi/2\), then

$$
A=\sin\frac{\pi}{2}=1
$$

So the area under the cosine curve from \(0\) to \(\pi/2\) is \(1\).

Location of Figure 9: The area under the curve \(y=\cos x\) from \(x=0\) to \(x=b\), with \(0\leq b\leq\pi/2\).

<div style="text-align: center;">
<img src="figure_9_cosine_area.png" style="width: 520px; display: block; margin: 0 auto 10px auto;">
<span><strong>Figure 9.</strong> Area under the cosine curve from \(0\) to \(b\); for \(b=\pi/2\), the area is \(1\).</span>
</div>

<div class="example-end">$\blacksquare$</div>

## Example 9 {.green}

What is wrong with the following calculation?

$$
\int_{-1}^{3}\frac{1}{x^2}\,dx
=\left.-\frac{1}{x}\right|_{-1}^{3}
=-\frac13-1
=-\frac43
$$

## Solution {.green}

The calculation is incorrect because the Fundamental Theorem of Calculus, Part 2, requires the integrand to be continuous on the entire closed interval \([a,b]\). Here,

$$
f(x)=\frac{1}{x^2}
$$

is not defined at \(x=0\), which lies inside \([-1,3]\). Therefore, \(f\) is not continuous on the interval, and the theorem cannot be applied directly.

There is also a useful reason to question the result: \(1/x^2\) is positive wherever it is defined, so an integral representing its accumulated area cannot give a negative value.

The improper integral must be split at the discontinuity and treated using limits:

$$
\int_{-1}^{3}\frac{1}{x^2}\,dx
=
\int_{-1}^{0}\frac{1}{x^2}\,dx
+
\int_{0}^{3}\frac{1}{x^2}\,dx
$$

Each part is defined as a one-sided limit. For the left part,

$$
\begin{aligned}
\int_{-1}^{0}\frac{1}{x^2}\,dx
&=\lim_{c\to0^-}\int_{-1}^{c}x^{-2}\,dx\\
&=\lim_{c\to0^-}\left[-\frac1x\right]_{-1}^{c}\\
&=\lim_{c\to0^-}\left(-\frac1c-1\right)\\
&=+\infty
\end{aligned}
$$

For the right part,

$$
\begin{aligned}
\int_{0}^{3}\frac{1}{x^2}\,dx
&=\lim_{d\to0^+}\int_d^3x^{-2}\,dx\\
&=\lim_{d\to0^+}\left[-\frac1x\right]_d^3\\
&=\lim_{d\to0^+}\left(-\frac13+\frac1d\right)\\
&=+\infty
\end{aligned}
$$

Both parts diverge. Therefore, the improper integral does not exist as a finite value:

$$
\boxed{\int_{-1}^{3}\frac{1}{x^2}\,dx\text{ diverges}}
$$

The error was applying the theorem across a point where the integrand is discontinuous.

<div class="example-end">$\blacksquare$</div>

## Differentiation and Integration as Inverse Processes

The two parts of the Fundamental Theorem of Calculus express the close relationship between differentiation and integration.

### Part 1: Differentiating an Accumulation Function

If \(f\) is continuous and

$$
g(x)=\int_a^x f(t)\,dt
$$

then

$$
g'(x)=f(x)
$$

In words, differentiating an accumulation function recovers the original integrand.

### Part 2: Evaluating a Definite Integral

If \(f\) is continuous on \([a,b]\) and \(F'=f\), then

$$
\int_a^b f(x)\,dx=F(b)-F(a)
$$

In words, a definite integral can be evaluated by finding an antiderivative and subtracting its values at the endpoints.

Together, these results show that differentiation and integration are inverse processes, with the endpoint difference in Part 2 accounting for the net accumulation over an interval. Part 1 differentiates an integral with a variable upper limit; Part 2 evaluates a definite integral using an antiderivative.

# Quick Check

## Question 1 {.red}

Evaluate

$$
\int_0^2 3x^2\,dx
$$

## Answer {.red}

An antiderivative of \(3x^2\) is \(x^3\). Hence,

$$
\begin{aligned}
\int_0^2 3x^2\,dx
&=\left.x^3\right|_0^2\\
&=2^3-0^3\\
&=8
\end{aligned}
$$

$$
\boxed{8}
$$

## Question 2 {.red}

Can the Fundamental Theorem of Calculus, Part 2, be applied directly to \(\int_{-1}^{1}1/x^2\,dx\)? Explain briefly.

## Answer {.red}

No. The function \(1/x^2\) is not continuous on \([-1,1]\), because it is undefined at \(x=0\). The integral is improper and diverges.

<div class="question-end">$\blacksquare$</div>

# Scenario Problem

## Problem {.green}

A mechatronic actuator moves along a straight guide. Its velocity at time \(t\), measured in metres per second, is modelled by

$$
v(t)=3t^2+2t
$$

for \(0\leq t\leq2\). If the actuator is at position \(s(0)=0.5\) metres at \(t=0\), determine its displacement over the two seconds and its final position at \(t=2\).

## Solution {.green}

The displacement is the integral of velocity over the time interval:

$$
\Delta s=\int_0^2 v(t)\,dt
$$

Substitute the given velocity function:

$$
\Delta s=\int_0^2(3t^2+2t)\,dt
$$

An antiderivative is

$$
F(t)=t^3+t^2
$$

By the Fundamental Theorem of Calculus, Part 2,

$$
\begin{aligned}
\Delta s
&=\left.(t^3+t^2)\right|_0^2\\
&=(2^3+2^2)-(0^3+0^2)\\
&=8+4\\
&=12\text{ m}
\end{aligned}
$$

Thus, the actuator's displacement is

$$
\boxed{\Delta s=12\text{ m}}
$$

Final position equals initial position plus displacement:

$$
s(2)=s(0)+\Delta s
$$

$$
s(2)=0.5+12=12.5\text{ m}
$$

Therefore, the actuator is at position

$$
\boxed{s(2)=12.5\text{ m}}
$$

The theorem has converted the accumulated velocity into a net change in position by evaluating an antiderivative at the two endpoints.

<div class="example-end">$\blacksquare$</div>

# Summary

The second part of the Fundamental Theorem of Calculus states that if \(f\) is continuous on \([a,b]\) and \(F'=f\), then \(\int_a^b f(x)\,dx=F(b)-F(a)\). It provides a short and exact method for evaluating definite integrals using antiderivatives rather than limits of Riemann sums. The result is often written as \(\left.F(x)\right|_a^b=F(b)-F(a)\). In applications, integrating a rate of change gives the net change in the corresponding quantity; in particular, \(\int_a^b v(t)\,dt=s(b)-s(a)\). The continuity condition matters: the theorem cannot be applied directly across an interior discontinuity, as shown by the divergent integral of \(1/x^2\) across zero.

The two parts of the Fundamental Theorem describe differentiation and integration as inverse processes. Part 1 says that differentiating an accumulation function \(\int_a^x f(t)\,dt\) recovers \(f(x)\), while Part 2 says that a definite integral can be evaluated by subtracting endpoint values of an antiderivative. Together, these results connect rates, accumulated quantities, and areas under curves.

# Exercises

Exercises help in transforming theoretical concepts into practical understanding. Mathematics is learned by doing and solving exercises which train you to analyze problems, select appropriate methods, and construct logical solutions. Attempting problems sometimes leads to mistakes which provide opportunities for learning and improvement. Regular practice increases speed, accuracy, and confidence. Exercises are given in the recommended book which has also been provided to you and you are expected to solve them on your own.

## Exercises

Solve the odd number exercises from exercise 1 to 50.
