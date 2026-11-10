def comprobar_numero(contrasena):
	for caracter in contrasena:
		if caracter.isdigit():
			return True
	return False
