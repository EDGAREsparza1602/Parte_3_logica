# Ingenieria_en_Mecatronica

# Programa_Ambigüedad

# Definimos la gramática como un diccionario donde las llaves son los símbolos no terminales y los valores son las reglas de producción
grammar = {
    'expr': ['expr + expr', 'expr - expr', 'expr * expr', 'expr / expr', '( expr )', 'number'],
    'number': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
}

# Función para generar todas las posibles interpretaciones de una expresión a partir de la gramática
def generate_expressions(grammar, symbol):
    if symbol not in grammar:  # Si es un símbolo terminal
        return [symbol]
    
    expressions = []
    for production in grammar[symbol]:
        # Generamos expresiones a partir de la producción
        parts = production.split()
        sub_expressions = []
        for part in parts:
            # Generamos subexpresiones recursivamente
            sub_expressions.append(generate_expressions(grammar, part))
        # Hacemos el producto cartesiano de las subexpresiones
        from itertools import product
        for combination in product(*sub_expressions):
            expressions.append(' '.join(combination))
    
    return expressions

# Función para evaluar una expresión aritmética
def evaluate_expression(expr):
    return eval(expr)

if __name__ == '__main__':
    # Definimos una expresión aritmética ambigua
    ambiguous_expr = '2 + 3 * 4'
    print("Expresión aritmética ambigua:", ambiguous_expr)

    # Generamos todas las posibles interpretaciones de la expresión
    interpretations = generate_expressions(grammar, 'expr')
    print("Posibles interpretaciones:")
    for interpretation in interpretations:
        try:
            print(interpretation, "=", evaluate_expression(interpretation))
        except Exception as e:
            print(interpretation, "no es una expresión válida:", e)
