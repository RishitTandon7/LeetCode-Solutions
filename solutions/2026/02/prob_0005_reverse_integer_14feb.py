def reverseInteger(x):
    sign = -1 if x < 0 else 1
    x *= sign

    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    reversed_num *= sign

    return reversed_num