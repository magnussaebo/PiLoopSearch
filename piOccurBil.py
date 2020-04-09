import ast
import piBillion
pi = piBillion.pi

f = open('occurBil.txt', 'r')
temp = f.read()
f.close()

# for 10^7 -1
occurList = ast.literal_eval(temp)

"""
def makeOccurList():
    for num in range(1, 10**7):
        temp = pi.find(str(num))
        occurList.append(temp)
        print("done with " + str(num))
    return occurList
"""
