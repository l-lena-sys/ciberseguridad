def comprobar_mayusculas(contrasena):
	for caracter in contrasena:
		if caracter.isupper():
			return True
	return False

def comprobar_longitud(contrasena):
	if len(contrasena) < 8:
		return False
	else:
		return True

contrasena="hola12345"
print(contrasena)
print(comprobar_longitud(contrasena))
print(comprobar_mayusculas(contrasena))
