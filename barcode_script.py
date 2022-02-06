import os
from barcode import EAN13
# pip install python-barcode
from barcode.writer import ImageWriter

number = '59012341233123232132457'
my_code = EAN13(number, writer=ImageWriter)
my_code.save("new_code1.png")
# os.system("")
# pip install python-barcode
