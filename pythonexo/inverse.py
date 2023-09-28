def inverser_entier(entier):
    entier_str = str(entier)
    
    if entier_str[0] == '-':
        inverse_str = '-' + entier_str[:0:-1]
    else:
        inverse_str = entier_str[::-1]
    
    inverse = int(inverse_str)
    
    return inverse

entier1 = -6523
entier2 = 123

inverse1 = inverser_entier(entier1)
inverse2 = inverser_entier(entier2)

print(f"Inversion de {entier1}: {inverse1}")
print(f"Inversion de {entier2}: {inverse2}")

A = {'a', 'b', 'c'}
B = {'c', 'r'}

difference_A_B = A - B
difference_B_A = B - A
union_A_B = A | B
intersection_A_B = A & B
difference_symetrique_A_B = A ^ B

print("Différence A - B:", difference_A_B)
print("Différence B - A:", difference_B_A)
print("Union A | B:", union_A_B)
print("Intersection A & B:", intersection_A_B)
print("Différence symétrique A ^ B:", difference_symetrique_A_B)