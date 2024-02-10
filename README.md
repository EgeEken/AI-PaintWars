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

At first i used the model recommended by the class material. Increasing the parameter count, and implementing a two layer neural network system instead of simply 8 parameters that would apply to each sensor directly. This allows for a higher level of "reasoning" to be performed by the algorithm, as now the weights will take into account the relations between the sensors as well.

![image](https://github.com/EgeEken/AI-PaintWars/assets/96302110/a2bce5dc-308a-486d-8f7d-41ce20f4e1bc)

But a core issue is that the model would still only judge the quality of the model by the distance taken from the starting point, which could correctly incentivize avoiding obstacles, but also to simply move away rather than go over as much land as possible. This is not the best way to train a model for the goal of winning at the paintwars game, for this reason:

![image](https://github.com/EgeEken/AI-PaintWars/assets/96302110/1e3b8bdc-6340-4e57-8d43-8251db9e56c3)


So to fit better for the task, i changed the rewarding mechanisms to select the "Superior Genes" which would be selected and then mutated to look for a new best gene parameter to "evolve". The new version i made instead looks for the amount of tiles went over. 

I trained a few models this way but after noticing the success of the one trained on an empty arena alone, i decided to make a full team of the models trained on arena 0, which had a pretty good success rate of 68% against the opponent algorithm given to us by the teacher

The training is done on the file NN_algorithm.py, i implemented a pretty intuitive system to change training parameters, all the learning parameters can be tweaked with these variables:

```python
learning_rate = 0.9
mutation_rate = 10

w_size = 10
```
The code prepares the correct sizes for the parameters and weights accordingly, so no need to add or change code to make it work

```python
sensors = np.array([sensors["sensor_back_right"]["distance"],
			sensors["sensor_back"]["distance"],
			sensors["sensor_back_left"]["distance"],
			sensors["sensor_left"]["distance"],
			sensors["sensor_front_left"]["distance"],
			sensors["sensor_front"]["distance"],
			sensors["sensor_front_right"]["distance"],
			sensors["sensor_right"]["distance"]])
	
len_s = len(sensors)
sensors = sensors.reshape((1,len_s))
rot_w1 = np.array(param[:w_size*len_s]).reshape((len_s,w_size))
rot_w2 = np.array(param[w_size*len_s:w_size*(len_s+1)]).reshape((w_size,1))
	
tra_w1 = np.array(param[w_size*(len_s+1):w_size*(len_s+1) + (len_s*4)]).reshape((len_s,4))
tra_w2 = np.array(param[w_size*(len_s+1) + (len_s*4):paramcount]).reshape((4,1))
	
rotation = sensors.dot(rot_w1).dot(rot_w2)[0][0]
	
translation = sensors.dot(tra_w1).dot(tra_w2)[0][0]
	
translation = math.tanh(translation)
rotation = math.tanh(rotation)
```

If there is already a base model that is intended to be used as a starting point for the model, it will load the file "bestParam1" and use it as the weights, if no such bestParam1 file is found, it will start fresh with a randomly generated weights parameter

After sufficient training and testing i decided to replace one of the team member robots with a simple algorithm that simply turns around when faced with an obstacle, and this actually ended up giving slightly better results overall, so i kept this as my final version to submit.

Here are some visuals of it in action:

![arena0_](https://github.com/EgeEken/AI-PaintWars/assets/96302110/fbdaa911-a761-4094-9db6-3dae9070c714)

![arena1_](https://github.com/EgeEken/AI-PaintWars/assets/96302110/cff6581a-8cff-4ffa-8ce8-0d5c56b65778)

![arena3_](https://github.com/EgeEken/AI-PaintWars/assets/96302110/a989c7d9-2542-4a6e-854c-6103e5dc8466)

![arena4_](https://github.com/EgeEken/AI-PaintWars/assets/96302110/aed07beb-1284-4b6f-b516-52265517f860)

![arena5_](https://github.com/EgeEken/AI-PaintWars/assets/96302110/598b38da-9b22-449b-b8ce-dec0c4b35366)

I have also made a bash script to run matches with my model against the given opponent model, clean up and save the results in a text file, and then return the number of wins for each side and draws, so thanks to the shell class in the second year for that, here are the results of my final model against the given opponent algorithm:

<img width="256" alt="image" src="https://github.com/EgeEken/AI-PaintWars/assets/96302110/aed9ffdb-ace2-4a17-8e83-9998270d95dd">

