# Calculus and Analytical Geometry

## Indeterminate Forms and L'Hospital's Rule

### Dr. Aamir Alaud Din

# Objectives

After preparing this topic, you should be able to:

1. Identify indeterminate forms of types $\frac{0}{0}$ and $\frac{\infty}{\infty}$ and explain why these forms do not determine a limit by themselves.
2. State and apply L'Hospital's Rule to evaluate limits that produce the indeterminate forms $\frac{0}{0}$ or $\frac{\infty}{\infty}$, while checking its conditions.
3. Rewrite indeterminate products of type $0\cdot\infty$ as quotients and evaluate them using suitable limit methods.
4. Transform indeterminate differences of type $\infty-\infty$ into more manageable expressions and evaluate their limits.
5. Evaluate indeterminate powers of types $0^0$, $\infty^0$, and $1^\infty$ by taking logarithms and applying limit methods.

# The Why Section

- In mechanical engineering and mechatronics, mathematical models describe quantities such as displacement, force, vibration, and system response. Near a critical operating condition, a model may produce a quotient in which both numerator and denominator approach zero or both grow without bound. Substitution alone then does not reveal the limiting value.
- In computer science and data science, limits are used to study the behavior of algorithms, continuous models, and functions near boundary values. A formula may contain two terms that become very large while their difference remains finite, or a small factor multiplied by a factor that grows without bound.
- These expressions are called *indeterminate forms* because the visible form alone does not tell us the value of the limit. Different functions with the same indeterminate form can have different limits, so we need systematic methods rather than assumptions based only on substitution.
- L'Hospital's Rule provides one such method for quotients of differentiable functions of types $\frac{0}{0}$ and $\frac{\infty}{\infty}$. Rewriting products and differences as quotients can extend its usefulness, while logarithms help us handle indeterminate powers.
- For example, a mechatronic controller may estimate a response from a formula involving a difference of two large terms or a ratio that becomes $0/0$ at a target setting. This topic provides methods for determining the response approached near that setting. The scenario problem at the end illustrates how this can be done numerically.

# Objective 1: Indeterminate Forms

## Forms $\frac{0}{0}$ and $\frac{\infty}{\infty}$

- Suppose that $f(x)\to0$ and $g(x)\to0$ as $x\to a$. The quotient $\frac{f(x)}{g(x)}$ has the indeterminate form $\frac{0}{0}$. This form does not imply that the limit is zero or that the limit fails to exist.
- For example, common factors may be cancelled in a rational expression to reveal a finite limit.

## Example 1 {.green}

Find

$$
\lim_{x\to1}\frac{\ln x}{x-1}
$$

## Solution {.green}

As $x\to1$, $\ln x\to0$ and $x-1\to0$. The quotient therefore has the indeterminate form $\frac{0}{0}$.
We will evaluate this limit using L'Hospital's Rule in Objective 2.

<div class="example-end">$\blacksquare$</div>

- Another indeterminate form occurs when $f(x)\to\infty$ (or $-\infty$) and $g(x)\to\infty$ (or $-\infty$). The quotient has the form $\frac{\infty}{\infty}$, and its limit depends on the relative rates at which the numerator and denominator grow.
- For example, a quotient of two functions that both grow without bound can approach zero, a nonzero finite number, or infinity.

## Example 2 {.green}

Calculate

$$
\lim_{x\to\infty}\frac{e^x}{x^2}
$$

## Solution {.green}

As $x\to\infty$, both $e^x$ and $x^2$ approach infinity, so the expression has the form $\frac{\infty}{\infty}$.
We will evaluate this limit by applying L'Hospital's Rule in Objective 2.

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

What indeterminate form is obtained when $f(x)\to0$ and $g(x)\to0$ in $\frac{f(x)}{g(x)}$?

## Answer {.red}

The form is $\frac{0}{0}$. It does not determine the limit by itself.

## Question 2 {.red}

If both the numerator and denominator approach infinity, must their quotient approach $1$?

## Answer {.red}

No. The quotient depends on their relative rates of growth.

<div class="question-end">$\blacksquare$</div>

# Objective 2: L'Hospital's Rule

## Statement of L'Hospital's Rule

- L'Hospital's Rule is a method for evaluating certain limits of quotients that have the indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$.
- Suppose $f$ and $g$ are differentiable on an open interval containing $a$, except possibly at $a$, and $g'(x)\ne0$ on that interval. If both functions approach zero or both approach positive or negative infinity as $x\to a$, then, provided the limit on the right exists (finite or infinite), we have the following rule.

## Theorem: L'Hospital's Rule {.orange}

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=
\lim_{x\to a}\frac{f'(x)}{g'(x)}
$$

The rule applies when the original quotient has the indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$ and the limit of the quotient of derivatives exists in the required sense.

