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

n = int(input())

p1 = "    _~_    "
p2 = "   (o o)   "
p3 = "  /  V  \\  "
p5 = "   ^^ ^^   "

print(p1 * n)
print(p2 * n)
print(p3 * n)

nums = "1 2 3 4 5 6 7 8 9"[:2*n]
p4 = " /(  " + "  )\\ ".join(nums.split())
print(p4)
# p4 = " /(  "+ str(n) +r"  )\ "


print(p5 * n)