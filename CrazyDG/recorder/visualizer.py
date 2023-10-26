import matplotlib.pyplot as plt



def plot_T( acc, acccmd, vel, pos, date ):

    fig = plt.figure( figsize=(14,14) )

    ax1 = fig.add_subplot( 331 )
    ax2 = fig.add_subplot( 332 )
    ax3 = fig.add_subplot( 333 )
    ax4 = fig.add_subplot( 334 )
    ax5 = fig.add_subplot( 335 )
    ax6 = fig.add_subplot( 336 )
    ax7 = fig.add_subplot( 337 )
    ax8 = fig.add_subplot( 338 )
    ax9 = fig.add_subplot( 339 )

    ax1.plot( acc[0,:]   , label='acc x' )
    ax2.plot( acc[1,:]   , label='acc y' )
    ax3.plot( acc[2,:]   , label='acc z' )
    ax1.plot( acccmd[0,:], label='acc command x' )
    ax2.plot( acccmd[1,:], label='acc command y' )
    ax3.plot( acccmd[2,:], label='acc command z' )

    ax4.plot( vel[0,:], label='velocity x' )
    ax5.plot( vel[1,:], label='velocity y' )
    ax6.plot( vel[2,:], label='velocity z' )

    ax7.plot( pos[0,:], label='position x' )
    ax8.plot( pos[1,:], label='position y' )
    ax9.plot( pos[2,:], label='position z' )

    convenience( ax1 )
    convenience( ax2 )
    convenience( ax3 )
    convenience( ax4 )
    convenience( ax5 )
    convenience( ax6 )
    convenience( ax7 )
    convenience( ax8 )
    convenience( ax9 )

    plt.savefig( f'./flight_data/{date}/T.png' )


def plot_Thrust( thrust, thrustcmd, date ):

    fig = plt.figure( figsize=(7,7) )

    ax1 = fig.add_subplot(111)
    ax1.plot( thrust[0,:]   , label='thrust' )
    ax1.plot( thrustcmd[0,:], label='thrust command' )

    convenience( ax1 )

    plt.savefig( f'./flight_data/{date}/thrust.png' )


def plot_R( att, attcmd, date ):

    fig = plt.figure( figsize=(14,14) )

    ax1 = fig.add_subplot( 311 )
    ax2 = fig.add_subplot( 312 )
    ax3 = fig.add_subplot( 313 )

    ax1.plot( att[0,:]   , label='euler att x' )
    ax2.plot( att[1,:]   , label='euler att y' )
    ax3.plot( att[2,:]   , label='euler att z' )
    ax1.plot( attcmd[0,:], label='euler att command x' )
    ax2.plot( attcmd[1,:], label='euler att command y' )
    ax3.plot( attcmd[2,:], label='euler att command z' )

    convenience( ax1 )
    convenience( ax2 )
    convenience( ax3 )

    plt.savefig( f'./flight_data/{date}/R.png' )




def convenience( axn: plt.Axes ):
    axn.tick_params( axis='both', labelsize=7 )
    axn.legend( fontsize=8 )
    axn.grid()