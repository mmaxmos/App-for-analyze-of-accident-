# -*- coding: utf-8 -*-
"""
Главный модуль
"""
import tkinter as tki
from tkinter import ttk
from library.work_with_data import remove_record, open_data, open_table, add_record, filter_records, sort_records
from library.style import change_theme
from library.page_help import page_help
from scripts.pages import page_base_statistic, page_freq, page_graph_bar, page_graph_boxplot, page_graph_hist, page_graph_pie, page_graph_scatter, page_pivot, map_create

def gui():
    '''
    Графический интерфейс
    Вход и выход: None
    '''
    def popup(event):
        """
        Привязка события нажатия правой кнопки мыши
        """
        mainmenu.post(event.x_root, event.y_root)
    root=tki.Tk()
    root.title("ДТП Кто виноват?")
    root.geometry('740x500+40+30')
    mainmenu = tki.Menu(root, tearoff=0)
    frm = ttk.Frame(root)
    frm.pack(expand=True, fill='both')
    root.bind("<Button-3>", popup)
    lbl = tki.Label(frm, text="Добро пожаловать в приложение", font=('Arial', 10))
    lbl.pack(anchor="n")
    lbl = tki.Label(frm, text="ДТП Кто виноват?", font=('Arial', 12, 'bold'))
    lbl.pack(anchor="n")
    lbl = tki.Label(frm, text="Приложение для анализа данных ДТП в Аризоне за 2012-2016 гг.",
                    fg="grey")
    lbl.pack(anchor="n")
    lbl = tki.Label(frm, text="Отметьте какую таблицу открыть:")
    lbl.pack(anchor="n")

    selected = tki.IntVar()
    rad1 = ttk.Radiobutton(frm, text="accident", value=0, var=selected)
    rad1.pack()

    rad2 = ttk.Radiobutton(frm, text="persons", value=1, var=selected)
    rad2.pack()

    rad3 = ttk.Radiobutton(frm, text="vehicle", value=2, var=selected)
    rad3.pack()
    btn = tki.Button(frm, text='Открыть', command=lambda:open_data(frm, selected))
    btn.pack(anchor="n")

    menu12 = tki.Menu(mainmenu, tearoff=0)
    menu12.add_command(label="accident", command=lambda: open_table('accident.csv', frm))
    menu12.add_command(label="persons", command=lambda: open_table('persons.csv', frm))
    menu12.add_command(label="vehicle", command=lambda: open_table('vehicle.csv', frm))

    menu1 = tki.Menu(mainmenu, tearoff=0)
    menu1.add_cascade(label="Открыть", menu=menu12)
    menu1.add_command(label="Фильтровать", command=lambda:filter_records(frm))
    menu1.add_command(label="Сортировать", command=lambda:sort_records(frm))
    menu1.add_command(label="Удалить запись", command=lambda:remove_record(frm))
    menu1.add_command(label="Добавить запись", command=lambda: add_record(frm))
    menu1.add_separator()
    menu1.add_command(label="Выйти", command=root.destroy)

    menu2 = tki.Menu(mainmenu, tearoff=0)
    menu2.add_command(label="Основные статистики количественных данных",
                      command=lambda:page_base_statistic(frm))
    menu2.add_command(label="Таблица частот", command=lambda:page_freq(frm))
    menu2.add_command(label="Сводная таблица", command=lambda:page_pivot(frm))

    menu3 = tki.Menu(mainmenu, tearoff=0)
    menu3.add_command(label="Столбчатые диаграммы", command=lambda:page_graph_bar(frm))
    menu3.add_command(label="Гистограммы", command=lambda:page_graph_hist(frm))
    menu3.add_command(label="Круговые диаграммы", command=lambda:page_graph_pie(frm))
    menu3.add_command(label="Диаграммы рассеивания", command=lambda:page_graph_scatter(frm))
    menu3.add_command(label="Диаграммы Бокса-Вискера", command=lambda:page_graph_boxplot(frm))
    test = tki.PhotoImage(file='library/map.png')
    mainmenu.add_cascade(label="Работа с БД", menu = menu1)
    mainmenu.add_cascade(label="Текстовые отчёты", menu=menu2)
    mainmenu.add_cascade(label="Графические отчёты", menu = menu3)
    mainmenu.add_command(label="Карта", command=lambda:map_create(frm, test))
    mainmenu.add_command(label="Стиль", command=lambda: change_theme(frm))
    mainmenu.add_command(label="Справка", command=lambda: page_help(frm))

    root.iconbitmap('library/accident.ico')
    root.config(menu=mainmenu)
    root.mainloop()

if __name__ == "__main__":
    gui()
    