import utilidades
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

contrasena="Hola1234"
contrasena2="holahola"
print(contrasena)
print(comprobar_longitud(contrasena))
print(utilidades.comprobar_numero(contrasena))
print(utilidades.comprobar_numero(contrasena2))
print(comprobar_mayusculas(contrasena))
