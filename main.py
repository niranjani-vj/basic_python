# print("Welcome to the real world, It suck you will love it!")
# name = "monica"
# print(f"-{name}")

# #input()

# instaId = input("What's your insta id ? ")

# print(f"My insta id : {instaId}")

# # Area of rectangle calculation

# length = float(input("What is the length ? "))
# width = float(input("What is the width ? "))

# area = length * width

# print(f"Area of rectangle is : {area}")

# if conditions
# age = int(input("what's your age??"))
# if age>25:
#     print("Welcome to the real world, it suck you will love it")
# elif age>18:
#     print("How you doin'??")
# else:
#     print("Hey there kiddo!")

#String methods:

#validate username:

username = input("Enter your username:")

if len(username)>12:
    print(f"{username} is more than 12 letters")
elif not username.find(" ") == -1:
    print(f"{username} must not have any spaces")
elif not username.isalpha():
    print(f"{username} must not have any digit")
else:
    print(f"Thanks! Your username : {username}")