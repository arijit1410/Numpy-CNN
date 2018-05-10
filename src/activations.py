import numpy as np

def activation(x, func):

    if func == 'relu':

        return (x+abs(x))/2
 

# def backActivate(error, inUnits, outUnits,  func):
def backActivate(error, inUnits,  func):

    if func == 'relu':

        def ReLU(y):
            return 1 if y > 0 else 0

        ReLU = np.vectorize(ReLU)

        return error*ReLU(inUnits)
   



