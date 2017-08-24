def frequency(l):
    minCount = len(l)
    maxCount = 0
    newList=[]
    l.sort()
    i=0
    while i < len(l):
        count =0
        for j in range(i,len(l)):
            if l[i]==l[j]:
                count =count +1
        newList.append([l[i],count])
        if count==len(l):
            minCount=count
            maxCount=count
        if count < minCount:
            minCount = count
        elif count > maxCount:
            maxCount = count

        i=i+count
    FreListmax=[]
    FreListmin=[]
    for e in range(len(newList)):
        if minCount==maxCount:
            FreListmin.append(newList[e][0])
            FreListmax.append(newList[e][0])
            break
        if minCount==newList[e][1]:
            FreListmin.append(newList[e][0])
        elif maxCount==newList[e][1]:
            FreListmax.append(newList[e][0])
    print(FreListmin,FreListmax)


list=[1,1,1,1,1,1,1,1,1]
frequency(list)
