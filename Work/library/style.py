# -*- coding: utf-8 -*-
"""
Модуль для смены темы приложения
"""
from tkinter import ttk
import tkinter as tki
from library.work_with_data import clear
def change_theme(frm):
    '''
    Функция для изменения темы приложения
    Вход:
    frm : Frame
        Frame, в котором необходимо вывести доступные темы

    Выход: None
    '''
    clear(frm)
    selected_theme = tki.StringVar()
    style = ttk.Style()
    def change():
        style.theme_use(selected_theme.get())
    ttk.Label(frm, text='Выберете тему для приложения:',
              font=('Arial', 10, 'bold')).pack(anchor='n')
    ttk.Label(frm, text='Текущая тема:').pack(anchor='n')
    ttk.Label(frm, text=style.theme_use()).pack(anchor='n')
    frame2=tki.Frame(frm)
    for theme in style.theme_names():
        ttk.Radiobutton(frame2, text=theme,
                    value=theme,
                    variable=selected_theme,
                    command=change).pack(anchor='nw')
    frame2.pack(anchor='n')
    