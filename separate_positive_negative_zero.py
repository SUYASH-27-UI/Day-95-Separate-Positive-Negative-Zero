numbers = [10, -5, 0, 25, -8, 0, 15]

positive = []
negative = []
zero = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
