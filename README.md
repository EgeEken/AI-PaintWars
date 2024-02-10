# AI Paint Wars

This repository includes my code, files and descriptions (text and visual) of my progress for the project, for instructions on how to run them, refer to the project repository created by the class teachers: [LU3IN025-robots](https://github.com/nekonaute/SU-LU3IN025-robots/)

## Description
Two teams of 8 robots ("red team" and "blue team") compete to visit an arena divided into squares. A square belongs to the team that visited it last. Time is limited, and the team with the most squares after 2000 iterations wins. This is a competitive variation on the multi-agent patrol problem, a classic robotics problem.

## Rules
- no communication
- no additional information beyond that provided by sensors
- no construction or use of maps

## My Progress 

After trying out a few conditional algorithms, and not being satisfied with the success rate, as well as being a bit frustrated with dealing with edge cases (often quite literally "edge" cases, where the robots would get stuck on edges because the parameter i chose for rotation was a little too high for example), i decided to train a Neural Network using an evolutionary learning algorithm.

At first i used the model recommended by the class material, which would judge the quality of the model by the distance taken from the starting point, which could correctly incentivize avoiding obstacles, but also to simply move away rather than go over as much land as possible. This is not the best way to train a model for the goal of winning at the paintwars game, for this reason:

![image](https://github.com/EgeEken/AI-PaintWars/assets/96302110/2b8de771-15f8-4211-93d0-d6dbd19eadb3)

So to fit better for the task, i changed the rewarding mechanisms to select the "Superior Genes" which would be selected and then mutated to look for a new best gene parameter to "evolve". The new version i made instead looks for the amount of tiles went over. 

I trained a few models this way but after noticing the success of the one trained on an empty arena alone, i decided to make a full team of the models trained on arena 0, which had a pretty good success rate of 68% against the opponent given to us by the teacher

The training is done on the file NN_algorithm.py, i implemented a pretty intuitive system to change training parameters, all the learning parameters can be tweaked with these variables:

```python
learning_rate = 0.9
mutation_rate = 10

w_size = 10
```
The code prepares the correct sizes for the parameters and weights and biases accordingly, so no need to add or change code to make it work



