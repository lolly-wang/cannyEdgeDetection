'''
  File name: helpers.py
  Author: Luoli Wang
  Date created: Sep 20 2019
'''

'''
  File clarification:
    Helpers file that contributes the project
    You can design any helper function in this file to improve algorithm
'''
import numpy as np
from interp import interp2


# Given mag map and the orientation of neighbor points, return two neighbor maps
def find_neighbor(Mag, Ori):
    nr = Mag.shape[0]
    nc = Mag.shape[1]
    x, y = np.meshgrid(np.arange(nc), np.arange(nr))

    x1 = np.cos(Ori) + x
    y1 = np.sin(Ori) + y
    x1 = np.clip(x1, 0, nc - 1)
    y1 = np.clip(y1, 0, nr - 1)

    x2 = np.cos(Ori + np.pi) + x
    y2 = np.sin(Ori + np.pi) + y
    x2 = np.clip(x2, 0, nc - 1)
    y2 = np.clip(y2, 0, nr - 1)

    mag1 = interp2(Mag, x1, y1)
    mag2 = interp2(Mag, x2, y2)

    return mag1, mag2


