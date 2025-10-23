print("QWERRdfgd34".lower())
print("QWERRdfgd34".upper())
print("QWERRdfgd34".isdigit())

name = "Alisa"
n = 7
print(f"Hello, {name}! How are you?{n}")
# "dfg {name}".format("Alisa")


# ------------------------------
# 8 task

ex = input("Enter ex:\n")  # 5-3+1
# len_ex = len(ex)  # 5

n = (len(ex) + 1) // 2  # кількість цифр

# 1 var
# print(int(ex[0]) + (1 if ex[1] == "+" else -1) * int(ex[2]) + (1 if ex[3] == "+" else -1) * int(ex[4]))

# 2 var
# sum = int(ex[0])
# for i in range (1, len(ex), 2):
#     sum += (1 if ex[i] == "+" else -1) * int(ex[i+1])

# print(sum)

# 3 var
sum = int(ex[0])
for i in range(1, len(ex)):
    if ex[i] == "+":
        sum += int(ex[i+1])
    elif ex[i] == "-":
        sum -= int(ex[i+1])
print(sum)

# 4 var
# ex.replace("-", "+")
# map()