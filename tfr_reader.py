import os
import io
from struct import unpack


# Basic definitions for reading file data.
# TFR data is stored in one of three ways

# A single byte
def pbyte(file, pos):
    file.seek(pos)
    return unpack('B',file.read(1))[0]

# A little-endian 2-byte 'word'
def pword(file, pos):
    file.seek(pos)
    return unpack('<H', file.read(2))[0]

# A little-endian 4-byte 'long'
def plong(file, pos):
    file.seek(pos)
    return unpack('<L', file.read(4))[0]

# The first byte is always 0, as far as I can tell

# Offset 1
# Pilot Status. 
# Should always be (0) Alive in TIE95 due to auto-restore
def status(file):
    pilotstatus = ['Alive','Captured','Killed']
    return pilotstatus[pbyte(file, 1)]

# Offset 2
# Pilot Rank.
# Technically "Flight Cadet" and "Flight Officer"
def rank(file):
    pilotrank = ['Cadet','Officer','Lieutenant','Captain','Commander','General']
    return pilotrank[pbyte(file, 2)]

# Offset 3
# Current difficulty setting.
# This won't be able to tell you what difficulty each mission was completed at
def difficulty(file):
    difficultyrating = ['Easy','Normal','Hard']
    return difficultyrating[pbyte(file, 3)]

# Offset 4
# Total score.
def score(file):
    return plong(file, 4)

# Offset 8
# Skill rating.
def skill(file):
    return pword(file, 8)

# Offset 10
# Secret Order Rank.
# First through Inner should have 'Circle' appended to them
def secretorder(file):
    secretorderrank = ['None','First','Second','Third','Fourth','Inner',"Emperor's Hand","Emperor's Eyes","Emperor's Voice","Emperor's Reach"]
    return secretorderrank[pbyte(file, 10)]

# Offsets 11 through 28 Unknown

# Offset 29
