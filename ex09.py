print('Welcome to the shopping system!')
price = float(input('What is the price of the product you want to buy? US$'))
# Mostra as opções de valores com os valores já convertidos
payment = int(input('What is your payment method?\n'
                    '1.Cash or cheque(US${:.2f})\n'
                    '2.1x Debit card(US${:.2f})\n'
                    '3.2x Credit card(US${:.2f})\n'
                    '4.3x or more in Credit card(US${:.2f})\n'
                    'Choose an number: '.format(price - (price * 0.1), price - (price * 0.05), price,
                                                price + (price * 0.2))))
# Reavalia o preço de acordo com o método de pagamento escolhido
# 1- 90%  2- 95%  3- 100%  4- 120%
if payment == 1:
    newprice = price - (price * 0.1)
    print('You received 10% discount! Your purchase price is US${:.2f}\n'
          'Thank you for your purchase, come back often!'.format(newprice))
elif payment == 2:
    newprice = price - (price * 0.05)
    print('You received 5% discount! Your purchase price is US${:.2f}\n'
          'Thank you for your purchase, come back often!'.format(newprice))
elif payment == 3:
    installments = int(input('How many installments do you want to make? '))
    # Verifica se o número de parcelas está entre 1 e 2
    if 1 != installments != 2:
        print('In this option, the number of installments only can be 1 or 2!\n'
              'Make the purchase again!')
    else:
        newprice = price
        per_installment = newprice / installments
        print('Your US${:.2f} purchase, it was divides into {} installments of US${:.2f}\n'
              'Thank you for your purchase, come back often!'.format(newprice, installments, per_installment))
elif payment == 4:
    # Recebe em quantas parcelas serão e devolve a resposta
    installments = int(input('How many installments do you want to make? '))
    # Verifica se o número de parcelas é realmente três ou maior
    if 3 > installments:
        print('In this option, the minimum number of installments is 3!\n'
              'Make the purchase again.')
    else:
        newprice = price + (price * 0.2)
        per_installment = newprice / installments
        print('Your US${:.2f} purchase, it was divided into {} installments of US${:.2f}\n'
              'Thank you for your purchase, come back often!'.format(newprice, installments, per_installment))
else:
    print('You do not choose any of allowed options! Make the purchase again.')
