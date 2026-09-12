# Day-95-Separate-Positive-Negative-Zero
# Python Day 95 - Separate Positive, Negative and Zero

This program separates positive numbers, negative numbers, and zeros from a list into different lists.

## Example

Input:

```text
[10, -5, 0, 25, -8, 0, 15]
```

Output:

```text
Positive numbers: [10, 25, 15]
Negative numbers: [-5, -8]
Zeros: [0, 0]
```

## Concepts Used

* Lists
* `for` loop
* `if-elif-else`
* `append()` method
* Comparison operators

## How It Works

1. Store numbers in a list.
2. Create separate lists for positive, negative, and zero values.
3. Use a `for` loop to check each number.
4. Add positive numbers to the positive list.
5. Add negative numbers to the negative list.
6. Add zeros to the zero list.
7. Print all three lists.

## Python Code

```python
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
```

## Output

```text
Positive numbers: [10, 25, 15]
Negative numbers: [-5, -8]
Zeros: [0, 0]
```
