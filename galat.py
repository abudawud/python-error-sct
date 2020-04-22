#!/usr/bin/env python3

# Import module trigonometri
from math import cos, radians as rad

valDec=0     # variabel untuk nilai dengan 2 desimal
valReal=0     # variabel untuk nilai sebenarnya

# lakukan perulangan dari 1 - 360
for n in range(360):
    # konversi dari derajat ke radian
    valRad = rad(n + 1)
    # hitung nilai tiap n
    valDec += round(100 * cos(valRad) )
    valReal += cos(valRad)

# konversi ke desimal
valDec /= 100.0
# Print nilai dengan 2 angka desimal
print("Nilai 2 desimal dari total cos(n), n = 1 - 360: ", (valDec) )
# Print nilai sebenarnya
print("Nilai sebenarnya dari total cos(n), n = 1 - 360: ", (valReal) )
# Print galat sesungguhnya
print("Galat sesungguhnya adalah sekitar: ", (abs(valDec - valReal)) )