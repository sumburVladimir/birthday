import random
from datetime import date, datetime

year_range = [str(i) for i in range(1992, 2022)]
month_range = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day_range = [str(i).zfill(2) for i in range(1,28)]


argz = {"Year": random.choice(year_range),
        "Month": random.choice(month_range),
        "Day" : random.choice(day_range),
        }

print(str(date.today()))

with open('file.txt', 'w') as out:
    for i in range(100000):
        out.writelines(format(random.choice(year_range)+'-'+random.choice(month_range)+'-'+random.choice(day_range)+'\n'))
        out.writelines('2021-12-11 \n')


with open('file.txt', 'r') as f:
    i = 0
    for line in f:
        if str(date.today()) == line.strip('\n'):
            i+=1
            print(format("Birthday!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "+line))
print(i)
