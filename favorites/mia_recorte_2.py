import moviepy
from moviepy.editor import *


def calcular_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


tempos = [
    (0, 0, 46),
]

# secs_1 = calcular_segundos(
#     *(int(e) for e in input('horas:minutos:segundos (início) = ').split(":")))
# secs_2 = calcular_segundos(
#     *(int(e) for e in input('horas:minutos:segundos (final) = ').split(":")))

# name = f"{input('Resultado nome sem extensão: ')}.mp4"

for secs_1 in tempos:
    main_video_path = input("path: ".replace('"', ''))
    secs_2 = None
    print(secs_1, secs_2)
    video = VideoFileClip(main_video_path).subclip(secs_1, secs_2)
    video.write_videofile(
        main_video_path.replace(".mp4", "-new.mp4"))
