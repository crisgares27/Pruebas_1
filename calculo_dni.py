'''

numero / 23 , el resto cotejar en tabla:
#Posición     0   1   2   3  4   5   6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22

#Letra        T   R   W   A  G   M   Y  F  P  D  X    B   N   J   Z   S   Q   V   H   L   C   K   E
'''

#import random
#dni = 17378389
#second_dni = random.int(1000000, 99999999)

letter_position = input("Introduce el número de tu DNI, no en texto, por favor: ")
letter_position = int(letter_position)
letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print('La letra del tu DNI es: ', letras[letter_position%23])