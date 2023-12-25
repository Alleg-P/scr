# Задача 3: Элементы подсписка

def sublist_elements(lst):
    n = lst[0]
    m = lst[-1]
    k = lst[1]

    print("Числа подcписка: ", end="")
    first = True
    for item in lst[n:m:k]:
        if first:
            print(item, end="")
            first = False
        else:
            print(",", item, end="")
    print()
    
    
sublist_elements([1, 2, 3, 4, 5])   
sublist_elements([2, 1, 6])
