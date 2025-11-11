#sum until negative number 
sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    sum += num
print("Sum:", sum)
#output
Enter a number: 5
Enter a number: 10
Enter a number: 15
Enter a number: -1
Sum: 30
