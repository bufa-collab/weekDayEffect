from typing import Dict
from pandas_datareader import data
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime 
import calendar
from statsmodels.stats.stattools import jarque_bera
from statsmodels.tsa.stattools import adfuller
from datetime import datetime




#Calculamos los Retornos Diarios USD ARS


def dailyReturn(dailyDataUSDARS):
    for i in range (1, len (dailyDataUSDARS)):
        retornos_USDARS.append (dailyDataUSDARS['Adj Close'][i]/ dailyDataUSDARS['Adj Close'] [i-1]-1)
    print ('El retorno diario de USD ARS es=', retornos_USDARS)

retornos_USDARS= []
wkDict = {"lunes":"Monday","martes":"Tuesday","miércoles":"Wednesday","jueves":"Thursday","viernes":"Friday","sabado":"Saturday","domingo":"Sunday"}

def weekdayName(x: int,y: dict):
    if x in y.keys():
        x = y[x]
    return x
        



if __name__ == "__main__":
    inicio= '2019-01-01' #Fecha Inicial
    fin= '2020-01-01' #Fecha Final
    dailyDataUSDARS= web.get_data_yahoo('ARS=X', inicio, fin, interval='d')
    weekdayFunc = lambda x : x.strftime('%A')
    dayName = [weekdayName(weekdayFunc(x),wkDict) for x in dailyDataUSDARS.index]
    dailyDataUSDARS['dayName'] = dayName
    wkList = []
    wkNumber = 0
    for x in dailyDataUSDARS['dayName']:
        if x == "Monday":
            wkNumber = wkNumber + 1
        wkList.append(wkNumber)
    dailyDataUSDARS['weekNumber'] = wkList
    #print(dailyDataUSDARS)
    weeklyDataUSDARS = dailyDataUSDARS.groupby("weekNumber").sum()
    adjCloseWK = weeklyDataUSDARS['Adj Close']
    dailyData = dailyDataUSDARS[dailyDataUSDARS["dayName"] == "Monday"]
    print(len(dailyData))
    for i in wkDict.values():
        dailyData = dailyDataUSDARS[dailyDataUSDARS["dayName"] == i]
        # print(weeklyDataUSDARS.describe())
        # print(dailyDataUSDARS.kurtosis())
        # print(dailyDataUSDARS.skew())
        # print(weeklyDataUSDARS)
        # print(jarque_bera(dailyDataUSDARS['Adj Close']))
        print(len(dailyData))
        try:
            print(adfuller(dailyData['Adj Close']))
        except:
            print(f"El tamaño de la muestra para los dias: {i} es insuficiente")
        #plt.plot(dailyData['Adj Close'])    
    
