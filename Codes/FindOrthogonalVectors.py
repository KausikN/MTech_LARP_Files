'''
Finds combination of vectors that are orthogonal to each other.
'''

# Imports
import numpy as np
from tqdm import tqdm

# Main Functions
def FindOrthogonalVectors_3x3(allowedValues=[-1, 0, 1]):
    '''
    Finds combination of vectors that are orthogonal to each other.
    '''
    # Initialize
    possibleVecs = []
    for i in tqdm(allowedValues):
        for j in allowedValues:
            for k in allowedValues:
                possibleVecs.append([i, j, k])

    # Find orthogonal vectors
    orthogonalVecs = []
    for i in tqdm(range(len(possibleVecs))):
        for j in range(i+1, len(possibleVecs)):
            for k in range(j+1, len(possibleVecs)):
                if np.dot(possibleVecs[i], possibleVecs[j]) == 0 and \
                    np.dot(possibleVecs[i], possibleVecs[k]) == 0 and \
                    np.dot(possibleVecs[j], possibleVecs[k]) == 0:
                    orthogonalVecs.append([possibleVecs[i], possibleVecs[j], possibleVecs[k]])
    # Return
    return orthogonalVecs

def FindPossibleVecs_Recursive(N, allowedValues=[-1, 0, 1], curVec=[]):
    if N <= 0: return [curVec]

    possibleVecs = []
    for i in (allowedValues):
        possibleVecs.extend(FindPossibleVecs_Recursive(N-1, allowedValues, curVec+[i]))
    return possibleVecs

def FindOrthogonalVecs_Recursive(N, possibleVecs=[-1, 0, 1], curVecIndices=[]):
    if N <= 0:
        for i in range(len(curVecIndices)-1):
            for j in range(i+1, len(curVecIndices)):
                if np.dot(possibleVecs[curVecIndices[i]], possibleVecs[curVecIndices[j]]) != 0:
                    return []
        return curVecIndices

    startIndex = 0 if len(curVecIndices) == 0 else curVecIndices[-1]+1
    for i in (range(startIndex, len(possibleVecs))):
        vecIndices = FindOrthogonalVecs_Recursive(N-1, possibleVecs, curVecIndices + [i])
        if len(vecIndices) != 0:
            return vecIndices
    return []

def FindOrthogonalVectors_NxN(N, allowedValues=[-1, 0, 1]):
    '''
    Finds combination of vectors that are orthogonal to each other.
    '''
    # Initialize
    possibleVecs = FindPossibleVecs_Recursive(N, allowedValues)
    # Find orthogonal vectors
    orthogonalMatrices = []
    startIndex = 0
    for i in tqdm(range(startIndex, len(possibleVecs))):
        vecIndices = FindOrthogonalVecs_Recursive(N-1, possibleVecs, [i])
        if len(vecIndices) != 0:
            orthogonalVecs = [possibleVecs[i] for i in vecIndices]
            # print("FOUND:")
            # for v in orthogonalVecs:
            #     print(v)
            #     print()
            # print()
            orthogonalMatrices.append(orthogonalVecs)
    # Return
    return orthogonalMatrices


# Driver Code
# Params
allowedValues = [1, -1, 2, -2]
N = 4
# Params

# RunCode
orthogonalMatrices = FindOrthogonalVectors_NxN(N, allowedValues)
for orthogonalVecs in orthogonalMatrices:
    for v in orthogonalVecs:
        print(v)
        print()