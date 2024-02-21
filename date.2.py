from datetime import timedelta, datetime

x = datetime.now()
a = x - timedelta(days = 1)
b = x + timedelta(days = 1)

print("Yesterday is: ", a.strftime("%Y-%m-%d"))
print("Today is: ", x.strftime("%Y-%m-%d"))
print("Tomorrow is: ", b.strftime("%Y-%m-%d"))
