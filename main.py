#Variables del codigo
puntaje = 0;

# Mensaje de bievenida
print ("Bienvenido a mi trivia sobre la pandemia")
print ("Pondremos a prueba tus conocimientos")

nombre = input("Ingresa tu nombre: ")

# Instrucciones de la trivia:
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa (en mayuscula o minuscula) y presionando 'Enter' para enviar tu respuesta:\n")
print ("Nota:", nombre, ", obtendras puntos a memida que respondas correctamente\n")

print ("Pregunta 1:\n")

# Pregunta 1
print ("1) ¿Donde se inicio el covid?")
print ("a) China")
print ("b) EE.UU")
print ("c) Rusia")
print ("d) Perú")
respuesta_1 = input("\nTu respuesta: ").lower()

while respuesta_1 not in ("a", "b", "c", "d", "x"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if (respuesta_1 == "a"):
  print ("Muy bien", nombre, "!")
  puntaje = puntaje + 1
elif (respuesta_1 == "x"):
  print ("Wuau, encontraste un código oculto", nombre, "!, se te dará un punto adicional")
  puntaje = puntaje + 1
else:
  print ("Incorrecto! ")
  print ("La respuesta correcta es : a) China")
print ("Tu puntaje es: ", puntaje)

# Pregunta 2
print ("\nPregunta 2:\n")
print ("2) ¿Cuantas dosis deberias tener si tienes más de 18 años?")
print ("a) Ninguna")
print ("b) 2")
print ("c) 3")
print ("d) 4")
respuesta_2 = input("\nTu respuesta: ").lower()

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if (respuesta_2 == "d"):
  print ("Muy bien", nombre, "!")
  puntaje = puntaje + 1
else:
  print ("Incorrecto! ")
  print ("La respuesta correcta es : d) 4")
  print ("Ya puedes tener tu 4ta dosis, vacunate")
print ("Tu puntaje es: ", puntaje)

# Pregunta 3
print ("\nPregunta 3:\n")
print ("3) ¿Que es el SARS-CoV-2 ?")
print ("a) Proteina")
print ("b) Bacteria")
print ("c) Virus")
print ("d) Ninguna de las anteriores")
respuesta_3 = input("\nTu respuesta: ").lower()

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if (respuesta_3 == "c"):
  print ("Muy bien", nombre, "!")
  puntaje = puntaje + 1
else:
  print ("Incorrecto! ")
  print ("La respuesta correcta es : c) Virus")
  print ("Ya puedes tener tu 4ta dosis, vacunate")
print ("Tu puntaje es: ", puntaje)

# Pregunta 4
print ("\nPregunta 4:\n")
print ("4) ¿En que año se confirmo el paciente cero en el Perú?")
print ("a) 2021")
print ("b) 2019")
print ("c) 2020")
print ("d) 2022")
respuesta_4 = input("\nTu respuesta: ").lower()

while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if (respuesta_4 == "c"):
  print ("Muy bien", nombre, "!")
  puntaje = puntaje + 1
else:
  print ("Incorrecto! ")
  print ("La respuesta correcta es : c) 2020")
print ("Tu puntaje es: ", puntaje)

print ("Tu puntaje total es: ", puntaje)

print (nombre, ", muchas gracias por participar")


