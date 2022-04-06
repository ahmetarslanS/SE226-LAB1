name = input('What is your name? ')
print('Hello ' + name)

id = input('What is your Student ID? ')
print('Your ID is ' + id)

number1 = int(input('Please enter a number. '))
number2 = int(input('Please enter a number. '))

sum = number1 + number2
diff = number1 - number2
prod = number1 * number2

print('Number 1 : ', number1)
print('Number 2 : ', number2)
print('Summation : ', sum)
print('Difference : ', diff)
print('Product : ', prod)

a = 1
asterisk = '*'

for a in range(4):
    print(a * asterisk)
    a += 1
