# -*- coding: utf-8 -*-
"""
Графический интерфейс. Модуль для вывода различных страниц.
"""
import tkinter as tki
from tkinter import ttk
import pandas as pd
from scripts.reports import basic_statistics, frequency1, pivot
from library.work_with_data import table_create, clear
from scripts.graphics import graph_bar, graph_pie, graph_hist, graph_scatter, graph_boxplot
from tkinter import filedialog as fld

def saveas_data_charts(fig):
    '''
    Сохранение графиков 
    Вход:
    fig : Figure
        График
    Выход: None.
    '''
    ftypes = [('png', '*.png'), ('jpeg', '*.jpeg'), ('pdf', '*.pdf'), ('Все файлы', '*')]
    dlg = fld.SaveAs(filetypes = ftypes, defaultextension=".xlsx", initialdir='graphics')
    fl = dlg.show()
    fig.savefig(fl, dpi=100)

def saveas_data_reports(datal):
    '''
    Сохранение отчетов
    Вход:
    datal : DataFrame
        Отчет
    Выход: None.
    '''
    ftypes = [('Excel файлы', '*.xlsx'), ('csv файлы', '*.csv'), ('Все файлы', '*')]
    dlg = fld.SaveAs(filetypes = ftypes, defaultextension=".xlsx", initialdir='output')
    flp = dlg.show()
    if '.xlsx' in flp:
        datal.to_excel(flp, index=False)
    else: 
        datal.to_csv(flp) 

