# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: Melani Chong

import random

def bienvenida():
    #Mostrar bienevenida y datos generales del jugador
    print('¡Te doy la bienvenida a la Trivia de Python!')
    nombre = input('Ingresa tu nombre, por favor: ')
    edad = int(input('Ingresa tu edad, por favor: '))
    return nombre, edad

def validar_edad(nombre, edad):
    # Validar si el jugador tiene la edad mínima para jugar
    if edad >= 18:
        print(f'\n¡Hola {nombre}, es hora de comenzar con la Trivia sobre Python!\n')
        print('Antes de comenzar, las instrucciones del juego son las siguientes:')
        print('Debes contestar correctamente las preguntas. Por cada respuesta correcta, ganarás 1 punto.')
        print('Por cada respuesta incorrecta, no sumarás puntos. Sin embargo, si te equivocas más de tres veces, pierdes el juego.')
        print('¡Ahora sí, a jugar!')
        print('------------------------------------')
    else:
        print(f'Lo siento {nombre}, no tienes la edad mínima para jugar' )
        exit()

def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    # Verificar si la respuesta del jugador o usuario es correcta
    if respuesta_usuario == respuesta_correcta:
        print('\nRespuesta correcta.')
        return True
    else:
        print('\nRespuesta incorrecta.')
        print(f'La respuesta correcta es: {respuesta_correcta}.')
        return False
    
def juego_trivia():
    # Funcion principal del juego
    nombre, edad = bienvenida()
    validar_edad(nombre, edad)

    # Preguntas y respuestas
    trivia =  [
        ('¿Un algoritmo es un conjunto de instrucciones secuenciales que permiten la resolución de un problema?',  ('A.Verdadero', 'B.Falso'), 'A'),
        ('Un lenguaje de programación es un conjunto de reglas, sintaxis y semántica que permite a los programadores escribir instrucciones que una computadora puede entender y ejecutar', ('A.Verdadero', 'B.Falso'), 'A'),
        ('Son ejemplos de lenguajes interpretados: Ruby, JavaScript y Python', ('A.Verdadero', 'B.Falso'), 'A'),
        ('JavaScript fue creado por Guido van Rossum a finales de los años 80:', ('A.Verdadero', 'B.Falso'), 'B'),
        ('Los diccionarios son una variable que permite almacenar varios datos inmutables (no se pueden modificar una vez creados) de tipos diferentes:', ('A.Verdadero', 'B.Falso'), 'B'),
        ('Las listas permiten modificar los datos una vez creados, es decir no son inmutables:', ('A.Verdadero', 'B.Falso'), 'A'),
        ('Permite utilizar una clave para declarar y acceder a un valor, además permite modificar los valores: ¿hablamos de los diccionarios?', ('A.Verdadero', 'B.Falso'), 'A'),
        ('En el ámbito de la informática, la indentación cumple una función similar a la de la sangría en la escritura formal del lenguaje humano', ('A.Verdadero', 'B.Falso'), 'A'),
        ('¿La indentación es obligatoria en Python? ', ('A.Verdadero', 'B.Falso'), 'A'),
        ('Se encarga de ejecutar una misma acción “mientras que” una determinada condición se cumpla. ¿Lo anterior corresponde al bucle for?', ('A.Verdadero', 'B.Falso'), 'B'),
        ('¿El bucle for permite iterar sobre una variable compleja del tipo lista o tupla?', ('A.Verdadero', 'B.Falso'), 'A')
    ]

    # Mezclar preguntas
    random.shuffle(trivia)

    #Inicializar variables
    score = 0
    contador_errores = 0
    numero_pregunta = 0
    aciertos = []

    # Recorrer cada pregunta
    for pregunta, opciones, respuesta_correcta in trivia:
        print('-----------------------------------')
        print(pregunta)
        for opcion in opciones:
            print(opcion)
        
        # Obtener respuesta del usuario
        respuesta_usuario = input('Responde (A o B): ').upper()
        aciertos.append(respuesta_usuario)

        # Verificar si la respuesta es correcta
        if verificar_respuesta(respuesta_usuario, respuesta_correcta):
            score += 1
        else:
            contador_errores += 1
            print(f'Llevas {contador_errores} errores')

        # Verificar si el jugador ha cometido 3 errores
        if contador_errores >= 3:
            print('Has cometido 3 errores. ¡PERDISTE EL JUEGO!')
            break 


    if contador_errores < 3:
        mostrar_resultados(score, aciertos, [respuesta for _, _, respuesta in trivia])

def mostrar_resultados(score, aciertos, respuestas):
    # Mostrar los resultados finales del juego
    print('---------------------------------')
    print('            RESULTADOS           ')
    print('---------------------------------')

    # Mostrar respuestas correctas
    print('Respuestas correctas: ', end='')
    for respuesta in respuestas:
        print(respuesta, end='')
    print()

    # Mostrar respuestas del jugador
    print('Respuestas del jugador: ', end='')
    for acierto in aciertos:
        print(acierto, end='')
    print()

    # Calcular y mostrar el puntaje final 
    puntaje_final = int(score / len(respuestas) * 100)
    print(f'Tu puntaje es: {puntaje_final}%')

    # Mensaje final
    print('\n¡Gracias por jugar esta trivia sobre Python, bonita día!')

# Iniciar el juego
juego_trivia()
