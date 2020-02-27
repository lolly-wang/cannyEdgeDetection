'''
  File name: edgeLink.py
  Author: Luoli Wang
  Date created: Sep 20 2019
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents ，the final canny edge detection map
'''

import numpy as np
from helpers import find_neighbor


def edgeLink(M, Mag, Ori):
    mag = Mag * M
    s = np.copy(mag)
    s[s == 0] = np.nan
    mean = np.nanmean(s)

    hi = 0.7 * mean
    lo = 0.00001 * hi

    strong = mag >= hi
    while True:
        weak = np.logical_and(mag >= lo, mag < hi)
        mag1, mag2 = find_neighbor(mag, Ori + np.pi / 2)
        has_strong_neighbor = np.logical_or(mag1 >= hi, mag2 >= hi)
        candidate = np.logical_and(has_strong_neighbor, weak)

        if candidate.any() != 0:
            strong = np.logical_or(strong, candidate)
            mag = np.maximum(strong * hi, mag)
        else:
            break
    return strong
