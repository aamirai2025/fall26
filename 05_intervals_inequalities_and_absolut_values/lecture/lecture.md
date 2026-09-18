# Calculus and Analyticl Geometry

## Intervals, Inequalities, and Absolute Values

### Dr. Aamir Alaud Din

### August 25, 2026

# Objectives

After preparing this topic, you should be able

1. To represent and interpret intervals and inequalities on the real number line.

2. To understand absolute value as distance between two real numbers.

3. To translate distance statements into neighborhoods of $c$ and understand the basic language of $x\rightarrow c$ needed for limits, continuity, and derivatives.

# The Why Section

* Before studying limits, we need a precise way to describe:

    1. **where a number is,**

    2. **how far one number is from another, and**

    3. **which values of $x$ are close to a particular number $c$.**

* These ideas form the foundation for the notation $x\rightarrow c$.

## Objective 1: Why Study Intervals and Inequalities?

* When we study a limit, we are interested in what happens when the input $x$ is **near a particular number $c$**.

* Therefore, we need a precise way to describe the possible values of $x$.

* For example, $2<x<5$ means that $x$ lies between $2$ and $5$.

* In interval notation,

$$
x\in(2,5).
$$

* Similarly, $c-\delta<x<c+\delta$ describes an interval centered at $c$.

* Intervals and inequalities therefore allow us to describe:

    * **where $x$ is;**
    * **which endpoints are included or excluded;**
    * **the set of possible values of $x$;**
    * **the values of $x$ near $c$.**

* These ideas will be used repeatedly when we study limits and continuity.

# Objective 1: Intervals and Inequalities

## The Real Number Line

- The real number line represents every real number as a point.

<div style="text-align: center;">
<img src="../images/0501.png" style="width: 1573px; border-radius: 12px; display: block; margin: 0 auto 10px auto;">

<span><strong>Figure 1.</strong> The real number line.</span>
</div>

- Moving to the right means numbers become larger.

- Moving to the left means numbers become smaller.

- For example, $-2<3$ because $-2$ lies to the left of $3$.

## Inequalities

- An inequality compares two quantities.

- The four basic symbols are:

    1. $\lt\;\;\;\Longrightarrow\;\;\;$Less than

    2. $\gt\;\;\;\Longrightarrow\;\;\;$Greater than

    3. $\leq\;\;\;\Longrightarrow\;\;\;$Less than or equal to

    4. $\geq\;\;\;\Longrightarrow\;\;\;$Greater than or equal to

- For example, $x<4$ means $x$ is somewhere to the left of $4$.

- Similarly, $x>4$ means $x$ is somewhere to the right of $4$.

## Open and Closed Endpoints

- Consider $x<4$.

- The number $4$ is not included.

- We represent this using an open endpoint $\circ$.

- But $x\leq4$ includes $4$, so we use a filled endpoint $\bullet$.

<div style="text-align: center;">
<img src="../images/0502.png" style="width: 1573px; border-radius: 12px; display: block; margin: 0 auto 10px auto;">

<span><strong>Figure 2.</strong> Open and closed endpoints on number line.</span>
</div>

- This distinction is important because neighborhoods used in limits are usually open intervals.

## Intervals

- An interval is a set of real numbers between two endpoints.

- For example, $2<x<5$ means all numbers between $2$ and $5$.

- In interval notation,

$$
x\in(2,5).
$$

- The parentheses mean that $2$ and $5$ are not included.

<div style="text-align: center;">
<img src="../images/0503.png" style="width: 1573px; border-radius: 12px; display: block; margin: 0 auto 10px auto;">

<span><strong>Figure 3.</strong> Representation of $(2,5)$ on real number line.</span>
</div>

## Important Types of Intervals

- Open interval $a<x<b$ becomes $(a,b)$.

- Closed interval $a\leq x\leq b$ becomes $[a,b]$.

- Left-closed, right-open $a\leq x<b$ becomes $[a,b)$.

- Left-open, right-closed $a<x\leq b$ becomes $(a,b]$.

## Intervals Extending to Infinity

- For $x>3$, we write $(3,\infty)$.

- For $x\leq3$, we write $(-\infty,3]$.

- Remember that $\infty$ is not a real number, so we always use a parenthesis with infinity.

## Example 1 {.green}

Write $-2<x<4$ in interval notation.

## Solution {.green}

The endpoints are both excluded. Therefore,

