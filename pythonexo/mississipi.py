chaine = "mississippi"

comptes = {}

for lettre in chaine:
    if lettre in comptes:
        comptes[lettre] += 1
    else:
        comptes[lettre] = 1

for lettre, compte in comptes.items():
    print(f"{lettre}: {compte}")
