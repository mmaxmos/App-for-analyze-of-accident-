# -*- coding: utf-8 -*-
"""
Модуль для вывода справочной информации
"""
import tkinter as tki
from library.work_with_data import clear
def page_help(frm):
    '''
    Функция для вывода справочной информации о приложении
    Вход:
    frm : Frame
        Frame, в котором выведется текст
    Выход: None
    '''
    clear(frm)
    with open('library/help.txt', encoding='utf-8') as file:
        text = file.readlines()
        text = ''.join(text)
        textline = tki.Text(frm)
        textline.insert(1.0, text)
        textline.pack()
    