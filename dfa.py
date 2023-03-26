with open('dfa.txt') as file:
    *tranz, fin = file

stari = dict()

for i in tranz:
    trzs = i.strip().split(' ')
    print(trzs)
    try:
        stari[trzs[0]][trzs[1]] = trzs[2]
    except:
        stari[trzs[0]] = dict()
        stari[trzs[0]][trzs[1]] = trzs[2]
print(stari)
stare_start='q0'
stare_finala=set(fin.strip().split(' '))
print(stare_finala)
def read():
    return input("Introdu cuvant: ")

def dfa(input):
    stare_curenta = stare_start
    drum=[stare_curenta]
    for chestie in input:
        stare_curenta = stari[stare_curenta].get(chestie)
        if stare_curenta is None:
            return False
        drum.append(stare_curenta)
    return [stare_curenta in stare_finala,drum]

input = read()
if dfa(input)[0]:
    print(f"Cuvantul '{input}' este acceptat, drumul este {dfa(input)[1]}")
else:
    print(f"Cuvantul '{input}' nu este acceptat")

