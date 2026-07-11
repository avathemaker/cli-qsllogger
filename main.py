import datetime
from zoneinfo import ZoneInfo
import func 
from globle import fname 
from globle import f
import globle


#time 
time = (datetime.datetime.now(datetime.timezone.utc))#get time in utc
year = str(time.year)
month = str(time.strftime('%m'))
day = str(time.day)
hour = str(time.strftime('%H'))
minute = str(time.strftime('%M'))
second = str(time.strftime('%S'))
#main 
newfile = input("is this a new file:")
if newfile == "y":
    f.write(" <ADIF_VER:5>3.1.7\n")
    f.write("<EOH>\n")
    
#user config 
usercall = input("what is your call \n")
usercalln = len(usercall)
f.write("\n")


#main loop
while True:
    func.call()
    func.freq()
    func.rsts()
    func.rstr()
    func.mode() 

    #testing
   ##print(hour)
   ## print(minute)
   ## print(second)


    #write text 
    f.write(f"<operator:{usercalln}>{usercall}\n")
    f.write(f"<qso_date:8>:{year}{month}{day}\n")
    f.write(f"<time_on:6>{hour}{minute}{second}\n")
    f.write(f"<time_off:6>{hour}{minute}{second}\n")
    f.write(f"<qso_date_off:8>{year}{month}{day}\n")
    f.write("<eor>")
    f.write("\n")
