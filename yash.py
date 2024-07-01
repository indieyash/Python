print("welcome to general awareness quiz")
playing = input("do you want to play? ")
if playing.lower() != "yes" :
    quit()  
print("okay lets play this quiz")
score = 0
answer = input("full form of sql in computer ")
if answer == "structured query language":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " question correct")
answer = input("what is major component in cng ")
if answer == "methane":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " question correct")
answer = input("world environmental day is celeberated on which month and date ")
if answer == "june 5":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " question correct")
answer = input("earth is protected from ultra-violet radiation by means of  ")
if answer == "ozone layer":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " question correct")
answer = input("the highest policy making body in national planning in india is  ")
if answer == "national development council":
    print("correct")
    score +=1
else:
    print("incorrect")
print("you got " + str(score) + " question correct")
print("you got " + str((score/ 5) * 100) + "%.")
