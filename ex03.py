number1 = int(input('Hey! Enter an integer number: '))
number2 = int(input('Now one more: '))
# Comparação entre as duas variáveis
if number1 > number2:
    print('Between {} and {}, the highest value is {} and the lowest is {}'.format(number1, number2, number1, number2))
elif number1 < number2:
    print('Between {} and {}, the highest value is {} and the lowest is {}'.format(number1, number2, number2, number1))
else:
    print('There is no higher or lower! {} and {} have the same value'.format(number1, number2, number1, number2))
