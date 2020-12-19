#Written by Brian Leung

###PURPOSE:
#This file just helps declutter the 'quest.py' file.

###CONTEXT:
#Thanks to Matlab, I found the characteristic equation of a 4x4 matrix:
#           L^4 + c3*L^3 + c2*L^2 + c1*L^1 + c0*L^0
#Where L is the eigenvalue you're checking (lambda).
#Its first derivative is obviously:
#           4*L^3 + 3*c3*L^2 + 2*c2*L^1 + c1*L^0

#In order to save myself the effort, I just put the full expression for each coefficient of lambda
#into the following functions below.I technically could have made this even uglier and made 2 functions, 
#one which calculates the characteristic and other which calculates its derivative, but I find no need
#for that. (yet...)

def l0_coeff(K):
    return (
          K[0,0]*K[1,1]*K[2,2]*K[3,3] - K[0,0]*K[1,1]*K[2,3]*K[3,2] - K[0,0]*K[1,2]*K[2,1]*K[3,3] 
        + K[0,0]*K[1,2]*K[2,3]*K[3,1] + K[0,0]*K[1,3]*K[2,1]*K[3,2] - K[0,0]*K[1,3]*K[2,2]*K[3,1] 
        - K[0,1]*K[1,0]*K[2,2]*K[3,3] + K[0,1]*K[1,0]*K[2,3]*K[3,2] + K[0,1]*K[1,2]*K[2,0]*K[3,3] 
        - K[0,1]*K[1,2]*K[2,3]*K[3,0] - K[0,1]*K[1,3]*K[2,0]*K[3,2] + K[0,1]*K[1,3]*K[2,2]*K[3,0] 
        + K[0,2]*K[1,0]*K[2,1]*K[3,3] - K[0,2]*K[1,0]*K[2,3]*K[3,1] - K[0,2]*K[1,1]*K[2,0]*K[3,3] 
        + K[0,2]*K[1,1]*K[2,3]*K[3,0] + K[0,2]*K[1,3]*K[2,0]*K[3,1] - K[0,2]*K[1,3]*K[2,1]*K[3,0] 
        - K[0,3]*K[1,0]*K[2,1]*K[3,2] + K[0,3]*K[1,0]*K[2,2]*K[3,1] + K[0,3]*K[1,1]*K[2,0]*K[3,2] 
        - K[0,3]*K[1,1]*K[2,2]*K[3,0] - K[0,3]*K[1,2]*K[2,0]*K[3,1] + K[0,3]*K[1,2]*K[2,1]*K[3,0]
        )

def l1_coeff(K):
    return (
          K[0,0]*(-K[1,1]*K[2,2] + K[1,2]*K[2,1] - K[1,1]*K[3,3] + K[1,3]*K[3,1] - K[2,2]*K[3,3] + K[2,3]*K[3,2]) 
        + K[0,1]*( K[1,0]*K[2,2] - K[1,2]*K[2,0] + K[1,0]*K[3,3] - K[1,3]*K[3,0]) 
        + K[0,2]*(-K[1,0]*K[2,1] + K[1,1]*K[2,0] + K[2,0]*K[3,3] - K[2,3]*K[3,0])  
        + K[0,3]*(-K[1,0]*K[3,1] + K[1,1]*K[3,0] - K[2,0]*K[3,2] + K[2,2]*K[3,0]) 
        + K[1,1]*(-K[2,2]*K[3,3] + K[2,3]*K[3,2]) 
        + K[1,2]*( K[2,1]*K[3,3] - K[2,3]*K[3,1]) 
        + K[1,3]*(-K[2,1]*K[3,2] + K[2,2]*K[3,1])
        )
     
def l2_coeff(K):
    ret = 0
    for i in range(0,3):
        for j in range(i+1,4):
            ret+=K[i,i]*K[j,j]-K[i,j]*K[j,i]
    return ret

def l3_coeff(K):
    return -1*(K[0,0] + K[1,1] + K[2,2] + K[3,3])

#Returns value of the characteristic equation
def chr_eq(L,c0,c1,c2,c3):
    return (L**4+c3*L**3+c2*L**2+c1*L+c0)

#Returns the value of the derivative of the characteristic
def diff_chr_eq(L,c1,c2,c3):
    return (4*L**3+3*L**2*c3+2*L*c2+c1)