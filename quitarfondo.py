from rembg import remove
from PIL import Image
import sys
import os

def quitar_fondo(imagen, i):
    input_path = imagen
    output_path = f'./ANANDA-00-NOV NOBG/imagen_sin_fondo_{i}.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    

    return output_path

count = 0
for i in os.listdir('./ANANDA-00-NOV'):
    quitar_fondo(f'./ANANDA-00-NOV/{i}', count)
    count += 1