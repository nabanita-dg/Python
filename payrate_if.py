hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hour:")
r = float(rate)
pay=0
if h<=40:
    pay=h*r
else:
    pay=(40*r)+(h-40)*r*1.5
print(pay)