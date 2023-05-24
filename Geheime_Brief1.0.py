print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')

print('''

24-5-2023

Korte uitleg: Je voert een woord in. Kies daarna je lievelingsgetal tussen 1 en 25. 

Dan wordt van dat woord een geheim woord gemaakt die niemand kan begrijpen.

Dat woord en je lievelingsgetal moet je daarna weten om te ontrafelen wat het geheim woord betekent.

''')



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def geheim():

    text = input('\nVoer een woord die we in geheime tekst gaan converteren: ')
    shift = int(input('\nVoer uw lievelingsgetal in (1-25): '))

    l1 = []
    l2 = []

    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift

        l1.append(position)
        l2.append(new_position)

    s = ''

    for i in l1:
        s+= alphabet[i]

    s2 = ''

    for i in l2:
        s2 += alphabet[i]


    print(f'\nHet geheim woord is: {s2}')
    print(f'\nVoor het ontrafelen gebruikt u uw lievelingsgetal: {shift}')


geheim()

def ontrafelen():
    text = input('\nVoer het geheim woord in: ')
    shifts = int(input('\nVoer uw lievelingsgetal in (1-25): '))

    l3 = []
    l4 = []

    for letter in text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            re_position = position - shifts



        l3.append(position)
        l4.append(re_position)

        z = ''
        z2 = ''

        for i in l3:
            z+= alphabet[i]

        for i in l4:
            z2+=alphabet[i]


    print('\nHet geheim woord is: {} en is ontrafeld als: {}'.format(z,z2))


keuze = input('\nWilt u uw woord gaan ontrafelen? Kies ja of nee: ')

while keuze not in ['ja','nee']:
    keuze = input('\nIk begreep het niet. Voer ja of nee in. ')

if keuze == 'ja':
    ontrafelen()
    input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')

else:
    input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')

