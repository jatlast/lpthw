def zero_through_x(x, numbers):
    while 0 <= x:
        print(f"At the top i is {x}")
        numbers.append(x)

        x = x - 1
        print("Numbers now: ", numbers)
        print(f"At the bottome i is {x}")
    numbers.sort()
    return numbers

print("The numbers: ")

numbers = []
numbers = zero_through_x(10, numbers)

for num in numbers:
    print(num)