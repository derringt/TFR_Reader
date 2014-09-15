import os
import io
from struct import unpack

<<<<<<< HEAD
=======
ranks = ['Cadet', 'Officer', 'Lieutenant', 'Captain', 'Commander', 'General']

>>>>>>> f821efc6b203702f58b4ee034a676935e023269c
def pbyte(file, pos):
    file.seek(pos)
    return unpack('B',file.read(1))[0]

def pword(file, pos):
    file.seek(pos)
    return unpack('<H', file.read(2))[0]

def plong(file, pos):
    file.seek(pos)
    return unpack('<L', file.read(4))[0]
<<<<<<< HEAD
=======

file = 'test.tfr'
pilot = open(file, 'rb')

score = plong(pilot, 4)
print 'Score = ' + `score`

rank = pbyte(pilot, 2)
print ranks[rank]

pilot.close()
>>>>>>> f821efc6b203702f58b4ee034a676935e023269c
