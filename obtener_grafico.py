#!/usr/bin/env python
import json
import matplotlib.pyplot as plt
import numpy as np

# Configura la cabecera para indicar que el contenido es de tipo aplicación JSON
print("Content-type: application/json\n")

# Genera datos para el gráfico (en este caso, una simple función seno)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Crea el gráfico utilizando Matplotlib
plt.plot(x, y)
plt.title('Gráfico Seno')
plt.xlabel('X')
plt.ylabel('Y')

# Convierte el gráfico a formato JSON y lo imprime
grafico_json = json.dumps(plt.to_dict())
print(grafico_json)
