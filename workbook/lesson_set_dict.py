#1 
def task1():
    to_do = {
        "today": ["read", "clear", "dog"],
        "tomorrow": ["read", "call my mom"]
    }

    # print(to_do)
    print("To do for today:")
    for item in to_do["today"]:
        print("-", item)
        
    print("To do for tomorrow:")
    for item in to_do["tomorrow"]:
        print("-", item)
        
# task1()

#2
def task2():
    users = {
        0: "Alice",
        1: "Bob",
        2: "Jack"
    }

    user_id = int(input("Your id: "))

    if user_id in users:
        print(f"Hello, {users[user_id]}!")
    else:
        print("Hello everybody!")
        
#3
def task3():
    films = {
        'Iron Man': 2008,
        'Avengers: Endgame': 2019,
        'Thor': 2011,
        'Guardians of the Galaxy': 2014
    }

    sorted_films = dict(sorted(films.items()))

    # print(films)
    # print(sorted(films.items()))
    print("sorted_films:", sorted_films, "\n")
    print("sorted_films.items():", sorted_films.items(), "\n")

    for name, year in sorted_films.items():
        print(f"---('{name}': {year})---")
        
    print("\n")   
    
    for name_year in sorted_films.items():
        print(name_year)
        
#4
def task4():
    n = int(input("n: "))

    # squares = {}  # dict()
    # for i in range(1, n+1):
    #     # dict[key] = value
    #     squares[i] = i ** 2

    squares = {i: i ** 2 for i in range(1, n+1)}

    print(squares)
    
#5
def task5():
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [i for i in range(7)]

    # week_dict = {}
    # for day in range(7):
    #     week_dict[weeks[day]] = days[day]
        
    # week_dict = {weeks[day]: days[day] for day in range(7)}

    # zip(keys, values)
    # zip(список_ключів, список_значень)
    # списки ключів та значень повинні співпадати за розміром!!
    week_dict = dict(zip(weeks, days))

    print(week_dict)
    
    # n = int(input())
    # for day, number in week_dict.items():
        # if number == n:
        #     print(day)
        #     break
        
task5()