#Written by Brian Leung
import numpy as np
import eig_helper as eh
from math import sqrt
import time

"""
Parameters:
    body_vecs: Nx3 numpy array of unit length body measurement vectors, where N>=2
    weights: Nx1 numpy array of weights, corresponding to each of the unit body vectors 
    inertial_vecs: Nx3 numpy array corresponding inertial vectors
Output:
    Quaternion of current attitude <q0 q1 q2 q3>, where q0 is the scalar term
    (It'll just be a 1x4 numpy array, since numpy doesnt support quaternions natively.)
"""
def quest(body_vecs,weights,inertial_vecs):
    ##ENFORCING DIMENSIONS
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

    ##DETERMINING APPROXIMATE EIGENVALUE
    eig_guess = weights.sum()
    
    #Calculating K matrix:
    B = np.zeros((3,3))
    for i in range(vec_count):
        B += weights[i]*body_vecs[i,:].reshape(3,1).dot(inertial_vecs[i,:].reshape(1,3))

    Z = np.array([[B[1,2]-B[2,1]],[B[2,0]-B[0,2]],[B[0,1]-B[1,0]]])
    sigma = B[0,0] + B[1,1] + B[2,2] #trace of B
    S = B+B.T
    K = np.zeros((4,4))
    K[0,0]=sigma
    K[1:,0]=Z.reshape(3)
    K[0,1:]=Z.reshape(3)
    K[1:,1:]=S-sigma*np.identity(3)
    
    ##NEWTON RAPHSON TO FIND ACTUAL EIGENVALUE
    c_l3 = eh.l3_coeff(K)
    c_l2 = eh.l2_coeff(K)
    c_l1 = eh.l1_coeff(K)
    c_l0 = eh.l0_coeff(K)
    while (abs(eh.chr_eq(eig_guess,c_l0,c_l1,c_l2,c_l3)) >= 0.00000001): #arbitrary precision
        eig_guess -= eh.chr_eq(eig_guess,c_l0,c_l1,c_l2,c_l3)/eh.diff_chr_eq(eig_guess,c_l1,c_l2,c_l3)

    ##SINGULARITY HANDLING
    #Could this check be done somewhat earlier in the program, 
    #so we don't have to redo everything?
    pre_crp_mat = (eig_guess+sigma)*np.identity(3)-S
    if np.linalg.det(pre_crp_mat) == 0:
        ##Rotate the measured body vectors 90 degrees around the Z axis, making the alt_body
        #This is equivalent to rotating the body frame itself -90 degrees.
        #All of this is completely arbitrary, just remember how to revert back to the original.
        rot_mat = np.array([[0,-1,0],[1,0,0],[0,0,1]])
        for i in range(vec_count):
            body_vecs[i,:] = (rot_matrix.dot(body_vecs[i,:].reshape(3,1))).reshape(3)
        ##Calculate the alternate quaternion
        alt_quat = quest(body_vecs,weights,inertial_vecs).reshape(-1,)
        ##Rotate the alternate quaternion back to original
        #TODO: I'll make this cleaner.
        alt_quat_mat = np.array([
            [alt_quat[0],-alt_quat[1],-alt_quat[2],-alt_quat[3]],
            [alt_quat[1], alt_quat[0],-alt_quat[3], alt_quat[2]],
            [alt_quat[2],-alt_quat[3], alt_quat[0],-alt_quat[1]],
            [alt_quat[3],-alt_quat[2], alt_quat[1], alt_quat[0]]
        ])
        return alt_quat_matrix.dot(np.array([[0.7071068],[0],[0],[0.7071068]]))
    
    ##CALCULATE OUTPUT IN CRPs
    crp = np.linalg.inv(pre_crp_mat).dot(Z)
    
    ##CONVERT TO QUATERNIONS
    temp_quat = np.array([[1.0],[0.0],[0.0],[0.0]])
    temp_quat[1:,0] = crp.reshape(3)
    quat = 1/sqrt(1+(crp.T).dot(crp))*temp_quat

    '''
    #Various debug statements
    print("B = \n",B)
    print("Z = \n",Z)
    print("sigma = \n",sigma)
    print("S = \n",S)
    print("K = \n",K)
    print("Actual eigenvalue is = ",eig_guess)
    print("CRP =\n",crp)
    '''
    return(quat)

def main():
    body_0 = np.array([[1,0,0],[0,1,0]])
    body = np.array([[0.8660254,-0.5,0],[0.5,0.8660254,0]])
    body_90 = np.array([[0,1,0],[-1,0,0]])
    body_180 = np.array([[-1,0,0],[0,-1,0]])
    inertial = np.array([[1,0,0],[0,1,0]])
    
    body_raw = np.array([[0.7814,0.3751,0.4987],[0.6163,0.7075,-0.3459]])
    inertial_raw = np.array([[0.2673,0.5345,0.8018],[-0.3124,0.9370,0.1562]])
    
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
    tic = time.perf_counter()
    out = quest(body_180,weight,inertial)
    toc = time.perf_counter()
    print("time= ",toc-tic)
    print("output=")
    print(out)

if __name__ == "__main__":
    main()