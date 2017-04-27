# from scipy import spatial

# dataSetI = [3, 54, 3, 2]
# dataSetII = [3, 14, 7, 2]
# result = 1 - spatial.distance.cosine(dataSetI, dataSetII)

# print(result)


import math
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sum_of_xx, sum_of_xy, sum_of_yy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sum_of_xx += x*x
        sum_of_yy += y*y
        sum_of_xy += x*y
    return (sum_of_xy)/math.sqrt((sum_of_xx)*(sum_of_yy))

v1,v2 = [2, 54, 13, 15], [2, 54, 13, 15]
print(v1, v2, cosine_similarity(v1,v2))