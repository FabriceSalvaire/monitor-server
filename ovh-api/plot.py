####################################################################################################

import datetime as datetime

from matplotlib import pyplot as plt
import matplotlib.dates as mpl_dates

from OvhApi import Client, dump_json

####################################################################################################

client = Client()
service = client.get_vps()[0]
period = 'lastday'
period = 'lastweek'
period = 'lastmonth'
ressource = 'mem:used'
data = client.get_vps(service, 'monitoring', period=period, type=ressource)

print data.keys()
print data['unit']

timestamps = [d['timestamp'] for d in data['values']]
values = [d['value'] for d in data['values']]

dates = [datetime.datetime.fromtimestamp(x) for x in timestamps]

axe = plt.gca()
timestamp_formater = mpl_dates.DateFormatter('%Y-%m-%d %H:%M:%S')
axe.xaxis.set_major_formatter(timestamp_formater)
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
plt.grid(True)

plt.plot(dates, values, 'o-')
plt.show()

####################################################################################################
# 
# End
# 
####################################################################################################
