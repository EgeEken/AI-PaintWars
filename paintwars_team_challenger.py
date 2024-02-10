# Projet "robotique" IA&Jeux 2023/2024
#
# 
#  Prénom Nom: Tarik Ege EKEN

import numpy as np
import math


#t = ["", "", "", "", "", "", "", ""]
best_0 = ["best_0" for i in range(8)]


t = best_0 

param1 = np.loadtxt(t[0])
param2 = np.loadtxt(t[1])
param3 = np.loadtxt(t[2])
param4 = np.loadtxt(t[3])
param5 = np.loadtxt(t[4])
param6 = np.loadtxt(t[5])
param7 = np.loadtxt(t[6])
param8 = np.loadtxt(t[7])

def NN_player(param, sensors):
	
	s = np.array([sensors["sensor_back_right"]["distance"],
			sensors["sensor_back"]["distance"],
			sensors["sensor_back_left"]["distance"],
			sensors["sensor_left"]["distance"],
			sensors["sensor_front_left"]["distance"],
			sensors["sensor_front"]["distance"],
			sensors["sensor_front_right"]["distance"],
			sensors["sensor_right"]["distance"]])
	len_s = len(s)

	paramcount = len(param)
	w_size = (paramcount - (len_s*4) - 4) // (len_s + 1)
	
	s = s.reshape((1,len_s))
	
	rot_w1 = np.array(param[:w_size*len_s]).reshape((len_s,w_size))
	rot_w2 = np.array(param[w_size*len_s:w_size*(len_s+1)]).reshape((w_size,1))
	
	tra_w1 = np.array(param[w_size*(len_s+1):w_size*(len_s+1) + (len_s*4)]).reshape((len_s,4))
	tra_w2 = np.array(param[w_size*(len_s+1) + (len_s*4):paramcount]).reshape((4,1))
	
	
	rotation = s.dot(rot_w1).dot(rot_w2)[0][0]
	
	translation = s.dot(tra_w1).dot(tra_w2)[0][0]
	
	return math.tanh(translation), math.tanh(rotation)


def get_team_name():
    return "EGE" # à compléter (comme vous voulez)

def step(robotId, sensors):
	global param1, param2, param3, param4
	
	if robotId % 8 == 0:
		translation, rotation = NN_player(param1, sensors)
		
	if robotId % 8 == 1:
		translation, rotation = NN_player(param2, sensors)
		
	if robotId % 8 == 2:
		translation, rotation = NN_player(param3, sensors)
		
	if robotId % 8 == 3:
		translation, rotation = NN_player(param4, sensors)
		
	if robotId % 8 == 4:
		translation, rotation = NN_player(param5, sensors)
		
	if robotId % 8 == 5:
		translation, rotation = NN_player(param6, sensors)
		
	if robotId % 8 == 6:
		#translation, rotation = NN_player(param7, sensors)
		translation = 1
		rotation = 0
		if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
			rotation = 0.5
		elif sensors["sensor_front_right"]["distance"] < 1:
			rotation = -0.5
			
	if robotId % 8 == 7:
		translation, rotation = NN_player(param8, sensors)
	
	
	return translation, rotation
