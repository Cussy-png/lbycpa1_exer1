# Lab Activity 1
print(" Verification of I.D. Number")
ID = input(" Please enter your I.D. Number:")

FULLID = int(ID[0]) * 8 + int(ID[1]) * int(7) + int(ID[2]) * int(6) + int(ID[3]) * int(5) + int(ID[4]) * int(4) + int(ID[5]) * int(3) + int(ID[6]) * int(2) + int(ID[7]) * int(1)
print(FULLID)

if FULLID % 11 == 0:
    IDVERSION = FULLID/11
    if IDVERSION < 16:
        print("student")
    elif IDVERSION >= 16:
        print("faculty")
else:
    print("invalid")


