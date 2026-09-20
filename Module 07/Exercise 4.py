def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
sample_list = [4, 7, 12, 3, 9]
result = sum_list(sample_list)

print(f"List: {sample_list}")
print(f"Sum: {result}")