from ...crazy import CrazyDragon

from ...recorder import Recorder

from .constants import Kp, Kd, g

from numpy        import array, zeros
from numpy.linalg import norm

from time import sleep



def landing_supporter( cf: CrazyDragon, recorder:Recorder, option=1, dt=0.1, step=0.03 ):

    des     = zeros(3)
    acc_cmd = zeros(3)
    P_pos   = zeros(3)
    D_pos   = zeros(3)
    care_g  = array([0,0,9.81])

    print( 'landing supporter', recorder.record_length )

    pos = cf.pos
    vel = cf.vel

    des[:] = 0

    for _ in range( 30 ):

        if ( norm( pos ) < 0.05 ):
            break

        P_pos[:] = des - pos
        D_pos[:] = vel

        acc_cmd[:] = 0
        acc_cmd[:] += P_pos * Kp
        acc_cmd[:] -= D_pos * Kd
        acc_cmd[:] += care_g

        cf.command[:] = acc_cmd

        print( acc_cmd )

        sleep( dt )

    print( 'land' )