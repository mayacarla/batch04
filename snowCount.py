#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints: the snow count of inputted file name

import matplotlib.pyplot as plt
import numpy as np

fileName = input("Enter file name: ")

ca = plt.imread(fileName)
countSnow = 0
t = .75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i, j, 0] > t) and (ca[i, j, 1] > t) and (ca[i, j, 2] > t):
            countSnow += 1


print("Snow count  is ", str(countSnow))
