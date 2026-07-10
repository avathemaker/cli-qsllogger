 
from globle import f

def call():
 print ("what is the callsign")
 callsign = input()
 print ("is the right y or n")
 right = input()
 if right =="y":
   cn = len(callsign)
   callsignadi = f"<call:{cn}>{callsign}\n"
   f.write(callsignadi)
   ##print("working")
   ##f.write("working")
 else:
         call()
def freq():
    print ("what the the freq")
    fre = input()
    print ("is this righ y or n")
    right = input()
    if right == "y":
        adifre = f"<freq:6>{fre}\n"
        f.write(adifre)
    if right == "n":
        freq()

def rsts():
    print("what is the rsts")
    s = input()
    print("is this right y or n")
    right = input()
    if right == "y":
        cn = len(s)
        sr= f"<rst_sent:{cn}>{s}\n"
        f.write(sr)
    if right == "n": 
           rsts()
def rstr():
    print("what is the rstr")
    s = input()
    print("is this right y or n")
    right = input()
    if right == "y":
       ## print("good")
        cn = len(s)
        sr= f"<rst_rcvd:{cn}>{s}\n"
        f.write(sr)
    if right == "n":
        rstr()
