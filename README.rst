.. -*- mode: rst -*-

Chaotic attractors
==================

Python scripts for some 3rd order chaotic systems (Lorenz attractor,
Nose-Hoover oscillator, Rossler attractor, Riktake model, Duffing map etc.)

Main info
~~~~~~~~~

+---------------------+-----------------------------------------+
| **Title**           | Analysis and modeling chaotic systems   |
+=====================+=========================================+
| **Author**          | Alexander Kapitanov                     |
+---------------------+-----------------------------------------+
| **Contact**         | <email_hidden>                          |
+---------------------+-----------------------------------------+
| **Project lang**    | Python 3                                |
+---------------------+-----------------------------------------+
| **First Release**   | 30 May 2019                             |
+---------------------+-----------------------------------------+
| **License**         | GNU GPL 3.0.                            |
+---------------------+-----------------------------------------+

Dependencies
~~~~~~~~~~~~

Project requires:

- Python (>= 3.6)
- NumPy (>= 1.19.0)
- SciPy (>= 1.5.1)
- Pandas (>= 1.1.0)
- Matplotlib (>= 3.2.2)
- Pytest (>= 5.4.3)
- Pre-commit (>= 2.6.0)

Source code
~~~~~~~~~~~

You can check the latest sources with the command::

    git clone https://github.com/capitanov/chaospy.git

Chaotic model
~~~~~~~~~~~~~~

Lorenz attractor

::

    dx/dt = sigma * (y - x)
    dy/dt = rho * (x - z) - y
    dz/dt = x * y - beta * z

where sigma= 10, rho= 28 and beta= 8/3.

.. image:: https://raw.githubusercontent.com/capitanov/chaospy/master/img/Lorenz_3d.gif?sanitize=true

See Also
~~~~~~~~

- `Wikipedia -> chaotic attractors. <https://en.wikipedia.org/wiki/Attractor>`__
- `My articles on habrahabr. (russian language) <https://habr.com/users/capitanov/topics/>`__
