# -*- coding: utf-8 -*-
"""
Модуль для работы с базой данных
"""
import tkinter as tki
from tkinter import ttk
from tkinter import filedialog as fld
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

def clear(frm):
    '''
    Очищение фрейма
    Вход:
    frm : Frame - Фрейм, в котором необходимо удалить все виджеты
    Выход: None
    '''
    for widgets in frm.winfo_children():
        widgets.destroy()

def open_data(frm, selected):
    '''
    Открытие базы данных из начальной страницы
    Вход:
    frm : Frame
        Фрейм, где необходимо вывести БД
    selected : tki.IntVar()
        Выбор пользователя
    Выход: None
    '''
    global data
    col = np.array(['accident.csv', 'persons.csv', 'vehicle.csv'])
    par=col[selected.get()]
    data = pd.read_csv('data/' + par, delimiter=';')
    clear(frm)
    table_create(data, frm)

def open_table(par, frm):
    '''
    Открытие базы данных
    Вход:
    par : String
        Название БД
    frm : Frame
        Фрейм, где необходимо вывести БД

    Выход: None
    '''
    global data
    clear(frm)
    data = pd.read_csv('data/' + par, delimiter=';')
    clear(frm)
    table_create(data, frm)

def saveas_data(data):
    '''
    Сохранение таблицы
    Вход:
    data : DataFrame
       Таблица для сохранения
    Выход: None
    '''
    ftypes = [('Excel файлы', '*.xlsx'), ('csv файлы', '*.csv'), ('Все файлы', '*')]
    dlg = fld.SaveAs(filetypes = ftypes, defaultextension=".xlsx", initialdir='output')
    flp = dlg.show()
    if '.xlsx' in flp:
        data.to_excel(flp, index=True)
    elif '.csv' in flp:
        data.to_csv(flp)

def remove_record(frm):
    '''
    Удаление записи из БД и вывод на экран БД
    Вход:
    frm : Frame
        Фрейм, куда выводится БД
    Выход: None
    '''
    def remove():
        ''' Обработка нажатия кнопки '''
        global data
        row_id = entry.get()
        data = data[data.iloc[0:,0] != int(row_id)]
        top.destroy()
        clear(frm)
        table_create(data, frm)
    top = tki.Toplevel()
    top.title("Удалить запись")
    lbl = tki.Label(top, text="Введите ID строки, которую хотите удалить:")
    lbl.pack(padx=10, pady=10)
    entry = tki.Entry(top)
    entry.focus()
    entry.pack(padx=10, pady=10)
    btn = tki.Button(top, text="Удалить", command=remove)
    btn.pack(padx=10, pady=10)

def add_record(frm):
    '''
    Добавление записи в БД и вывод на экран БД
    Вход:
    frm : Frame
        Фрейм, куда выводится БД
    Выход: None
    '''
    global data
    def add(data):
        values = []
        if 'id' in data.columns:
            values.append(len(data.index)+1)
        for entry in entries:
            values.append(entry.get())
        new_row = pd.Series(values, index=data.columns)
        data.loc[len(data.index)] = new_row
        top.destroy()
        clear(frm)
        table_create(data, frm)
    top = tki.Toplevel()
    top.title("Добавить запись")
    entries = []
    dts = data.columns
    if 'id' in data.columns:
        tki.Label(top, text='id:').grid(row=0, column=0, padx=10, pady=10)
        tki.Label(top, text=len(data.index)+1).grid(row=0, column=1, padx=10, pady=10)
        dts = data.columns[1:]
    for i, column in enumerate(dts):
        if i<12:
            tki.Label(top, text=column).grid(row=i+1, column=0, padx=10, pady=10)
            entry = tki.Entry(top)
            entry.grid(row=i+1, column=1, padx=10, pady=10)
        else:
            tki.Label(top, text=column).grid(row=i-11, column=2, padx=10, pady=10)
            entry = tki.Entry(top)
            entry.grid(row=i-11, column=3, padx=10, pady=10)
        entries.append(entry)

    btn = tki.Button(top, text="Добавить", command=lambda:add(data))
    btn.grid(row=len(data.columns), columnspan=2, padx=10, pady=10)

