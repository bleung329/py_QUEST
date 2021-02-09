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
    ###Important Values###
    #True: throw errors, False: return <0,0,1>
    error_vector = np.array([0,0,1])
    throw_error = True
    
    #True: try its best with both sides being bright, False: resort to error
    handle_opposite_sides = True

    max_voltage = 1
    min_voltage = 0
    ###End Important Values###
    
    sv_approx = np.zeros((1,3))
    #Scale the pd voltage according to the minimum and maximum voltages. (ideally taken across all days)
    pd_volts = (pd_volts-min_voltage)/(max_voltage-min_voltage)
    
    #Determines which sensors we should be paying attention to.
    #Find largest pd voltage value.
    primary_sensor = np.argmax(pd_volts)
    #Find second largest pd voltage value.
    temp = pd_volts
    temp[primary_sensor] = 0
    secondary_sensor = np.argmax(pd_volts)
    
    #If both sensors are on opposite sides of the craft, something doesn't seem right. This will handle it.
    if (secondary_sensor == (primary_sensor+2)%4):
        #Change the secondary sensor to one of the sides next to the primary side, trying to make a best guess.
        if (handle_opposite_sides):
            temp[secondary_sensor] = 0
            secondary_sensor = np.argmax(pd_volts)
        else:
            if (throw_error):
                raise ValueError("Brightness is high on opposite sides of the craft.")
            else:
                return error_vector

    #We can now process this using arccos.
    pd_angles = np.arccos(pd_volts)
    #pd_angles now has the angles of incidence of the 4 sensors in radians.
    #TL TR BL BR
    if (primary_sensor==0):
        primary_vec = np.array([np.tan(pd_angles[0]),1])
    if (primary_sensor==1):
        primary_vec = np.array([-1,np.tan(pd_angles[0])])
    if (primary_sensor==2):
        primary_vec = np.array([np.tan(pd_angles[0]),-1])
    if (primary_sensor==3): 
        primary_vec = np.array([1,np.tan(pd_angles[0])])
    if (secondary_sensor==0):
        secondary_vec = np.array([np.tan(pd_angles[0]),1])
    if (secondary_sensor==1):
        secondary_vec = np.array([-1,np.tan(pd_angles[0])])
    if (secondary_sensor==2):
        secondary_vec = np.array([np.tan(pd_angles[0]),-1])
    if (secondary_sensor==3): 
        secondary_vec = np.array([1,np.tan(pd_angles[0])])
    if (secondary_sensor%2==0):
        
    secondary_unit_vec = secondary_vec / (secondary_vec**2).sum()**0.5
    print(pd_angles)

def main():
    pudding = np.array([0.56,0.34,0.2,0.1])
    45pudding = np.array([0.7071,0,0,0.7071])
    estimate_sun_vec(pudding)

if __name__ == "__main__":
    main()