def display(list):
    print(the_list[7] + '|' + the_list[8] + '|' + the_list[9])
    print(the_list[4] + '|' + the_list[5] + '|' + the_list[6])
    print(the_list[1] + '|' + the_list[2] + '|' + the_list[3])
    return '\nDankuwel voor het spelen!'

def f2():
    keuze_X_O = input('Maak een keuze tussen X of O: ')

    while keuze_X_O not in ['X','O']:
        keuze_X_O = input('Maak een keuze tussen X of O: ')

    return (keuze_X_O)

def f3():
    keuze19 = int(input('Maak een keuze tussen index 1-9: '))

    while keuze19 not in list(range(1,10)):
        keuze19 = int(input('Maak een keuze tussen index 1-9: '))

    return (keuze19)

def f4(the_list,XO,keuze19):
    the_list[keuze19] = XO

    #HORIZONTAAL
    if (the_list[1] == 'X' and the_list[2] == 'X' and the_list[3] == 'X') or (the_list[4] == 'X' and the_list[5] == 'X' and the_list[6] == 'X') or (the_list[7] == 'X' and the_list[8] == 'X' and the_list[9] == 'X'):
        print('X heeft gewonnen!')
        print(display(the_list))
        quit()

    #Verticaal
    elif (the_list[1] == 'X' and the_list[4] == 'X' and the_list[7] == 'X') or (the_list[2] == 'X' and the_list[5] == 'X' and the_list[8] == 'X') or (the_list[3] == 'X' and the_list[6] == 'X' and the_list[9] == 'X'):
        print('X heeft gewonnen!')
        print(display(the_list))
        quit()

    #diagonaal
    elif (the_list[1] == 'X' and the_list[5] == 'X' and the_list[9] == 'X') or (the_list[3] == 'X' and the_list[5] == 'X' and the_list[7] == 'X'):
        print('X heeft gewonnen!')
        print(display(the_list))
        quit()

    # HORIZONTAAL
    if (the_list[1] == 'O' and the_list[2] == 'O' and the_list[3] == 'O') or (
            the_list[4] == 'O' and the_list[5] == 'O' and the_list[6] == 'O') or (
            the_list[7] == 'O' and the_list[8] == 'O' and the_list[9] == 'O'):
            print('O heeft gewonnen!')
            print(display(the_list))
            quit()

        # Verticaal
    elif (the_list[1] == 'O' and the_list[4] == 'O' and the_list[7] == 'O') or (
            the_list[2] == 'O' and the_list[5] == 'O' and the_list[8] == 'O') or (
            the_list[3] == 'O' and the_list[6] == 'O' and the_list[9] == 'O'):
            print('O heeft gewonnen!')
            print(display(the_list))
            quit()

        # diagonaal
    elif (the_list[1] == 'O' and the_list[5] == 'O' and the_list[9] == 'O') or (
        the_list[3] == 'O' and the_list[5] == 'O' and the_list[7] == 'O'):
            print('O heeft gewonnen!')
            print(display(the_list))
            quit()
    return(display(the_list))
def f6():
    for i in range(1,10):
        if the_list[i] == '':
            return True

the_list = ['E','','','','','','','','','']
display(the_list)

while f6():
    XO = f2()
    keuze19 = f3()
    f4(the_list,XO,keuze19)
