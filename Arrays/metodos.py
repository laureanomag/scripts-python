import numpy as np

# INSPECCIONAR LA ESTRUCTURA

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# .shape → tupla con las dimensiones del array
print(a.shape)   # (2, 3) → 2 filas, 3 columnas

# .ndim → cantidad de dimensiones
print(a.ndim)    # 2

# .size → total de elementos (filas × columnas)
print(a.size)    # 6

# .dtype → tipo de dato de los elementos
print(a.dtype)   # int64

# CAMBIAR FORMA

a = np.array([1, 2, 3, 4, 5, 6])

# .reshape() → cambia la forma sin modificar los datos
# el total de elementos tiene que ser el mismo
print(a.reshape(2, 3))
# [[1 2 3]
#  [4 5 6]]

print(a.reshape(3, 2))
# [[1 2]
#  [3 4]
#  [5 6]]

# -1 le dice a NumPy que calcule ese eje automáticamente
print(a.reshape(-1, 1))
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

# .flatten() → aplana a 1D, devuelve una copia nueva
b = np.array([[1, 2], [3, 4]])
print(b.flatten())   # [1 2 3 4]

# .ravel() → aplana a 1D, devuelve una vista (más eficiente)
print(b.ravel())     # [1 2 3 4]

# .T → transpone: filas pasan a ser columnas
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.T)
# [[1 4]
#  [2 5]
#  [3 6]]

# ESTADÍSTICAS

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# .sum() → suma todos los elementos
print(a.sum())         # 21

# .sum(axis=0) → suma por columnas (recorre hacia abajo)
print(a.sum(axis=0))   # [5 7 9]

# .sum(axis=1) → suma por filas (recorre hacia la derecha)
print(a.sum(axis=1))   # [ 6 15]

# .mean() → promedio de todos los elementos
print(a.mean())        # 3.5

# .mean(axis=0) → promedio por columnas
print(a.mean(axis=0))  # [2.5 3.5 4.5]

# .mean(axis=1) → promedio por filas
print(a.mean(axis=1))  # [2. 5.]

# .min() → valor mínimo de todos los elementos
print(a.min())         # 1

# .max() → valor máximo de todos los elementos
print(a.max())         # 6

# .std() → desvío estándar de todos los elementos
print(a.std())         # 1.70

# .argmin() → índice aplanado donde está el mínimo
print(a.argmin())      # 0  → el 1 está en la posición 0

# .argmax() → índice aplanado donde está el máximo
print(a.argmax())      # 5  → el 6 está en la posición 5

# MODIFICAR ELEMENTOS

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# .clip() → limita los valores a un rango mínimo y máximo
# valores menores al mínimo pasan al mínimo
# valores mayores al máximo pasan al máximo
print(a.clip(2, 5))
# [[2 2 3]
#  [4 5 5]]
# → el 1 era menor a 2, queda en 2
# → el 6 era mayor a 5, queda en 5

# .sort() → ordena in-place (modifica el array original)
b = np.array([5, 1, 3, 2])
b.sort()
print(b)   # [1 2 3 5]

# .fill() → rellena todo el array con un valor (modifica el original)
c = np.array([[1, 2], [3, 4]])
c.fill(0)
print(c)
# [[0 0]
#  [0 0]]


# TIPO DE DATO
# ------------------------------------------------------------

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# .astype() → convierte los elementos al tipo indicado
print(a.astype(float))
# [[1. 2. 3.]
#  [4. 5. 6.]]

print(a.astype(str))
# [['1' '2' '3']
#  ['4' '5' '6']]


# ------------------------------------------------------------
# COPIAR
# ------------------------------------------------------------

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# .copy() → crea una copia totalmente independiente
# si modificás la copia, el original NO cambia
copia = a.copy()
copia[0, 0] = 99

print(a[0, 0])     # 1  → el original no cambió
print(copia[0, 0]) # 99 → la copia sí cambió

# sin .copy() los cambios SÍ afectan al original
vista = a
vista[0, 0] = 99
print(a[0, 0])     # 99 → el original cambió también