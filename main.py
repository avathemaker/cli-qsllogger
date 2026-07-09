import datetime
##from func import call
import func 
from globle import fname 
from globle import f
time =str( datetime.datetime.now())
callsign = "call"
opater = "kr4lvm"
fre = 7.200
fname = "file1"
##f= open("{fname}.adi","a")


#main 
print("name the file")
fname =input()
f= open(fname,"a")
f.write("\n")

while True:
    func.call()
    func.freq()
    func.rsts()
    func.rstr()
    f.write("   ")
    f.write(time)
    f.write("\n")

