from ...crazy import CrazyDragon

from .constants import Kp, Kd, g

from numpy import zeros

from time import sleep



def landing_supporter( cf: CrazyDragon, option=1, dt=0.1, step=0.03 ):

    des     = zeros(3)
    acc_cmd = zeros(3)
    P_pos   = zeros(3)
    D_pos   = zeros(3)

    print( 'landing supporter' )

    pos = cf.pos
    vel = cf.vel

    g = 9.81

    des[:] = pos

    for _ in range( 10 ):

        P_pos[:] = des - pos
        D_pos[:] = vel

        acc_cmd[:] = 0
        acc_cmd[:] += P_pos * Kp
        acc_cmd[:] -= D_pos * Kd

        acc_cmd[2] = g

        cf.command[:] = acc_cmd

        sleep( dt )

    if option:
        des[:] = pos
    else:
        des[:2] = 0
        des[2:] = pos[2]

    for _ in range( 30 ):

        P_pos[:] = des - pos
        D_pos[:] = vel

        acc_cmd[:] = 0
        acc_cmd[:] += P_pos * Kp
        acc_cmd[:] -= D_pos * Kd

        g -= step

        acc_cmd[2] = g

        cf.command[:] = acc_cmd

        sleep( dt )

    print( 'land' )