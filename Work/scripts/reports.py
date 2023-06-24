# -*- coding: utf-8 -*-
"""
Модуль для создания отчетов
"""
import pandas as pd
import numpy as np
def basic_statistics():
    '''
    Основные статистики количественных данных
    Вход: None
    Выход: stat:DataFrame - статистика
    '''
    data = pd.read_csv('data/accident.csv', delimiter=';')
    datap = pd.read_csv('data/persons.csv', delimiter=';')
    datav = pd.read_csv('data/vehicle.csv', delimiter=';')
    stat = pd.DataFrame(columns=['name', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
    stat.loc['vehicle'] = data['vehicle'].describe().T
    stat.loc['peds'] = data['peds'].describe().T
    stat.loc['fatals'] = data['fatals'].describe().T
    stat.loc['age'] = datap['age'].describe().T
    stat.loc['model_year'] = datav['model_year'].describe().T
    name = ['vehicle', 'peds', 'fatals', 'age', 'model year']
    for i in range(5):
        stat.iloc[i, 0] = name[i]
    return stat

def frequency1(par, data):
    '''
    Таблица частот передаваемого столбца
    Вход:
    par : string
        Название столбца
    data : DataFrame
        База данных
    Выход:
    freq : DataFrame
        Таблица частот
    '''
    frs = data[par].value_counts()
    freq = pd.DataFrame()
    freq[par] = frs.index
    freq['amount'] = list(frs)
    freq['part(%)'] = list(frs)/frs.sum()*100
    return freq

def pivot(data, par1, par2, par3, par4, par5):
    '''
    Сводная таблица по параметрам
    Вход:
    data : DataFrame
        База данных
    par1 : String
        Index 1
    par2 : String
        Index 2
    par3 : String
        Values
    par4 : String
        Columns
    par5 :String
        Метод агрегации
    Выход:
    pvt : DataFrame
        Сводная таблица
    '''
    col = np.array([par2, par4])
    qpar = (col == 'Не выбрано')
    if par5=='np.sum':
        par5=np.sum
    if par5=='np.mean':
        par5=np.mean
    if par5=='min':
        par5=min
    if par5=='max':
        par5=max
    if (qpar==(1, 0)).all():
        pvt = pd.pivot_table(data, index=[par1], values=[par3],
                    columns=[par4], aggfunc=par5, fill_value=0)
    elif (qpar==(1, 1)).all():
        pvt = pd.pivot_table(data,
                    index=[par1],
                    values=[par3],
                    aggfunc=par5,
                    fill_value=0)
    elif (qpar==(0, 0)).all():
        pvt = pd.pivot_table(data,
                    index=[par1, par2],
                    values=[par3],
                    columns=[par4],
                    fill_value=0)
    elif (qpar==(0, 1)).all():
        pvt = pd.pivot_table(data,
                    index=[par1, par2],
                    values=[par3],
                    fill_value=0)
    pvt.insert(loc=0, column=par1, value=pvt.index)
    return pvt