<div class="theorem-end">$\blacksquare$</div>

- Differentiate the numerator and denominator separately. Do not apply the quotient rule to the original quotient.
- The form must first be checked. L'Hospital's Rule cannot be applied just because a limit contains a quotient.
- The rule may be applied again if the quotient of derivatives is still indeterminate and the conditions remain satisfied.
- It is also valid for suitable one-sided limits and limits as $x\to\infty$ or $x\to-\infty$.

## Example 3 {.green}

Find

$$
\lim_{x\to1}\frac{\ln x}{x-1}
$$

## Solution {.green}

Direct substitution gives $\frac{0}{0}$, so L'Hospital's Rule applies.

$$
\begin{aligned}
\lim_{x\to1}\frac{\ln x}{x-1}
&=\lim_{x\to1}\frac{\frac{d}{dx}(\ln x)}{\frac{d}{dx}(x-1)}\\
&=\lim_{x\to1}\frac{1/x}{1}\\
&=1
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

## Example 4 {.green}

Calculate

$$
\lim_{x\to\infty}\frac{e^x}{x^2}
$$

## Solution {.green}

Both the numerator and denominator approach infinity. Applying L'Hospital's Rule once gives another indeterminate quotient.

$$
\begin{aligned}
\lim_{x\to\infty}\frac{e^x}{x^2}
&=\lim_{x\to\infty}\frac{e^x}{2x}
\end{aligned}
$$

The new quotient is still of type $\frac{\infty}{\infty}$. Applying the rule again gives

$$
\begin{aligned}
\lim_{x\to\infty}\frac{e^x}{2x}
&=\lim_{x\to\infty}\frac{e^x}{2}\\
&=\infty
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

## Example 5 {.green}

Find

$$
\lim_{x\to\infty}\frac{\ln x}{\sqrt{x}}
$$

## Solution {.green}

Both $\ln x$ and $\sqrt{x}$ approach infinity, so L'Hospital's Rule applies.

$$
\begin{aligned}
\lim_{x\to\infty}\frac{\ln x}{\sqrt{x}}
&=\lim_{x\to\infty}\frac{1/x}{1/(2\sqrt{x})}\\
&=\lim_{x\to\infty}\frac{2\sqrt{x}}{x}\\
&=\lim_{x\to\infty}\frac{2}{\sqrt{x}}\\
&=0
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

## Example 6 {.green}

Find

$$
\lim_{x\to0}\frac{\tan x-x}{x^3}
$$

## Solution {.green}

As $x\to0$, both numerator and denominator approach zero. Apply L'Hospital's Rule.

$$
\begin{aligned}
\lim_{x\to0}\frac{\tan x-x}{x^3}
&=\lim_{x\to0}\frac{\sec^2x-1}{3x^2}
\end{aligned}
$$

The new quotient is still of type $\frac{0}{0}$. Apply the rule again.

$$
\begin{aligned}
\lim_{x\to0}\frac{\sec^2x-1}{3x^2}
&=\lim_{x\to0}\frac{2\sec^2x\tan x}{6x}\\
&=\frac13\lim_{x\to0}\frac{\sec^2x\tan x}{x}\\
&=\frac13
\end{aligned}
$$

In the last step, $\sec^2x\to1$ and $\lim_{x\to0}\frac{\tan x}{x}=1$.

<div class="example-end">$\blacksquare$</div>

## Important Caution

- L'Hospital's Rule must not be used when the original expression is not of type $\frac{0}{0}$ or $\frac{\infty}{\infty}$.
- For example, the limit below is evaluated directly because its denominator does not approach zero.

$$
\lim_{x\to\pi}\frac{\sin x}{1-\cos x}
=
\frac{\sin\pi}{1-\cos\pi}
=
0
$$

# Quick Check

## Question 1 {.red}

Evaluate $\displaystyle\lim_{x\to1}\frac{x^2-1}{x-1}$ using L'Hospital's Rule.

## Answer {.red}

$$
\begin{aligned}
\lim_{x\to1}\frac{x^2-1}{x-1}
&=\lim_{x\to1}\frac{2x}{1}\\
&=2
\end{aligned}
$$

## Question 2 {.red}

Can L'Hospital's Rule be applied immediately to $\displaystyle\lim_{x\to0}\frac{1+\cos x}{x+1}$?

## Answer {.red}

No. Direct substitution gives $\frac{2}{1}=2$, not an indeterminate form.

<div class="question-end">$\blacksquare$</div>

# Objective 3: Indeterminate Products (Type $0\cdot\infty$)

