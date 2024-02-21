from datetime import datetime

x = datetime(2022, 2, 10, 12, 30, 15)  
y = datetime(2022, 2, 10, 12, 35, 20) 

xsec = x.second
ysec = y.second
c = abs(xsec - ysec)
print(c)