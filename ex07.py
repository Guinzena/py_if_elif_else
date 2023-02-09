print("Let's try to make a triangle and analyzing it!")
side1 = float(input('Tell me the value of the first side: '))
side2 = float(input('Now tell me the value of the second side: '))
side3 = float(input('And finally say the value of the third side: '))
# Descobre se é possível fazer um triângulo com as medidas
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print('{}, {} and {} make a triangle!'.format(side1, side2, side3))
    # Descobre qual o tipo do triângulo formado
    if side1 == side2 == side3:
        print('And the triangle formed is equilateral!')
    elif side1 != side2 and side1 != side3 and side2 != side3:
        print('And the triangle formed is scalene!')
    else:
        print('And the triangle formed is isosceles!')
else:
    print('The entered values cannot form a triangle!')
