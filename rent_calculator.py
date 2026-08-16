rent = int (input("enter your hostle/flat rent = "))
food = int(input("enter the amount of food orderd = "))
electricity_spend = int(input("enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int (input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill)// persons

print("Each person will pay = ",output)