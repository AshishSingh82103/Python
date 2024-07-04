#-------------------global scope = > when function not find the value in own scope then pick with global scope-----------------------
userName = "singhashish"

def func():
    # userName = "Ashish"
    print(userName)

func()
print(userName)

x = 10 
def func():
    y = 5
    print(x + y)

func()






