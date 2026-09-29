# Calculus and Analytical Geometry

## Derivatives

### Dr. Aamir Alaud Din

# Derivatives in General

- Consider the general function

$$
y = f(x)  \qquad (1)
$$

- We are interested in finding the instantaneous change in $y$ with respect to $x$.

- Before looking into the instantaneous change, we look into the change in $y$ as $x$ changes.

- This change can be computed as shown below.

$$
y + \Delta y = f(x + \Delta x) \qquad (2)
$$

- We are interested in finding the change in $y$ $\left( \Delta y \right)$ per unit change in $x$ $\left( \Delta x \right)$ _i.e.,_ how much $y$ changes per unit change in $x$ $\left( \frac{\Delta y}{\Delta x} \right)$.

- Therefore, we modify $(2)$  as shown  below.

$$
\begin{align}
\Delta y &= f(x  + \Delta x) - y \\
&= f(x  + \Delta x) - f(x) \qquad \qquad \qquad (\text{Using equation }(1))
\end{align}
$$

- In order to arrive at $\frac{\Delta y}{\Delta x}$,  we  divide both  sides of  above equation.

$$
\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

-  We can modify the denominator of the above equations  as shown below.

$$
\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{(x  + \Delta  x) - \Delta x} \qquad (3) 
$$

- Let

$$
\begin{align}
y_1  &=  f(x) \\
y_2 &= f(x +  \Delta  x)  \\
x_1  &= \Delta x \\
x_2  &= x + \Delta x
\end{align}
$$

- Using the above four relations, we can write equation $(3)$ as follows.

$$
\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{(x  + \Delta  x) - \Delta x} = \frac{y_2 - y_1}{x_2 - x_1} \qquad (4) 
$$

- It means, equation $(3)$ represents the  slope of the line.

- Note that the  points on the right  hand side  of equation $(3)$ are the coordinates of points $P$ and $Q$ in figure 2.

- These points intersect at two different points on the graph, therefore the line passing through these points is the secant line and the slope of the line in equation $(3)$ or $(4)$ is the slope of the secant line.

- In real physical world, we deal  with problems involving continuously varying quantities and in these problems  we need  instantaneous changes in the dependent variable with respect to  (per unit change) the independent  variable.

- Let's represent the small change with $\delta$ and  this  change is so small that $\delta \rightarrow 0$.

- Therefore, we modify equation $(3)$  as shown below.

$$
\lim_{\delta x \rightarrow 0} \frac{\delta y}{\delta x} = \lim_{\delta x \rightarrow 0} \frac{f(x + \delta x) -  f(x)}{\delta x} \qquad (5)
$$

- Since $\delta x \rightarrow 0$,  it means the points $x$  and  $x + \delta x$  are very close  such that

$$
(x + \delta x) - x \approx 0
$$

- It confirms that point $P$  approaches  point  $Q$ and therefore secant line becomes the tangent line as shown in figure.

- This gives the instantaneous change.

- In short form we write

$$
\lim_{\delta x \rightarrow 0} \frac{\delta y}{\delta x} = \frac{dy}{dx}
$$

- So, finally we can write the slope of tangent line (equation $(5)$) as given below.

$$
\frac{dy}{dx} = \lim_{\delta x \rightarrow 0} \frac{f(x + \delta x) -  f(x)}{\delta x} \qquad (6)
$$

- Suppose the angle between the tangent line with the horizontal is $\theta$, then the angle between the tangent line and the line $\delta x$ is also $\theta$, however the triangle is a micro triangle.

- In the micro triangle, we have the following trigonometric identity.

$$
\tan \theta = \frac{f(x + \delta x) - f(x)}{\delta x}
$$

- Since $\delta x \rightarrow 0$, we can rewrite the above equation as shown below.

$$
\tan \theta = \lim_{\delta x \rightarrow 0} \frac{f(x + \delta x) - f(x)}{\delta x} \qquad (7)
$$

- Equations (6) and (7) confirm the following identity.

$$
\tan \theta = \frac{dy}{dx}
$$

- This is because, $\tan \theta$ is also the slope of line (hypotenuse).

- Finally, equation $(6)$ says that we can find derivative along the curve, but in real world problems we need derivatives at fixed points _e.g.,_ at $t = 5$ or $x=3$ etc.

# Derivatives in Real World

- Consider the following simple trigonometric function.

$$
y = \sin x
$$

- The first derivative of this function is

$$
\frac{dy}{dx} = \cos x
$$

- Instead of using the first principle, we are interested in derivatives at fixed points.

- For a complete understanding, we consider the following points.

$$
x = \frac{\pi}{4}, \frac{\pi}{2}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{3\pi}{2}, \frac{7\pi}{4}
$$

## Case-I: $\mathbf{x = \frac{\pi}{4}}$

- For $x = \pi/4$,

$$
y = \sin (\pi/4) = 0.707
$$

- So, the point is $(x, y) = (\pi/4, 0.707)$.

- Now,

$$
m = \frac{dy}{dx} = \cos x = \cos (\pi/4) = 0.707
$$

- Using the point $(\pi/4, 0.707)$ slope $(0.707)$ form, we can find the $y$-intercept as given below.

$$
y - y_1 = m(x - x_1)
$$

$$
y - 0.707 = 0.707 (x - \pi/4)
$$

- On $y$-axis, $x=0$, therefore

$$
y - 0.707 = -0.707(\pi/4)
$$

$$
y = 0.707 -0.707(\pi/4) = 0.1513 = c
$$

- Now, we can write the equation of line.

$$
y = 0.707x + 0.1513
$$

- At $x=0$, $y = 0.1513$ and at $x=\pi/2$, $y=1.262$.

- Therefore, we have two points $(x_1, y_1) = (0, 0.1513)$ and $(x_2, y_2) = (\pi/2, 1.262)$.

- Joining these two points will automatically draw the tangent to the graph of $y=\sin x$ at $x=\pi/4$.
