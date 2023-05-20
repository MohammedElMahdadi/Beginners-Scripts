print('''
Welkom bij de grondige leeftijd check 1.0

Idee:

(1)
Geeft afhankelijk van geboortejaar een inschatting van:

- Aantal jaren
- Aantal maanden
- Aantal weken
- Aantal dagen
- Aantal uren
- Aantal minuten
- Aantal seconden
- Aantal microseconden

(2)
Heeft een functie dat kan checken of een jaar een schrikkeljaar is.

(3)
Heeft een functie of een jaar een priemjaar is.

(4)
Heeft een functie om te berekenen hoeveel dagen het duurt tot een bepaalde datum in de toekomst.

(5)
.
.
.

''')

geboortejaar = int(input('In welk jaar bent u geboren? '))

jaren = 2023 - geboortejaar
maanden = jaren * 12
weken = maanden * 52
dagen = weken * 7
uren = dagen * 24
minuten = uren * 60
seconden = minuten * 60

print('Eerste Resultaat: \n')

print(f'Aantal jaren: {jaren}')
print(f'Aantal maanden: {maanden}')
print(f'Aantal weken: {weken}')
print(f'Aantal dagen: {dagen}')
print(f'Aantal uren: {uren}')
print(f'Aantal minuten: {minuten}')
print(f'Aantal seconden: {seconden}')

def schrikkeljaarchecker(jaar):

    if jaar%4 != 0:
        print(f'{jaar} is geen schrikkeljaar.')

    elif jaar%4 == 0:
        if jaar%100 != 0:
            print(f'{jaar} is een schrikkeljaar!')
        elif jaar%400 == 0:
            print(f'{jaar} is een schrikkeljaar!')
        else:
            print(f'{jaar} is geen schrikkeljaar.')


jaar = int(input('Van welk jaar wilt u checken of het een schrikkeljaar is?: '))

schrikkeljaarchecker(jaar)

