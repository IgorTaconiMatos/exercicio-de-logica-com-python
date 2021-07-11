from collections import defaultdict
from typing import List


def ano_com_mais_pessoas_trabalhando(matriz: List[List[int]]) -> List[List[int]]:
    """Calcula em qual/quais ano/anos houve mais pessoas trabalhando.
    Args:
            matriz: base de dados
    """
    registro = defaultdict(lambda: 0)

    for index in matriz:
        for ano in range(index[0], index[1] + 1):
            registro[ano] += 1

    resultado = list(
        filter(
            lambda x: max([k[1] for k in registro.items()]) in x,
            registro.items(),
        )
    )

    return resultado
