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
where mu = 1, a = 5.

![](https://github.com/capitanov/chaospy/blob/master/img/Rikitake_3D.png)
#### Nose–Hoover
```
dx/dt = y
dy/dt = y * z - x
dz/dt = 1 - y^2
```
Nose-Hoover doesn't have default parameters.

![](https://github.com/capitanov/chaospy/blob/master/img/Nose_Hoover_3D.png)
#### Wang system
```
dx/dt = x - y * z
dy/dt = x - y + x * z
dz/dt = -3 * z + x * y
```

![](https://github.com/capitanov/chaospy/blob/master/img/Wang_3D.png)
#### Duffing map
```
dx/dt = y
dy/dt = -a * y - x**3 + b * cos(z)
dz/dt = 1
```
where a = 0.1 and b = 11.

![](https://github.com/capitanov/chaospy/blob/master/img/Duffing_3D.png)
#### Lotka–Volterra
```
dx/dt = x * (1 - x - 9*y)
dy/dt = -y * (1 - 6*x - y + 9*z)
dz/dt = z * (1 - 3*x - z)

```
![](https://github.com/capitanov/chaospy/blob/master/img/Lotka_3D.png)
#### Chua
```
dx/dt = alpha * (y - x - h(t))
dy/dt = x - y + z
dz/dt = -beta * y

ht = mu1*x + 0.5*(mu0 - mu1)*(np.abs(x + 1) - np.abs(x - 1))
```
where alpha = 15.6, beta = 28, mu0 = -1.143, mu1 = -0.714.

![](https://github.com/capitanov/chaospy/blob/master/img/Chua2_3D.png)






See more: [Wikipedia about attractors](https://en.wikipedia.org/wiki/Attractor "Attractors")

My topics (Russian lang.): https://habr.com/users/capitanov/topics/
