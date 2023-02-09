print('Welcome to national swimming conference!')
name = str(input('What your name? '))
age = int(input('How old are you? '))
# Cadastra de acordo com a idade do nadador
if age <= 9:
    classroom = 'Mirim'
elif 9 < age <= 14:
    classroom = 'Childish'
elif 14 < age <= 19:
    classroom = 'Junior'
elif age == 20:
    classroom = 'Senior'
else:
    classroom = 'Master'
print('Hello {}, acoording to your age. \n'
      'You have been registred as a swimmer in the {} class.'.format(name, classroom))
