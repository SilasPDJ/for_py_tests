# tktiter
from msilib.schema import File
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


class ColorConverterB:
    @staticmethod
    def hex2rgb(value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    @staticmethod
    def rgb2hex(rgb):
        return '#%02x%02x%02x' % rgb


class Backend(ColorConverterB):
    root = None
    STRUCTURE = {}
    JSON_FILE = "datas/sample.json"
    __charsplit = ' |'
    # fucntions

    def timer_helper(self, min=1, seconds=15):
        import datetime
        from datetime import timedelta, datetime
        now = mystart = datetime.now()
        myend = mystart + timedelta(seconds=seconds)

        while True:
            now = datetime.now()
            # myend = mystart + timedelta(minutes=min)
            if now < myend:
                pass
            else:
                print("JUST TO SEE")
                break

    def init_main(self, e=None):

        COLORS = {"ZERAR": '#ffffff',
                  "COMPRAR": '#119850', "VENDER": '#cc3030'}
        TO_READ = self.STRUCTURE["HISTOGRAMA_POSITION"]

        op_atual_cont = {"COMPRAR": 0, "VENDER": 0}

        QTD_P_OPERAR = 2

        # logical system

        while True:
            now_color = self.__get_color(*TO_READ)
            now_color = self.rgb2hex(now_color)
            print(now_color)
            to_click = None

            __op_name = None
            for op_name, c in COLORS.items():
                if c.upper() == now_color.upper():
                    to_click = self.STRUCTURE[op_name]
                    if op_name in op_atual_cont:
                        op_atual_cont[op_name] += 1
                        if op_name == "COMPRAR":
                            __op_name = op_name
                            op_atual_cont["VENDER"] = 0
                            break
                        else:
                            __op_name = op_name
                            op_atual_cont["COMPRAR"] = 0
                            break

            if to_click is not None:
                print(to_click)

            if __op_name in op_atual_cont:
                print(op_atual_cont[__op_name],
                      op_atual_cont[__op_name] <= QTD_P_OPERAR)
                if op_atual_cont[__op_name] <= QTD_P_OPERAR:
                    # pygui.click(to_click)
                    pass
            else:
                pass
            pygui.click(to_click)

            self.timer_helper()
            # TODO: COMO??????? definir variável para ver se está posicionado ou não
            # TODO: calcular tempo com base no relógio
            # PRINT SCREEN DA REGIÃO DE ALTURA PROCURAR POR LINHA AMARELA?????????????????
            # A CONTAGEM DE ORDENS ESTÁ FUNCIONANDO INCORRETAMENTE

    def get_screen_bt_position(self, bt):  # and integrates
        bt_name = bt["text"]

        self.press_key_b4("ESC")
        x, y = pygui.position()
        self.STRUCTURE[bt_name] = (x, y)

        # sdkaldalsçdçaslk
        self.set_bt_text_coord(bt, coords=(x, y))

        print(self.STRUCTURE)
        self.__make_dump4json()

    # def read_histograma(self, e):
        pass

    def __make_dump4json(self):
        # clean keys
        lof_keys = list(self.STRUCTURE.keys())
        for k in lof_keys:
            self.STRUCTURE["".join(k.split(self.__charsplit)[
                                   :1])] = self.STRUCTURE.pop(k)

        with open(self.JSON_FILE, "wt") as f:
            json.dump(self.STRUCTURE, f)

    # ###### private

    @staticmethod
    def __get_color(*coords):

        im = pyautogui.screenshot()
        im.save("datas/teste.png")
        if coords == None:
            x, y = pygui.position()
        elif len(coords) == 2:
            x, y = coords
        else:
            raise ValueError("the number of arguments must be == 2 or == 0")
        # print(x, y)
        px = im.getpixel((x, y))
        # print(px)
        return px

    @staticmethod
    def press_key_b4(key: str):
        from keyboard import is_pressed
        """
        Só dá break quando uma tecla específica é pressionada, e então, continua o código
        :param key:
        :return:
        """
        while True:
            #
            if is_pressed(key):
                if is_pressed(key):
                    return True
            else:
                ...

    def set_bt_text_coord(self, *bts, coords=None):
        coords_data = None
        if coords is not None:
            x, y = coords
        else:
            try:
                with open(self.JSON_FILE) as f:
                    coords_data = json.loads(f.read())
                    self.STRUCTURE = coords_data.copy()
            except FileNotFoundError:
                return

        for e, bt in enumerate(bts):
            if coords_data is not None:
                key_value = list(coords_data)[e]
                if key_value == bt["text"]:
                    x, y = coords_data[key_value]

            newtext = "".join(bt["text"].split(self.__charsplit)[:1])
            bt["text"] = newtext + f" | X: {x}, Y: {y}"


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

        bt_compra = self.button("COMPRAR", bg="#ffac01")
        bt_venda = self.button("VENDER", bg="#25b367")
        bt_zerar = self.button("ZERAR", bg="#ff0000")
        bt_get_posxy = self.button(
            "HISTOGRAMA_POSITION", bg="white", fg="black")
        self.bt_iniciar = self.button(
            "INICIAR", lambda: self.init_main(), bg="yellow", fg="black")

        bt_compra.configure(command=partial(
            self.get_screen_bt_position, bt_compra))
        bt_venda.configure(command=partial(
            self.get_screen_bt_position, bt_venda))
        bt_zerar.configure(command=partial(
            self.get_screen_bt_position, bt_zerar))
        bt_get_posxy.configure(command=partial(
            self.get_screen_bt_position, bt_get_posxy))

        self.__pack(bt_compra, bt_venda, bt_zerar,
                    bt_get_posxy, self.bt_iniciar)

        self.set_bt_text_coord(bt_compra, bt_venda, bt_zerar,
                               bt_get_posxy)

        # check json file

    @staticmethod
    def __unable_bts(self, *els):
        for el in els:
            el['state'] = tk.DISABLED

    def button(self, text, command=None, fg='#FFF', bg='#000'):
        bt = tk.Button(self, text=text, command=lambda: self.start(
            command), fg=fg, bg=bg, font=("Arial", 14))
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
