#!/usr/bin/python3

import cgi, os
import cgitb; cgitb.enable()
import tfr_reader as TFR

form = cgi.FieldStorage()

# Read file data
fileitem = form['file']
pilot = fileitem.file

score = TFR.plong(pilot,4)
lasersfired = TFR.plong(pilot,1908)
warheadsfired = TFR.pword(pilot,1920)
laserhits = TFR.plong(pilot,1912)
warheadhits = TFR.plong(pilot,1922)
laserless = score - (laserhits * 3)
golf = score + (lasersfired * 2) + (warheadsfired * 100) - (laserhits * 3) - (warheadhits * 100)

print("""\
Content-Type: text/html\n
<html>
<body>
""")

print('Score : ',score,'<br>\n')
print('Lasers Fired : ',lasersfired,'<br>\n')
print('Warheads Fired : ',warheadsfired,'<br>\n')
print('Lasers Hit : ',laserhits,'<br>\n')
print('Warheads Hit : ',warheadhits,'<br>\n')
print('Laserless Score : ',laserless,'<br>\n')
print('Golf Score : ',golf,'<br>\n')

print("""\
</body>
</html>
""")
