#! -*-coding: utf-8 -*-
import math
import random

def init(finallis):
    fi = open("car.data", "r")
    lis = fi.readlines()
    fi.close()
    count = 0
    for ele in lis:
        temp = ele.split(',')
        temp[-1] = temp[-1][0:-1]
        if (count == 0):
            count += 1
            continue
        finallis.append(temp)

def initname(namelis):
    fi = open("car.name", "r")
    lis = fi.readlines()
    fi.close()
    for ele in lis:
        ele = ele[0:-1]
        namelis.append(ele.split(","))

def EntD(lis):
    result = 0
    for ele in lis:
        if(ele != 0):
            result -= ele*(math.log2(ele))
        else:
            result -= 0
    return result

def classify(lis):
    total = 0
    unacc = 0
    acc = 0
    good = 0
    vgood = 0
    for ele in lis:
        total += 1
        if (ele[-1] == "good"):
            good += 1
        elif (ele[-1] == "vgood"):
            vgood += 1
        elif (ele[-1] == "unacc"):
            unacc += 1
        elif (ele[-1] == "acc"):
            acc += 1
    try:
        pkgood = float(good / total)
        pkvgood = float(vgood / total)
        pkunacc = float(unacc / total)
        pkacc = float(acc / total)
        lisClass = [pkgood, pkvgood, pkunacc, pkacc]
        Ent = EntD(lisClass)  # 得到信息熵
    except ZeroDivisionError:
        return 0
    return Ent

def classify_buying(lis):
    dict = ["vhigh", "high", "med", "low"]
    vhigh = 0
    high = 0
    med = 0
    low = 0
    total = 0
    vhighlis = []
    highlis = []
    medlis = []
    lowlis = []
    for ele in lis:
        total += 1
        if(ele[0]==dict[0]):
            vhigh += 1
            vhighlis.append(ele)
        elif(ele[0]==dict[1]):
            high += 1
            highlis.append(ele)
        elif(ele[0]==dict[2]):
            med += 1
            medlis.append(ele)
        elif(ele[0]==dict[3]):
            low += 1
            lowlis.append(ele)
    try:
        pkvhigh = float(vhigh / total)
        pkhigh = float(high / total)
        pkmed = float(med / total)
        pklow = float(low / total)
        result = pkvhigh*classify(vhighlis) + pkhigh*classify(highlis) + pkmed*classify(medlis) + pklow*classify(lowlis)
    except ZeroDivisionError:
        return 0
    return result

def classify_maint(lis):
    dict = ["vhigh", "high", "med", "low"]
    vhigh = 0
    high = 0
    med = 0
    low = 0
    total = 0
    vhighlis = []
    highlis = []
    medlis = []
    lowlis = []
    for ele in lis:
        total += 1
        if (ele[1] == dict[0]):
            vhigh += 1
            vhighlis.append(ele)
        elif (ele[1] == dict[1]):
            high += 1
            highlis.append(ele)
        elif (ele[1] == dict[2]):
            med += 1
            medlis.append(ele)
        elif (ele[1] == dict[3]):
            low += 1
            lowlis.append(ele)
    try:
        pkvhigh = float(vhigh / total)
        pkhigh = float(high / total)
        pkmed = float(med / total)
        pklow = float(low / total)
        result = pkvhigh*classify(vhighlis) + pkhigh*classify(highlis) + pkmed*classify(medlis) + pklow*classify(lowlis)
    except ZeroDivisionError:
        return 0
    return result

def classify_doors(lis):
    dict = ["2", "3", "4", "5more"]
    twodoors = 0
    threedoors = 0
    fourdoors = 0
    fivedoors = 0
    total = 0
    twodoorslis = []
    threedoorslis = []
    fourdoorslis = []
    fivedoorslis = []
    for ele in lis:
        total += 1
        if (ele[2] == dict[0]):
            twodoors += 1
            twodoorslis.append(ele)
        elif (ele[2] == dict[1]):
            threedoors += 1
            threedoorslis.append(ele)
        elif (ele[2] == dict[2]):
            fourdoors += 1
            fourdoorslis.append(ele)
        elif (ele[2] == dict[3]):
            fivedoors += 1
            fivedoorslis.append(ele)
    try:
        pk1 = float(twodoors / total)
        pk2 = float(threedoors / total)
        pk3 = float(fourdoors / total)
        pk4 = float(fivedoors / total)
        result = pk1*classify(twodoorslis) +pk2*classify(threedoorslis) + pk3*classify(fourdoorslis) + pk4*classify(fivedoorslis)
    except ZeroDivisionError:
        return 0
    return result

def classify_person(lis):
    dict = ["2", "4", "more"]
    twopeople = 0
    fourpeople = 0
    morepeople = 0
    total = 0
    twopeoplelis = []
    fourpeoplelis = []
    morepeoplelis = []
    for ele in lis:
        total += 1
        if (ele[3] == dict[0]):
            twopeople += 1
            twopeoplelis.append(ele)
        elif (ele[3] == dict[1]):
            fourpeople += 1
            fourpeoplelis.append(ele)
        elif (ele[3] == dict[2]):
            morepeople += 1
            morepeoplelis.append(ele)
    try:
        pk1 = float(twopeople / total)
        pk2 = float(fourpeople / total)
        pk3 = float(morepeople / total)
        result = pk1*classify(twopeoplelis) + pk2*classify(fourpeoplelis) + pk3*classify(morepeoplelis)
    except ZeroDivisionError:
        return 0
    return result

