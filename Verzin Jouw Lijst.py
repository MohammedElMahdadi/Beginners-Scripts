# Speluitleg: De gebruiker krijgt een list. Kiest een index, en verandert de index met een verzonnen object.

the_list = ['', '', '']

def display():
    print('Welkom bij verzin een index!')
    print(the_list)

def keuze_index():
    keuze_index = int(input('Kies de indexen 0 1 2: '))

    while keuze_index not in [0,1,2]:
        keuze_index = int(input('Kies de indexen 0 1 2: '))

    return keuze_index

def keuze_object():
    keuze_object = input('Kies een object op de gegeven: ')
    return keuze_object

def g(ind,obj):
    the_list[ind] = obj
    print(the_list)

def verder_spelen():
    keuze_verder = input('Wilt u verder spelen? Kies: JA of NEE ')

    while keuze_verder not in ['JA','NEE']:
        keuze_verder = input('Wilt u verder spelen? Kies JA of NEE ')

    if keuze_verder == 'JA':
        verder = True
    elif keuze_verder == 'NEE':
        print('Tot de volgende keer!')
        quit()

    return keuze_verder

#THE LOGIC

display()
game_on = True

while game_on:
    ind = keuze_index()
    obj = keuze_object()
    g(ind,obj)
    game_on = verder_spelen()
