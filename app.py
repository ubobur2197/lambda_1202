# 1
number = int(input("Son kiriting: "))

multiplier = lambda number: number * 5

print(f"5 ga ko'paytirilgan son: {multiplier(number)}")


# 2
multiple_numbers = lambda number1, number2: number1 * number2

print(f"Ko'paytma natijasi: {multiple_numbers(5, 4)}")


# 3
even_odd = lambda number: number % 2 == 0

print(even_odd(9))


# 4
function = lambda num1, num2: num1 if num1 > num2 else num2

print(f"Katta son: {function(6, 2)}")


# 5
name_len = lambda name: True if len(name) > 7 else False

print(name_len("Bobur"))
