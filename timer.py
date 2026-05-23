import time
a = input('你想要记时多久？')
a = int(a)
for i in range(a):
    print(f'还有{a - i}秒')
    a - 1
    time.sleep(1)
#第一次初次版本