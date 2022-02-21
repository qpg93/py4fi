""" static 2d plotting """
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

print('mpl.__version__:\n', mpl.__version__)

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# one-dimensional data sets
np.random.seed(1000)
y = np.random.standard_normal(20)
x = np.arange(len(y))
plt.plot(x, y)
# take the index values as the respective x values
plt.plot(y)
plt.plot(y.cumsum())
plt.grid(False)     # turn off the grid
plt.axis('equal')   # equal scaling for two axes

# set minimum and maximum values of each axis
plt.plot(y.cumsum())
plt.xlim(-1, 20)
plt.ylim(np.min(y.cumsum() - 1),
         np.max(y.cumsum() + 1))

plt.figure(figsize=(10, 6))
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
plt.xlabel('index')
plt.ylabel('value')
plt.title('a simple plot')

# two-dimensional data sets
y = np.random.standard_normal((20, 2)).cumsum(axis=0)
plt.figure(figsize=(10, 6))
plt.plot(y, lw=1.5)
plt.plot(y, 'ro')
plt.xlabel('index')
plt.ylabel('value')
plt.title('a simple plot')

plt.figure(figsize=(10, 6))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.plot(y, 'ro')
# 0 stands for best location of legend
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('a simple plot')

y[:, 0] = y[:, 0] * 100
plt.figure(figsize=(10, 6))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.plot(y, 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('a simple plot')

fig, ax1 = plt.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=8)
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('a simple plot')
# create a second axis object that shares the x-axis
ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value 2nd')

plt.figure(figsize=(10, 6))
# numrows, numcols, fignum(1 ~ numrows*numcols)
plt.subplot(211)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.ylabel('value')
plt.title('a simple plot')
plt.subplot(212)
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value')

plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st data set')
plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color='g', label='2nd')
plt.legend(loc=0)
plt.xlabel('index')
plt.title('2nd data set')

# other plot styles
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(10, 6))
plt.plot(y[:, 0], y[:, 1], 'ro')
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('scatter plot')

plt.figure(figsize=(10, 6))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('scatter plot')

c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(10, 6))
plt.scatter(y[:, 0], y[:, 1], c=c, cmap='coolwarm', marker='o')
plt.colorbar()
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('scatter plot')

plt.figure(figsize=(10, 6))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('histogram')

plt.figure(figsize=(10, 6))
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'],
         stacked=True, bins=20, alpha=0.5)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('histogram')

fig, ax = plt.subplots(figsize=(10, 6))
plt.boxplot(y)
# set individual x labels, setp: set properties
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel('value')
plt.title('boxplot')


def func(num):
    """ find integral """
    return 0.5 * np.exp(num) + 1


# integral limits
a, b = 0.5, 1.5
x = np.linspace(0, 2)
y = func(x)
Ix = np.linspace(a, b)
Iy = func(Ix)
# coordinates for the polygon to be plotted
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(x, y, 'b', linewidth=2)
# define minimum y value for ordinate axis
plt.ylim(bottom=0)
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)
plt.text(0.5 * (a + b), 1,
         r'$\int_a^b f(x)\mathrm{d}x$',
         horizontalalignment='center',
         fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
