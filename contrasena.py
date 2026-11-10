import utilidades
def comprobar_mayusculas(contrasena):
	for caracter in contrasena:
		if caracter.isupper():
			return True
	return False

def comprobar_longitud(contrasena):
	if len(contrasena) < 12:
		return False
	else:
		return True

contrasena="Hola12345"
contrasena2="holaholahol"
contrasena3="holaholahola"
print(contrasena)
print(f"Longitud contraseña 1: {comprobar_longitud(contrasena)}")
print(f"Longitud contraseña 2: {comprobar_longitud(contrasena2)}")
print(f"Longitud contraseña 3: {comprobar_longitud(contrasena3)}")
print(f"Digitos contraseña 1: {utilidades.comprobar_numero(contrasena)}")
print(f"Digitos contraseña 2: {utilidades.comprobar_numero(contrasena2)}")
print(f"Mayúsculas contraseña 1: {comprobar_mayusculas(contrasena)}")
