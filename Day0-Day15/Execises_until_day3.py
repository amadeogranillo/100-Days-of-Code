"""str1 = 'X-DSPAM-Confidence: 0.8475
colon =  str1.find(':')
piece = str1[colon+1:].strip()
value = float(piece)
print(value)
print("Hello"+input("What is your name")+"!")"""


"""print("Welcome to the tip calculator\n")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip = int(input("Percentage? 10,12 or 15?"))
percentage = bill + (bill* (tip/100))
to_pay = percentage / people
final = "{:.2f}".format(to_pay)
print("Each person pay: $",final)"""








print("""     .. ..oooo.....ooo...
  .odSS4PYYYSSOOXXXXXXXXXOodbgooo.
 /SSYod$$$$SSOIIPXXXXXXXXXYYP.oo.*b.
($$Yd$$$$SSSOII:XXXXXXXX:IIoSSS$$b.Y,
 \Yd$$$$SSSOII:XXXXXXXXXX:IIOOSSS$$$b\
  d$$$$SSSOOI:XP"YXXXXXXXX:IIOOSSSS$$$\
  Y$$$SSSOOII:XbdXXXXXP"YX:IIOOOSS$$$$)
  'Y$$$SSSOI:XXXXXXXXXbodX:IIOOSS$$$$$/
   "Y$$$SSSOI(PoTXXXXXTo)XXIIOOOSS$$$*'
     ""*Y$S(((PXXXXXXXY))dIIOSSS$$dP'
        "*'()P;XXXXXXXXY)IIOSSS$P".oS,
        (S'(P;XXXXXXXP;Y)XXYOP".oSSSSb
       (S'(P;'XXXXXXX';Y).ooooSSSSSSSS)
       (S'(P;'XXXXXXP';Y).oSSSSSSSSSSSP
       (SS'Y);YXXXXX';(Y.oSSSSSSSSSSSSP
        YSS'Y)'YXXX".(Y.oSSP.SSSSSSSSY
         YSS'"" XXX""oooSSP.SSSSSSSSY
         SSSSSS YXXX:SSSSP.SSSSSSSSY
         SSSSSP  YXb:SSSP.S"SSSSSSP
         S(OO)S   YXb:SY    )SSSSS
         SSSSO    )YXb.I    ISSSSP
         YSSSY    I."YXXb   Y(SS)I
         )SSS(    dSSo.""*b  YSSSY
         OooSb   dSSSSP      )SSS(
                 dSSSY       OooSS
                 OooSP""")


"""print("Welcome to Treasure Island. Your mission is to find the treasure")

direction = input("You are at a cross road. Where do you want to go? Left or right?").lower()


if direction == "left":
    lake = input(
        'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait ofr a boat. Type "swim" to swim across').lower()
    if lake == "wait":
        door = input(
            'You arrive at the island unharmed. There are 3 doors. One red, one yellow and one blue. Which one do you choose?').lower()
        if door == "red":
            print("Burned by fire. Game over")
        elif door == "blue":
            print("Eaten by beasts. Game over")
        elif door == "yellow":
            print("You Win!!")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game over")
else:
    print("You fell into a hole and died. Game over")
"""


