from random import randrange
# Importei Emojis pra ficar bonito
import emoji
option = str(input('Nice too meet you! Do you wanna play Jokenpô with me?(yes/no) '))
# Minimiza tudo para evitar conflitos com a digitação
option = option.lower()
# Descobre qual foi a opção escolhida
if option == 'yes' or option == 'y':
    user_choice = int(input(emoji.emojize("I will play at the same time as you! What's your choice?\n"
                            '1.:raised_fist: Rock;\n'
                            '2.:raised_hand: Paper;\n'
                            '3.:victory_hand: Scissors: ')))
    # Gera qual foi a escolha do computador
    computer_choice = randrange(1, 4)
    # Descobre se o que aconteceu foi uma vitória, derrota ou empate
    if user_choice == computer_choice:
        result = 'That was a draw! :crossed_swords:'
    elif user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 3 \
            or user_choice == 3 and computer_choice == 1:
        result = 'The winner is me! :grinning_squinting_face:'
    elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1\
            or user_choice == 3 and computer_choice == 2:
        result = 'The winner is you! :clapping_hands::glowing_star:'
    else:
        result = 'You have to choose a valid option!'
    # Substituí o número da escolha do usuário por um emoji
    if user_choice == 1:
        user_choice = ':raised_fist:'
    elif user_choice == 2:
        user_choice = ':raised_hand:'
    else:
        user_choice = ':victory_hand:'
    # Substituí o número da escolha do computador por um emoji
    if computer_choice == 1:
        computer_choice = ':raised_fist:'
    elif computer_choice == 2:
        computer_choice = ':raised_hand:'
    else:
        computer_choice = ':victory_hand:'
    # Imprime o resultado
    print(emoji.emojize('\nMy choice: {} / Your choice: {} \n'
          '{}'.format(computer_choice, user_choice, result)))
elif option == 'no' or option == 'n':
    print(emoji.emojize('Oh what a pity! Next time then :pensive_face:'))
else:
    print(emoji.emojize("Are you ok? I didn't understand your answer :grinning_face_with_sweat:"))
