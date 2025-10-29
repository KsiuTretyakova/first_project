# [1, "a", 2.0]
# list()

#1
# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))
# print(value_list[len(value_list)//2:])

#2
# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))
# v_l2 = value_list[:-2]
# v_l1 = value_list[-2:]

# result = v_l1 + v_l2
# print(result)

# v_list = value_list[-2:]
# print(v_list)
# v_list.extend(v_l2)
# print(v_list)

# v_list.append(v_l2)
# print(v_list)
# v_list.append("try")
# print(v_list)



# list(map(int, list))

#3
# languages = "Ukrainian French Bulgarian Norwegian Latvian"
# list_lang = languages.split()
# list_lang.sort()
# # print(list_lang)
# print(" ".join(list_lang))



# languages = "Ukrainian French Bulgarian Norwegian Latvian"
# list_lang = languages.split()
# print(" ".join(sorted(list_lang)))


#4
# languages = "Ukrainian French Bulgarian Norwegian Latvian"
# list_lang = languages.split()
# list_lang.sort(reverse=True)
# # print(list_lang)
# print(" ".join(list_lang))



languages = "Ukrainian French Bulgarian Norwegian Latvian"
list_lang = languages.split()
print(list_lang)

print(" ".join(sorted(list_lang, reverse=True)))


print(list_lang[::-1])