$$
\boxed{x\in(-2,4)}
$$

<div class="example-end">$\blacksquare$</div>

## Example 2 {.green}

Write $[-3,5)$ as an inequality.

## Solution {.green}

The square bracket at $-3$ means included, so

$$
x\geq-3.
$$

The parenthesis at $5$ means excluded, so

$$
x<5.
$$

Therefore,

$$
\boxed{-3\leq x<5}
$$

<div class="example-end">$\blacksquare$</div>

## Example 3 {.green}

Solve

$$
3x-2<10.
$$

## Solution {.green}

Adding $2$ to both sides,

$$
3x<12.
$$

Dividing by $3$,

$$
x<4.
$$

Therefore,

$$
\boxed{x\in(-\infty,4)}
$$

<div class="example-end">$\blacksquare$</div>

## Example 4 {.green}

Solve

$$
-2x+3<7.
$$

## Solution {.green}

Subtracting $3$ from both sides,

$$
-2x<4.
$$

Dividing by $-2$ reverses the inequality:

$$
x>-2.
$$

Therefore,

$$
\boxed{x\in(-2,\infty)}
$$

### Important Note {.red}

Multiplication or division by a negative number reverses the inequality.

<div class="example-end">$\blacksquare$</div>

## Example 5 {.green}

Solve

$$
2<3x-1<8.
$$

## Solution {.green}

Adding $1$ to all three parts,

$$
3<3x<9.
$$

Dividing all parts by $3$,

$$
1<x<3.
$$

Therefore,

$$
\boxed{x\in(1,3)}
$$

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question No. 1 {.red}

Express the inequality

$$
-4\leq x<3
$$

in interval notation.

## Question No. 2 {.red}

Solve

$$
-3x+6\geq12
$$

and express your answer in interval notation.

<div class="question-end">$\blacksquare$</div>

# Objective 2: Absolute Value as Distance

- Intervals and inequalities describe **where a number is**.

- Absolute value gives us a way to describe **how far one number is from another**.

## What Is Absolute Value?

- The **absolute value of a number** is its **distance from zero**.

- For example,

$$
|5|=5
$$

- because $5$ is $5$ units from zero.

- Also,

$$
|-5|=5
$$

- because $-5$ is also $5$ units from zero.

<div style="text-align: center;">
<img src="../images/0504.png" style="width: 1600px; border-radius: 12px; display: block; margin: 0 auto 10px auto;">

<span><strong>Figure 4.</strong> Absolute value as distance from $0$.</span>
</div>

Therefore,

$$
|x|\geq0.
$$

## Absolute Value as Distance Between Two Numbers

- The distance between $x$ and $c$ is

$$
|x-c|.
$$

- For example, the distance between $x=3$ and $c=7$ is

$$
|3-7|=|-4|=4.
$$

- The distance between $x=9$ and $c=7$ is

$$
|9-7|=2.
$$

Thus,

$$
|x-c|=\text{distance from }x\text{ to }c.
$$

- This interpretation is more important for limits than simply memorizing the definition of absolute value.

## Absolute-Value Equations

- Consider

$$
|x|=3.
$$

- This means that $x$ is exactly $3$ units from zero.

- Therefore,

$$
\boxed{|x|=3\iff x=\pm3}
$$

## Example 6 {.green}

Solve

$$
|x-4|=2.
$$

## Solution {.green}

The equation $|x-4|=2$ means that $x$ is exactly $2$ units from $4$.

Therefore,

$$
x-4=2
\qquad
\text{or}
\qquad
x-4=-2.
$$

Thus,

$$
x=6
\qquad
\text{or}
\qquad
x=2.
$$

Hence,

$$
\boxed{x=2,6}
$$

<div class="example-end">$\blacksquare$</div>

## Absolute-Value Inequalities

- Consider

$$
|x|<3.
$$

- This means that the distance of $x$ from zero is less than $3$.

- Therefore, $x$ must lie between $-3$ and $3$:

$$
-3<x<3.
$$

- Thus,

$$
\boxed{|x|<3\iff-3<x<3}
$$

### Fundamental Rule

- For $a>0$,

$$
|x|<a\iff-a<x<a.
$$

- More generally,

$$
\boxed{|x-c|<a\iff c-a<x<c+a}.
$$

- This is one of the most important translations for limits.

## Example 7 {.green}

Solve

$$
|x-5|<2.
$$

## Solution {.green}

