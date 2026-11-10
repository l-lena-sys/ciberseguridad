import utilidades
def comprobar_longitud(contrasena):
	if len(contrasena) < 8:
		return False
	else:
		return True

contrasena="Hola1234"
contrasena2="Holahola"
print(contrasena)
print(comprobar_longitud(contrasena))
print(utilidades.comprobar_numero(contrasena))
print(utilidades.comprobar_numero(contrasena2))
