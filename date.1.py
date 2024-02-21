from datetime import datetime, timedelta

x = datetime.now()
c = x-timedelta(days = 5)

print("Date five dayse ago: ", c.strftime("%Y-%m-%d"))
