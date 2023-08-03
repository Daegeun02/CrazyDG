from crazy import CrazyDragon

from .smoother import smooth_command

from numpy import array, zeros

from time import sleep

from constants import Kp, Kd, g



def goto( cf: CrazyDragon, destination, T, dt=0.1 ):

    cur     = zeros(3)
    des     = zeros(3)
    des_cmd = zeros(3)
    acc_cmd = zeros(3)
    P_pos   = zeros(3)
    D_pos   = zeros(3)
    care_g  = array([0,0,g])

    print( 'goto =>', destination )

    n = int( T / dt )
    t = 0

    command = cf.command

    cur[:] = cf.pos
    pos    = cf.pos
    vel    = cf.vel

    des[:] = destination

    cf.destination[:] = des

    for _ in range( n ):

        des_cmd[:] = smooth_command( 
            des, cur, t, int( T/2 )
        )

        P_pos[:] = des_cmd - pos
        D_pos[:] = vel

        acc_cmd[:] = 0
        acc_cmd[:] += P_pos * Kp
        acc_cmd[:] -= D_pos * Kd
        acc_cmd[:] += care_g

        command[:] = acc_cmd

        t += dt

        sleep( dt )