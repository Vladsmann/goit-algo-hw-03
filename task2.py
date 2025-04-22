import random

def get_numbers_ticket(min, max, quantity):
    
    if min and quantity < 1:  
        return []
    
    if max and quantity > 1000:  
        return []
    
    numb_dif = max - min
    if quantity >= numb_dif:
       return []
    
    lottery_numbers = []
    
    all_numbers = list(range(min, max))
    
    lottery_numbers = random.sample(all_numbers, quantity)
    
    lottery_numbers.sort()
    
    return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 14, 7)
print("Ваші лотерейні числа:", lottery_numbers)