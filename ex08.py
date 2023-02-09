print("Hey! Let's calculate your body mass index")
weight = float(input("What's your weight?(Kg) "))
# Pega a altura em centímetros e passa para metros
height = float(input("And what's your height(Cm)? ")) / 100
# Calcula o IMC
BMI = weight / height ** 2
# Acha em que classificação a pessoa está
if BMI <= 18.5:
    print('Your body mass index is {:.1f}, you are underweight.'.format(BMI))
elif 18.5 < BMI <= 25:
    print('Your body mass index is {:.1f}, you have the ideal weight.'.format(BMI))
elif 25 < BMI <= 30:
    print('Your body mass index is {:.1f}, you are overweight.'.format(BMI))
elif 30 < BMI <= 40:
    print('Careful! Your body mass index is {:.1f}, you are with obesity.'.format(BMI))
else:
    print('Maximum care! Your body mass index is {:.1f}, you are with morbidly obesity.'.format(BMI))
