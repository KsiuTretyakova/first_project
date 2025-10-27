#1
# name = "Oksana"
# def name_hello(name):
#     print(f"Hello, {name}!")
# name_hello(name) 
    
# def name_hello(name="NON"):
#     return f"Hello, {name}!"
    
# print(name_hello())
# print(name_hello(name))

# ------------------------------

#2
# def copy_string(text, n):
#     return (" " + text + " ") * n

# text = input("Enter text:")
# n = int(input("Enter n:")) 
# print(copy_string(text, n), end=" ")

#3
# def sum_a_b(a, b):
#     return a + b 

# num_1 = int(input("Num_1: "))
# num_2 = int(input("Num_2: "))

# print(sum_a_b(num_2, num_1))

#4
# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     else:
#         return word[:n]

def n_letter(word, n):
    if len(word) < n:
        return word
    return word[:n]
    # print(1)

string = "letter"
n = 3
print(n_letter(string, n))

# "letter"