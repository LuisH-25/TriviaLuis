# Librerias
import random  # Importamos la librería random
import time  

# Constantes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
time.sleep(1)  # Espera de 1 segundo

# Variables
puntaje = random.randint(1, 5)
preguntas = ["","¿Donde se inicio el covid?","¿Cuantas dosis deberias tener si tienes más de 18 años?","¿Que es el SARS-CoV-2 ?","¿En que año se confirmo el paciente cero en el Perú?"]
alternativas = [["","","",""],["a) China", "b) EE.UU", "c) Rusia","d) Perú"],["a) Ninguna", "b) 2", "c) 3","d) 4"],["a) Proteina", "b) Bacteria", "c) Virus","d) Ninguna de las anteriores"],["a) 2021", "b) 2019", "c) 2020","d) 2022"]]
respuestas = ["","","","",""]
respuestas_correctas = ["","a","d","c","c"]
conforme = "no"
edad = 0
nombre = ""
contador = 0;

time.sleep(1)
# Mensaje de bievenida
print (CYAN + "\nBienvenido a mi trivia sobre la pandemia" + RESET)
print ("Pondremos a prueba tus conocimientos")
time.sleep(1)


while conforme=="no":        # validacion del nombre
  nombre = input(YELLOW + "\nIngrese nombre:" + RESET)
  nombre = nombre.lower()
  time.sleep(1)
  conforme = input(GREEN + "\n¿" + nombre + " es su nombre? Responda con 'si' o  'no' : " + RESET).lower()
  while conforme not in ("si", "no"):
    conforme = input(RED + "\nResponda con 'si' o  'no' por favor: " + RESET).lower()
    time.sleep(1)
      
conforme = "no"

while conforme=="no":        # validacion de la edad
  edad = input(YELLOW + "\nIngrese su edad:" + RESET)
  
  time.sleep(1)
  while edad.isnumeric() == False:
    edad = input(RED+"\nIngrese una edad numérica valida "+RESET)
  conforme = input(GREEN+"\n¿" + edad+" es su edad? Responda con 'si' o  'no' : "+RESET).lower()
  time.sleep(1)
  while conforme not in ("si", "no"):
    conforme = input(RED + "\nResponda con 'si' o  'no' por favor: " + RESET).lower()

time.sleep(1)
    
# Instrucciones de la trivia:
print(YELLOW + "\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa (en mayuscula o minuscula) y presionando 'Enter' para enviar tu respuesta:\n" + RESET)
puntaje_inicial = random.randint(0, int(edad))

print(GREEN + "Nota:", nombre, ", obtendras puntos a memida que respondas correctamente "+ RESET)
conforme = input(YELLOW + "Obtuviste un puntaje inicial que esta entre 0 y "+edad+", quieres adivinar tu puntaje (si aciertas tendras puntos extras) Responda con 'si' o  'no'" + RESET)
if conforme == "x":
  puntaje = puntaje +20
  print("x se considera como si, y se te añadirá puntos extras por ser una persona con mucha suerte")
  
while conforme not in ("si", "no"):
  conforme = input(RED + "\nResponda con 'si' o  'no' por favor: " + RESET).lower()
  time.sleep(1)
if(conforme == 'si'):
  puntaje1 = input(RED + "\n¿Cual es su puntaje inicial?" + RESET)
  time.sleep(1)
  while puntaje1.isnumeric() == False:
    puntaje1 = input(RED+"\nIngrese un número "+RESET)
    time.sleep(1)
  if(puntaje1== puntaje_inicial):
    print(GREEN + "ACERTASTE"+ RESET)
    puntaje= puntaje_inicial + puntaje *2
  else:
    print ("El número a adivinar era: " + str(puntaje_inicial))
    
  print ("Tu puntaje inicial es: " + str(puntaje))
time.sleep(1)

conforme = "si"
while conforme == "si":
  
  print ("Comenzamos en: ")
  for contador in range (5,0,-1):
    print(contador)
    time.sleep(1)  # Espera 1 seg
  
  cantidad_preguntas = len(preguntas)
  for x in range (1,cantidad_preguntas):
    time.sleep(1)
    print(CYAN + "PREGUNTA " + str(x) + ":\n" + RESET)
    print(YELLOW+str(x) + ") " + preguntas[x] + RESET)
    for y in range (0,cantidad_preguntas-1):
      print(alternativas[x][y])
    respuestas[x] = input("\nTu respuesta es: ").lower()
    while respuestas[x] not in ("a", "b", "c", "d"):
      respuestas[x] = input(RED + "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " + RESET)
      puntaje = puntaje - 1
    
    if (respuestas_correctas[x] == respuestas[x]):
      print (GREEN + "Muy bien " + nombre + " !" + RESET)
      puntaje = puntaje + 1
    else:
      print (RED + "Incorrecto! " + RESET)
      print (GREEN + "La respuesta correcta es : "+ respuestas_correctas[x] + RESET)
      puntaje = puntaje - 1
    ##print ("Tu puntaje es: ", puntaje)
  
    print("\n")
    time.sleep(1)  # Espera 1 seg
    
  condicion= input("\n¿Deseas ver tus respuestas?").lower()
  while condicion not in ("si", "no"):
    condicion = input("Debes responder si ó no. Ingresa nuevamente tu respuesta: ").lower()
  
  if condicion == "si":
    for z in range (1,len(respuestas)):
      print("PREGUNTA " + str(z) + ": " + respuestas[z])
  condicion= input("\n¿Deseas volver a realizar la trivia?").lower()
  while condicion not in ("si", "no"):
    condicion = input(RED +"Debes responder si ó no. Ingresa nuevamente tu respuesta: " + RESET).lower()
  
for contador in range(0,5,1):
  print(".")
  time.sleep(1) # Espera 2 segundos antes de continuar.
  
print ("Tu puntaje total es: ", puntaje)
print (nombre, ", muchas gracias por participar")


