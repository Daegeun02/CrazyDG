from threading import Thread

from ..crazy import CrazyDragon

from ..control import Controller
from ..control import alpha

from .visualizer import plot_R, plot_T, plot_Thrust

from os import system

import datetime

from numpy import zeros, array

from time import sleep



class Recorder( Thread ):

    def __init__( self , _cf: CrazyDragon, CTR: Controller, n=18000 ):

        super().__init__()

        self._cf = _cf
        self.CTR = CTR

        self.recording = True

        self.idxn = 0

        self.record_datas = {
            'acc'   : zeros((3,n)),
            'acccmd': zeros((3,n)),
            'vel'   : zeros((3,n)),
            'pos'   : zeros((3,n)),
            'att'   : zeros((3,n)),
            'cmd'   : zeros((4,n)),
            'thrust': zeros((1,n))
        }

        self.data_pointer = {
            'acc'   : _cf.acc,
            'acccmd': _cf.command,
            'vel'   : _cf.vel,
            'pos'   : _cf.pos,
            'att'   : _cf.att,
            'cmd'   : CTR.command,
            'thrust': CTR.thrust
        }


    def run( self ):

        _cf = self._cf

        data_pointer = self.data_pointer
        record_datas = self.record_datas

        while self.recording:

            for key, pointer in data_pointer.items():

                record_datas[key][:,self.idxn] = pointer[:]

            self.idxn += 1

            sleep( 0.1 )

    
    def join( self ):

        self.recording = False

        super().join()

        acc    = self.record_datas['acc']
        acccmd = self.record_datas['acccmd']
        vel    = self.record_datas['vel']
        pos    = self.record_datas['pos']
        att    = self.record_datas['att']
        cmd    = self.record_datas['cmd']
        thrust = self.record_datas['thrust']

        attcmd    = cmd[0:3,:]
        thrustcmd = cmd[ 3 ,:] * alpha

        d = datetime.datetime.now()
        date      = f'{d.year}-{d.month}-{d.day:02}-{d.hour:02}-{d.minute:02}-{d.second:02}'
        self.date = date

        system( f'cd ./flight_data && mkdir {date}' )

        plot_T( acc, acccmd, vel, pos, date )
        plot_R( att, attcmd, date )
        plot_Thrust( thrust, thrustcmd )