def get_ticket_data():
    tickets = {}
    # "_" - символ, який можна використовувати замість змінної циклу (наприклад "i"), коли цикл лише для кількості повторювань, без підстановки значень (наприклад, значень змінної "i"
    
    '''
    for i in range(3):
        print(1)
    
    аналог (і - не використовувалося у циклі)
    
    for _ in range(3):
        print(1)
    '''
    
    # "   string st  t       ".strip()
    # "string st  t"
    
    for _ in range(3):
        category = input("category: ").strip() #.upper()
        price = float(input("price: ").strip())
        sold = int(input("sold: ").strip())
        tickets[category] = (price, sold)
        
    return tickets

# print(get_ticket_data())

def calculate_revenue(tickets):
    tickets_by_class = {}
    total = 0
    
    # {'a': (3.0, 5)}.items() => ('a', (3.0, 5))
    
    # key, value = ('a', (3.0, 5))
    # key = 'a', value = (3.0, 5)
    
    # category, (price, sold) = ('a', (3.0, 5))
    # category = 'a', (price, sold) = (3.0, 5)
    # category = 'a', price = 3.0, sold = 5
    for category, (price, sold) in tickets.items():
        revenue = price * sold
        tickets_by_class[category] = revenue
        total += revenue  # total = total + revenue
    
    return tickets_by_class, total

print(calculate_revenue(get_ticket_data()))

# data = get_ticket_data()
# result = calculate_revenue(data)
# print(result)