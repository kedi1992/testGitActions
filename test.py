from datetime import datetime, timedelta
# welcome
data_string = f"\n{datetime.today().strftime('%Y-%m-%d: %H:%M:%S')} log dumped"

with open('data.txt', 'a') as fp:
    fp.write(data_string)
    fp.close()
