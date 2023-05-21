print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')

from random import shuffle

mylist1 = ['','X','']

def husselen(list2):
    shuffle(list2)
    return list2

def user_input():
    keuze = int(input('Geef een keuze tussen index: 1 2 of 3 \n'))

    while keuze not in [1,2,3]:
        keuze = int(input('Geef een keuze tussen index: 1 2 of 3 \n'))

        if keuze in [1,2,3]:
            break
    return keuze-1

def check_winst(mylist,keuze):
    if mylist[keuze] == 'X':
        print('U heeft gewonnen!\n')

    else:
        print('U heeft verloren!\n')


def verder_spelen():
    verder = input('\nWilt u verder spelen? Type: ja of nee\n')

    while verder not in ['ja','nee']:
        verder = input('\nWilt u verder spelen? Type: ja of nee \n')

    if verder == 'ja':
        spel = True

    else:
        spel = False
        input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')
        quit()

    return spel

#LOGIC
print('''
Welkom bij het raad X spel! 

Raad of X nou verstopt zit op index 1 2 of 3!

[ , X , ] In dit geval op index 1

[ ?  , ? , ? ]
''')

game_on = True

while game_on:

    mylist = husselen(mylist1)
    keuze = user_input()
    check_winst(mylist,keuze)
    print(f"{mylist} stond op index {mylist.index('X')+1}")
    game_on = verder_spelen()




input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')