correctTally = 0
input("Get 3 correct in a row to get a bonus")

answer = int(input("What is 23425*59348?\n"))
if answer == 1390226900:
    print("Correct")
    correctTally += 1
else: print("Wrong\n")

answer = input("Montevideo is the capital of what country?\n")
if answer == "Uruguay":
    print("Correct")
    correctTally += 1
else: print("Wrong\n")

answer = input("What element is represented by the symbol B on the periodic table?\n")
if answer == "Boron":
    print("Correct")
    correctTally += 1
else: print("Wrong\n")


