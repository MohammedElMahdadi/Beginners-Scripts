print('''

Welkom bij de Pizzaria!

PRIJSLIJST IN EURO'S:

KLEINE PIZZA: 15
MEDIUM PIZZA: 20
GROTE PIZZA:  25

MET PEPPERONI VOOR KLEINE PIZZA: +2
MET PEPPERONI VOOR MEDIUM OF GROOT: +3

EXTRA GERASPTEKAAS: +1

''')

size = input('Welke grootte van de pizza? type: Groot Klein of Medium \n')
pepperoni = input('Wilt u met Pepperoni? Type: Ja of Nee \n')
kaas = input('Wilt u extra gerasptekaas bij de pizza? Type: Ja of Nee \n')

totale_kosten = 0

if size == 'Klein'.lower():
    totale_kosten += 15
elif size== 'Medium'.lower():
    totale_kosten += 20
elif size == 'Groot'.lower():
    totale_kosten += 25

if pepperoni == 'JA'.lower() and size == 'Klein'.lower():
    totale_kosten += 2
elif pepperoni == 'Ja'.lower() and (size == 'Medium'.lower() or size == 'Groot'.lower()):
    totale_kosten += 3
else:
    totale_kosten += 0

if kaas == 'Ja'.lower():
    totale_kosten += 1

print(f'Het te betalen bedrag is: {totale_kosten} EURO')




