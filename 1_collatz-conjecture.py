# Enter the number and this program tells how long it takes for that number to reach 1 according to Collatz Conjecture
# No error checking

num = int(input("Please enter a number:"))
orig = num
count = 0
while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3*num + 1
    count += 1

result = "{0} takes {1} steps to get to 1 using Collatz's conjecture".format(orig, count)
print(result)