- If $f(x)\to0$ and $g(x)\to\infty$ (or $-\infty$), the product $f(x)g(x)$ has the indeterminate form $0\cdot\infty$.
- The result depends on how quickly the factor approaching zero decreases compared with how quickly the other factor grows.
- To use L'Hospital's Rule, rewrite the product as a quotient so that it has the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$. Choose the rewrite that produces the simpler expression.

## Example 7 {.green}

Evaluate

$$
\lim_{x\to0^+}x\ln x
$$

## Solution {.green}

As $x\to0^+$, $x\to0$ and $\ln x\to-\infty$. The product has the indeterminate form $0\cdot(-\infty)$.
Write the product as a quotient.

$$
\begin{aligned}
\lim_{x\to0^+}x\ln x
&=\lim_{x\to0^+}\frac{\ln x}{1/x}
\end{aligned}
$$

Both numerator and denominator approach negative infinity and positive infinity respectively, giving a quotient of type $\frac{-\infty}{\infty}$. L'Hospital's Rule gives

$$
\begin{aligned}
\lim_{x\to0^+}\frac{\ln x}{1/x}
&=\lim_{x\to0^+}\frac{1/x}{-1/x^2}\\
&=\lim_{x\to0^+}(-x)\\
&=0
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

What is the indeterminate form of $x\ln x$ as $x\to0^+$?

## Answer {.red}

It is $0\cdot(-\infty)$.

## Question 2 {.red}

Rewrite $x\ln x$ as a quotient suitable for L'Hospital's Rule as $x\to0^+$.

## Answer {.red}

One useful form is $\displaystyle\frac{\ln x}{1/x}$.

<div class="question-end">$\blacksquare$</div>

# Objective 4: Indeterminate Differences (Type $\infty-\infty$)

- If $f(x)\to\infty$ and $g(x)\to\infty$, the difference $f(x)-g(x)$ has the indeterminate form $\infty-\infty$.
- We cannot determine the limit by comparing the two infinite quantities informally. One term may grow faster than the other, or their difference may approach a finite value.
- A useful strategy is to combine the terms using a common denominator, factor, rationalize, or otherwise rewrite the difference as a quotient with an indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$.

## Example 8 {.green}

Compute

$$
\lim_{x\to1^+}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)
$$

## Solution {.green}

As $x\to1^+$, both $\frac{1}{\ln x}$ and $\frac{1}{x-1}$ approach infinity. The difference is of type $\infty-\infty$.
Combine the terms using a common denominator.

$$
\begin{aligned}
&\lim_{x\to1^+}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)\\
&=\lim_{x\to1^+}\frac{x-1-\ln x}{(x-1)\ln x}
\end{aligned}
$$

Both numerator and denominator approach zero, so L'Hospital's Rule applies.

$$
\begin{aligned}
&\lim_{x\to1^+}\frac{x-1-\ln x}{(x-1)\ln x}\\
&=\lim_{x\to1^+}\frac{1-\frac1x}{\ln x+\frac{x-1}{x}}\\
&=\lim_{x\to1^+}\frac{x-1}{x\ln x+x-1}
\end{aligned}
$$

The last quotient is still of type $\frac{0}{0}$. Applying L'Hospital's Rule again gives

$$
\begin{aligned}
\lim_{x\to1^+}\frac{x-1}{x\ln x+x-1}
&=\lim_{x\to1^+}\frac{1}{\ln x+2}\\
&=\frac12
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

## Example 9 {.green}

Calculate

$$
\lim_{x\to\infty}(e^x-x)
$$

## Solution {.green}

Both $e^x$ and $x$ approach infinity, so the difference has the form $\infty-\infty$.
Factor out $x$ to obtain

$$
e^x-x=x\left(\frac{e^x}{x}-1\right)
$$

By L'Hospital's Rule, $\frac{e^x}{x}\to\infty$ as $x\to\infty$. Therefore, the factor in parentheses grows without bound, and so does its product with $x$.

$$
\lim_{x\to\infty}(e^x-x)=\infty
$$

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

Why is $\infty-\infty$ called an indeterminate form?

## Answer {.red}

Because the form alone does not tell us whether the difference approaches a finite value, infinity, or another outcome.

## Question 2 {.red}

What algebraic step is useful for simplifying $\displaystyle\frac{1}{\ln x}-\frac{1}{x-1}$?

## Answer {.red}

Combine the fractions using a common denominator.

<div class="question-end">$\blacksquare$</div>

# Objective 5: Indeterminate Powers

## Forms $0^0$, $\infty^0$, and $1^\infty$

- Limits of the form $[f(x)]^{g(x)}$ can be indeterminate when the base and exponent approach particular values.
- The three forms considered here are $0^0$, $\infty^0$, and $1^\infty$. The notation describes the behavior of the base and exponent separately; it does not determine the limit of the whole power.
- A standard method is to let $y=[f(x)]^{g(x)}$ and take the natural logarithm.

