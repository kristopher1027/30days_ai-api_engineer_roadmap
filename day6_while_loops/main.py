counter = 5         # 1. Initialize a variable

while counter > 0:  # 2. Check the condition
    print(counter)  # 3. Run the code block
    counter -= 1    # 4. Change the variable (Crucial Step!)

# exercise1: Count down from five to one.
counter = 10
while counter > 0:
    print(counter)
    counter -= 1
print("Blast off! 🚀")


choice = ""

while choice != "quit":
    print("\n ----Menu -----")
    print("1 ==> say Hello")
    print("2 ==> tell a joke")
    print("3 ==> type quit to exit")

    choice = input("Enter Any Option   ")
    if choice == "1":
        print("Hello, Python Engineer")
    elif choice == "2":
        print("Why do programmers wear glasses? Because they can't C#! 🤓")
    elif choice == "3" or choice == "quit":
        print("Thank you for your time")
        break
    else:
        print("Invalid option Select again")
