# Kinematics

> [!IMPORTANT]
> See [Vector revision](./vectors.md) to review on vectors!

## Kinematics and Dynamics

* The study describes motion without regard to its cause is called **kinematics**
* The study fo motion and of of physical concepts such as force and mass is called **dynamics**

## Motion in One and Two Dimension

* Motion in 1 Dimension (1D) is the motion on a straight line.
* Motion in 2 Dimension (2D) is the motion on a plane.

## Position and Displacement

* **Position** is measured in reference to the coordination system and get the numerical value of $x$.
* The **displacement** of an object is defined as its change in position and is given by $\Delta = x_f - x_i$, where $x_f$ is the final known position and $x_i$ is the initial position.

> [!TIP]
> **Displacement** could be negative ot positive and displacement is *NOT* the same as distance traveled.

> [!NOTE]
> **Notation** : $x(t)$ is the location of particle/object as a function of time and the initial position is noted as $x_0 = x(t_0), t_0$ is usually selected as $t_0 = 0$.

## Velocity and Speed

* **Velocity** is defined as change of displacement over time. Velocity could be positive or negative.
* **Speed** is defined as change of *distance* over time. Speed is always positive.

### Velocity

#### Average Velocity

* **Average velocity** is defined as: 
$$\vec{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

> [!NOTE]
> **Average velocity** does *NOT* take into account the details of what happens during the interval of time.

#### Instantaneous Velocity

* **Instantaneous velocity** is the limit of the average velocity as the time interval becomes infinitestimally small as defined: 
$$v = \lim_{\Delta t \to 0}\frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

## Acceleration

* **Acceleration** could be defined as the change of velocity over time.
* **Average Acceleration** is defined as
$$\vec{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$
* and **Instantaneous Acceleration** is defined as:
$$a = \lim_{\Delta t \to 0}\frac{\Delta v}{\Delta t} = \frac{dv}{dt}$$

### Motion with Constant Acceleration

The motion with constant acceleration can be describes as:

* The first equation of motion relates to velocity to time:

> <details>    
>   $$a = \frac{dv}{dt} \Rightarrow dv = adt$$
> 
>   $$\int_{v_0}^{v_t}dv = \int_{t_0}^{t}adt = a \int_{t_0}^{t}dt = a(t - t_0)$$
> 
>   $$v - v_0 = a(t - t_0) = at \text{ as } (t_0 = 0)$$
> </details>

$$v = v_0 + at$$ 

* Similarly, The second equation of motion relates to position to time:

> <details>
>   $$v = \frac{dx}{dt} \Rightarrow dx = (v)dt = (v_0 + at)dt$$
> 
>   $$\int_{x_0}^{x}dx = \int_{t_0}^{t}v_0 + a \int_{t_0}^{t}t = v_0(t - t_0) + \frac{1}{2}a(t^2 - t^2_0)$$
>
>   $$x - x_0 = v_0(t - t_0) + \frac{1}{2}a(t^2 - t^2_0) = v_0 t + \frac{1}{2}a t^2 \text{ as } (t_0 = 0)$$
> </details>
$$x = x_0 + v_0 t + \frac{1}{2}at^2$$

* The third equation of motion relates to velocity to position: 

> <details>
> $$\frac{dv}{ds} = \frac{dv}{ds} \frac{dt}{dt} = \frac{dv}{dt} \frac{dt}{ds} = a \frac{1}{v}$$
> 
> $$v dv = a ds \Rightarrow \int_{v_0}^{v}v dv = \int_{x_0}^{x}a ds \Rightarrow \frac{1}{2} (v^2 - v^2_0) = a(s - s_0)$$
> </details>

$$v^2 = v^2_0 + 2a(x - x_0)$$

## Free Fall

Visit [Special types of Motion](./kinematics-special.md)

## Additional Materials

1. [Crash Course Physics Preview](https://youtu.be/OoO5d5P0Jn4)
2. [Motion in a Straight Line](https://youtu.be/ZM8ECpBuQYE)
