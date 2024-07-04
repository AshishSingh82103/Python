def print_kwargs(name, power):
    print("Name:", name, "Power:", power)


print_kwargs(name = "Ashish", power = "Super Powerful")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Ashish", power = "Super Powerful")
print_kwargs(name = "Ashish")
print_kwargs(name = "Ashish", power = "Super Powerful", lack = "Error handling")