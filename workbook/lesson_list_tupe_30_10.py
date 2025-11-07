#6
# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# ----------------------
# new_text = []  # New Delhi

# for word in text:
#     # print(word)
#     if word not in new_text:
#         new_text.append(word)
# print(len(new_text))
   
#-------------------------- 

# result = len(text)

# [0, 1, 2, 3, 4, 5, 6]

# for word_i in range(len(text)):
#     for i in range(word_i + 1, len(text)):
#         if text[word_i] == text[i]:
#             result -= 1
#             break

# print(result)

# ---------------------------
       
# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# print(len(set(text)))

# ---------------------------


# for word in text:
#     print(word)
    
# for word_i in range(len(text)):
#     print(word_i)


# ---------------------------

#9
# def set_numbers(numbers):
#     # min(list)
#     # list.index(n)
#     min_value = min(numbers)
#     min_index = numbers.index(min_value)
    
#     max_index = numbers.index(max(numbers))
    
#     numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    
#     return numbers

# numbers = "1 2 3 6 8 4 9 3 22 67 87"
# numbers = list(map(int, numbers.split()))

# print(numbers)
# print(set_numbers(numbers))


#10

# while True:
#     line = input("Enter text: ")
#     if line == "":
#         break
    
# while input() != "":
#     print(1)

# line = True  
# while line != "":
#     line = input("Enter text: ")

# run = True
# while run:
#     line = input("Enter text: ")
#     if line == "":
#         run = False

def task10():
    lines = []

    while True:
        line = input("Enter text: ")
        if line == "":
            break
        lines.append(line.upper())

    for el in lines: 
        print(el)

# task10()

# --------------------------------

#11
# numbers = [1, -2, -3, 5, 6, -3, 7, 8, -4]

# for i in range(len(numbers) - 1):
#     if numbers[i] * numbers[i + 1] > 0:
#         print(numbers[i], numbers[i + 1])
             
# --------------------------------------
#18

# text = "horse,  cat, parrot,Goldfish, dog"
# # text_list = text.split(", ")
# text_list = text.split(",")
# text_list = [w.strip() for w in text_list]

# text_list.sort(key=str.lower, reverse=True)

# print(text_list)
# print(", ".join(text_list))

# --------------------------------------
#17

n = int(input("n: "))
m = int(input("m: "))

# for row in range(n):  # проходить по діапазону від 0 до (n-1)
#     for col in range(m):  # проходить по діапазону від 0 до (m-1)
#         if (row + col) % 2 == 0:
#             print(".", end=" ")
#         else:
#             print("*", end=" ")
            
#     print()

# n x m
result = []
# m_list = []

for row in range(n):  # проходить по діапазону від 0 до (n-1)
    m_list = []
    for col in range(m):  # проходить по діапазону від 0 до (m-1)
        if (row + col) % 2 == 0:
            # print(".", end=" ")
            m_list.append(".")
        else:
            # print("*", end=" ")
            m_list.append("*")        
    # print()
    result.append(m_list)
  
print(result)



[
    [[0, 0], [0, 0], [0, 0]], 
    
    [[0, 0], [0, 0], [0, 0]], 
    
    [[0, 0], [0, 0], [0, 0]]
]

# range(n) -> від 0 до (n-1)
# range(k, n) -> від k до (n-1)
# range(k, n, s) -> від k до (n-1) з кроком s  -> [k, k + s, k+s + s, ..., (n-1)]

# range(1, 7, 3) -> [1, 4]
# range(1, 7, 10) -> [1]
# range(1, 7) -> [1, 2, 3, 4, 5, 6]
# range(7, 1, -2) -> [7, 5, 3]


