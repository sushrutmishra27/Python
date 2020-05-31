import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


apiKey='EVUDFH3RG5TIDTYT'

ts=TimeSeries(key=apiKey, output_format='pandas')
data,meta_data=ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
print(data)


i=1
#while i==1:
 #   data,meta_data=ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
  #  data.to_excel("output.xlsx")
   # time.sleep(60)
close_data=data['4. close']
percent=close_data.pct_change()

print(percent)
lastChange=percent[-1]

if abs(lastChange)>0.004:
    print('MSFT Alert:' + lastChange)
    
