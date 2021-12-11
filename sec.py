from datetime import date,datetime
import time
sec = datetime.now().second
print(sec)
while True:
    if datetime.now().second == 12:
        print('сработало событие по таймеру')
    else:
        print(datetime.now().second)
    time.sleep(1)