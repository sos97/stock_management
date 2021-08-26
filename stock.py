import time
import datetime
import pandas as pd

stock_name = "%5EIXIC"
period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
interval = '1wk'

query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{stock_name}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

df = pd.read_csv(query_string)

print(df)
