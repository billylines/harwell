import sys
import math
from math import sin, cos, sqrt

earth_mass= 5.97219e24
earth= 6378100
grav_const = 6.67384e-11
ball = [0,earth]
speed = [0, 0]

altitude = input("what is the starting altitude? (in meters)")

ball[1] += altitude

angle = input( "what is the starting angle of the rocket? (in degrees) ")

velocity = input( "what is the starting velocity of the rocket (in metres per second) ")

#b = input( "what is the drag factor? (kilograms per second) ")

#if (b < 0):  
#  sys.exit("The drag factor can not be negative!")

#mass = input( "what is the mass of the rocket? (kilograms) ")

#if (mass <= 0):  
#  sys.exit("The mass can not be negative or zero!")
  
angle = (angle / 360.0 ) * 2.0 * math.pi

speed[1] = sin(angle)*velocity
speed[0] = cos(angle)*velocity

timeframe = input("how often do you want to check the rockets position? (in seconds) ")
results = open("rocketresults.txt", "w")

tot_time = 0
max_time = 60*60*24

r = earth

while (r >= earth and tot_time < max_time):
  
  ball[0] = ball[0]+speed[0]*timeframe
  ball[1] = ball[1]+speed[1]*timeframe
  
  r2= ball[0]**2 + ball[1]**2
  r = sqrt(r2)
  g= grav_const *earth_mass/r2
  grav = [g*ball[0]/r, g*ball[1]/r]
  
  speed[1] = speed[1]-grav[1]*timeframe
  speed[0] = speed[0]-grav[0]*timeframe
 
  tot_time = tot_time + timeframe
  results.write(str(tot_time) + "\t" + str(ball[0]) + "\t" + str(ball[1]) + "\t" + str(speed[0]) + "\t" + str(speed[1]) + "\t" + str(grav[0]) + "\t" + str(grav[1]) + "\n")
 
results.close()
