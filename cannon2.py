import random
import sys
import math
from math import sin, cos

b = random.randint(2,10)

target = random.randint(500, 1000)

ball = [0, 0]

print "You need to hit the target with your cannon.\nIt is 50 metres long.\nYour target is " + str(target) + " metres away!"

reply= raw_input("Do you want a drag factor? (Y/N) " )

if reply== "Y" or reply == "y":
  print "The drag factor is " + str(b) + " kilograms per second"
elif reply== "N" or reply == "n":
  print "OK....=("
  b = 0

speed = [0, 0]

angle = input( "What is the starting angle of the cannon? (in degrees) ")

velocity = input( "What is the starting velocity of the ball (in metres per second) ")

mass = input( "What is the mass of the cannonball? (kilograms) ")

if (mass <= 0):  
  sys.exit("The mass can not be negative or zero!")
  
angle = (angle / 360.0 ) * 2.0 * math.pi

speed[1] = sin(angle)*velocity
speed[0] = cos(angle)*velocity

timeframe = input("How often do you want to check the balls position? (in seconds) ")

results = open("results.txt", "w")

tot_time = 0
gtimestime = 9.8 * timeframe

while ball[1] >= 0.0 :
  ball[0] = ball[0]+speed[0]*timeframe
  ball[1] = ball[1]+speed[1]*timeframe
  speed[1] = (speed[1]-gtimestime)- b*speed[1]/mass*timeframe
  speed[0] = speed[0]-speed[0]*b/mass*timeframe
  tot_time = tot_time + timeframe
  results.write(str(tot_time) + "\t" + str(ball[0]) + "\t" + str(ball[1]) + "\t" + str(speed[0]) + "\t" + str(speed[1]) + "\n")
 
if ball[0] >= target-25 and ball[0] <= target+25 : 

  print "You hit! Read results.txt to make a graph"
  results.close()
else :
  print "You missed. Read results.txt to make a graph."
  results.close()
  print " you needed to hit " + str(target-25) + " - " + str(target + 25) + " metres to win!"