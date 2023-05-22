print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')

print('''

22-5-2023

Welkom bij stat1.0! Vul alle waarden in met spatie tussen de waarden. Let er op dat het moet bestaan uit gehele getallen.

Versie 1.0 verschaft: minimum , maximum , gemiddelde , variantie en standaarddeviatie.

''')

def domein():

    domein = []
    waarden = input("\nVul de waarden in met een spatie er tussen: ")

    waarden_lijst = waarden.split()

    for waarde in waarden_lijst:
        domein.append(int(waarde))

    return domein

def maximum(domein):
    print(f'\nHet maximum is: {max(domein)}')


def minimum(domein):
    print(f'\nHet minimum is: {min(domein)}')

def gemiddelde(domein):
    total_sum = 0

    for n in domein:
        total_sum += n

    print(f'\nHet gemiddelde is: {round((total_sum / len(domein)),2)}')

def variantie(domein):
    eerste_som = 0

    for waarde in domein:
        eerste_som += waarde

    gemiddelde = eerste_som / len(domein)

    out = []

    for n in domein:
        out.append((n-gemiddelde)**2)

    print(f'\nDe variantie is: {round(sum(out)/len(out),1)}')
    print(f'\nDe standaarddeviatie is: {round((sum(out)/len(out))**0.5,1)}')

def doorgaan():
    d = input('Wilt u nogmaals stat1.0 gebruiken? kies: ja of nee ')

    while d not in ['ja','nee']:
        d = input('Wilt u nogmaals stat1.0 gebruiken? kies ja of nee')

    if d == 'ja':
        j = True
    else:
        print('Bedankt voor het gebruiken van stat1.0!')
        quit()

    return j


domein = domein()
maximum(domein)
minimum(domein)
gemiddelde(domein)
variantie(domein)

print('\nBedankt voor het gebruiken van stat1.0!')
input('\nToets ENTER ')