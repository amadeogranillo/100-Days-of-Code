
name = input("Whats your name")
location = input("Location?")
def greet(name, location):
    print(f"Hey {name}")
    print(f"How do you do {name}")
    print(f"How is the weather in {location}")

greet(name,location)

number = 1.2

print(number.__round__())