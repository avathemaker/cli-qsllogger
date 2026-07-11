 
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
    freq = float(input())
    freqstr = str(freq)
    print ("is this righ y or n")
    right = input()
    freqnuberstr = len(freqstr)
    if right == "y":
        adifre = f"<freq:6>{freq}\n"
        f.write(adifre)
        if freq <= 2.00:
            band = "160m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif  freq <= 4.00:
            band = "80m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif  freq <= 5.45:
            band = "60m"
            f.write(f"<band:{freqnuber}str>{band}")
        elif  freq <= 7.300:
            band = "40m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif freq <= 10.150:
            band = "30m"
            f.write(f"<band:{freqnuberstr}>{band}")

        elif freq <= 14.350:
            band = "20m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif freq <= 18.168:
            band = "17m"
            f.write(f"<band:{freqnuberstr}>{band}")

        elif freq <= 21.450:
            band <= "15m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif freq <= 24.990:
            band <= "12m"
            f.write(f"<band:{freqnuberstr}>{band}")
        elif freq <= 29.700:
            band <= "10m"
            f.write(f"<band:{freqnuberstr}>{band}")

        f.write("\n")

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
