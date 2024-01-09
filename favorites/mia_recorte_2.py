import moviepy
from moviepy.editor import *


def calcular_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


main_video_path = r"O:\OneDrive\Área de Trabalho\believe-fiao\recorte\DVD-2.mp4"


secs_1 = calcular_segundos(
    *(int(e) for e in input('horas:minutos:segundos (início) = ').split(":")))
secs_2 = calcular_segundos(
    *(int(e) for e in input('horas:minutos:segundos (final) = ').split(":")))

name = f"{input('Resultado nome sem extensão: ')}.mp4"

print(secs_1, secs_2)
video = VideoFileClip(main_video_path).subclip(secs_1, secs_2)
video.write_videofile(
    f"O:\\OneDrive\\Área de Trabalho\\believe-fiao\\recorte\\{name}")
