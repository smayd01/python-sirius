import numpy as np
import scipy.integrate as spi


class LorenzDynamics:
    def __init__(self, t_start, t_finish, t_step, start, sigma, rho, beta, noise_x, noise_y, noise_z):
        self.t_start = t_start
        self.t_finish = t_finish
        self.t_step = t_step
        self.sigma = sigma
        self.beta = beta
        self.rho = rho
        self.start = start
        self.noise_x = np.random.normal(0, noise_x)
        self.noise_y = np.random.normal(0, noise_y)
        self.noise_z = np.random.normal(0, noise_z)

    def __call__(self, variables: list[float], t):
        x, y, z = variables
        dx_dt = self.sigma * (y - x) + self.noise_x
        dy_dt = x * (self.rho - z) - y + self.noise_y
        dz_dt = x * y - self.beta * z + self.noise_z
        return [dx_dt, dy_dt, dz_dt]
