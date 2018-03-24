#! -*-coding: utf-8 -*-

import generate

def initTree():
    try:
        fi = open("tree.txt", "r")
        lis = fi.readlines()
        fi.close()
    except IOError:
        print("IOError!")
    treelis = []
    for ele in lis:
        ele = ele[0:-1]
        treelis.append(ele.split("->"))
    return treelis

def connectTestData():
    try:
        fi = open("testdata.txt", "r")
        lis = fi.readlines()
        fi.close()
    except IOError:
        print("IOError!")
    testdata = []
    for ele in lis:
        ele = ele[0:-1]
        testdata.append(ele)
    return testdata

if __name__=="__main__":
    generate.main()
    treelis = initTree()
    testdata = connectTestData()
    correct = 0
    wrong = 0
    for Data in testdata:
        data = Data.split(",")
        for branch in treelis:
            flag = True
            for i in range(len(branch)-1):
                node = int(branch[i][0])
                if(data[node] != branch[i][2:]):
                    flag = False
                    break
            if(flag == True):   #找到数据对应分支
                if(data[-1] == branch[-1]):
                    correct += 1
                else:
                    wrong += 1
    result = float(correct / (correct + wrong))
    print(result)