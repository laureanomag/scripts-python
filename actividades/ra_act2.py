import numpy as np #se importa la librería numpy para manejar arrays
import matplotlib.pyplot as plt #se importa la librería matplotlib para mostrar imágenes y gráficos
from PIL import Image #se importa la librería PIL para manejar imágenes
import requests #se importa la librería requests para hacer solicitudes HTTP
import io #se importa la librería io para manejar flujos de datos en memoria

# Imagen de Pikachu
url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png'

try:
    # Añadimos 'User-Agent' para que el sitio no nos bloquee
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    
    # Abrimos la imagen
    mi_imagen = Image.open(io.BytesIO(response.content))

    print(f"Tamaño: {mi_imagen.size}")

    # Convertir a array
    mi_imagen_como_array = np.asarray(mi_imagen)
    print(f"Shape del array: {mi_imagen_como_array.shape}")

    # Mostrar imagen
    plt.imshow(mi_imagen_como_array)
    plt.axis('off')
    plt.show()
except Exception as e:
    print(f"Error técnico: {e}")
