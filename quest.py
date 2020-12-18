#Written by Brian Leung
import numpy as np


"""
Input:
    body_vecs: Nx3 numpy matrix of body measurement vectors, where N>=2
    weights: Nx1 numpy matrix of weights, corresponding to each of the body vectors 
    inertial_vecs: Nx3 numpy matrix corresponding inertial vectors
Output:
    Quaternion of current attitude 
    (It'll just be a 1x4 numpy matrix, since numpy doesnt support quaternions natively.)
"""
def quest(body_vecs=None,weights=None,inertial_vecs=None):
    #ENFORCING DIMENSIONS
    #Ensuring proper dimensions
    if (body_vecs.shape[1] != 3 || inertial_vecs.shape[1] != 3 || weights.shape[1] != 1):
        raise ValueError("Check the dimensions on your matrices.")
    #Ensuring same number of inertial and body vectors
    if (body_vecs.shape != inertial_vecs.shape):
        raise ValueError("Unequal numbers of inertial and body vectors.")
    #Ensuring same number of weights and body vectors
    if (body_vecs.shape[0] != weights.shape[0]):
        raise ValueError("Unequal numbers of weights and body vectors.")
    #1. DETERMINE APPROXIMATE EIGENVALUE
    eig_approx = weights.sum()
    #2. REFINE GUESS USING NEWTON RAPHSON
    
    #3. CALCULATE OUTPUT IN CRPs
    return(eig_approx)
def main():
    body = np.matrix('1,0,0;0,1,0')
    inertial = np.matrix('1,0,0;0,1,0')
    wah = np.matrix('1,1')
    print(quest(body,wah,inertial))
    

if __name__ == "__main__":
    main()