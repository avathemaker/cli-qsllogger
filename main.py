import datetime
from zoneinfo import ZoneInfo
import func 
from globle import fname 
from globle import f
import globle
time = str(datetime.datetime.now())

#main 
newfile = input("is this a new file")
if newfile == "Y":
   ## usercall = input("what is your call")
    f.write(" <ADIF_VER:5>3.1.7")

    
f.write("\n")
while True:
    func.call()
    func.freq()
    func.rsts()
    func.rstr()
    f.write("   ")
    f.write(time)
    f.write("\n")

