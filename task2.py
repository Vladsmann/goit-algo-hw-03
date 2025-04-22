import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1:  
        return []
    
    if max > 1000:  
        return []
    
    if quantity < 1:
        return []
    
    if quantity > 1000:
        return []

    numb_dif = max - min + 1
    if quantity >= numb_dif:
       return []
    
    lottery_numbers = []
    
    all_numbers = list(range(min, max))
    
    lottery_numbers = random.sample(all_numbers, quantity)
    
    lottery_numbers.sort()
    
    return lottery_numbers

lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 15, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 4, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(-10, 10, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1000, 1200, 3)
print("Ваші лотерейні числа:", lottery_numbers)