# Gravity Simulator

This is a gravity simulator where you can simulate the movement and interaction of multiple massive objects in a vacuum caused by gravity.

## Applications

Solar systems simulations, orbital mechanics, interplanetary travel planning, asteroid collapse prediction, having fun etc.

## The Physics

For now, we are just using the good old classical Newtonian gravity:

$$ F = G \frac{m_1 \cdot m_2}{r^2}  $$

Pay us and maybe we'll do Einstein tensors. Also, your machine probably can't handle that anyway.

The formula above describes the gravitational 'force' between two bodies. Applying the formula for each pair of bodies, we get the acceleration at each moment in time.

Supports N number of bodies with their own mass, initial position, velocity and acceleration. It wouldn't be fun if we couldn't simulate multiple objects.


## The Coding

Currently made with Object Oriented approach, calculating forces between all possible bodies. If you have $n$ bodies, there will be
$S = 1 + 2 + ... + (n - 1)$
pairs of forces.

$O(n^2)$ time complexity.

The program calculates the acceleration caused by gravity from each body for each body, then calculates new velocity, then updates position.


## How to use

Clone the git repository:
```
$ git clone https://github.com/masroor47/gravity-simulator.git
```

In the root folder create a virtual environment:
```
$ virtualenv venv
```

Mac / Linux
```
$ source venv/bin/activate
```
Install requirements and run:
```
$ pip install -r requirements.txt

$ python simulator/main
```