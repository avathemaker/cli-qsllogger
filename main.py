import datetime


time =str( datetime.datetime.now())
callsign = "call"
opater = "kr4lvm"
fre = 7.200
f= open("test3.txt","a")
def call():
 print ("what is the callsign")
 callsign = input()
 print ("is the right y or n")
 right = input()
 if right =="y":
    f.write(callsign)
    
 else:
         call()
def freq():
    print ("what the the freq")
    fre = input()
    print ("is this righ y or n")
    right = input()
    if right == "y":
        f.write("  ")
        f.write(fre)
    if right == "n":
        freq()

def rsts():
    print("what is the rsts")
    s = input()
    print("is this right y or n")
    right = input()
    if right == "y":
        f.write("  ")
        f.write(s)
    if right == "n": 
           rsts()
def rstr():
    print("what is the rstr")
    s = input()
    print("is this right y or n")
    right = input()
    if right == "y":
       ## print("good")
        f.write(" ")
        f.write(s)
    if right == "n":
        rstr()
f.write("\n")        
while True:
   ## print(time)
    call()
    freq()
    rsts()
    rstr()
    f.write("   ")
    f.write(time)
    f.write("\n")

