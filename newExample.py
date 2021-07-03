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

dailyDataUSDARS= pd.read_excel("gonzalez/Datoshistoricos.xlsx")

print(dailyDataUSDARS[['Retornos USD/ARS','Fecha']])