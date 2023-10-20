import math

w = float(input())  # width
h = float(input())  # height

mostellerFormula = math.sqrt(w*h)/60
haycockFormula = 0.024265*(w**0.5378)*(h**0.3964)
boydFormula = 0.0333*(w**(0.6157-0.0188*math.log10(w)))*(h**0.3)

print(mostellerFormula, haycockFormula, boydFormula, sep='\n')