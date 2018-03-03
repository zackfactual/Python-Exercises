# assign integer, string, and float to variables
age = 26
firstName = "Zachary"
checkingBalance = 3455.71

# use print() and .format() wildcard notation to print variables assigned
print("My name is {}, I'm {} years old, and I have ${} in my checking account.".format(firstName,age,checkingBalance))

# use arithmetic operators
ageNextYear = age + 1
ageLastYear = age - 1
twiceAge = age * 2
print("Next year I'll be {}. Last year I was {}. In another {} years I'll be {}.".format(ageNextYear,ageLastYear,age,twiceAge))
thirdCheckingBalance = int(checkingBalance / 3)
thirdCheckingBalanceRemainder = int(3 % checkingBalance)
print("If I gave a third of my checking balance to charity I'd have ${} left over with a remainder of {}.".format(thirdCheckingBalance, thirdCheckingBalanceRemainder))

# if elif else in a while loop
while age < 64:
    age += 1
    if age == 35:
        print("{}, old enough to run for president!".format(age))
    elif age == 64:
        print("Will you still need me, will you still feed me, when I'm {}?".format(age))
    else:
        print("{}".format(age))
        
colorList = ["red","orange","yellow","green","blue","indigo","violet"]
for color in colorList:
    print(color)

hexTuple = ("#FF0000","#FFA500","#FFFF00","#00FF00","#0000FF","#4B0082","#EE82EE")
for hex in hexTuple:
    print(hex)

favoriteColor = input("What is your favorite color of the rainbow? ")

def displayFavoriteColor():
    return "Your favorite color of the rainbow is " + favoriteColor.lower()
print(displayFavoriteColor())

if favoriteColor not in colorList:
    print("That's not a color of the rainbow.")
          
yourAge = input("What's your age? ")

if favoriteColor == "green" or yourAge == "26":
    print("We have something in common.")

if favoriteColor == "green" and yourAge == "26":
    print("We have so much in common.")


