import random
import pyinputplus as pyip
min=1
max=100
point=random.randint(1,100)
guess=pyip.inputInt("請輸入整數",min=1,max=100)
while True:
    if point==guess:
        print("猜中了")
        break
    else:
        if point>guess:
            min=guess
            print(f"{min}到{max}")
            guess=pyip.inputInt("請輸入整數",min=1,max=100)
        else:
            max=guess
            print(f"{min}到{max}")
            guess=pyip.inputInt("請輸入整數",min=1,max=100)
        continue
print("遊戲結束")