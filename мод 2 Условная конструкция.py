from time import sleep

print("Добрый день, вам необходимо ввести 3-числа")
sleep(1)
first=int(input("Введите 1-е число:  "))
sleep(1)
second=int(input("Введите 2-е число:  "))
sleep(1)
third=int(input("Введите 3-е число:  "))
if first==second==third:
    print(3)
elif first==second or first==third or third==second:
    print(2)
else:
    print(0)