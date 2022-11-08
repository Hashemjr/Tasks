print("Welcome to my Calculator\n")
x = int(input("Enter a number: "))
y = int(input("Another number: "))
z = input("Enter the sign of operation: ")

if (z == '+'):
    print(x+y)
elif (z == '-'):
    print(x-y)
elif (z == '*'):
    print(x*y)
elif (z == '/'):
    print(x/y)
elif (z == '**'):
    print(x ** y)

print("This is a tag")