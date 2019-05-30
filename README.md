# Chaotic attractors

Python scripts for some 3rd order chaotic systems (Lorenz attractor, Nose-Hoover oscillator, Rossler attractor, Riktake model)

**License: GNU GPL 3.0.**

### Info:

| **Title**         | Analysis and modeling chaotic systems |
| -- | -- |
| **Author**        | Alexander Kapitanov                   |
| **Contact**       | sallador@bk.ru                        |
| **Project lang**  | Python                                |
| **Libraries**     | Numpy, Scipy, etc.                    |
| **First Release** | 30 May 2019                           |
| **Version**       | 1.0                                   |

### List of chaotic 3D systems:

#### Lorenz
```
dx/dt = sigma * (y - x)

dy/dt = rho * (x - z) - y

dz/dt = x * y - beta * z
```
where sigma= 10, rho= 28 and beta= 8/3.

![](https://github.com/capitanov/chaospy/blob/master/img/Lorenz.png)
#### Rossler 3D system
```
dx/dt = -(y + z)

dy/dt = x + a * y

dz/dt = b + z * (x - c)
```
where a = 0.2, b = 0.2 and c = 5.7.

![](https://github.com/capitanov/chaospy/blob/master/img/Rossler_3D.png)
#### Rikitake
```
dx/dt = -mu * x + z * y

dy/dt = -mu * y + x * (z - a)

dz/dt = 1 - x * y
```
where mu= 1, a = 5.

![](https://github.com/capitanov/chaospy/blob/master/img/Rikitake_3D.png)
#### Nose–Hoover
```
dx/dt = y

dy/dt = y * z - x

dz/dt = 1 - y^2
```
Nose-Hoover doesn't have default parameters.
![](https://github.com/capitanov/chaospy/blob/master/img/Nose_Hoover_3D.png)

See more: [Wikipedia about attractors](https://en.wikipedia.org/wiki/Attractor "Attractors")

My topics (Russian lang.): https://habr.com/users/capitanov/topics/
