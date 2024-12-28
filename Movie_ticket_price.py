#  Questions On Conditionals



'''
 Movie Ticket Pricing
>>> Movie tickets are priced based on age:
 > Rs100 for adults(18 and above),
 > Ra70 for children
 > Everyone gets a Rs20 discount on sunday.

'''

age = int(input("Enter age"))
day = "friday"

price = 100 if age >= 18 else 70

if day == "friday":
    price -= 20 

print("Ticket price for you is Rs",price)