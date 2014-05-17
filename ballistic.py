import sys
import math
from math import sin, cos

ball = [0, 0]
speed = [0, 0]

angle = input( "what is the starting angle of the cannon? (in degrees) ")

velocity = input( "what is the starting velocity of the ball (in metres per second) ")

b = input( "what is the drag factor? (kilograms per second) ")

if (b < 0):  
  sys.exit("The drag factor can not be negative!")

mass = input( "what is the mass of the cannonball? (kilograms) ")

if (mass <= 0):  
  sys.exit("The mass can not be negative or zero!")
  
angle = (angle / 360.0 ) * 2.0 * math.pi

speed[1] = sin(angle)*velocity
speed[0] = cos(angle)*velocity

timeframe = input("how often do you want to check the balls position? (in seconds) ")

results = open("results.txt", "w")

tot_time = 0
gtimestime = 9.8 * timeframe

while ball[1] >= 0.0:
  ball[0] = ball[0]+speed[0]*timeframe
  ball[1] = ball[1]+speed[1]*timeframe
  speed[1] = (speed[1]-gtimestime)- b*speed[1]/mass*timeframe
  speed[0] = speed[0]-speed[0]*b/mass*timeframe
  tot_time = tot_time + timeframe
  results.write(str(tot_time) + "\t" + str(ball[0]) + "\t" + str(ball[1]) + "\t" + str(speed[0]) + "\t" + str(speed[1]) + "\n")
 
results.close()
