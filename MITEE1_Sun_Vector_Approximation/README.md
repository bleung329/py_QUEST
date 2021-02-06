# Sun Vector Approximation using Antenna Photodiodes

## Usage
### estimate_sun_vec(pd_volts)
* pd_volts: 4x1 numpy array consisting of the photodiode voltages. Will be <Top,Left,Bottom,Right>

* returns: 1x3 numpy array <x,y,z> of the approximated unit length sun vector, with respect to body frame

## Why did I make this?
The [MiTEE](http://clasp-research.engin.umich.edu/groups/s3fl/mitee/home/) 1 mission has launched. Unfortunately, we are unable to receive the sun vector data from the photodiode pyramids (as of Feb 3 2021). Our magnetometer is able to output an magnetic field vector but since 2 vectors are needed to resolve an attitude, we will need to find a second vector. We've decided to use the antenna photodiodes (which were originally used for detecting whether antennas deployed) to roughly estimate a sun vector. While likely high in error, it will be better than no attitude information at all.
