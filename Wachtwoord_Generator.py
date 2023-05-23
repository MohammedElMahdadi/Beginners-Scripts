print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')

print(
    '''
Welkom bij mijn wachtwoord generator.
    
Wilt u een wachtwoord laten verzinnen? 
    
Maak dan gebruik van dit programma.
    
U kunt zelf kiezen uit hoeveel letters, cijfers en speciale tekens het wachtwoord moet bestaan.
    '''
)


import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
cijfers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
speciale_tekens = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

aantal_letters = int(input('Uit hoeveel letters moet het wachtwoord bestaan? '))
aantal_cijfers = int(input('Uit hoeveel cijfers moet het wachtwoord bestaan? '))
aantal_spec = int(input('Uit hoeveel speciale tekens moet het wachtwoord bestaan? '))

l = []

for c in range(aantal_cijfers):
    l.append(str(random.choice(cijfers)))

for z in range(aantal_letters):
    l.append(str(random.choice(letters)))

for s in range(aantal_spec):
    l.append(str(random.choice(speciale_tekens)))

random.shuffle(l)

ww = ''.join(l)

print(f'\nHet wachtwoord is: {ww}')


input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')











