import datetime
from zoneinfo import ZoneInfo
import func 
from globle import fname 
from globle import f
import globle
time = (datetime.datetime.now(datetime.timezone.utc))
year = str(time.year)
month = str(time.strftime('%m'))
day = str(time.day)
#main 
newfile = input("is this a new file")
if newfile == "y":
   ## usercall = input("what is your call")
    f.write(" <ADIF_VER:5>3.1.7\n")
    
    f.write("<EOH>\n")
    
f.write("\n")
while True:
    func.call()
    func.freq()
    func.rsts()
    func.rstr()
    f.write("   ")
    f.write(f"<qso_date:8>:{year}{month}{day}")
    f.write("\n")

