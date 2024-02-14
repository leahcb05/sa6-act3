num = 12345
summation = lambda x : sum(int(digit) for digit in str(x))
result = summation(num)
print(result)