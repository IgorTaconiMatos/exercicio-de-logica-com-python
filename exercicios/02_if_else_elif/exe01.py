"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input("Digite uma letra: ")).strip().upper()
if "AEIOUY" in letra:
    print("É uma vogal")
else:
    print("É uma consante")
