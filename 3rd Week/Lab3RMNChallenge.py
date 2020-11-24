value = int(input("Enter an integer value from 1 to 999: "))

Rnums = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD': 400, 'D':500, 'CM': 900, 'M':1000}

M = value // Rnums['M']
value -= Rnums['M']*M

CM = value // Rnums['CM']
value -= Rnums['CM']*CM

D = value // Rnums['D']
value -= Rnums['D']*D

CD = value // Rnums['CD']
value -= Rnums['CD']*CD

C = value // Rnums['C']
value -= Rnums['C']*C

XC = value // Rnums['XC']
value -= Rnums['XC']*XC

L = value // Rnums['L']
value -= Rnums['L']*L

XL = value // Rnums['XL']
value -= Rnums['XL']*XL

X = value // Rnums['X']
value -= Rnums['X']*X

IX = value // Rnums['IX']
value -= Rnums['IX']*IX

V = value // Rnums['V']
value -= Rnums['V']*V

IV = value // Rnums['IV']
value -= Rnums['IV']*IV

I = value

Roman = (M * 'M') + (CM * 'CM') + (D * 'D') + (CD * 'CD') + (C * 'C') + (XC * 'XC') + (L * 'L') + (XL * 'XL') + (X * "X") + (IX * 'IX') + (V * "V") + (IV * 'IV') + (I * "I")
print("Roman numeral equivalent: " + str(Roman))
