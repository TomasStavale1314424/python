import random
import sys

# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?","¿Cuál de las siguientes opciones es un número entero en Python?","¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?","¿Cuál es el operador de comparación para verificar si dos valores son iguales?"]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),("3.14", "'42'", "10", "True"),("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "===")

]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]


"""CREO EL PUNTAJE"""
PlayerPoints = float(0)

"""TOME EL CODIGO DE AYUDA Y LO IMPLEMENTE"""
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for quest, solution, correct_solution in questions_to_ask:
    
    # Se muestra la pregunta y las respuestas posibles
    print(quest)
    for i, answer in enumerate(solution):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):

        """MODIFICO EL INPUT PARA PODER INGRESAR STRING Y VERIFICO QUE NO LO SEA"""
        user_answer = input("Respuesta: ")
        if user_answer.isdigit():
            user_answer = int(user_answer) - 1
        else:
            print("Respuesta no Valida")
            sys.exit(1)                 
        # Se verifica si la respuesta es correcta

        """MODIFICO EL IF PARA VERIFICAR QUE LA RESPUESTA DADA ESTE ENTRE LAS OPCIONES POSIBLES"""
        if user_answer == correct_solution:
            print("¡Correcto! +1p")
            PlayerPoints += 1
            break
        elif user_answer >= 0:
            if user_answer < 4:
                print("Incorrecto -0.5p")
                PlayerPoints -= 0.5
                continue
            else:
                print("Respuesta no Valida")
                sys.exit(1)       
        else:
            print("Respuesta no Valida")
            sys.exit(1)    
    else:
# Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print("Fallaste. La respuesta correcta es:")
        print(solution[correct_solution])
# Se imprime un blanco al final de la pregunta
    print()

"""MUESTRA LOS PUNTOS DEL JUGADOR/ORA"""

print("El puntaje del jugador/ora fue de ",PlayerPoints)