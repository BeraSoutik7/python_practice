def greet():
    print("Hiii User")

def mod_greet(func):
    def inner():
        print("Hello User")
        
    return inner



greet = mod_greet(greet)
greet()

