n = int(input("Enter a nuber:"))
total = 0
while n>0:
    total += n%10
    n//=10
print("sum of digits:",total)