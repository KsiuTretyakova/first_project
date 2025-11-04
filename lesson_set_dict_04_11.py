#6
def task6():
    text = "Lorem ipsum dolor sit amet"
    text = list(text)

    letters = {i: text.count(i) for i in text}

    print(letters)

#7
def task7():
    text = "Project Gutenberg offers over 59,000 free eBooks"

    number_count = 0
    alpha_count = 0

    for ch in text:
        if ch.isdigit():
            number_count += 1
        elif ch.isalpha():
            alpha_count += 1

    result = {
        "LETTERS": alpha_count,
        "DIGITS": number_count
    }

    # print(result)

    for key, value in result.items():
        print(key, value)
        
#10
def task10():
    numbers1 = [1, 5, 3, 8, 0, 1]
    numbers2 = [23, 9, 0, 1, 5]

    # [1, 5, 3, 8, 0, 1, 23, 9, 0, 1, 5]
    # {1, 5, 3, 8, 0, 23, 9}

    result = len(set(numbers1 + numbers2))
    print(result)
    
# ----------------------------------
numbers1 = {1, 5, 3, 8, 0}
numbers2 = {23, 9, 0, 1, 5}

# Об'єднання множин
print(numbers1.union(numbers2))  # a | b
print(numbers1 | numbers2)

# A - B = A (без B)
# {1, 5, 3, 8, 0} - {23, 9, 0, 1, 5} = {3, 8}
print(numbers1.difference(numbers2))  # a - b
print(numbers1 - numbers2)

# об'єднані множини мінус перетин
# {1, 5, 3, 8, 0} ^ {23, 9, 0, 1, 5} = {3, 23, 8, 9}
print(numbers1.symmetric_difference(numbers2))  # a ^ b
print(numbers1 ^ numbers2)

# перетин множин (спільні елементи)
# {1, 5, 3, 8, 0} & {23, 9, 0, 1, 5} = {0, 1, 5}
print(numbers1.intersection(numbers2))
print(numbers1 & numbers2)


#10

students = [
    {"name":"Bob", "points":[12, 10, 11]},
    {"name":"Alice", "points":[10, 10, 11]},
    {}
]

# result
# Bob-10 Alice-10 ...