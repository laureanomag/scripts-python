import numpy as np

 #Funciones de NumPy
# CREAR ARRAYS

# np.array() → convierte una lista en array
a = np.array([7, 2, 9, 10])
print(a)        # [ 7  2  9 10]

# np.zeros() → array relleno de ceros, útil para inicializar
b = np.zeros((3, 4))   # 3 filas, 4 columnas
print(b)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# np.ones() → array relleno de unos
c = np.ones((2, 3))
print(c)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# np.full() → array relleno con un valor específico
d = np.full((2, 2), 7)
print(d)
# [[7 7]
#  [7 7]]

# np.arange() → valores en un rango con un paso definido
e = np.arange(0, 10, 2)   # de 0 a 9, de a 2
print(e)   # [0 2 4 6 8]

# np.linspace() → N valores igualmente espaciados entre dos puntos
f = np.linspace(0, 1, 5)   # 5 valores entre 0 y 1
print(f)   # [0.   0.25 0.5  0.75 1.  ]

# np.eye() → matriz identidad (diagonal de unos, resto ceros)
g = np.eye(3)
print(g)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# np.random.randint() → array de enteros aleatorios
h = np.random.randint(0, 10, (3, 3))   # entre 0 y 9, forma (3, 3)
print(h)   # valores distintos cada vez que se ejecuta

# OPERACIONES MATEMÁTICAS

a = np.array([1, 2, 3, 4, 5])

# np.add() → suma un valor a cada elemento
print(np.add(a, 10))        # [11 12 13 14 15]

# np.subtract() → resta un valor a cada elemento
print(np.subtract(a, 2))    # [-1  0  1  2  3]

# np.multiply() → multiplica cada elemento por un valor
print(np.multiply(a, 3))    # [ 3  6  9 12 15]

# np.divide() → divide cada elemento por un valor
print(np.divide(a, 2))      # [0.5 1.  1.5 2.  2.5]

# np.power() → eleva cada elemento a una potencia
print(np.power(a, 2))       # [ 1  4  9 16 25]

# np.sqrt() → raíz cuadrada de cada elemento
print(np.sqrt(a))           # [1.   1.41 1.73 2.   2.23]

# np.abs() → valor absoluto de cada elemento
print(np.abs(np.array([-3, -1, 2])))   # [3 1 2]

# ESTADÍSTICAS

a = np.array([1, 2, 3, 4, 5])

# np.mean() → promedio de todos los elementos
print(np.mean(a))      # 3.0

# np.sum() → suma de todos los elementos
print(np.sum(a))       # 15

# np.min() → valor mínimo
print(np.min(a))       # 1

# np.max() → valor máximo
print(np.max(a))       # 5

# np.std() → desvío estándar
print(np.std(a))       # 1.41

# np.median() → valor del medio cuando están ordenados
print(np.median(a))    # 3.0

# np.cumsum() → suma acumulada: cada elemento suma todos los anteriores
print(np.cumsum(a))    # [ 1  3  6 10 15]

# np.argmin() → índice donde está el valor mínimo
print(np.argmin(a))    # 0

# np.argmax() → índice donde está el valor máximo
print(np.argmax(a))    # 4


# COMPARAR Y FILTRAR

a = np.array([1, 2, 3, 4, 5])

# np.where(condición, valor_si_true, valor_si_false)
# donde a > 2 deja el valor, donde no pone 0
print(np.where(a > 2, a, 0))   # [0 0 3 4 5]

# np.unique() → devuelve los valores únicos sin repetidos
x = np.array([3, 1, 2, 2, 3, 3])
print(np.unique(x))             # [1 2 3]

# np.sort() → devuelve el array ordenado (no modifica el original)
print(np.sort(np.array([5, 1, 3, 2])))   # [1 2 3 5]


# FORMA Y ESTRUCTURA

a = np.array([1, 2, 3, 4, 5, 6])

# np.reshape() → cambia la forma sin modificar los datos
print(np.reshape(a, (2, 3)))
# [[1 2 3]
#  [4 5 6]]

# np.concatenate() → une arrays en una misma dimensión
b = np.array([7, 8, 9])
print(np.concatenate([a, b]))   # [1 2 3 4 5 6 7 8 9]

# np.stack() → apila arrays creando una nueva dimensión
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(np.stack([c, d]))
# [[1 2 3]
#  [4 5 6]]

# np.split() → divide en partes iguales
partes = np.split(a, 3)
print(partes)   # [array([1, 2]), array([3, 4]), array([5, 6])]

# np.transpose() → convierte filas en columnas y viceversa
m = np.ones((2, 3))
print(np.transpose(m).shape)   # (3, 2)