$$
\ln y=g(x)\ln f(x)
$$

- This transforms the power into a product. After evaluating $\lim \ln y$, use the continuity of the exponential function to recover the limit of $y$.

$$
\lim y=e^{\lim\ln y}
$$

## Example 10 {.green}

Calculate

$$
\lim_{x\to0^+}(1+\sin4x)^{\cot x}
$$

## Solution {.green}

As $x\to0^+$, the base $1+\sin4x\to1$ and the exponent $\cot x\to\infty$. The expression has the indeterminate form $1^\infty$.
Let

$$
y=(1+\sin4x)^{\cot x}
$$

Taking natural logarithms gives

$$
\ln y=\cot x\ln(1+\sin4x)
=\frac{\ln(1+\sin4x)}{\tan x}
$$

As $x\to0^+$, the last quotient is of type $\frac{0}{0}$. Apply L'Hospital's Rule.

$$
\begin{aligned}
\lim_{x\to0^+}\ln y
&=\lim_{x\to0^+}\frac{4\cos4x/(1+\sin4x)}{\sec^2x}\\
&=4
\end{aligned}
$$

Therefore,

$$
\lim_{x\to0^+}y=e^4
$$

<div class="example-end">$\blacksquare$</div>

## Example 11 {.green}

Find

$$
\lim_{x\to0^+}x^x
$$

## Solution {.green}

As $x\to0^+$, the base $x\to0$ and the exponent $x\to0$. The expression has the indeterminate form $0^0$.
Let $y=x^x$. Taking natural logarithms gives

$$
\ln y=x\ln x
$$

From Objective 3, $\lim_{x\to0^+}x\ln x=0$. Therefore,

$$
\begin{aligned}
\lim_{x\to0^+}y
&=e^{\lim_{x\to0^+}\ln y}\\
&=e^0\\
&=1
\end{aligned}
$$

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

What transformation is useful when evaluating a limit of the form $[f(x)]^{g(x)}$?

## Answer {.red}

Take the natural logarithm: $\ln y=g(x)\ln f(x)$.

## Question 2 {.red}

Evaluate $\displaystyle\lim_{x\to0^+}x^x$.

## Answer {.red}

Since $\lim_{x\to0^+}x\ln x=0$, the limit is $e^0=1$.

<div class="question-end">$\blacksquare$</div>

## Scenario Problem {.green}

A mechatronic actuator is tested near a reference setting $x=1$. Its normalized response is described by

$$
R(x)=\frac{\ln x}{x-1}
$$

The response formula is undefined at $x=1$, but the controller needs the response value approached as the setting gets closer to $1$. Determine this limiting response.

## Solution {.green}

Direct substitution produces the indeterminate form $\frac{0}{0}$ because $\ln1=0$ and $1-1=0$.
Apply L'Hospital's Rule by differentiating the numerator and denominator separately.

$$
\begin{aligned}
\lim_{x\to1}R(x)
&=\lim_{x\to1}\frac{\ln x}{x-1}\\
&=\lim_{x\to1}\frac{1/x}{1}\\
&=1
\end{aligned}
$$

The normalized response approaches $1$ as the input approaches the reference setting. This gives the controller a well-defined limiting value even though the original formula is undefined at the exact setting.

# Summary

- The forms $\frac{0}{0}$ and $\frac{\infty}{\infty}$ are indeterminate because they do not determine a limit by themselves.
- L'Hospital's Rule evaluates suitable quotient limits by differentiating the numerator and denominator separately.
- The original quotient must have type $\frac{0}{0}$ or $\frac{\infty}{\infty}$ before L'Hospital's Rule is applied.
- If the quotient of derivatives remains indeterminate, the rule may be applied again when its conditions continue to hold.
- A product of type $0\cdot\infty$ can often be rewritten as a quotient.
- A difference of type $\infty-\infty$ can often be simplified using a common denominator, factoring, or rationalization.
- For indeterminate powers $0^0$, $\infty^0$, and $1^\infty$, take logarithms to transform the power into a product.
- After finding the limit of $\ln y$, recover the limit of $y$ by exponentiating.
- Always check the form and the conditions before using L'Hospital's Rule, and prefer a simpler algebraic method when one is available.


# Exercises

## Exercises Set

Solve the odd number exercises from exercise 1 to 90.

* Exercises help transform theoretical concepts into practical understanding.

* Mathematics is learned by doing and solving exercises will train you to analyze problems, select appropriate methods, and construct logical solutions.

* Attempting problems sometimes leads to mistakes which provide opportunities for learning and improvement.

* Regular practice increases speed, accuracy, and confidence.

* Exercises are given in the Exercises file and you are expected to solve them on your own.