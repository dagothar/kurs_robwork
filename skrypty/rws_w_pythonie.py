#!/usr/bin/python

# importuj biblioteki
import sys
sys.path.append('/home/dagothar/robwork/RobWork/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkSim/libs/release')
sys.path.append('/home/dagothar/robwork/RobWorkStudio/libs/release')
import rw, rws, rwsim
import time

# uruchom RWS
studio = rws.getRobWorkStudioInstance()

# wczytaj komorke robocza
studio.openWorkCell('../sceny/ur5/Scene.wc.xml')

# odczekaj chwile
time.sleep(1)
wc = studio.getWorkCell()
state = studio.getState()

# wypisz nazwe komorki
print wc.getName()
rw.info(wc.getName()) # do logu

# znajdz robota
robot = wc.findDevice('robot')

# ustaw robota w pewnej pozycji
q = rw.Q(6, -1, 0, -1, 0, 0, 0)
robot.setQ(q, state)
studio.setState(state)

# zapisz widok do pliku
studio.updateAndRepaint()
studio.saveViewGL('widok.png')

# czekaj poki program nie jest zakonczony
input('Nacisnij Enter...')
