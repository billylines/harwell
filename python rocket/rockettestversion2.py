import sys
import math
from math import sin, cos, sqrt

earth_mass= 5.97219e24
earth= 6378100
grav_const = 6.67384e-11
ball = [0,0]
speed = [0, 0]

r= 0

while (r < earth):
  starting_x = 0
  starting_y = 6378100
  
  ball[0] = starting_x
  ball[1] = starting_y
  r = sqrt(ball[0]**2+ball[1]**2)
  
 # if (r < earth):
  #  print "That's inside the Earth! Try again"
  

angle = 90
angle = (angle / 360.0 ) * 2.0 * math.pi

v_values = [10000+100*i for i in range(0,21)]

max_time = 60*60*24*50

for velocity in v_values:

  ball[0] = starting_x
  ball[1] = starting_y
  
  #engine_on = raw_input( "do you want to mount an engin on your rocket? (Y/N)")

  #if (engine_on == "Y"):
  #  engine_thrust = input("what is the thrust of the engine going to be? (kg*metres/seconds**2)")
  #  engine_time = input("How long is it going to burn? (seconds)")
  #else:
  engine_thrust = 0
  engine_time = 0

  mass = 10

  if (mass <= 0):  
    sys.exit("The mass can not be negative or zero!")
    
  #b = input( "what is the drag factor? (kilograms per second) ")

  #if (b < 0):  
  #  sys.exit("The drag factor can not be negative!")

    

  speed[1] = sin(angle)*velocity
  speed[0] = cos(angle)*velocity

  timeframe = 0.1
  results = open("rocketresults " + str(timeframe) +", " + str(velocity) + ", " + str(mass) + ".txt", "w")

  tot_time = 0

  r = earth

  while (r >= earth and tot_time < max_time):
    
    ball[0] = ball[0]+speed[0]*timeframe
    ball[1] = ball[1]+speed[1]*timeframe
    
    r2= ball[0]**2 + ball[1]**2
    r = sqrt(r2)
    tot_spd = sqrt(speed[0]**2+speed[1]**2)
    g= grav_const *earth_mass/r2
    grav = [g*ball[0]/r, g*ball[1]/r]
    
    if (tot_time > engine_time):
      engine_thrust = 0
    
    eng = [engine_thrust*speed[0]/tot_spd, engine_thrust*speed[1]/tot_spd]
    
    speed[0] = speed[0]-grav[0]*timeframe+eng[0]/mass*timeframe
    speed[1] = speed[1]-grav[1]*timeframe+eng[1]/mass*timeframe
  
    tot_time = tot_time + timeframe
    results.write(str(tot_time) + "\t" + str(ball[0]) + "\t" + str(ball[1]) + "\t" + str(speed[0]) + "\t" + str(speed[1]) + "\t" + str(grav[0]) + "\t" + str(grav[1]) + "\n")
  
  results.close()
