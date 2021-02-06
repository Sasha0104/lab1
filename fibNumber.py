a = 0
b = 1
temp = 0

c = int(input("Input your number: "))

while b < c:
    temp = b;
    b = b + a;
    a = temp;

if b == c or c == 0:
    print("Your number is the Fibonacci number!")
else:
    print("Your number is NOT the Fibonacci number!")