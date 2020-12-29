#Written by Brian Leung
import numpy as np
import quest as qu
import unittest

class quest_test(unittest.TestCase):
	def test_180(self):
		b_x_180 = np.array([[1,0,0],[0,-1,0]])
		b_x_correct = np.array([0,1,0,0])
		b_y_180 = np.array([[-1,0,0],[0,1,0]])
		b_y_correct = np.array([0,0,1,0])
		b_z_180 = np.array([[-1,0,0],[0,-1,0]])
		b_z_correct = np.array([0,0,0,1])
		w = np.array([[1],[1]])
		i = np.array([[1,0,0],[0,1,0]])
		self.assertTrue(abs(np.sum(b_z_correct-qu.quest(b_z_180,w,i)))<0.0001)
		self.assertTrue(abs(np.sum(b_x_correct-qu.quest(b_x_180,w,i)))<0.0001)
		self.assertTrue(abs(np.sum(b_y_correct-qu.quest(b_y_180,w,i)))<0.0001)
		

if __name__ == "__main__":
	unittest.main()
