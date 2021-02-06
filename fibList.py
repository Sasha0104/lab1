a = 0
b = 1
temp = 0

c = int(input("Input your number: "))

print("All the Fibonacci numbers until " + str(c) + " (including): ")
print(0)

while b <= c:
    print(b)
    temp = b;
    b = b + a;
    a = temp;