Using the fundamental rule,

$$
-2<x-5<2.
$$

Adding $5$ to all parts,

$$
3<x<7.
$$

Therefore,

$$
\boxed{x\in(3,7)}
$$

### Logic {.green}

$|x-5|<2$ means that $x$ is within $2$ units of $5$.

Therefore,

$$
(5-2,5+2)=(3,7).
$$

<div class="example-end">$\blacksquare$</div>

## Example 8 {.green}

Solve

$$
|2x-8|<2.
$$

## Solution {.green}

We write

$$
-2<2x-8<2.
$$

Adding $8$ to all parts,

$$
6<2x<10.
$$

Dividing all parts by $2$,

$$
3<x<5.
$$

Therefore,

$$
\boxed{x\in(3,5)}
$$

- The interval $(3,5)$ is centered at $4$.

- Its equivalent distance form is

$$
\boxed{|x-4|<1}.
$$

- This form says that $x$ is within $1$ unit of $4$.

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

Solve

$$
|x-3|<4.
$$

## Question 2 {.red}

Solve

$$
|2x+4|\leq6.
$$

<div class="question-end">$\blacksquare$</div>

# Objective 3: From Distance to the Language of Limits

- We now combine intervals, inequalities, and absolute value.

- This is the central foundation for understanding $x\rightarrow c$.

## What Does “Close to $c$” Mean?

- Suppose we say, "$x$ is close to $c$."

- Mathematically, we can specify the allowed distance using a positive number $\delta$:

$$
|x-c|<\delta,
\qquad \delta>0.
$$

- This means that $x$ is less than $\delta$ units away from $c$.

- Using the fundamental absolute-value rule,

$$
|x-c|<\delta
\iff
c-\delta<x<c+\delta.
$$

- In interval notation,

$$
\boxed{|x-c|<\delta
\iff
x\in(c-\delta,c+\delta)}.
$$

## Neighborhood Around $c$

- The interval

$$
(c-\delta,c+\delta)
$$

- is a symmetric interval centered at $c$.

- Its radius is $\delta$.

- For example, let

$$
c=4,\qquad\delta=1.
$$

- Then

$$
(c-\delta,c+\delta)=(3,5).
$$

- Therefore,

$$
|x-4|<1
\iff
3<x<5.
$$

- This interval is called a **neighborhood of $c$**.

## Example 9 {.green}

Rewrite

$$
|x-6|<0.5
$$

as an interval.

## Solution {.green}

Using

$$
|x-c|<\delta
\iff
c-\delta<x<c+\delta,
$$

we get

$$
6-0.5<x<6+0.5.
$$

Therefore,

$$
\boxed{5.5<x<6.5}
$$

Or,

$$
\boxed{x\in(5.5,6.5)}.
$$

<div class="example-end">$\blacksquare$</div>

## What Does $x\rightarrow c$ Mean?

- When we write

$$
x\rightarrow c,
$$

- we are interested in values of $x$ that get closer and closer to $c$.

- In a limit, we do not require $x=c$.

- Therefore, we use

$$
0<|x-c|<\delta.
$$

- The condition

$$
|x-c|<\delta
$$

- puts $x$ inside the neighborhood of $c$.

- The condition

$$
0<|x-c|
$$

- ensures that

$$
x\neq c.
$$

- Thus,

$$
\boxed{0<|x-c|<\delta}
$$

- means that $x$ is within $\delta$ units of $c$, but $x$ is not equal to $c$.

## Deleted Neighborhood

- The neighborhood

$$
(c-\delta,c+\delta)
$$

- contains the point $c$.

- But

$$
0<|x-c|<\delta
$$

- excludes $c$.

- Therefore, the corresponding deleted neighborhood is

$$
\boxed{(c-\delta,c)\cup(c,c+\delta)}.
$$

- This distinction is fundamental because a limit studies the behavior of $f(x)$ as $x$ approaches $c$, not necessarily the value of $f(c)$.

## One-Sided Neighborhoods

- Limits can also involve approaching $c$ from only one side.

- From the right,

$$
x>c.
$$

- Within $\delta$ units from the right,

$$
c<x<c+\delta.
$$

- From the left,

$$
x<c.
$$

- Within $\delta$ units from the left,

$$
c-\delta<x<c.
$$

- These intervals provide the basic language for right-hand and left-hand limits.

## Example 10 {.green}

Let

