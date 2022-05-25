from PIL import Image
import os


def resize():
    print('Resimensionando imagens!')
    tamanho = (1120, 620)
    lista = [x for x in os.listdir('images')]
    for i in lista:
        im = Image.open('images\\' + i)
        im_menor = im.resize(tamanho)
        im_menor.save('resized_images\\' + i)
