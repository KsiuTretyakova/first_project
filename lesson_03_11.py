#12

# numbers = list(map(int, input("Enter list: ").split()))

#12.1
# result = 1

# for n in numbers:
#     result *= n  # result = result * n

# print(result)

# -------------------------
#12.2
# n = 0
# result = 1
# while n < len(numbers):
#     result *= numbers[n]  # result = result * numbers[n]
#     n += 1
    
# print(result)

#-------------------------------------
#16

# numbers = list(map(int, input("Enter list: ").split()))

# index = 4

# # while len(numbers) > index:
# while numbers:
#     index = 4
#     index %= len(numbers)
#     # index2 = index % len(numbers)
#     numbers.pop(index)
#     print(numbers)
    
    
#-------------------
name = "A"

def enter_name():
    global name, name_in_def
    name_in_def = "B"
    name = "C"


enter_name()  
print("name:", name)

print("name_in_def:", name_in_def)