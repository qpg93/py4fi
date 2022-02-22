""" static 3d plotting """
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

strike = np.linspace(50, 150, 24)
# time to maturity
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)
strike[:2].round(1)
# the dummy implied volatility values
iv = (strike - 100) ** 2 / (100 * strike) / ttm
# iv[:5, :3]
fig = plt.figure(figsize=(10, 6))
# ax = fig.gca(projection='3d')
ax = plt.axes(projection='3d')
surf = ax.plot_surface(strike, ttm, iv,
                       rstride=2, cstride=2,
                       cmap=plt.cm.coolwarm,
                       linewidth=0.5,
                       antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
# set the viewing angle
ax.view_init(30, 60)
ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
