"""
Peça ao usuário a altura 4 pessoas e calcule a média.
"""

pessoa1 = float(input('Altura da 1a pessoa: '))
pessoa2 = float(input('Altura da 2a pessoa: '))
pessoa3 = float(input('Altura da 3a pessoa: '))
pessoa4 = float(input('Altura da 4a pessoa: '))
média = (pessoa1 + pessoa2 + pessoa3 + pessoa4) / 4

print(f'A média do grupo é {média:.2f} m')
