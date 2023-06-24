# -*- coding: utf-8 -*-
"""
Модуль для построения графиков и карты
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graph_bar(datal, par, frm):
    '''
    Столбчатая диаграмма количества происшествий при различных условиях
    Вход:
    datal : DataFrame
        База данных
    par : string
        Название параметра для построения графика
    frm : tki.Toplevel()
        Окно, в котором необходимо вывести график

    Выход: figure: plt.Figure() - график

    Автор: Максим Мосалев
    '''
    figure = plt.Figure()
    axs = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, frm)
    bar1.get_tk_widget().pack(side='top', fill='both', expand=1)
    datal[par].value_counts().sort_index(ascending=True).plot.bar(ax=axs)
    axs.grid()
    axs.set_title('Number of accident - ' + par)
    return figure

def graph_pie(datal, par, frm):
    '''
    Круговая диаграмма количества происшествий при различных условиях
    Вход:
    datal : DataFrame
        База данных
    par : string
        Название параметра для построения графика
    frm : tki.Toplevel()
        Окно, в котором необходимо вывести график

    Выход: figure: plt.Figure() - график

    Автор: Мухамед Борукаев
    '''
    figure = plt.Figure()
    axs = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, frm)
    bar1.get_tk_widget().pack(side='top', fill='both', expand=1)
    dat = datal[par].value_counts().sort_index(ascending=True)
    axs.pie(dat,
            autopct='%1.1f%%',
            textprops={'fontsize':10})
    axs.legend(labels=dat.index.to_list(),
                # title=p,
                title_fontsize=11,
                fontsize=10)

    axs.set_title('Number of accident - ' + par)
    return figure

def graph_hist(datal, par, frm):
    '''
    Гистограммы по данным из столбца
    Вход:
    datal : DataFrame
        База данных
    par : string
        Название параметра для построения графика
    frm : tki.Toplevel()
        Окно, в котором необходимо вывести график

    Выход: figure: plt.Figure() - график

    Автор: Максим Мосалев
    '''
    figure = plt.Figure()
    axs = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, frm)
    bar1.get_tk_widget().pack(side='top', fill='both', expand=1)
    axs.hist(datal[par], color='g', bins=20)
    axs.set_title('Number of ' + par)
    return figure

def graph_scatter(datal, par1, par2, frm):
    '''
    Диаграмма рассеивания по двум столбцам
    Вход:
    datal : DataFrame
        База данных
    par1 : string
        Название столбца для построения графика
     par2 : string
         Название столбца для построения графика
    frm : tki.Toplevel()
        Окно, в котором необходимо вывести график

    Выход: figure: plt.Figure() - график

    Автор: Максим Мосалев
    '''
    figure = plt.Figure()
    axs = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, frm)
    bar1.get_tk_widget().pack(side='top', fill='both', expand=1)
    axs.set_title(par2 + ' - ' + par1)
    axs.scatter(x=datal[par1], y=datal[par2])
    return figure

def graph_boxplot(datal, par1, par2, frm):
    '''
    График ящик с усами по двум столбцам
    Вход:
    datal : DataFrame
        База данных
    par1 : string
        Название столбца 1 для построения графика
     par2 : string
        Название столбца 2 для построения графика
    frm : tki.Toplevel()
        Окно, в котором необходимо вывести график

    Выход: figure: plt.Figure() - график

    Автор: Максим Мосалев
    '''
    figure = plt.Figure()
    axs = figure.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure, frm)
    bar1.get_tk_widget().pack(side='top', fill='both', expand=1)
    axs.set_title(par2 + ' - ' + par1)
    dat=[]
    for i in set(datal[par2]):
        dat.append(datal[datal[par2]==i][par1])
    axs.grid()
    axs.boxplot(dat)
    return figure
