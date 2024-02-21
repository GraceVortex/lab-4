from datetime import datetime, timedelta

x = datetime.now()
print("W/0 microsec time is: ", x.replace(microsecond=0))

