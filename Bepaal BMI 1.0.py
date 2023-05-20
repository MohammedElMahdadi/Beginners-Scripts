#SCRIPT UITLEG: De gebruiker wordt helemaal ondervraagd en op een gegeven moment returnt de script hele zinnen daarover.

naam = input('Wat is uw naam? ')
achternaam = input('Wat is uw achternaam? ')
geboortejaar = int(input('Wat is uw geboortejaar? '))
lengte = float(input("Wat is uw lengte in meters? "))
gewicht = float(input("Wat is uw gewicht in kg? "))


print('Goedendag ' + naam + ' ' + achternaam + '.')
print(f'U bent {2023-geboortejaar} jaar oud. ')

#FORMULE BMI: kg/m**2
bmi_waarde = gewicht/(lengte**2)

if bmi_waarde < 18.5:
    print(f'Uw BMI-Waarde is: {round(bmi_waarde,2)}. Dat betekent dat u veel te mager bent! Zoek contact op met uw huisarts!')
elif bmi_waarde >=18.5 and bmi_waarde < 25:
    print(f'Uw BMI-Waarde is: {round(bmi_waarde,2)}. Dat is goed, houden zo!')
else:
    print(f'Uw BMI-Waarde is: {round(bmi_waarde,2)}. Dat is veel te hoog! Zoek een geschikt dieet!')
