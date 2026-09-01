val1 = 10 + 10
print(f"sum:= {val1}")

val2 = 20-10
print(f"subtraction:= {val2}")

val3 = 20//3
print(f"floor division := {val3}")

val4 = 20/3
print(f"division := {val4}")

val5 = 2**3
print(f"exponential:= {val5}")

val6 = 2*3
print(f"multiple:= {val6}")

val7 = 10%3
print(f"remainder:= {val7}")

# Exercise 1
original_price = 100
discount_sale = 15

discount_amount = original_price*discount_sale/100
final_price = original_price-discount_amount

print(f"Final Price:= {final_price}")

# exercise 2
score = 85
low_bound = 70
high_bound = 90

is_inside_bounds = (score >= low_bound) and (score <= high_bound)
print(f"is_inside_bounds := {is_inside_bounds}")

# exercise 3
age = int(input("Enter Your Age"+ "\n"))
has_id = True
can_enter = (age >= 18) and (has_id == True) 
print(f"can enter: {can_enter}")