def page_graph_bar(frm):
    clear(frm)
    def clck():
        """    Обработка нажатия кнопки    """
        window = tki.Toplevel()
        window.title("График")
        window.geometry("650x500+50+40")
        par = cmb.get()
        if (par=='sex'):
            datal = pd.read_csv('data/persons.csv', delimiter=';')
        else:
            datal = pd.read_csv('data/accident.csv', delimiter=';')
        fig = graph_bar(datal, par, window)
        fr = tki.Frame(window)
        tki.Button(fr, text='Сохранить как', command=lambda:saveas_data_charts(fig)).grid(column=0, row=0)
        tki.Button(fr, text=' Закрыть ', command=window.destroy).grid(column=1, row=0)
        fr.pack(side='right')

    tki.Label(frm, text="Столбчатая диаграмма", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметр для построения графика:').pack(fill='both', anchor='n')
    cmb = ttk.Combobox(frm)
    cmb['values'] = ('vehicle', 'peds',	'county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb.current(0)
    cmb.focus()
    cmb.pack(anchor='n')
    tki.Button(frm, text='  Создать  ', command=clck).pack(anchor='n')
    cmb.bind("<Return>", lambda events:clck())

def page_graph_pie(frm):
    clear(frm)
    def clck():
        """    Обработка нажатия кнопки    """
        window = tki.Toplevel()
        window.title("График")
        window.geometry("650x500+50+40")
        par=cmb.get()
        if (par=='sex'):
            datal = pd.read_csv('data/persons.csv', delimiter=';')
        else:
            datal = pd.read_csv('data/accident.csv', delimiter=';')
        fig = graph_pie(datal, par, window)
        fr = tki.Frame(window)
        btn = tki.Button(fr, text='Сохранить как', command=lambda:saveas_data_charts(fig))
        btn.grid(column=0, row=0)
        btn2 = tki.Button(fr, text='Закрыть', command=window.destroy)
        btn2.grid(column=1, row=0)
        fr.pack(side='right')
    tki.Label(frm, text="Круговая диаграмма", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметр для построения графика:').pack(fill='both', anchor='n')
    cmb = ttk.Combobox(frm)
    cmb['values'] = ('vehicle', 'peds',	'county',	'month',	'year',
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb.current(0)
    cmb.focus()
    cmb.pack(anchor='n')
    tki.Button(frm, text='  Создать  ', command=clck).pack(anchor='n')
    cmb.bind("<Return>", lambda events:clck())

def page_graph_hist(frm):
    clear(frm)
    def clck():
        """    Обработка нажатия кнопки    """
        window = tki.Toplevel()
        window.title("График")
        window.geometry("650x500+50+40")
        par=cmb.get()
        if(par=='age'):
            datal = pd.read_csv('data/persons.csv', delimiter=';')
        elif(par=='model_year'):
            datal = pd.read_csv('data/vehicle.csv', delimiter=';')
        else:
            datal = pd.read_csv('data/accident.csv', delimiter=';')
        fig = graph_hist(datal, par, window)
        fr = tki.Frame(window)
        btn = tki.Button(fr, text='Сохранить как', command=lambda:saveas_data_charts(fig))
        btn.grid(column=0, row=0)
        btn2 = tki.Button(fr, text='Закрыть', command=window.destroy)
        btn2.grid(column=1, row=0)
        fr.pack(side='right')
    tki.Label(frm, text="Гистограмма", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметр для построения графика:').pack(fill='both', anchor='n')
    cmb = ttk.Combobox(frm)
    cmb['values'] = ('vehicle', 'peds',	'month',
                     'hour', 'fatals',	'age', 'model_year')
    cmb.current(0)
    cmb.focus()
    cmb.pack(anchor='n')
    btn = tki.Button(frm, text='  Создать  ', command=clck)
    btn.pack(anchor='n')
    cmb.bind("<Return>", lambda events:clck())

def page_graph_scatter(frm):
    clear(frm)     
    def clck():
        """    Обработка нажатия кнопки    """
        window = tki.Toplevel()
        window.title("График")
        window.geometry("650x500+50+40")
        par1=cmb1_sc.get()
        par2=cmb2_sc.get()
        dataa = pd.read_csv('data/accident.csv', delimiter=';')
        datap = pd.read_csv('data/persons.csv', delimiter=';')
        datav = pd.read_csv('data/vehicle.csv', delimiter=';')
        datal = pd.merge(datap, dataa, on='accident_id')
        datal = pd.merge(datal, datav, on='accident_id')
        fig = graph_scatter(datal, par1, par2, window)
        fr = tki.Frame(window)
        btn = tki.Button(fr, text='Сохранить как', command=lambda:saveas_data_charts(fig))
        btn.grid(column=0, row=0)
        btn2 = tki.Button(fr, text=' Закрыть ', command=window.destroy)
        btn2.grid(column=1, row=0)
        fr.pack(side='right')
    tki.Label(frm, text="Диаграмма рассеивания", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметры для построения графика:').pack(fill='both', anchor='n')
    fsct=tki.Frame(frm)
    lbl21 = tki.Label(fsct, text='По оси X:  ')
    lbl21.grid(column=0, row=0)
    cmb1_sc = ttk.Combobox(fsct)
    cmb1_sc['values'] = ('vehicle', 'peds',	'month', 'year',
                         'hour', 'fatals',	'age', 'model_year')
    cmb1_sc.current(0)
    cmb1_sc.grid(column=1, row=0)
    lbl22 = tki.Label(fsct, text='По оси Y:  ')
    lbl22.grid(column=0, row=1)
    cmb2_sc = ttk.Combobox(fsct)
    cmb2_sc['values'] = ('vehicle', 'peds',	'month', 'year',
                         'hour', 'fatals',	'age', 'model_year')
    cmb2_sc.current(0)
    cmb2_sc.grid(column=1, row=1)
    fsct.pack(anchor='n')
    btn = tki.Button(frm, text='  Создать  ', command=clck)
    btn.pack(anchor='n')
    cmb2_sc.bind("<Return>", lambda events:clck())
    
def page_graph_boxplot(frm):
    clear(frm)     
    def help(param, dat):
        a = 1
        window2 = tki.Toplevel()
        window2.title("Справка")
        for i in set(dat[param]):
            lbl=tki.Label(window2, text=str(a) + ' - ' + str(i))
            lbl.pack(anchor='nw')
            a+=1
        btn2 = tki.Button(window2, text='Закрыть', command=window2.destroy)
        btn2.pack(anchor='s')
            
    def clck():
        """    Обработка нажатия кнопки    """
        window = tki.Toplevel()
        window.title("График")
        window.geometry("650x500+50+40")
        par1=cmb2_sc.get()
        par2=cmb1_sc.get()
        dataa = pd.read_csv('data/accident.csv', delimiter=';')
        datap = pd.read_csv('data/persons.csv', delimiter=';')
        datav = pd.read_csv('data/vehicle.csv', delimiter=';')
        datal = pd.merge(datap, dataa, on='accident_id')
        datal = pd.merge(datal, datav, on='accident_id')
        fig = graph_boxplot(datal, par1, par2, window)
        fr = tki.Frame(window)
        btn = tki.Button(fr, text='  ?  ', command=lambda:help(par2, datal))
        btn.grid(column=0, row=0)
        btn = tki.Button(fr, text='Сохранить как', command=lambda:saveas_data_charts(fig))
        btn.grid(column=1, row=0)
        btn2 = tki.Button(fr, text=' Закрыть ', command=window.destroy)
        btn2.grid(column=2, row=0)
        fr.pack(side='right')
    lbl0 = tki.Label(frm, text="Диаграмма Бокса-Вискера", font=('Arial', 10, 'bold'))
    lbl0.pack(anchor="n")
    lbl1 = tki.Label(frm, text='Выберете параметры для построения графика:')
    lbl1.pack(fill='both', anchor='n')
    fsct=tki.Frame(frm)
    lbl21 = tki.Label(fsct, text='По оси X:  ')
    lbl21.grid(column=0, row=0)
    cmb1_sc = ttk.Combobox(fsct)
    cmb1_sc['values'] = ('county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb1_sc.current(0)
    cmb1_sc.grid(column=1, row=0)
    lbl22 = tki.Label(fsct, text='По оси Y:  ')
    lbl22.grid(column=0, row=1)
    cmb2_sc = ttk.Combobox(fsct)
    cmb2_sc['values'] = ('vehicle', 'peds', 'fatals', 'age', 'model_year')
    cmb2_sc.current(0)
    cmb2_sc.grid(column=1, row=1)
    fsct.pack(anchor='n')
    btn = tki.Button(frm, text='  Создать  ', command=clck)
    btn.pack(anchor='n')
    cmb2_sc.bind("<Return>", lambda events:clck())
    
def page_base_statistic(frm):
    clear(frm)
    lbl = tki.Label(frm, text="Основные статистики", font=('Arial', 10, 'bold'))
    lbl.pack(anchor="n")
    table_create(basic_statistics(), frm)
    
def page_freq(frm):
    clear(frm)
    def clck():
        """    Обработка нажатия кнопки    """
        clear(frame)
        par=cmb.get()
        if(par=='sex'):
            datal = pd.read_csv('data/persons.csv', delimiter=';')
        else:
            datal = pd.read_csv('data/accident.csv', delimiter=';')
        frq = frequency1(par, datal)
        table_create(frq, frame)
    frame=tki.Frame(frm)
    tki.Label(frm, text="Таблица частот", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметр для построения таблицы:').pack(fill='both', anchor='n')
    cmb = ttk.Combobox(frm)
    cmb['values'] = ('county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb.current(0)
    cmb.focus()
    cmb.pack(anchor='n')
    tki.Button(frm, text='  Создать  ', command=clck).pack(anchor='n')
    cmb.bind("<Return>", lambda events:clck())
    
def page_pivot(frm):
    clear(frm)
    def clck():
        """    Обработка нажатия кнопки    """
        clear(frame)
        par1=cmb1.get()
        par2=cmb2.get()
        par3=cmb3.get()
        par4=cmb4.get()
        par5=cmb5.get()
        dataa = pd.read_csv('data/accident.csv', delimiter=';')
        datap = pd.read_csv('data/persons.csv', delimiter=';')
        datav = pd.read_csv('data/vehicle.csv', delimiter=';')
        datal = pd.merge(datap, dataa, on='accident_id')
        datal = pd.merge(datal, datav, on='accident_id')
        pvt = pivot(datal, par1, par2, par3, par4, par5)
        table_create(pvt, frame)
    frm_cmb = tki.Frame(frm)
    frame=tki.Frame(frm)
    tki.Label(frm, text="Сводна таблица", font=('Arial', 10, 'bold')).pack(anchor="n")
    tki.Label(frm, text='Выберете параметры для построения таблицы:').pack(fill='both', anchor='n')
    
    tki.Label(frm_cmb, text=' Индекс 1: ').grid(column=0, row=0)
    cmb1 = ttk.Combobox(frm_cmb)
    cmb1['values'] = ('county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb1.current(0)
    cmb1.grid(column=0, row=1)
    tki.Label(frm_cmb, text=' Индекс 2: ').grid(column=1, row=0)
    cmb2 = ttk.Combobox(frm_cmb)
    cmb2['values'] = ('Не выбрано', 'county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb2.current(0)
    cmb2.grid(column=1, row=1)
    tki.Label(frm_cmb, text=' Значение: ').grid(column=2, row=0)
    cmb3 = ttk.Combobox(frm_cmb)
    cmb3['values'] = ('vehicle', 'peds', 'fatals', 'age', 'model_year')
    cmb3.current(0)
    cmb3.grid(column=2, row=1)
    tki.Label(frm_cmb, text=' Столбец: ').grid(column=3, row=0)
    cmb4 = ttk.Combobox(frm_cmb)
    cmb4['values'] = ('Не выбрано', 'county',	'month',	'year',	
                     'hour',	'lgt_cond',	'weather', 'fatals',	'road_fc',
                     'dow',	'large_truck',	'speeding',	'ped_f',	'pedal',	'pedal_f',
                     'distracted_driver',	'drowsy_driver', 'sex')
    cmb4.current(0)
    cmb4.grid(column=3, row=1)
    tki.Label(frm_cmb, text=' Метод агрегации: ').grid(column=4, row=0)
    cmb5 = ttk.Combobox(frm_cmb)
    cmb5['values'] = ('np.sum', 'min', 'max', 'np.mean')
    cmb5.current(0)
    cmb5.grid(column=4, row=1)
    frm_cmb.pack(anchor='n')
    btn = tki.Button(frm, text='  Создать  ', command=clck)
    btn.pack(anchor='n')
    cmb1.bind("<Return>", lambda events:clck())
   
def map_create(frm, test):
    clear(frm)
    tki.Label(frm, text="Карта США, Аризона", font=('Arial', 10, 'bold')).pack(anchor="n")
    canvas = tki.Canvas(frm, bg = 'white', height = 800, width = 800)
    canvas.pack()
    canvas.create_image(130,-30,anchor = 'nw', image = test)
    
