from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()

#The 2nd number controls forward or backward
me.send_rc_control(0,50,0,0)
sleep(2)

#the 1st number controls left and right
me.send_rc_control(30,0,0,0)
sleep(2)

#the last number controls up and down
me.send_rc_control(0,0,0,30)
sleep(2)
me.send_rc_control(0,0,0,0)
me.land()