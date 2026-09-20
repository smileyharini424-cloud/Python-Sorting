numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("Original List:", numbers)

for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    if not swapped:
        break

print("Ascending Order:", numbers)

numbers.reverse()

print("Descending Order:", numbers)
