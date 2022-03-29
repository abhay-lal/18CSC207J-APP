count = 0
TupleList = [8,'k','abc',True,(),9,6,'B']
for i in range(len(TupleList)):
    if type(TupleList[i]) is tuple:
        break
    count += 1

print(count)