def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!") 

print("We can give function numbers directly too:")
cheese_and_crackers(20, 30)

print("We can also use variables from our script:") 
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) 

print("We can even do math inside the parentheses:")
cheese_and_crackers(10 + 20, 5 + 6)

print("We can also combine variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)