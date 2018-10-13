from firebase import firebase
import time as t
import RPi.GPIO as g
import serial as s
rfid=s.Serial("/dev/ttyUSB0",9600,timeout=1)
card="44001851707D"
g.setmode(g.BOARD)
g.setup(40,g.OUT)
g.setwarnings(False)
b="on"
data=firebase.FirebaseApplication("https://cloud-1-849dc.firebaseio.com/",None)
new line is added
while(1):
	dat=rfid.readline()
	print dat 
	if(dat==card):
		a=data.get("a","a1")  
		print "got:::"
		while(1):
			a=data.get("a","a1") 
			if(a=="on"):
				print "not getting " 
				g.output(40,1)
				data.put("a","b/c","led on")
				t.sleep(1)
			else:
				g.output(40,0)
				data.put("a","b/c","led off")
				t.sleep(1)
		
	else:
		print "invalid card"
