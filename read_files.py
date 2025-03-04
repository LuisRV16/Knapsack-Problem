import os

dirList = os.listdir('R01000')

completeData = {}

def test_cases():

    for fname in dirList:

        f = open('R01000/' + fname)

        f.readline()

        n = int(f.readline())
        capacity = int(f.readline())

        f.readline()

        values = []
        weights = []
                            
        for i in range(n):
            line = f.readline()
            v, w = line.split()
            values.append(int(v))
            weights.append(int(w))

        
        completeData[fname] = (capacity, values, weights)
    
    return completeData