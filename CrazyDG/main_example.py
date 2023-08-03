from navigation import Navigation

from control import Controller

from recorder import Recorder

from crazy import CrazyDragon

from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils                   import uri_helper

from numpy import array

nav_config = {
    'body_name': 'cf1'
}

ctr_config = {
    'dt': 0.1,
    'n' : 5
}



uri = uri_helper.uri_from_env( default='radio://0/80/2M/E7E7E7E702' )


if __name__ == "__main__":
    
    _cf = CrazyDragon()

    with SyncCrazyflie( uri, cf=_cf ) as scf:

        NAV = Navigation( _cf, nav_config )
        CTR = Controller( _cf, ctr_config )
        RCD = Recorder( _cf, CTR )

        NAV.start()
        CTR.start()
        RCD.start()

        ## your guidance function ##
        CTR.init_send_setpoint()
        ##       from here        ##

        ############################

        CTR.stop_send_setpoint()

        NAV.join()
        CTR.join()
        RCD.join()

    NAV.qtm.close()
