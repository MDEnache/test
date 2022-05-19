import random
from random import randint

generatedNo = randint(1, 6)

userNo = int(input("Enter your number:"))

print("Your number is", userNo)
print("The generated number is ", generatedNo)


if generatedNo == userNo:
    print('Game is a tie!')
elif generatedNo > userNo:
    print("Computer won!")
elif generatedNo < userNo:
    print("You won!!!")
else:
    print('Try again!')
