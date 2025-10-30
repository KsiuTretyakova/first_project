# for i in range(5):
# for i in "String":
#     print(i, end=" ")
#     print(1, end=" ")
    
# n = 10
# while True:
# while n > 0:
#     print(1, end=" ")
#     n -= 1

# ---------------------------
# n = 10
# while n > 0:
#     if n % 2 == 0:
#         n -= 1
#         continue
#     elif n == 5:
#         break
#     print(n, end="   ")
#     n -= 3

# n = int(input())

# print(f'''
#    _~_    
#   (o o)   
#  /  V  \  
# /(  1  )\ 
#   ^^ ^^   
# ''', end='')

# n = int(input())
# n = 5
# str_n = "123456789"
# print("    _~_    " * n)
# print("   (o o)   " * n)
# print(r"  /  V  \  " * n)
# if n == 1:
#     number = " /(  "+ str(n) +r"  )\ "
# print(number * n)
# print("   ^^ ^^   " * n)

number_p = int(input())

p1 = "    _~_    "
p2 = "   (o o)   "
p3 = "  /  V  \\  "
p5 = "   ^^ ^^   "

print(p1 * number_p)
print(p2 * number_p)
print(p3 * number_p)

nums = "1 2 3 4 5 6 7 8 9"[:2*number_p]
# p4 = " /(  " + "  )\\  /(  ".join(nums.split()) + "  )\\ "
p4 = " /(  " + r"  )\  /(  ".join(nums.split()) + r"  )\ "
print(p4)

# for n in range(1, number_p+1):
#     print(f" /(  {n}  )\\ ", end="")

# p4 = " /(  "+ str(n) +r"  )\ "

# print()
print("\n" + p5 * number_p)
# print(r"\n" + p5 * number_p)