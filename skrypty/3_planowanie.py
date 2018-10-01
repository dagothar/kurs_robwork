#!/usr/bin/python

# importuj biblioteki
import sys
sys.path.append('/home/dagothar/robwork/RobWork/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkSim/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkStudio/libs/release')
import rw, rws, rwsim


# wczytanie komorki roboczej
wcloader = rw.WorkCellLoaderFactory.getWorkCellLoader('.wc.xml')
wc = wcloader.loadWorkCell('../sceny/ur5/Scene.wc.xml')
print wc.getName()
state = wc.getDefaultState()
robot = wc.findDevice('robot')


# planuj
cd = rw.CollisionDetector.make(wc)
planner = rw.QToQPlanner.makeRRT(cd, robot, state)
q_from = rw.Q(6,0,-1,0,0,0,0)
q_to = rw.Q(6, 3,0.2,1,-1,0,0)
result = planner.query(q_from, q_to) 

for q in result:
	print q
