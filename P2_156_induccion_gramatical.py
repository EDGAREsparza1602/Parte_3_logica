import random
from collections import defaultdict

# Función para convertir una cadena en una lista de símbolos
def tokenize(string):
    return string.split()

# Función para construir una gramática en FNC a partir de ejemplos
def inductive_grammar_learning(examples):
    # Inicializamos un diccionario para almacenar las reglas de producción
    productions = defaultdict(list)

    # Para cada ejemplo, convertimos la cadena en una lista de símbolos y agregamos las reglas de producción
    for example in examples:
        tokens = tokenize(example)
        if len(tokens) > 1:
            # Si la cadena tiene más de un símbolo, agregamos reglas para los pares de símbolos consecutivos
            for i in range(len(tokens) - 1):
                productions[tokens[i]].append(tokens[i + 1])
        # Agregamos una regla terminal para el último símbolo
        productions[tokens[-1]].append(tokens[-1])

    # Generamos un conjunto de reglas para los símbolos no terminales
    non_terminals = set(productions.keys())

    # Para la simplicidad, no generamos combinaciones complicadas
    # En un contexto real, esto debería ser más elaborado para cumplir con la FNC
    return productions

# Función para generar nuevas cadenas a partir de la gramática aprendida
def generate_from_grammar(grammar, start_symbol, length=10):
    # Inicializamos la cadena resultante con el símbolo inicial
    result = [start_symbol]

    # Iteramos para generar la cadena de acuerdo con la gramática
    while len(result) < length:
        # Elegimos aleatoriamente una producción para el símbolo actual
        current_symbol = result[-1]
        production = random.choice(grammar.get(current_symbol, [current_symbol]))
        # Dividimos la producción en símbolos y los agregamos a la cadena resultante
        result.pop()  # Quitamos el símbolo actual
        result.extend(production.split())  # Agregamos la producción

    # Retornamos la cadena generada
    return ' '.join(result)

if __name__ == '__main__':
    # Definimos una lista de ejemplos de cadenas válidas en el lenguaje
    examples = [
        "a b c",
        "a d e f g",
        "a b c d e f"
    ]

    # Aplicamos el algoritmo de inducción gramatical para aprender la gramática
    learned_grammar = inductive_grammar_learning(examples)
    print("Gramática aprendida:")
    for key, value in learned_grammar.items():
        print(key, "->", value)

    # Generamos nuevas cadenas a partir de la gramática aprendida
    print("\nNuevas cadenas generadas:")
    for _ in range(5):
        generated_string = generate_from_grammar(learned_grammar, 'a')
        print(generated_string)
