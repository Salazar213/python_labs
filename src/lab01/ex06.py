n = int(input("N: "))
person = 0
online = 0
for i in range(n):
    surname, name, age, form = input().split()
    if form == "True":
        person += 1
    else:
        online += 1
print(person, online)
