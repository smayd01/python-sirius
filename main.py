import matplotlib.pyplot as plt
from Attractor_Lorenz import LorenzDynamics
from Attractor_Lorenz import Simulator

attractor1 = LorenzDynamics.LorenzDynamics(0, 100, 0.01, [1, 0, 0], 10.0, 28.0, 2.667, 2.0, 2.0, 2.0)
simulator = Simulator.Simulator(attractor1)
all_values = simulator.run()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(*all_values)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