def classify_lugboot(lis):
    dict = ["small", "med", "big"]
    small = 0
    med = 0
    big = 0
    total = 0
    smalllis = []
    medlis = []
    biglis = []
    for ele in lis:
        total += 1
        if (ele[4] == dict[0]):
            small += 1
            smalllis.append(ele)
        elif (ele[4] == dict[1]):
            med += 1
            medlis.append(ele)
        elif (ele[4] == dict[2]):
            big += 1
            biglis.append(ele)
    try:
        pk1 = float(small / total)
        pk2 = float(med / total)
        pk3 = float(big / total)
        result = pk1*classify(smalllis) + pk2*classify(medlis) + pk3*classify(biglis)
    except ZeroDivisionError:
        return 0
    return result

def classify_safety(lis):
    dict = ["low", "med", "high"]
    low = 0
    med = 0
    high = 0
    total = 0
    lowlis = []
    medlis = []
    highlis = []
    for ele in lis:
        total += 1
        if (ele[5] == dict[0]):
            low += 1
            lowlis.append(ele)
        elif (ele[5] == dict[1]):
            med += 1
            medlis.append(ele)
        elif (ele[5] == dict[2]):
            high += 1
            highlis.append(ele)
    try:
        pk1 = float(low / total)
        pk2 = float(med / total)
        pk3 = float(high / total)
        result = pk1*classify(lowlis) + pk2*classify(medlis) + pk3*classify(highlis)
    except ZeroDivisionError:
        return 0
    return result

def findnode(finallis):
    Ent = classify(finallis)
    try:
        temp = finallis[0]
        if(temp[0] != None):
            GainBuying = Ent - classify_buying(finallis)
        else:
            GainBuying = -1
        if (temp[1] != None):
            GainMaint = Ent - classify_maint(finallis)
        else:
            GainMaint = -1
        if (temp[2] != None):
            GainDoors = Ent - classify_doors(finallis)
        else:
            GainDoors = -1
        if (temp[3] != None):
            GainPerson = Ent - classify_person(finallis)
        else:
            GainPerson = -1
        if (temp[4] != None):
            GainLugboot = Ent - classify_lugboot(finallis)
        else:
            GainLugboot = -1
        if(temp[5] != None):
            GainSafety = Ent - classify_safety(finallis)
        else:
            GainSafety = -1
        rootlis = [GainBuying, GainMaint, GainDoors, GainPerson, GainLugboot, GainSafety]
        rootnode = rootlis.index(max(rootlis))
        return rootnode
    except IndexError:
        return None

def extend(rootnode, rootlis, namelis, stage, string, treelis):
    stage += 1

    if(stage==8):
        unacc = 0
        acc = 0
        good = 0
        vgood = 0
        for ele in rootlis:
            if(ele[-1]=="unacc"):
                unacc += 1
            elif(ele[-1]=="acc"):
                acc += 1
            elif(ele[-1]=="good"):
                good += 1
            elif(ele[-1]=="vgood"):
                vgood += 1
        temp = max(unacc, acc, good, vgood)
        if(temp == unacc):
            string += "->unacc"
        elif(temp == acc):
            string += "->acc"
        elif(temp == good):
            string += "->good"
        elif(temp == vgood):
            string += "->vgood"
        string = string[2:]
        treelis.append(string)
        #出口
    else:
        try:
            if(rootnode != None):
                string = string + "->" + str(rootnode) + ":"
            tempnamelis = namelis[rootnode]
            templist1 = []
            templist2 = []
            templist3 = []
            templist4 = []
            templist = [templist1, templist2, templist3, templist4]
            for ele in rootlis:
                for i in range(len(tempnamelis)):
                    if(tempnamelis[i] == ele[rootnode]):
                        ele[rootnode] = None
                        templist[i].append(ele)
            for node in range(len(tempnamelis)):
                tempstring = string + tempnamelis[node]
                tempnode = findnode(templist[node])
                extend(tempnode, templist[node], namelis, stage, tempstring, treelis)
        except TypeError:
            extend(rootnode, rootlis, namelis, stage, string, treelis)

def writetree(treelis):
    fi = open("tree.txt", "w+")
    fi.write("\n".join(treelis))
    fi.write("\n")
    fi.close()

def main():
    finallis = []
    namelis = []
    init(finallis)
    initname(namelis)
    lisdata = []
    listest = []
    treelis = [] #最终生成的树
    for ele in listest:
        rand = random.uniform(0, 1)
        if(rand > 0.5):
            lisdata.append(ele)
        else:
            listest.append(ele)
    # 分为训练集和测试集
    fi = open("testdata.txt", "w+")
    for ele in finallis:
        fi.write(",".join(ele))
        fi.write("\n")
    fi.close()
    rootnode = findnode(finallis) # root节点
    stage = 1   #全局变量，表示层数，初始为1，用于迭代
    extend(rootnode, lisdata, namelis, stage, "", treelis) #生成决策树
    writetree(treelis)

