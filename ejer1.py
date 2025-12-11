nums = ""

while True:
    try:

        num1 = input("Introduce un numero: ")

        if num1 == "done":
            break

        num1 = int(num1)
        nums += str(num1)

    except ValueError:

        print("Please enter a valid input")

total = 0
for i in nums:

    total += int(i)

print("Total: ", total)
print("Count: ", len(nums))
print("Average: ", total / len(nums))
