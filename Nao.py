## @module Nao
#  @author Cifro Nix (http://about.me/Cifro)
#  @version 1.1
#
#  Contains functions for basic Nao's positions and actions
#
#  Requires naoqi-sdk-1.10.52 or newer
#
#  Up to date source code is available at:
#  https://github.com/Cifro/Nao
#



motionProxy = None
behaviorProxy = None



## Run any behavior
#  @param name Directory name of behavior
def run(name):
	if(behaviorProxy.isBehaviorInstalled(name)):
		behaviorProxy.runBehavior(name)
	else:
		print "Behavior ", name, " is not installed"



## Behavior sitDown
def sitDown():
	name = "sitDown"
	if(behaviorProxy.isBehaviorInstalled(name)):
		behaviorProxy.runBehavior(name)
	else:
		print "Behavior ", name, " is not installed"



## Behavior standUp
def standUp():
	name = "standUp"
	if(behaviorProxy.isBehaviorInstalled(name)):
		behaviorProxy.runBehavior(name)
	else:
		print "Behavior ", name, " is not installed"



## Prints all available behaviors
def availableBehaviors():
	behaviors = behaviorProxy.getInstalledBehaviors()
	if behaviors:
		print "\n".join(behaviors)
	else:
		print "No behaviors."



## Install all behaviors
def installBehaviors():
	import os, sys
	if(sys.platform == "win32"):
		targetDir = os.path.realpath(os.environ["appdata"] + "/Aldebaran/naoqi/behaviors/")
		thisDir = os.path.realpath(os.getcwd() + "/behaviors/")
		xcopy = "xcopy /S /Y " + thisDir + " " + targetDir
		os.system(xcopy)
	else:
		# Desktop Linux or Nao Linux
		# @todo
		targetDir = ""
		thisDir = ""

	print "\nBehaviors was installed into ", targetDir



## Zero
#  All motors to 0
#
#  @param maxSpeedFraction Percents of maximum joints speed
def zero(maxSpeedFraction = 0.5):
	numBodies = len(motionProxy.getJointNames("Body"))
	targetAngles = [0.0] * numBodies
	motionProxy.angleInterpolationWithSpeed("Body", targetAngles, maxSpeedFraction)



## Init
#  Nao is ready to do anything from this position
#
#  @param maxSpeedFraction Percents of maximum joints speed
#  @param motion Motion Naoqi module
def init(maxSpeedFraction = 0.5, motion = None):

	if motion is None:
		import motion

	# Define The Initial Position in degrees
	HeadYawAngle       = 0
	HeadPitchAngle     = 0

	ShoulderPitchAngle = 80
	ShoulderRollAngle  = 20
	ElbowYawAngle      = -80
	ElbowRollAngle     = -60
	WristYawAngle      = 0
	HandAngle          = 0

	HipYawPitchAngle   = 0
	HipRollAngle       = 0
	HipPitchAngle      = -25
	KneePitchAngle     = 40
	AnklePitchAngle    = -20
	AnkleRollAngle     = 0

	Head     = [HeadYawAngle, HeadPitchAngle]

	LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
	RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

	LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
	RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]

	# Gather the joints together
	targetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

	# Convert to radians
	targetAngles = [x * motion.TO_RAD for x in targetAngles]

	# We use the "Body" name to signify the collection of all joints
	names = "Body"
	# Ask motion to do this with a blocking call
	motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)



## Stand
#  Standing position with low power consumption.
#
#  @param maxSpeedFraction Percents of maximum joints speed
#  @param motion Motion Naoqi module
def stand(maxSpeedFraction = 0.5, motion = None):

	if motion is None:
		import motion

	HeadYaw = -0.266079
	HeadPitch = -10.7252

	# Left arm
	LHand = 0.232026
	LWristYaw = 6.23791
	LElbowRoll = -33.6601
	LElbowYaw = -70.3158
	LShoulderPitch = 91.2292
	LShoulderRoll = 9.4899

	# Left leg
	LHipRoll = 6.4185
	LHipPitch = 11.692
	LHipYawPitch = -9.22623
	LAnklePitch = 4.04062
	LAnkleRoll = -6.15002
	LKneePitch = -5.18802

	# Right arm
	RHand = 0.406934
	RWristYaw = 9.92936
	RElbowRoll = 24.9637
	RElbowYaw = 67.6742
	RShoulderPitch = 85.1695
	RShoulderRoll = -6.4185

	# Right Leg
	RHipRoll = -3.86483
	RHipPitch = 10.8083
	RHipYawPitch = -9.22623
	RAnklePitch = 3.60596
	RAnkleRoll = 3.78175
	RKneePitch = -4.2164


	Head     = [HeadYaw, HeadPitch]

	LeftArm  = [LShoulderPitch, LShoulderRoll, LElbowYaw, LElbowRoll, LWristYaw, LHand]
	RightArm = [RShoulderPitch, RShoulderRoll, RElbowYaw, RElbowRoll, RWristYaw, RHand]

	LeftLeg  = [LHipYawPitch, LHipRoll, LHipPitch, LKneePitch, LAnklePitch, LAnkleRoll]
	RightLeg = [RHipYawPitch, RHipRoll, RHipPitch, RKneePitch, RAnklePitch, RAnkleRoll]

	# Gather the joints together
	targetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

	# Convert to radians
	targetAngles = [x * motion.TO_RAD for x in targetAngles]

	# We use the "Body" name to signify the collection of all joints
	names = "Body"
	# Ask motion to do this with a blocking call
	motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)



if __name__ == "__main__":
	import sys
	if(sys.argv[1] and sys.argv[1] == "installBehaviors"):
		installBehaviors()
	else:
		print "Usage:\n$> python Nao.py installBehaviors"