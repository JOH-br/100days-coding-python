bill_value = round(float(input("What's your bill value? ")), 2)

tip_set = int(input("How much tip do you want to pay? 10, 12 or 20? "))
while tip_set not in [10, 12, 20]:
  print("Invalid Tip Response! Please try again")
  tip_set = int(input("How much tip do you want to pay? 10, 12 or 20? "))

want_split = input("Do you want to split the bill? \n( Y / N ) ").upper()
while want_split not in ["Y", "N", "YES", "NO"]:
  print("Invalid Response! Please try again")
  want_split = input("Do you want to split the bill? \n( Y / N ) ").upper()

bill_new_value = round(bill_value + (bill_value * tip_set / 100), 2)

if want_split in ["Y", "YES"]:
  split_bill = int(input("How many times do you want to split? "))
  while split_bill < 2:
    print("Invalid Response! Please enter a number greater than or equal to 2.")
    split_bill = int(input("How many times do you want to split? "))
    
  splited_bill = round(bill_new_value / split_bill, 2)
  
  print(f"Your bill is {bill_new_value} and split is {round(splited_bill, 2)} for each of {split_bill} people.")
else:
  print(f"Your bill is {bill_new_value}.")


""" Studant: Johnatas Dias dos Santos - Sao Paulo/Brazil, 08/mar/2026 """