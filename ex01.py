house = float(input('Hello! Welcome to funding central, \n'
                    'what is the value of the house you intend to buy? US$'))
wage = float(input('What is your wage income? US$'))
year = int(input('In how many years do you intend to pay? '))
# Calcula o número de prestações mensais
numinstallment = year * 12
# Calcula o valor max.(30%) que o comprador pode pagar de prestação
maxwage = wage * 0.3
# Calcula o valor das parcelas
installment = house / numinstallment
if installment < maxwage:
    print('Congratulations! Financing approved! \n'
          'The financing was made in {} installments, each worth US${:.2f}'.format(numinstallment, installment))
else:
    print('Oh No! Financing declined! \n'
          'For you, the monthly values exceed our policy, \n'
          'Try again with another house, or greater number of installments')
