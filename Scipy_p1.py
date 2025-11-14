from scipy.spatial.distance import euclidean,cityblock,cosine,hamming
import numpy as np
from random import randrange
v1=v2=np.array([])

for i in range(0,randrange(5,15)):
    v1=np.append(v1,randrange(0,10),axis=None)
    v2=np.append(v2,randrange(0,10),axis=None)
print(v1,v2)
print(euclidean(v1,v2))
print(cityblock(v1,v2))
print(hamming([randrange(0,2),randrange(0,2),randrange(0,2)],[randrange(0,2),randrange(0,2),randrange(0,2)]))
print(cosine([randrange(0,2),randrange(0,5),randrange(0,4)],[randrange(0,2),randrange(0,5),randrange(0,4)]))
