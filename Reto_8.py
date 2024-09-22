# Reto_08 
import random

# Decorador para registrar operaciones
def decorador(func):
    def funcion(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"Operación: {func.__name__}\nResultado:\n{result}\nOperación terminada")
        return result
    return funcion

class Matrix:
    def __init__(self, data):
        self.data = data

    @decorador
    def sumar(self, otra):
        return Matrix([[self.data[i][j] + otra.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])

    @decorador
    def multiplicar(self, otra):
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*otra.data)]for row in self.data]
        return Matrix(result)
    
    @decorador
    def determinante(self):
        return ((self.data[0][0]*self.data[1][1])-(self.data[0][1]*self.data[1][0]))
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    

# Generador de matrices aleatorias
def generate_random_matrix(rows, cols):
    while True:
        matrix_data = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
        yield Matrix(matrix_data)

# Uso del generador (solo sirve con matrices (2,2))
matrix_gen = generate_random_matrix(2, 2)
matrix_a = next(matrix_gen)
matrix_b = next(matrix_gen)

print("Matriz A:")
print(matrix_a)

print("Matriz B:")
print(matrix_b)

# Sumar, multiplicar y sacar la determinante de matrices
matrix_a.sumar(matrix_b)
matrix_a.multiplicar(matrix_b)
matrix_a.determinante()
matrix_b.determinante()