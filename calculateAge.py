print("Let's see how long you've lived in days, hours, minutes, and seconds")
name = input("Name: ")
print("What's your age? ")
age = int(input("Age: "))
days = age * 365
hours = age * 8760
minutes = age * 525948
seconds = age * 31556926
print("{}, you've been alive for {} days, which is {} hours, which is {} minutes, which is {} seconds.".format(name,days,hours,minutes,seconds))
