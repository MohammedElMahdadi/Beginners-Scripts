print('''

-----------------------------------------------------------------------------
Info Script-Schrijver:

Mohammed El Mahdadi
e-mail: mohammed_elmahdadi@outlook.com

-----------------------------------------------------------------------------
''')


def domein_som():
    lst = []

    n = int(input("\nVoer het aantal getallen in die je wil optellen: "))

    for i in range(0,n):
        ele = int(input('\nVoer de getallen zelf in, na elk getal toets je eerst ENTER: '))
        lst.append(ele)

    return lst

def domein_product():
    lst = []

    n = int(input("\nVoer het aantal getallen in die je wil vermenigvuldigen met elkaar: "))

    for i in range(0,n):
        ele = int(input('\nVoer de getallen zelf in, na elk getal toets je eerst ENTER: '))
        lst.append(ele)

    return lst

def product(mylist2):

    totale_product = 1

    for getal in mylist2:
        totale_product *= getal
    print(f'\nHet product van de getallen is: {totale_product}')

def som(mylist):

    totale_som = 0

    for getal in mylist:
        totale_som += getal

    print(f'\nDe Som van de getallen is: {totale_som}')

def deelbaarheidscheck():
    a = int(input('\nVoer een getal a in: '))
    b = int(input('\nVoer een getal b in: '))

    if a % b == 0:
        print(f'\n{a} = {b} x {a//b}')
        print('\nEr is geen restant.')
    else:
        print(f'\n{a} = {b} x {a//b} + {a%b}')
        print(f'\nDus rest = {a%b}')

def priem_check(n):
    priem = False

    if n <= 1:
        print(num, 'is geen priemgetal.')
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                priem = True
                break
    if priem:
        print(f"\n{n} is geen priemgetal.")
    else:
        print('\n{} is wel een priemgetal!'.format(n))

def welkomstext():
    print('''
    
    Welkom bij rekenmachine 1.0!
    
    U moet nu een functie kiezen.
    
    Voor het berekenen van de som, kies: S
    Voor het vermenigvuldigen van getallen, kies: P
    Voor het laten checken of een getal een priemgetal is, kies: PC 
    Voor het nagaan of een getal deelbaar is door een ander getal, kies: D
    ''')

    keuze = input('Kies een van de volgende functies die deze rekenmachine verschaft: S, P, PC of D \n')

    while keuze not in ['S','P','PC','D']:
        keuze = input('\nU heeft iets verkeerds ingetypt. Kies: S, P, PC of D ')

    if keuze == 'S':
        mylist = domein_som()
        som(mylist)
    elif keuze == 'P':
        mylist2 = domein_product()
        product(mylist2)
    elif keuze == 'D':
        deelbaarheidscheck()
    elif keuze == 'PC':
        n = int(input('\nVoer een getal in: '))
        priem_check(n)

    return keuze

def doorgaan():
    d = input('Wilt u gebruik maken van andere functies? Kies: ja of nee ')

    while d not in ['ja','nee']:
        d = input('Ik begreep u niet. Kies ja of nee. ')

    if d == 'ja':
        doorgaan = True

    elif d == 'nee':
        doorgaan = False
        input('\nBedankt voor het gebruik maken van de script! Toets ENTER om af te sluiten. \n')
        quit()

    return doorgaan


door = True

while door:
    welkomstext()
    door = doorgaan()



























#priemgetal check











