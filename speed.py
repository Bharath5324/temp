import speedtest
import csv
import datetime
time = str(datetime.datetime.now())
st = speedtest.Speedtest()
with open('/home/bharath/speed.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([time, str((st.download()*pow(10,-6)/8)), str((st.upload()*pow(10,-6)/8))])
