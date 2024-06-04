# -*- coding: utf-8 -*-
"""lab3_alpha_beta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rgj0fT3Q9ak-VAJrVFd0kRG3q2sVvrMU
"""

# name: Naveya Novely Datta
# ID: 21101321
# Section: 04

########################Task 1:###########################################

import random
import math

print("Task 1")
id = input("Enter ID: ")
#3print(id)

min_point = int(id[4])
max_point = int((id[-1]+id[-2]))*1.5
points_to_win = int(id[-1]+id[-2])
# print(min_point)
# print(max_point)
# print(points_to_win)

def alpha_beta(position,depth,maxamizing_player,alpha,beta,limits):
  if depth ==0:
    return limits[position]

  if maxamizing_player:
    max_val = -1*math.inf
    for i in range(2):   ############because 2 branch##############
      eval = alpha_beta((position*2)+i,depth-1,False,alpha,beta,limits) ##############limits list itiration and recursion################
      max_val = max(max_val,eval)
      alpha = max(alpha,max_val)
      if alpha >= beta:
        break
    return max_val

  else:
    min_val = math.inf
    for i in range(2):
      eval = alpha_beta((position*2)+i,depth-1,True,alpha,beta,limits)
      min_val = min(min_val,eval)
      beta = min(beta,min_val)
      if alpha >= beta:
        break
    return min_val

# limits = [66, 74, 14, 73, 19, 26, 32, 40]

limits = []
for i in range(8):
  random_point = random.randint(min_point, max_point)
  limits.append(random_point)
# print(limits)

depth = 3
a = -1*math.inf
b = math.inf

output=alpha_beta(0, depth, True,a,b, limits)
# print(output)

# win_point = 56

print("limits: ",limits)
print("Total points to win: ",points_to_win)
print("Achieved point by applying alpha-beta pruning = ",output)

if output >= points_to_win:
  print("The winner is Optimus Prime")
else:
  print("Winner is Megatron")

############################# Task 2:#####################################

print("Task 2")
shuffels = int(id[3])
#print(shuffels)

point_list = []
for i in range(shuffels):
  limits = []
  for i in range(8):
    random_point = random.randint(min_point, max_point)
    limits.append(random_point)
    a = -1*math.inf
    b = math.inf

  def alpha_beta(position,depth,maxamizing_player,alpha,beta,limits):
    if depth ==0:
      return limits[position]

    if maxamizing_player:
      max_val = -1*math.inf
      for i in range(2):
        eval = alpha_beta((position*2)+i,depth-1,False,alpha,beta,limits)
        max_val = max(max_val,eval)
        alpha = max(max_val,alpha)
        if alpha >= beta:
          break
      return max_val

    else:
      min_val = math.inf
      for i in range(2):
        eval = alpha_beta((position*2)+i,depth-1,True,alpha,beta,limits)
        min_val = min(min_val,eval)
        beta = min(min_val,beta)
        if alpha >= beta:
          break
      return min_val

  depth = 3
  a = -1*math.inf
  b = math.inf

  output_1=alpha_beta(0, depth, True,a,b, limits)
  point_list.append(output_1)
#print(point_list)

count = 0
for i in point_list:
  if i >= points_to_win:
    count += 1
highest_point = max(point_list)

print("After the shuffle:")
print("List of all points values from each shuffles: ",point_list)
print("The maximum value of all shuffles: ",highest_point)
print("Won "+str(count)+" times out of "+str(shuffels)+" number of shuffles")