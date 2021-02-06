#Written by Brian Leung

"""
PURPOSE:
    This function roughly estimates a sun vector, given the photodiode measurements for the antennas. 
PARAMETERS:
    pd_volts: 4x1 numpy array consisting of the photodiode voltages. Will be <Top,Left,Bottom,Right>
OUTPUT:
    1x3 numpy array <x,y,z> of the approximated unit length sun vector, with respect to body frame
"""
import numpy as np

def estimate_sun_vec(pd_volts):
    max_voltage = 6
    min_voltage = 0.5
    sv_approx = np.zeros((1,3))

def main():
    estimate_sun_vec(3)

if __name__ == "__main__":
    main()