l = [1,2,3]
s = []
s.append(l)
s.append(l)


for iCount in range(0, len(s)):
    print()
    for jCount in range(0, len(s[iCount])):
        print(s[iCount][jCount])