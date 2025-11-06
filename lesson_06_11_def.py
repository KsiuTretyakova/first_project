def countdown(n):
    if n == 0:
        print("Start!")
    else:
        print(n)
        countdown(n - 1) # n -= 1 countdown(n)
# countdown(5)

# print("------------------------------")
def countdown_new(n):
    if n > 0:
        print(n)
        countdown_new(n - 1) # n -= 1 countdown(n)
    print("Start!")
   
# countdown_new(5)

'''
countdown_new(5): print(5) -> countdown_new(4), print("Start!")
countdown_new(4): print(4) -> countdown_new(3), print("Start!")
countdown_new(3): print(3) -> countdown_new(2), print("Start!")
countdown_new(2): print(2) -> countdown_new(1), print("Start!")
countdown_new(1): print(1) -> countdown_new(0), print("Start!")
countdown_new(0): print("Start!")
'''

'''
print(5) -> print(4) -> print(3) -> print(2) -> print(1) -> print("Start!"), print("Start!"), print("Start!"), print("Start!"), print("Start!"), print("Start!")
'''

# print("------------------------------")
def countdown_new2(n):
    if n > 0:
        print(n)
        countdown_new2(n - 1) # n -= 1 countdown(n)
# print("Start!")
   
# countdown_new2(5)

# print("------------------------------")
def countdown_new_r(n):
    if n > 0:
        print(n)
        countdown_new_r(n - 1) # n -= 1 countdown(n)  
    return "Start!"
   
# print(countdown_new_r(5))

# ----------------------------------------
# ! - факторіал
# 5! = 5 * 4 * 3 * 2 * 1
# 1! = 1
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# print(factorial(5))

'''
factorial(5): 5 * factorial(4)
factorial(4): 4 * factorial(3)
factorial(3): 3 * factorial(2)
factorial(2): 2 * factorial(1)
factorial(2): 2 * factorial(1)
factorial(1): 1
'''

'''
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1
'''

#--------------------------------

def sum_numbers(a, b):
    return a + b

def sqr(a, b):
    return sum_numbers(a, b) ** 2

# print(sqr(2, 7))

#--------------------------------

# a = 5, b = 4
# 5 + 4
# 5 + 1 + 4 - 1 = 6 + 3
# 7 + 2
# 8 + 1
# 9 + 0
def add_number(a, b):
    if b == 0:
        return a
    return helper(a + 1, b - 1)

def helper(a, b):
    if b == 0:
        return a
    return add_number(a + 1, b - 1)

# print(add_number(5, 4))



#----------------------------------
#13

# 7 + 5
# 7 (+1) + 5 (-1)

# 7 + (-5)
# 7 (-1) + (-5) (+1) -> 6 + (-4)

# b == 0 -> a
# b > 0 -> (a + 1, b - 1)
# b < 0 -> (a - 1, b + 1)

def add_number(a, b):
    if b == 0:
        return a
    elif b > 0:
        return add_number(a + 1, b - 1)
    else:  # b< 0
        return add_number(a - 1, b + 1)
    
# ------------------------

#14

# while True:
#     n = int(input("Enter number: "))
#     if n == 0:
#         break

def print_number():
    n = int(input("Enter number: "))
    if n == 0:
        return
    else:
        print_number()
    print(n)
    

# print_number()

def print_number_str(n):
    if n == 0:
        return
    else:
        print_number_str()
    print(int(n[n.rfind(" ")+1:]))

n = int(input("Enter number: "))
print_number_str(n)