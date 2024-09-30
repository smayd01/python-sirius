
#
#
# class LorenzDynamics:
#     def __init__(self, t_start, t_finish, t_step, start, sigma, rho, beta, noise_x, noise_y, noise_z):
#         self.t_start = t_start
#         self.t_finish = t_finish
#         self.t_step = t_step
#         self.sigma = sigma
#         self.beta = beta
#         self.rho = rho
#         self.start = start
#         # self.noise_x = noise_x
#         # self.noise_y = noise_y
#         # self.noise_z = noise_z
#         self.noise_x = np.random.normal(0, noise_x)
#         self.noise_y = np.random.normal(0, noise_y)
#         self.noise_z = np.random.normal(0, noise_z)
#
#     def __call__(self, variables: list[float], t):
#         x, y, z = variables
#         # dx_dt = self.sigma * (y - x) + np.random.normal(0.0, self.noise_x)
#         # dy_dt = x * (self.rho - z) - y + np.random.normal(0.0, self.noise_y)
#         # dz_dt = x * y - self.beta * z + np.random.normal(0.0, self.noise_z)
#         dx_dt = self.sigma * (y - x) + self.noise_x
#         dy_dt = x * (self.rho - z) - y + self.noise_y
#         dz_dt = x * y - self.beta * z + self.noise_z
#         return [dx_dt, dy_dt, dz_dt]
#
#
# class Simulator:
#     def __init__(self, object):
#         self.object = object
#
#     def run(self):
#         start = self.object.start
#         t_start = self.object.t_start
#         t_finish = self.object.t_finish
#         t_step = self.object.t_step
#         t = np.arange(t_start, t_finish, t_step)
#         ode = spi.odeint(self.object.__call__, start, t)
#         return ode[:, 0], ode[:, 1], ode[:, 2]
#
#
# attractor1 = LorenzDynamics(0, 100, 0.01, [1, 0, 0], 10.0, 28.0, 2.667,2.0, 2.0, 2.0)
# simulator = Simulator(attractor1)
# all_values = simulator.run()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(*all_values)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()