def filter_records(frm):
    '''
    Фильтрация записей в БД и вывод на экран
    Вход:
    frm : Frame
        Фрейм, куда выводится БД
    Выход: None
    '''
    def apply_filter():
        global data
        column = combo_column.get()
        value = entry_value.get()
        sign = combo.get()

        if column in data.columns:
            cond = value.isdigit()
            if is_numeric_dtype(data[column]):
                value = float(value)
            if sign == '=':
                filtered_data = data[data[column] == value]
            elif sign == '>' and cond:
                filtered_data = data[data[column] > value]
            elif cond:
                filtered_data = data[data[column] < value]
            clear(frm)
            table_create(filtered_data, frm)
            top.destroy()
        else:
            tki.messagebox.showerror("Ошибка", "Выбранный столбец не существует.")

    top = tki.Toplevel()
    top.title("Фильтрация записей")

    lbl_column = tki.Label(top, text="Выберите столбец и введите значение:")
    lbl_column.grid(row=0, column=0, padx=10, pady=10)
    frame = tki.Frame(top)
    combo_column = ttk.Combobox(frame, values=list(data.columns))
    combo_column.grid(row=0, column=0, padx=10, pady=10)

    combo = ttk.Combobox(frame, values=['=', '>', '<'])
    combo.grid(row=0, column=1, padx=10, pady=10)
    combo.current(0)
    entry_value = tki.Entry(frame)
    entry_value.grid(row=0, column=2, padx=10, pady=10)
    frame.grid(row=1, column=0, padx=10, pady=10)
    btn_apply = tki.Button(top, text="Применить", command=apply_filter)
    btn_apply.grid(row=2, columnspan=2, padx=10, pady=10)

def sort_records(frm):
    '''
    Сортировка записей в БД и вывод на экран
    Вход:
    frm : Frame
        Фрейм, куда выводится БД
    Выход: None
    '''
    def apply_sort():
        global data
        column = combo_column.get()
        ascending = var_sort.get() == 1

        if column in data.columns:
            sorted_data = data.sort_values(by=column, ascending=ascending)
            clear(frm)
            table_create(sorted_data, frm)
            top.destroy()
        else:
            tki.messagebox.showerror("Ошибка", "Выбранный столбец не существует.")

    top = tki.Toplevel()
    top.title("Сортировка записей")

    lbl_column = tki.Label(top, text="Выберите столбец для сортировки:")
    lbl_column.grid(row=0, column=0, padx=10, pady=10)

    combo_column = ttk.Combobox(top, values=list(data.columns))
    combo_column.grid(row=0, column=1, padx=10, pady=10)

    var_sort = tki.IntVar()
    chk_sort = tki.Checkbutton(top, text="По возрастанию", variable=var_sort)
    chk_sort.grid(row=1, columnspan=2, padx=10, pady=10)

    btn_apply = tki.Button(top, text="Применить", command=apply_sort)
    btn_apply.grid(row=2, columnspan=2, padx=10, pady=10)

def table_create(data, frm):
    '''
    Вывод на экран таблицы
    Вход:
    data : DataFrame
        Таблица для вывода
    frm : Frame
        Фрейм для вывода таблицы
    Выход: None
    '''
    tv1 = ttk.Treeview(frm)
    treescrolly = ttk.Scrollbar(frm, orient="vertical", command=tv1.yview)
    treescrollx = ttk.Scrollbar (frm, orient= "horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")
    tv1["columns"]=list(data)
    tv1["show"]="headings"
    for i in list(data):
        tv1.column(i, width=90, anchor='c')
        tv1.heading(i, text=i)
    df_rows = data.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
    tv1.pack(expand=1, fill='both')
    btn = tki.Button(frm, text='Сохранить как', command=lambda:saveas_data(data))
    btn.pack(anchor='ne')
    frm.pack(expand=1, fill='both')
