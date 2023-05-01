print("welcome to my quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

print("ok! let's play :)")


answer = input("what is in your pants? ")

if answer == "poop":

    print('correct')
    score += 1

else:
    print("incorrect")

answer = input("what is in your butt? ")

if answer == "poop":

    print('correct')
    score += 1


else:
    print("incorrect")


answer = input("what is in your nose? ")

if answer == "poop":

    print('correct')
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + str((score / 3) * 100) + "%")
