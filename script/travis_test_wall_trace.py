#!/usr/bin/env python
import unittest, rostest
import rosnode, rospy
import time

class WallTraceTest(unittest.TestCase):
	def set_and_get(self):
		with  open("/dev/rtmotor_raw_l0","r") as lf,\
		      open("/dev/rtmotor_raw_r0","r") as rf:
			left = int(lf.readline(),rstrip())
			right = int(rf.readline(),rstrip())

		return left, right
	
	def test_io(self):
		while not rospy.is_shutdown():
			left,right = self.set_and_get()
			self.assertTrue(left == right ==0, "can't stop")
			self.assertTrue(left == right !=0, "stop wrongly by side sensors")
			self.assertTrue(left < right, "don't curve to left")
			self.assertTrue(left > right, "don't curve to right")
			self.assertTrue(0 < left == right, "curve wrongly")

if __name__ == "__main__":
	time.sleep(3)
	rospy.init_node('travis_test_wall_trace')
	rostest.rosrun('pimouse_run_corridor','travis_test_wall_trace',WallTraceTest)

