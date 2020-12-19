#Written by Brian Leung
import numpy as np


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
    eig_approx = weights.sum()
    
    #REFINE GUESS USING NEWTON RAPHSON
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
'''
    coeff_l3 = trace(K)
    coeff_l2 = 0
    for i in range(0,3):
        for j in range(i+1,4):
            coeff_l2+=K[i,j]*K[j,i]-K[i,i]*K[j,j]
    coeff_l1 = 0
    coeff_l0 = 0

    (trace(K)*l^3 - l^4 + l^2*coeff_l2 + 
        K1_1*(K2_2*(-K3_3*K4_4 + K3_4*K4_3) + K2_3*(K3_2*K4_4 - K3_4*K4_2) - K2_4*(K3_2*K4_3 + K3_3*K4_2)) + 
        K1_2*(K2_1*(K3_3*K4_4 - K3_4*K4_3) + K2_3*(-K3_1*K4_4 + K3_4*K4_1) + K2_4*(K3_1*K4_3 - K3_3*K4_1)) + 
        K1_3*(-K2_1*K3_2*K4_4 + K2_1*K3_4*K4_2 + K2_2*K3_1*K4_4 - K2_2*K3_4*K4_1 - K2_4*K3_1*K4_2 + K2_4*K3_2*K4_1) + 
        K1_4*(K2_1*K3_2*K4_3 - K2_1*K3_3*K4_2 - K2_2*K3_1*K4_3 + K2_2*K3_3*K4_1 + K2_3*K3_1*K4_2 - K2_3*K3_2*K4_1) + l*(K1_1*K2_2*K3_3 - K1_1*K2_3*K3_2 - K1_2*K2_1*K3_3 + K1_2*K2_3*K3_1 + K1_3*K2_1*K3_2 - K1_3*K2_2*K3_1 + K1_1*K2_2*K4_4 - K1_1*K2_4*K4_2 - K1_2*K2_1*K4_4 + K1_2*K2_4*K4_1 + K1_4*K2_1*K4_2 - K1_4*K2_2*K4_1 + K1_1*K3_3*K4_4 - K1_1*K3_4*K4_3 - K1_3*K3_1*K4_4 + K1_3*K3_4*K4_1 + K1_4*K3_1*K4_3 - K1_4*K3_3*K4_1 + K2_2*K3_3*K4_4 - K2_2*K3_4*K4_3 - K2_3*K3_2*K4_4 + K2_3*K3_4*K4_2 + K2_4*K3_2*K4_3 - K2_4*K3_3*K4_2))/(3*l^2*trace(K) - 4*l^3 + K1_1*K2_2*K3_3 - K1_1*K2_3*K3_2 - K1_2*K2_1*K3_3 + K1_2*K2_3*K3_1 + K1_3*K2_1*K3_2 - K1_3*K2_2*K3_1 + K1_1*K2_2*K4_4 - K1_1*K2_4*K4_2 - K1_2*K2_1*K4_4 + K1_2*K2_4*K4_1 + K1_4*K2_1*K4_2 - K1_4*K2_2*K4_1 + K1_1*K3_3*K4_4 - K1_1*K3_4*K4_3 - K1_3*K3_1*K4_4 + K1_3*K3_4*K4_1 + K1_4*K3_1*K4_3 - K1_4*K3_3*K4_1 + K2_2*K3_3*K4_4 - K2_2*K3_4*K4_3 - K2_3*K3_2*K4_4 + K2_3*K3_4*K4_2 + K2_4*K3_2*K4_3 - K2_4*K3_3*K4_2 + 2*l*(coeff_l2)
'''
    #CALCULATE OUTPUT IN CRPs
    return(eig_approx)

def main():
    body = np.array([[1,0,0],[0,1,0]])
    inertial = np.array([[1,0,0],[0,1,0]])
    weight = np.array([[1],[1]])
    a = np.array([[1,0,0]])
    b = np.array([[1,0,0]])
    b = np.transpose(b)
    #print(b.dot(a))
    print(quest(body,weight,inertial))
    

if __name__ == "__main__":
    main()