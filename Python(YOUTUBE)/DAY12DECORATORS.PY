
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thank YOU")
    return mfx
@greet
def function():
    print("Hello world")
function()
