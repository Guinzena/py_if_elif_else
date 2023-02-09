print('Good morning student! Welcome to averages calculator')
name = str(input('What your name? '))
grade1 = float(input('What was the grade of the 1st test? '))
grade2 = float(input('And what about the 2nd? '))
# Calcula a média das duas notas
average = (grade1 + grade2) / 2
if average < 5:
    print('Oh No {}! You are disapproved, your average was {:.1f}'.format(name, average))
elif 5 <= average <= 6.9:
    print('{} you got a second chance! You will have to go to summer school,\n'
          'your average was {:.1f}'.format(name, average))
else:
    print('Congratulations {}! You are approved! Your average was {:.1f}'.format(name, average))
