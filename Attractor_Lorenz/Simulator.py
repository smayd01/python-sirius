import numpy as np
import scipy.integrate as spi


class Simulator:
    def __init__(self, object):
        self.object = object

    def run(self):
        start = self.object.start
        t_start = self.object.t_start
        t_finish = self.object.t_finish
        t_step = self.object.t_step
        t = np.arange(t_start, t_finish, t_step)
        ode = spi.odeint(self.object.__call__, start, t)
        return ode[:, 0], ode[:, 1], ode[:, 2]

