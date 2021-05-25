#Tip Calculator

print("Welcome to Tip Calculator!!!\n")

name = input("What is Your Name???\n")

bill = float(input("What was the total bill in $$$ ???\n"))
tip = int(input("How much Tip would you like to give??? 10 or 20 or 50\n"))
people = int(input("How many people to split the bill???\n"))

tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill =bill+total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)

print("\n")

print("Analizing the answers given by.....\n")
print("Calculating the amount.....\n")
print("Fetching Data....\n")
print("Almost Done..........\n")

print("\n")

print("Dear "+ name + f" Each person should pay: ${final_amount}")

input("How well do you rate your experience with us.... In the scale of 0-10")

print("\n")

print("Dear "+ name + f" Each person should pay: ${final_amount}")
