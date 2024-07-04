def even_genrator(limit):
    for i in range(2, limit + 1, 2):
        return i
    
print(even_genrator(10)) # 2

def even_genrator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

print(even_genrator(10))

def even_genrator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_genrator(10):
    print(num)
