#Written by Brian Leung
import numpy as np
import eig_helper as eh

"""
Parameters:
    body_vecs: Nx3 numpy array of body measurement vectors, where N>=2
    weights: Nx1 numpy array of weights, corresponding to each of the body vectors 
    inertial_vecs: Nx3 numpy array corresponding inertial vectors
Output:
    Quaternion of current attitude 
    (It'll just be a 1x4 numpy array, since numpy doesnt support quaternions natively.)
"""
def quest(body_vecs,weights,inertial_vecs):
    #ENFORCING DIMENSIONS
    #Ensuring proper dimensions
    if (body_vecs.shape[1] != 3 or inertial_vecs.shape[1] != 3 or weights.shape[1] != 1):
        raise ValueError("Check the dimensions on your arrays.")
    #Ensuring same number of inertial and body vectors
    if (body_vecs.shape != inertial_vecs.shape):
        raise ValueError("Unequal numbers of inertial and body vectors.")
    #Ensuring same number of weights and body vectors
    if (body_vecs.shape[0] != weights.shape[0]):
        raise ValueError("Unequal numbers of weights and body vectors.")
    vec_count = body_vecs.shape[0]

    #DETERMINING APPROXIMATE EIGENVALUE
    eig_guess = weights.sum()
    
    #Calculating K matrix:
    B = np.zeros((3,3))
    for i in range(vec_count):
        B += weights[i]*body_vecs[i,:].reshape(-1,1).dot(inertial_vecs[i,:].reshape(1,-1))
    print("B = \n",B)
    Z = np.array([[B[1,2]-B[2,1]],[B[2,0]-B[0,2]],[B[0,1]-B[1,0]]])
    print("Z = \n",Z)
    sigma = np.trace(B)
    print("sigma = \n",sigma)
    S = B+B.T
    print("S = \n",S)
    K = np.zeros((4,4))
    K[0,0]=sigma
    K[1:,1]=Z.reshape(3)
    K[0,1:]=Z.reshape(3)
    K[1:,1:]=S-sigma*np.identity(3)
    print("K = \n",K)

    #STARTING NEWTON RAPHSON
    c_l3 = eh.l3_coeff(K)
    c_l2 = eh.l2_coeff(K)
    c_l1 = eh.l1_coeff(K)
    c_l0 = eh.l0_coeff(K)
    while (eh.chr_eq(eig_guess,c_l0,c_l1,c_l2,c_l3) != 0):
        eig_guess = eig_guess - eh.chr_eq(eig_guess,c_l0,c_l1,c_l2,c_l3)/eh.diff_chr_eq(eig_guess,c_l1,c_l2,c_l3)
    
    #CALCULATE OUTPUT IN CRPs
    return(eig_guess)

def main():
    body = np.array([[1,0,0],[0,1,0]])
    inertial = np.array([[1,0,0],[0,1,0]])
    weight = np.array([[1],[1]])
    
    #---Testing block for characteristic equation---
    '''
    M = np.array([
        [4,1,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,13]])
    c_l3 = eh.l3_coeff(M)
    c_l2 = eh.l2_coeff(M)
    c_l1 = eh.l1_coeff(M)
    c_l0 = eh.l0_coeff(M)
    print(c_l0)
    print(c_l1)
    print(c_l2)
    print(c_l3)
    print(eh.chr_eq(1,c_l0,c_l1,c_l2,c_l3))
    print(eh.diff_chr_eq(1,c_l1,c_l2,c_l3))
    '''
    #---End testing block---

    print(quest(body,weight,inertial))
    

if __name__ == "__main__":
    main()