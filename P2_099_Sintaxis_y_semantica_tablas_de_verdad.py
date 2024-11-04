# Ingenieria_en_Mecatronica

# Programa_Sintaxis_y_Semantica_Tablas_de_Verdad

import itertools

def generate_truth_table(variables):
    """Genera una tabla de verdad con todas las combinaciones posibles de valores."""
    table = []
    permutations = itertools.product([True, False], repeat=len(variables))
    for perm in permutations:
        row = {}
        for i, var in enumerate(variables):
            row[var] = perm[i]
        table.append(row)
    return table

def evaluate_expression(expression, values):
    """Evalúa la expresión lógica con los valores dados."""
    # Reemplaza los valores de las variables en la expresión
    for var, value in values.items():
        expression = expression.replace(var, str(value))
    
    # Evalúa la expresión y devuelve el resultado
    return eval(expression)

def print_truth_table(expression, variables):
    """
    Imprime la tabla de verdad para la expresión lógica dada.
    
    Args:
    - expression: String que representa la expresión lógica
    - variables: Lista de strings que representan los nombres de las variables
    """
    # Genera la tabla de verdad
    table = generate_truth_table(variables)
    
    # Imprime el encabezado de la tabla
    header = '\t'.join(variables + [expression])
    print(header)
    print('-' * len(header))
    
    # Imprime cada fila de la tabla
    for row in table:
        values = [str(row[var]) for var in variables]
        result = evaluate_expression(expression, row)
        values.append(str(result))
        print('\t'.join(values))

# Expresión lógica y variables
expression = 'not A or (B and C)'
variables = ['A', 'B', 'C']
print_truth_table(expression, variables)