$$
c=3,\qquad\delta=0.2.
$$

Describe the points within $0.2$ units of $3$, from the right.

## Solution {.green}

We need

$$
3<x<3.2.
$$

Therefore,

$$
\boxed{x\in(3,3.2)}.
$$

<div class="example-end">$\blacksquare$</div>

## Example 11 {.green}

Let

$$
c=3,\qquad\delta=0.2.
$$

Describe the points within $0.2$ units of $3$, from the left.

## Solution {.green}

We need

$$
2.8<x<3.
$$

Therefore,

$$
\boxed{x\in(2.8,3)}.
$$

<div class="example-end">$\blacksquare$</div>

## From Input Distance to Output Distance

- The idea of distance will eventually be applied to both the input and the output of a function.

- The input distance from $x$ to $c$ is

$$
|x-c|.
$$

- The output distance from $f(x)$ to a number $L$ is

$$
|f(x)-L|.
$$

- Thus, when studying a limit, we will compare:

$$
\underbrace{|x-c|}_{\text{input distance}}
\qquad\longrightarrow\qquad
\underbrace{|f(x)-L|}_{\text{output distance}}.
$$

- The important idea at this stage is not the formal definition of a limit, but the meaning of these two distances.

## Example 12 {.green}

Suppose

$$
f(x)=2x-1.
$$

We want $f(x)$ to be within $2$ units of $7$.

Write the corresponding condition on $x$.

## Solution {.green}

We want

$$
|f(x)-7|<2.
$$

Substituting $f(x)=2x-1$,

$$
|2x-1-7|<2.
$$

Thus,

$$
|2x-8|<2.
$$

From Objective 2,

$$
3<x<5.
$$

Therefore,

$$
\boxed{|f(x)-7|<2\quad\text{whenever}\quad3<x<5.}
$$

- Since

$$
3<x<5
\iff
|x-4|<1,
$$

- we can also write

$$
\boxed{|f(x)-7|<2
\quad\text{whenever}\quad
|x-4|<1.}
$$

- This example shows how a condition on the output can be translated into a condition on the input.

<div class="example-end">$\blacksquare$</div>

# Quick Check

## Question 1 {.red}

Rewrite

$$
|x-4|<0.2
$$

as an interval.

## Question 2 {.red}

If

$$
0<|x-3|<0.5,
$$

describe the corresponding interval(s) for $x$.

<div class="question-end">$\blacksquare$</div>

# Summary

- Today we built the mathematical language needed before studying limits.

- We learned that inequalities describe the location of numbers on the real number line:

$$
\boxed{a<x<b\iff x\in(a,b)}.
$$

- We learned that parentheses indicate excluded endpoints and square brackets indicate included endpoints.

- The most important interpretation is

$$
\boxed{|x-c|=\text{distance between }x\text{ and }c}.
$$

- Therefore,

$$
\boxed{|x-c|<a\iff c-a<x<c+a}.
$$

- Equivalently,

$$
\boxed{|x-c|<\delta
\iff
x\in(c-\delta,c+\delta)}.
$$

- If the point $c$ is excluded,

$$
\boxed{0<|x-c|<\delta}
$$

- corresponds to the deleted neighborhood

$$
\boxed{x\in(c-\delta,c)\cup(c,c+\delta)}.
$$

- We also learned the one-sided neighborhoods:

$$
\boxed{c<x<c+\delta}
$$

- for approaching $c$ from the right, and

$$
\boxed{c-\delta<x<c}
$$

- for approaching $c$ from the left.

- Finally, we introduced the two distances that will appear throughout the study of limits:

$$
\boxed{|x-c|}
\qquad\text{and}\qquad
\boxed{|f(x)-L|}.
$$

- The central idea is therefore

$$
\boxed{
\text{Location}
\;\longrightarrow\;
\text{Distance}
\;\longrightarrow\;
\text{Neighborhood}
\;\longrightarrow\;
x\rightarrow c
\;\longrightarrow\;
\text{Limits}
}
$$

- These ideas provide the required foundation for the next topics: **the idea of a limit, calculating limits, continuity, and derivatives**.

# Exercises

## Important Note {.red}

The goal of this lecture is not to memorize rules. You should be able to move fluently between the following forms:

$$
a<x<b,
\qquad
x\in(a,b),
\qquad
|x-c|<\delta.
$$

You should also be able to explain each expression geometrically on the real number line.

