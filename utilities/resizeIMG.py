from PIL import Image
import os


def resize():
    print('Resimensionando imagens!')
    tamanho = (1120, 620)
    lista = [x for x in os.listdir('cams')]
    for i in lista:
        im = Image.open('cams\\' + i)
        im_menor = im.resize(tamanho)
        im_menor.save('cams_resize\\' + i)
