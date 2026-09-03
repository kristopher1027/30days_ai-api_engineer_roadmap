# looping over a List
for fruit in ["apple", "cashew", "pineapple"]:
    print(fruit)
# looping over a string
for name in "christopher":
    print(name)
# looping through a name and greeting them
name = ["christopher", "john", "david", "joy", "james"]
for greet in name:
    print("Good Day Sir/Ma " + greet + "! to day 5")

# exercise 1
foods = ["rice", "beans", "sallad", "yam"]
for food in foods:
    print(food)

# exercise 2
total_num = 0
for num in range(1, 11):
    print(num)
    total_num = total_num + num

print("total num:", total_num)

#  exercise 3
scores = [50, 60, 70, 80, 90, 80]
threshold = 70
count = 0

for score in scores:
    if score > threshold:
        count += 1
        print(count)
print("Total Number above threshold: ", count)
