#!/usr/bin/python

# importuj biblioteki
import sys
sys.path.append('/home/dagothar/robwork/RobWork/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkSim/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkStudio/libs/release')
import rw, rws, rwsim


# operacje na wektorach
a = rw.Vector3d(1, 2, 3)
print a

b = rw.Vector3d(-1, 2, -3)
print b

c = a + b
print c


# operacje na orientacjach
rpy = rw.RPYd(0, 0, rw.Deg2Rad * 90) # 90 wokol osi x
print rpy

rot = rpy.toRotation3D()
print rot

eaa = rw.EAAd(rot)
print eaa

quat = rw.Quaterniond(rot)
print quat


# obrot wektora
b = rot * rw.Vector3d(0, 1, 0)
print b


# tworzenie macierzy transformacji
iden = rw.Transform3d()

T1 = rw.Transform3d(rw.Vector3d(1, 0, 0), rw.RPYd(0, 0, 0).toRotation3D())
T2 = rw.Transform3d(rw.Vector3d(), rw.RPYd(0, 0, rw.Deg2Rad*90).toRotation3D())

print T1 * T2
