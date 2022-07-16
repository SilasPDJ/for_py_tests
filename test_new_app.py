# tktiter
from pynput import mouse
from tkinter import Tk
from threading import Thread
from ctypes import windll
import json
from functools import partial
import pyautogui as pygui
import tkinter as tk
from time import sleep
pyautogui = pygui


class Backend:
    __mouse_is_blocked = False
    root = None

    STRUCTURE = {}
    # fucntions

    def get_screen_bt_position(self, bt_name):  # and integrates
        
        self.press_key_b4()
        x, y = pygui.position()
        self.STRUCTURE[bt_name] = (x, y)

        print(self.STRUCTURE)

    # ###### private

    def make_dump4json():
        pass

    @staticmethod
    def __get_color():
        im = pyautogui.screenshot()
        im.save("datas/teste.png")
        px = im.getpixel((pygui.position()))
        print(px)
        return px


class MainApplication(tk.Frame, Backend):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Backend.root = parent
        self.parent = parent
        self.root = parent
        LABELS = []
        self.increment_header_tip(
            LABELS, "APÓS SELECIONAR POSIÇÃO, PRESSIONE ESC")
        self.__pack(*LABELS)
        bt_compra = self.button("COMPRA À MERCADO", partial(
            self.get_screen_bt_position, "COMPRA"), bg="#ffac01")
        # bt_venda = self.button()
        self.__pack(bt_compra)

    def button(self, text, command=None, fg='#fff', bg='#000',):
        bt = tk.Button(self, text=text, command=lambda: self.start(
            command), fg=fg, bg=bg)
        return bt
        # threading...

    @staticmethod
    def increment_header_tip(labels: list, tip: str, font=("Currier", 12), fg="#000"):
        labels.append(
            tk.Label(root, text=tip, font=font, fg=fg))

    # Elements and placements
    @ staticmethod
    def __pack(*els, x=50, y=10, fill='x', side=tk.TOP, expand=0):
        try:
            x1, x2 = x
        except TypeError:
            x1, x2 = x, x

        try:
            y1, y2 = y
        except TypeError:
            y1, y2 = y, y
        for el in els:
            el.pack(padx=(x1, x2), pady=(
                y1, y2), fill=fill, side=side, expand=expand)

    def refresh(self):
        self.root.update()
        self.root.after(1000, self.refresh)

    def start(self, stuff):
        self.refresh()
        Thread(target=stuff).start()
    # threading


if __name__ == "__main__":
    root = tk.Tk()
    root.title = 'Autoesk'

    b = MainApplication(root)
    b.pack(side="top", fill="both", expand=True)

    root.geometry('500x800')
    root.mainloop()
