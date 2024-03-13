import moviepy
from moviepy.editor import *


def calcular_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


# Lista de valores fornecidos
tempos = [
    (0, 0, 0),
    (0, 6, 31),
    (0, 9, 52),
    (0, 13, 23),
    (0, 17, 23),
    (0, 22, 50),
    (0, 27, 59),
    (0, 35, 9),
    (0, 39, 30),
    (0, 43, 5),
    (0, 49, 4),
    (0, 52, 24)
]

# Calcula o total de segundos para cada valor e armazena em uma lista
segundos = [calcular_segundos(*tempo) for tempo in tempos]

print("Totais de segundos individuais:", segundos)


main_video_path = input('main videopath: ')


for e, secs_1 in enumerate(segundos[:-1]):
    secs_2 = segundos[e+1]
    name = f"video-{e:02d}.mp4"
    print(secs_1, secs_2)
    video = VideoFileClip(main_video_path).subclip(secs_1, secs_2)
    video.write_videofile(
        f"O:\\OneDrive\\Área de Trabalho\\believe-fiao\\recorte\\{name}")
