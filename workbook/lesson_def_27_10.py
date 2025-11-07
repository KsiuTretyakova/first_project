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

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     return word[:n]
#     # print(1)

# string = "letter"
# n = 3
# print(n_letter(string, n))

# "letter"


#----------------------------------
#6
# def teg_html (teg, text):
#     return f"<{teg}>{text}</{teg}>"

# text = input("Enter text: ")

# #1
# # teg, string = text.split()

# #2
# teg = text.split()[0]
# string = " ".join(text.split()[1:])

# print(teg_html(teg, string))


#10
# values = ""
def rainfall_statistics(values):
    months = [
        "January", "February", 
        "March", "April", "May", 
        "June", "July", "August", 
        "September", "October", "November",
        "December"
        ]
    
    rain = list(map(float, values.split()))
    
    total = sum(rain)
    
    average = total / 12  # len(rain) = 12
    
    max_rain = max(rain)
    min_rain = min(rain)
    
    # if rain.count(max_rain)
    max_month = months[rain.index(max_rain)]
    min_month = months[rain.index(min_rain)]
    
    return (total, average, (max_rain, max_month), (min_rain, min_month))


data = "22 22 24 49 72 98 101 82 51 40 36 24"

result = rainfall_statistics(data)

print(result)