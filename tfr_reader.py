import os
import io
from struct import unpack

def pbyte(file, pos):
    file.seek(pos)
    return unpack('B',file.read(1))[0]

def pword(file, pos):
    file.seek(pos)
    return unpack('<H', file.read(2))[0]

def plong(file, pos):
    file.seek(pos)
    return unpack('<L', file.read(4))[0]

def status(file):
    pilotstatus = ['Alive','Captured','Killed']
    return pilotstatus[pbyte(file, 1)]

def rank(file):
    pilotrank = ['Cadet','Officer','Lieutenant','Captain','Commander','General']
    return pilotrank[pbyte(file, 2)]

def difficulty(file):
    difficultyrating = ['Easy','Normal','Hard']
    return difficultyrating[pbyte(file, 3)]

def score(file):
    return plong(file, 4)

def skill(file):
    return pword(file, 8)

def secretorder(file):
    secretorderrank = ['None','First','Second','Third','Fourth','Inner',"Emperor's Hand","Emperor's Eyes","Emperor's Voice","Emperor's Reach"]
    return secretorderrank[pbyte(file, 10)]
