from re import findall


def valida(string: str) -> str:
	""" Verifica o fechamento de parênteses, chaves e colchetes de uma string.
	Args:
		string: string a ser verificada.
	"""
	parêntese = findall(r'\(|\)', string)
	colchete = findall(r'\[|\]', string)
	chave = findall(r'{|}', string)

	if not len(parêntese) % 2 and not len(colchete) % 2 and not len(chave) % 2:
		return 'é uma sequência válida'
	elif len(parêntese) % 2:
		return 'não é uma sequência válida (há um parêntese posicionado incoretamente)'
	elif len(colchete) % 2:
		return 'não é uma sequência válida (há um colchete posicionado incoretamente)'
	elif len(chave) % 2:
		return 'não é uma sequência válida (há uma chave posicionado incoretamente)'
