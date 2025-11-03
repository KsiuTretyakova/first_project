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