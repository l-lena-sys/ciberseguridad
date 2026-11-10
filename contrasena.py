def comprobar_longitud(contrasena):
	if len(contrasena) < 8:
		return False
	else:
		return True

contrasena="Hola12345"
print(contrasena)
print(comprobar_longitud(contrasena))
