from random import shuffle

mylist1 = ['','O','']

def husselen(list2):
    shuffle(list2)
    return list2

def user_input():
    keuze = input('Geef een keuze tussen 0 1 2 ')

    while keuze not in ['0','1','2']:
        keuze = input('Geef een keuze tussen 0 1 2 ')

        if keuze in ['0','1','2']:
            break
    return int(keuze)

def check_winst(mylist,keuze):
    if mylist[keuze] == 'O':
        print('U heeft gewonnen!')
    else:
        print('U heeft verloren!')

#LOGIC
print('''
Welkom bij het raad spel! 
Raad of een object nou verstopt zit op index 0, 1 of 2!
[, 'O', ] In dit geval op index 1
[X,X,X]
''')

mylist = mylist1

keuze = user_input()

check_winst(mylist,keuze)
