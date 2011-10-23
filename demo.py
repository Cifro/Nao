## Demo script for Nao.py module
#  @author Cifro Nix (http://about.me/Cifro)
#
#  Requires naoqi-sdk-1.10.52 or newer
#
#  Up to date source code is available at:
#  https://github.com/Cifro/Nao
#

import time
from naoqi import *
import Nao # Imports Nao Python module

IP = "127.0.0.1"
PORT = 9559

motionProxy = ALProxy("ALMotion", IP, PORT)
behaviorProxy = ALProxy("ALBehaviorManager", IP, PORT)

# Set the proxies for our module
Nao.motionProxy = motionProxy
Nao.behaviorProxy = behaviorProxy

# Set the stiffness
motionProxy.setStiffnesses("Body", 0.9)


# Init
Nao.init()
time.sleep(1)

# Stand
Nao.stand()
time.sleep(1)

# Zero
Nao.zero()
time.sleep(1)

# Nao sit down!
Nao.sitDown()

# Nao stand up!
Nao.standUp()

# Nao.run() can run any installed behavior
Nao.run("TaiChi")