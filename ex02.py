number = int(input('Choose an integer number: '))
conversion = int(input('Do you want convert {} to: \n'
                       '1.Binary\n'
                       '2.Octal\n'
                       '3.Hexadecimal\n'
                       'Choose an number: '.format(number)))
# Descobre qual foi a opção escolhida
if conversion == 1:
    # Calcula o binário
    binary = bin(number)
    print('The binary conversion of {} is {}'.format(number, binary[2:]))
elif conversion == 2:
    octal = oct(number)
    print('The octal conversion of {} is {}'.format(number, octal[2:]))
elif conversion == 3:
    hexadecimal = hex(number)
    print('The hexadecimal conversion of {} is {}'.format(number, hexadecimal[2:]))
else:
    print('Error! Do you have not entered any of the numbers in the list!')
