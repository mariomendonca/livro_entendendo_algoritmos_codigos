import datetime


def fac(x):
    if x == 1:
        return 1
    return x * fac(x - 1)


start_datetime = datetime.datetime.now()
x = fac(7)
end_datetime = datetime.datetime.now()
print(x)
print(end_datetime - start_datetime)
