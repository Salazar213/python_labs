m = int(input("Минуты "))
days = 0
if m <1440:
    print(f"{m//60}:{(m%60):02d}")
else:
    while m>1440:
        m-=1440
        days+=1
print(f"{days}\n{m//60}:{(m%60):02d}")
