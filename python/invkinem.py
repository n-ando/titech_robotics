#!/usr/bin/env python3
# coding: utf-8

nographics=False
import math
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as pat
except:
     nogaphics=True

def myatan2(y, x):
    if   x == 0 and y > 0:
        phi = math.pi/2
    elif x == 0 and y < 0:
        phi = -math.pi/2
    elif x > 0:
        phi = math.atan(y/x)
    elif x < 0:
        import numpy as np
        phi = math.pi - math.atan(np.sign(y/x)*y/x)
    return phi

# Forward kinematics
def fwdkinem(link, angle):
	theta1 = angle[0]
	theta2 = angle[1]
	l1 = link[0]
	l2 = link[1]
	j1_x = l1 * math.cos(theta1)
	j1_y = l1 * math.sin(theta1)
	pos_x = j1_x + l2 * math.cos((theta1 + theta2))
	pos_y = j1_y + l2 * math.sin((theta1 + theta2))
	return (pos_x, pos_y)
    
def fwdkinem2(link, angle):
	theta1 = angle[0]
	theta2 = angle[1]
	l1 = link[0]
	l2 = link[1]
	j1_x = l1 * math.cos(theta1)
	j1_y = l1 * math.sin(theta1)
	pos_x = j1_x + l2 * math.cos((theta1 + theta2))
	pos_y = j1_y + l2 * math.sin((theta1 + theta2))
	return (pos_x, pos_y)

def invkinem(link, pos):
    l1 = link[0]
    l2 = link[1]
    x = pos[0]
    y = pos[1]
    ld = math.sqrt(x ** 2 + y ** 2)
    b = math.acos((l1 ** 2 + l2 ** 2 - ld ** 2) / (2 * l1 * l2))
    a = math.acos((l1 ** 2 + ld ** 2 - l2 ** 2) / (2 * l1 * ld))
    phi = math.atan2(x, y)
    th = [0] * 2
    th[0] = (math.pi / 2) - a - phi
    th[1] = math.pi - b
    return th

def invkinem2(link, pos):
    l1 = link[0]
    l2 = link[1]
    x = pos[0]
    y = pos[1]
    ld = math.sqrt(x * x + y * y)
    b = math.acos((l1 * l1 + l2 * l2 - ld * ld) / (2 * l1 * l2))
    a = math.acos((l1 * l1 + ld * ld - l2 * l2) / (2 * l1 * ld))
    phi = math.atan2(x, y)
    th = [0] * 2
    th[0] = math.pi / 2 + a - phi
    th[1] = - math.pi + b
    return th

def plot_arm(ax, link, ang):
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    x1 = link[0] * math.cos(ang[0])
    y1 = link[0] * math.sin(ang[0])
    x2 = x1 + link[1] * math.cos(ang[0] + ang[1])
    y2 = y1 + link[1] * math.sin(ang[0] + ang[1])
    ax.plot([0, x1], [0, y1], 'k', linewidth = 2.0, zorder=1)
    ax.plot([x1, x2], [y1, y2], 'k', linewidth = 2.0, zorder=1)
    c0 = pat.Circle(xy=(0, 0), radius=.05, ec='w', fill=True, zorder=2)
    c1 = pat.Circle(xy=(x1, y1), radius=.05, ec='w', fill=True, zorder=2)
    c2 = pat.Circle(xy=(x2, y2), radius=.05, ec='w', fill=True, zorder=2)
    ax.text(x2, y2+0.1, "(x, y)=({:.2f},{:.2f})".format(x2,y2))
    ax.text(0+0.1, 0, "{:.2f}[deg]".format(ang[0]/math.pi*180))
    ax.text(x1+0.1, y1, "{:.2f}[deg]".format(ang[1]/math.pi*180))
    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)
     
link = (1.0, 1.0)
path = ((-1.0, 1.0), (-0.5, 1.0), (0.0, 1.0), (0.5, 1.0), (1.0,1.0))

if not nographics:
     fig = plt.figure(figsize = (30,10), facecolor='lightgray')

for i, pos in enumerate(path):

    # 肘が右・下の場合
    ang0 = invkinem(link, pos)
    deg0 = [x * 180 / math.pi for x in ang0]
    pos0 = fwdkinem(link, ang0)
    if not nographics:
        ax1 = fig.add_subplot(2, len(path), 1 + i, aspect = 1)
        ax1.set_title("Elbow(right/down)")
        plot_arm(ax1, link, ang0)

    # 肘が左・上の場合
    ang1 = invkinem2(link, pos)
    deg1 = [x * 180 / math.pi for x in ang1]
    pos1 = fwdkinem2(link, ang1)
    if not nographics:
        ax2 = fig.add_subplot(2, len(path), len(path) + 1 + i, aspect = 1)
        ax2.set_title("Elbow(left/up)")
        plot_arm(ax2, link, ang1)

    print("手先位置: (%.2f, %.2f)" % pos)
    print("関節角度: (%.2f, %.2f) or (%.2f, %.2f) [rad]" % tuple(ang0 + ang1))
    print("関節角度: (%.2f, %.2f) or (%.2f, %.2f) [deg]" % tuple(deg0 + deg1))
    print("手先位置: (%.2f, %.2f) or (%.2f, %.2f)" % tuple(pos0 + pos1), end='')
    print(" <-[検算] 順運動学で求めた手先位置")
    print("")
    
plt.show()


