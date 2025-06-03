import random
def get_trake(distance):
    position=[]
    position.append([791,1971,60])
    X =107+786

    first_0=791
    first_1=1971
    first_2=60

    all_x=0

    while all_x <=(X + distance):
        first_0 += random.randint(0, 2)
        first_1 += random.randint(-1, 2)
        first_2 += random.randint(20, 300)

        if first_1 >=1974:
            first_1 = 1972
        i = [first_0, first_1, first_2]
        all_x  = i[0]
        position.append(i)
    # print("第一次构建打的数组")
    # print(position)
    # print(len(position))

    t= position
    MAX_POINTS =len(t) // 50
    e = []

    i=1
    n=t[-1]
    for r in range(1,len(t)-2,MAX_POINTS):
        e.append(t[r])
    e.append(n)
    # print("重构数组")
    # print(e)

    return e