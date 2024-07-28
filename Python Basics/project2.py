# Rent calculator in python
rent = int(input("enter your flat rent ="))
food = int(input("enter the amount of the food ordered ="))
electricity_spend = int(input("enter the total amount of electricity spend ="))
charge_per_unit = int(input("enter the charge per unit ="))
persons = int(input("enter the number of persons living in flat"))
total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill)/persons
print("each persons will pay = ",output)