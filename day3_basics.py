user_age = int(input("How old are you? "))

if user_age < 18:
    print("You must be at least 18 years old to access this content.")
elif user_age >= 18 and user_age < 65:
    print("Welcome! You have access to this content.")
else:
    print("You are eligible for senior citizen benefits.")
