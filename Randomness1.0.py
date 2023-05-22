print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')

import random

print('''

22-5-2023

Vandaag ging het onder andere over randomness.

Wil je een kop of munt programma? kies KM
Wil je een getal raden tussen n en m? kies GR
Wil je namen invoeren, en dan random laten kiezen wie er moet betalen? kies RK

Als je STOP kiest, dan sluit het programma af.

''')

def KM():

    r = random.randint(0, 1)

    speler_1 = input('Kies kop of munt \n')

    while speler_1 not in ['kop','munt']:
        speler_1 = input('\nIk begrijp u niet. Kies kop of munt \n')

    if r == 1:
        print('\nHet was kop. \n')
    else:
        print('\nHet was munt. \n')


def RK():

    print('''
    
    Stel je wil Albert, Bart en Cor invullen, dan doe je dat zo:
    
    Albert, Bart, Cor
    
    ''')
    namen = input("\nVoer de namen in gescheiden met comma's: \n")

    split_namen = namen.split(', ')

    x = random.randint(0,len(split_namen)-1)

    print(f'\n{split_namen[x]} moet gaan betalen.\n')


def GR():
    print('\nKies de getallen n en m waar het random getal zich zal bevinden.\n')
    print('\nDus een getal tussen 1 en 10 geeft: n = 1 en m = 10 \n')

    n = int(input('\nVoer een grens n in: \n'))
    m = int(input('\nVoer een andere grens m in: \n'))

    r = random.randint(n,m)

    print('\nHet random getal is: {r}'.format(r=r))


def eind_functie():
    welke = input('\nWelke random functie wilt u gebruiken? kies: KM GR RK of STOP \n')

    while welke not in ['KM','GR','RK','STOP']:
        welke = input('\nWelke random functie wilt u gebruiken? kies: KM GR RK of STOP \n')

    if welke == 'KM':
        KM()

    elif welke == 'GR':
        GR()

    elif welke == 'RK':
        RK()

    else:
        print('\nBedankt voor het gebruikmaken van mijn script!\n')
        input('Toets ENTER ')
        quit()


s = True

while s:
    eind_functie()