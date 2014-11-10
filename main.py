#######################################
#                                     #
#   how to use servomotor on WEIO     #
#                                     #
#######################################

#servomotor library
# there are 6 pwm pins on weio (23, 22, 21, 20, 19, 18)
# servomotor use pwm pin. 
# write(angle) servo is a vairable of type Servo
# angle is the value to write to the servo, from 0 to 180, floating point permited
# for greater precision

from weioLib.weio import *
from things.servomotor import Servo
import urllib2

def get_velib_val():
    req = urllib2.Request('http://mathemagie.net/projects/velib/index.php')
    f = urllib2.urlopen(req)
    return f.read()

def setup():
    attach.process(myProcess)
    
def myProcess():
    print("Hello servo")
    s = Servo(23)
    while True:
        v =  get_velib_val()
        print v
        deg = (int(v) * 180) / 15
        print deg
        s.write(deg)
        delay(5000)
      
    
