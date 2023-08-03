from crazy import CrazyDragon

from threading import Thread

from .imu       import IMU
from .qualisys  import Qualisys

from time import sleep



class Navigation( Thread ):

    def __init__( self, cf: CrazyDragon, config ):

        super().__init__( self, daemon=True )

        self.cf = cf

        self.imu = IMU( cf )
        self.qtm = Qualisys( config['body_name'] )


    @classmethod
    def _on_pose( cls, cf: CrazyDragon, data: list ):
        
        cf.pos[:] = data[0:3]
        cf.att[:] = data[3:6]