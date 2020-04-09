OoBEndings = []
for list in listOfLoops:
    end = list[-1]
    if end[:3] == "out" and list[-2] not in OoBEndings:
        OoBEndings.append(list[-2])
        print("appended " + str(list[-2]))
print(OoBEndings)
