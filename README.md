# py_QUEST
An implementation of the QUEST algorithm in Python.

## Usage:
### quest(body_vecs, weights, inertial_vecs)
* body_vecs: Nx3 numpy array of unit length body measurement vectors, where N >=2.

* weights: Nx1 numpy array of weights, corresponding to each of the unit body vectors.

* inertial_vecs: Nx3 numpy array corresponding inertial vectors.

* returns: 4x1 numpy array <q0,q1,q2,q3> where q0 is the scalar. 

## What is QUEST?
QUEST is an algorithm used to determine the attitude of a spacecraft. It is an implementation of Paul B Davenport's solution to [Wahba's Problem](https://en.wikipedia.org/wiki/Wahba%27s_problem). Due to its speed, it has become a fairly popular method for many missions.

## Why did I make this?
The [MiTEE](http://clasp-research.engin.umich.edu/groups/s3fl/mitee/home/) 1 mission launches soon (as of Dec 2020) and the current algorithm being used is TRIAD 1. All attitude calculations will be done on the ground, which provides a lot of freedom in terms of processing power and time. In preparation for MiTEE 2, we want to ensure that we're capable of implementing QUEST. We also want to see how it runs compared to TRIAD.
