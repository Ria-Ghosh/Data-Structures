def sumOfDigits(n):
    assert int(n) == n, "The number should be a positive integer only"
    if n < 10:
        return n
    else:
        return int(n%10) + sumOfDigits(n//10)

print(sumOfDigits(99))