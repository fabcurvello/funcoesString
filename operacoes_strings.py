# Operações com Strings
texto = "Rio de Janeiro"
print(texto)

# Imprimindo caracteres específicos da String
print(texto[0]) # R
print(texto[1]) # i
print(texto[7]) # J

# Imprimindo caracteres da String a partir do final da String
print(texto[-1]) # o
print(texto[-2]) # r

# Imprimindo trechos da String
print(texto[:2]) # Ri - Da posição 0 à 2, excluindo a 2
print(texto[:5]) # Rio d
print(texto[7:]) # Janeiro - A partir da posição 7
print(texto[7:9]) # Ja - Da posição 7 à 9, excluindo a 9

# Imprimindo caracteres da String pulando intervalos
print(texto[::2]) # Rod aer - Caracter sim, caracter não, a partir do 0
print(texto[::3]) # R  nr - de 3 em 3
print(texto[::4]) # Rdar - de 4 em 4
print(texto[::-1]) # orienaJ ed oiR - de trás pra frente. de 1 em 1

# Imprimindo cada um dos caracteres da String
for letra in texto:
    print(letra)

# Buscando por caracteres na String
print("a" in texto) # True
print("b" in texto) # False
print(" " in texto) # True
print("Janeiro" in texto) # True

