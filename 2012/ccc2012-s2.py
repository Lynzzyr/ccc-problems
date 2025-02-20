# CCC 2012 S2

romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

in_num = input()

a = [ int(in_num[i]) for i in range(0, len(in_num), 2) ]
r = [ romans.get(in_num[i]) for i in range(1, len(in_num), 2) ]

output = 0

for i in range(len(a)):
    if ( i != len(a) - 1 ):
        if ( r[i + 1] > r[i] ):
            output -= a[i] * r[i]
        else:
            output += a[i] * r[i]
    else:
        output += a[i] * r[i]

print(output)