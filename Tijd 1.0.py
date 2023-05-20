print('''
Welkom bij de grondige leeftijd check 1.0

We zullen het hebben over:

- Aantal jaren
- Aantal maanden
- Aantal weken
- Aantal dagen
- Aantal uren
- Aantal minuten
- Aantal seconden
- Aantal microseconden

leeftijd check 2.0 zal veel preciezer gaan berekenen.
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

