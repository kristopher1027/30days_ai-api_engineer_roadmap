# grade band classifier

def classify_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(classify_grade(85))
print(classify_grade(90))

# number checker

def number_checker(num):
    if num < 0 :
        return "Negative"
    elif num > 0 :
        return "Positive"
    else:
        return "Zero"

print(number_checker(-5))
print(number_checker(5))

# service access control

def service_access(age, account_status):
    if age >= 18 and account_status == "active":
        return "Access Granted"
    else:
        return "Access Denial"

print(service_access(17, "active"))
print(service_access(20, "active"))
print(service_access(19, "suspend"))


# Exercise 1: Three-Way Temperature Classification
def temperature_class(temp):
    if temp >= 30:
        return "Hot"
    elif temp >= 20:
        return "Warm"
    else:
        return "Cold"

print(temperature_class(45))
print(temperature_class(20))
print(temperature_class(10))


# Exercise 2: Eligibility Check Using Two Conditions
def eligibity_check(has_ticket, is_registered):
    if has_ticket == True and is_registered == True :
        return "Eligible To Enter"
    else:
        return "Not Eligible"

print(eligibity_check(True, True))

# Exercise 3: Add an Invalid-Input Branch to a Simple Menu
def run_menu(user_choice):
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
    
    if user_choice == 1:
        return "Game is Loading....."
    elif user_choice == 2:
        return "Opening Setting"
    elif user_choice == 3:
        return "Exiting Application..."
    else:
        return "invalid selection please choose 1, 2 or 3"

print(run_menu(2))
