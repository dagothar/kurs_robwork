#!/usr/bin/python

# importuj biblioteki
import sys
sys.path.append('/home/dagothar/robwork/trunk/RobWork/libs/release')
import rw


# wczytanie komorki roboczej
wcloader = rw.WorkCellLoaderFactory.getWorkCellLoader('.wc.xml')
wc = wcloader.loadWorkCell('../sceny/ur5/Scene.wc.xml')
print wc.getName()


# kinematyka prosta
state = wc.getDefaultState()
robot = wc.findDevice('robot')
robot.setQ(rw.Q(6, 1, 0, 0, 1, 0, 0), state)

T = robot.baseTend(state)
print 'FK: ', T


# kinematyka odwrotna
solver = rw.JacobianIKSolver(robot, state)
vq = solver.solve(T, state)

print "Znaleziono ", vq.size(), " rozwiazan:"
for q in vq:
	print q
