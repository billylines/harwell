import random
import sys
import math
from math import sin, cos, sqrt

earth_mass= 5.97219e24
earth= 6378100
grav_const = 6.67384e-11
ball = [0,earth]
speed = [0, 0]

print "You have 24 hours to reach your chosen target, and hit it with a missile.\nIt is 200000 km across, so an inaccurate shot may still hit it.\nIt will (hopefully if the code works) guide itself towards the target.\nYou must help the missile hit the target by aiming towards it."

target = [raw_input("what the x of your target? (type 6378100 for the far East of Earth or random for random target) "),input("what is the y of your target? (type 0 for the other side of Earth) (if you typed random this number does not matter) ")]


if target[0] == "random":
  target[0] = random.randint(7000000, 9000000) 
  target[1] = random.randint(7000000, 9000000)
  print "your target is located at (" + str(target[0]) + ", " + str(target[1]) + ") "
else:  
  print "your target is located at (" + str(target[0]) + ", " + str(target[1]) + ") "





altitude = 0

ball[1] += altitude

angle = input( "Bearing in mind that the missile is on the north pole (0,6378100), what is the starting angle of the missile? (in degrees) ")

velocity = input( "what is the starting velocity of the missile (in metres per second) ")

#b = input( "what is the drag factor? (kilograms per second) ")

#if (b < 0):  
#  sys.exit("The drag factor can not be negative!")

#mass = input( "what is the mass of the rocket? (kilograms) ")

#if (mass <= 0):  
#  sys.exit("The mass can not be negative or zero!")
  
angle = (angle / 360.0 ) * 2.0 * math.pi

speed[1] = sin(angle)*velocity
speed[0] = cos(angle)*velocity

timeframe = 0.1

#timeframe = input("how often do you want to check the missile's position? (in seconds) ")
results = open("missileresults.txt", "w")

tot_time = 0
max_time = 60*60*24

r = earth
end_result = 0
guidance = [0,0]
 
r >= earth and tot_time < max_time
 
# and (int(target[1]) + 100000 >= int(ball[1]) >= int(target[1]) - 100000
#int(target) + 100000 >= int(ball) >= int(target) - 100000):

while (r >= earth and tot_time < max_time): 
  ball[0] = ball[0]+(speed[0]*timeframe)
  ball[1] = ball[1]+(speed[1]*timeframe)  
  
  
  r2= ball[0]**2 + ball[1]**2
  r = sqrt(r2)
  g= grav_const *earth_mass/r2
  grav = [g*ball[0]/r, g*ball[1]/r]
  
  speed[1] = speed[1]-grav[1]*timeframe
  speed[0] = speed[0]-grav[0]*timeframe
 
  tot_time = tot_time + timeframe
  results.write(str(tot_time) + "\t" + str(ball[0]) + "\t" + str(ball[1]) + "\t" + str(speed[0]) + "\t" + str(speed[1]) + "\t" + str(grav[0]) + "\t" + str(grav[1]) + "\n")
  if (int(target[0]) + 100000 >= int(ball[0]) >= int(target[0]) - 100000) and (int(target[1]) + 100000 >= int(ball[1]) >= int(target[1]) - 100000) :
    print "you hit! Read missileresults.txt to create a graph of your missile's path"
    end_result = 1
    
if end_result == 1:
  sys.end()
else:
  print "you failed! You either hit the Earth or ran out of fuel. Read missileresults.txt to make a graph of your path."
  
results.close()
