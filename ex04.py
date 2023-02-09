age = int(input('Welcome! Enter your age for verification: '))
# Vai verificar a idade e retornar a resposta devida
if age < 18:
    time = 18 - age
    # Imprime e coloca o enunciado pluralmente correto
    print("Relax! You still have {} years old.\n"
          "You don't need to elist yet, still {} {}, stay tuned!".format(age, time,
                                                                         'year' if time == 1 else 'years'))
elif age == 18:
    print('The time is now! You are 18 years old, this is the exact age range to enlist')
else:
    time = age - 18
    print('Pay attention! You are {} {} late for the enlistment, update your documents!'.format(time,
                                                                                                'year' if time == 1
                                                                                                else 'years'))
