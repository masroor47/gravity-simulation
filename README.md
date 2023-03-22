# Gravity Simulator

This is a gravity simulator where you can simulate the movement and interaction of multiple massive objects in vacuum caused by gravity.

## Applications

Solar systems simulations, orbital mechanics, interplanetary travel planning, asteroid collapse prediction, having fun etc.

## The Physics

For now, we are just using the good old classic Newtonian gravity:

$ F = G \frac{m1 m2}{r^2}  $

Pay us and maybe we'll do Einstein tensors. Also, your machine probably can't handle that anyway.

The formula above describes the gravitational 'force' between two objects in the absence of any other objects. But it wouldn't be fun if we couldn't simulate multiple objects.


## The Coding

Currently made with Object Oriented approach, calculating forces between all possible bodies. If you have $n$ bodies, there will be
$ S = 1 + 2 + ... + (n - 1) $
pairs of forces.

$ O(n^2) $ time complexity.

The program calculates the acceleration caused by gravity from each body for each body, then calculates new velocity, then updates position.


## How to use

From the root folder run:
```
python simulator/main
```