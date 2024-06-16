print("Welcome to my quiz game!!")

isPlaying = input("Do you want to play? ")

if isPlaying.lower() != "yes" :
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")



    print("incorrect!")


print("your score is " + str(score))
print("you got " + str((score/2)*100) + "%.")
