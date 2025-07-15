'''
Python ha un limite predefinito di ricorsione (di solito 1000 livelli). Anche se potessimo aspettare abbastanza a lungo, la ricorsione si fermerebbe con un RecursionError.
''' 

# Approccio ricorsivo per la sequenza di fibonacci, ovviamente ha diversi problemi di efficienza questo metodo 
def fibonacci(num):
    if num <= 0:
        return 0
    
    if num == 1:
        return 1
    
    return fibonacci(num-1) + fibonacci(num-2)


# Approccio ricorsivo per il fattoriale
def factorial(num):
    
    if num <= 1:
        return 1
    
    return num * factorial(num - 1)


# Approccio iterativo per il fattoriale
def iter_factorial(num):
    
    if num <= 1:
        return 1
    
    result = 1
    
    while num > 1:
        result *= num
        num -= 1
    
    return result


print(iter_factorial(1000))