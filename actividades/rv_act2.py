import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Asignar la imagen a una variable
ruta = r"C:\Users\Aspire 3\OneDrive\3ER AÑO\Reconocimiento Visual\Guido Sardelli.jpg"
mi_imagen = Image.open(ruta)

# Conocer el tamaño de la imagen
print(f"Tamaño: {mi_imagen.size}")

# Convertir la imagen en array
mi_imagen_como_array = np.asarray(mi_imagen)
print(mi_imagen_como_array)

# Conocer la forma del array
print(f"Shape: {mi_imagen_como_array.shape}")

# Visualizar el array como imagen
plt.imshow(mi_imagen_como_array)
plt.show()

# Separar los canales RGB
array_imagen_rojo = mi_imagen_como_array[:,:,0]
array_imagen_verde = mi_imagen_como_array[:,:,1]
array_imagen_azul = mi_imagen_como_array[:,:,2]

# Visualizar canales individuales
plt.imshow(array_imagen_rojo, cmap='gray')
plt.show()
plt.imshow(array_imagen_verde, cmap='gray')
plt.show()
plt.imshow(array_imagen_azul, cmap='gray')
plt.show()

# Transposición (ejemplo final del profe)
verde_transpuesta = np.transpose(array_imagen_verde)
plt.imshow(verde_transpuesta, cmap='gray')
plt.show()