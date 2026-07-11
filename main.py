import datetime
from zoneinfo import ZoneInfo
import func 
from globle import fname 
from globle import f
import globle
import json
usercall = "user"
usercalln = len(usercall)
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
    f.write(f"<CREATED_TIMESTAMP:15>{year}{month}{day} {hour}{minute}{second}")
    f.write("<EOH>\n")
    


#main loop
while True:
    #cli input loop
    cliinput = input("...")
    
    if cliinput == "user":
        filename = input("what is your user name")
        userfile = open(filename,"r")
        usercall = userfile.readline()
        print(usercall)
        

#help 
    elif cliinput == "help":
        func.help()
#exit 
    elif cliinput == "exit":
        print("exit cli logger")
        f.close()
        exit()
        
    elif cliinput == "end":
        f.write(f"<operator:{usercalln}>{usercall}\n")
        f.write(f"<qso_date:8>{year}{month}{day}\n")
        f.write(f"<time_on:6>{hour}{minute}{second}\n")
        f.write(f"<time_off:6>{hour}{minute}{second}\n")
        f.write(f"<qso_date_off:8>{year}{month}{day}\n")
        f.write("<eor>")
        f.write("\n")
    elif cliinput == "call":
        func.call()

    elif cliinput == "fr":
        func.freq()

    elif cliinput == "mode":
        func.mode()
    elif cliinput == "sr":
        func.rsts()
        func.rstr()
    elif cliinput == "log":
        #print(usercall)
        func.call()
        func.freq()
        func.rsts()
        func.rstr()
        func.mode()
        f.write(f"<operator:{usercalln}>{usercall}\n")
        f.write(f"<qso_date:8>{year}{month}{day}\n")
        f.write(f"<time_on:6>{hour}{minute}{second}\n")
        f.write(f"<time_off:6>{hour}{minute}{second}\n")
        f.write(f"<qso_date_off:8>{year}{month}{day}\n")
        f.write("<eor>")
        f.write("\n")
    elif cliinput == "usersetup":
        username = input("what is the name of the user")
        callsign = input("what is your call")
        grid = input("what is your grid sqare")
        write = str(f"{callsign}")
        userfile = open(username, "x") 
        userfile.write(write)
        print("user saved")
 
    
        

