#12
# def task12():
#     stocks = {
#         "IBM": 205.55,
#         "FB": 10.75,
#         "ACME": 45.23,
#         "AAPL": 612.78,
#         "HPQ": 37.2
#         }

#     # print(stocks.values())
#     # print(sorted(list(stocks.values())))
#     # for v in stocks.values():
#     #     print(v)

#     # item -> (key, value)
#     # item1 -> value
#     def get_value(item):
#         return item[1]
        
#     # print(stocks.items())
#     # print(list(stocks.items()))

#     # print(sorted(stocks.items(), key=get_value))

#     for key, value in sorted(stocks.items(), key=get_value):
#         print(value, key)


# item -> (key, value)
# item1 -> value
def get_value(item):
    return item[1]
     
def task12():
    stocks = {
        "IBM": 205.55,
        "FB": 10.75,
        "ACME": 45.23,
        "AAPL": 612.78,
        "HPQ": 37.2
        }

    for key, value in sorted(stocks.items(), key=get_value):
        print(value, key)
        
# task12()

# ---------------------------------------------

# 14

text = "a bb acD bb abc ac BCD a".lower().split()
# ['a', 'bb', 'acd', 'bb', 'abc', 'ac', 'bcd', 'a']

# tex_set = set(text) # {'a', 'bb', 'acd', 'abc', 'ac', 'bcd'}

result = {}
for word in text:
    result[word] = result.get(word, 0) + 1
    
    # if word not in result:
    #     result[word] = text.count(word)
    

for key, value in result.items():
    print(key, value)