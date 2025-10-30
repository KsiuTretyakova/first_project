#6
text = "New Delhi New York Paris Prague Reykjavik"

text = text.split()

# ----------------------
# new_text = []  # New Delhi

# for word in text:
#     # print(word)
#     if word not in new_text:
#         new_text.append(word)
# print(len(new_text))
   
#-------------------------- 

result = len(text)

[0, 1, 2, 3, 4, 5, 6]

for word_i in range(len(text)):
    for i in range(word_i + 1, len(text)):
        if text[word_i] == text[i]:
            result -= 1
            break

print(result)
        
        
    
    
    
    

# for word in text:
#     print(word)
    
# for word_i in range(len(text)):
#     print(word_i)