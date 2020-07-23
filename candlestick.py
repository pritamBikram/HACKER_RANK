import matplotlib.pyplot as plt
#import matplotlib.ticker as mticker
#from matplotlib.finance import candlestick_ohlc
from matplotlib import style
style.use('ggplot')
x=[1,2,3,4,5]
y= [7,9,1,5,6]
y1=[8,6,4,2,3]
#candlestick_ohlc(x,y)
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.title("STRAIGHT LINE")
plt.show()

