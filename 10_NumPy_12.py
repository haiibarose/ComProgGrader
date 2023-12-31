import numpy as np


def toCelsius(f):
    c = (f-32)*(5/9)
    return c


def BMI(wh):
    bmi = wh[:, 0]/np.square(wh[:, 1]/100)
    return bmi


def distanceTo(p, Points):
    distance = np.sqrt(np.abs(Points[:, 0]-p[0])**2 + np.abs(Points[:, 1]-p[1])**2)
    return distance


exec(input().strip())