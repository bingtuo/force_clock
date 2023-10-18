import time

minutes = int(input("输入你要专注多少分钟："))
seconds = minutes * 60

while seconds:
    min, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1    
//d 

print("时间到了！")
