'''
  File name: nonMaxSup.py
  Author: Luoli Wang
  Date created: Sep 20 2019
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''

from helpers import find_neighbor


def nonMaxSup(Mag, Ori):
    mag1, mag2 = find_neighbor(Mag, Ori)
    C1 = Mag >= mag1
    C2 = Mag >= mag2
    M = C1 * C2
    return M.astype(int)


