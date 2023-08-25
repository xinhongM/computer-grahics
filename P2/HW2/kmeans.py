import numpy as np
import matplotlib.pyplot as plt
import random
from numpy import *

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataMat, k):
    # 获取样本数与特征值
    m, n = shape(dataMat)
    # 初始化质心,创建(k,n)个以零填充的矩阵
    centroids = mat(zeros((k, n)))
    # 循环遍历特征值
    for j in range(n):
        # 计算每一列的最小值
        minJ = min(dataMat[:, j])
        # 计算每一列的范围值
        rangeJ = float(max(dataMat[:, j]) - minJ)
        # 计算每一列的质心,并将值赋给centroids
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    # 返回质心
    return centroids 


def kMeans(dataMat, k, distMeas=distEclud, createCent=randCent):
    # 获取样本数和特征数
    m, n = shape(dataMat)
    # clusterAssment包含两个列:一列记录簇索引值,第二列存储误差(误差是指当前点到簇质心的距离,后面会使用该误差来评价聚类的效果)
    clusterAssment = mat(zeros((m, 2)))

    centroids = createCent(dataMat, k)
    # print(centroids)
    # 初始化标志变量,用于判断迭代是否继续,如果True,则继续迭代
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        # 遍历所有数据找到距离每个点最近的质心,
        # 可以通过对每个点遍历所有质心并计算点到每个质心的距离来完成
        for i in range(m):
            minDist = inf # 正无穷
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataMat[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        for cent in range(k):
            ptsInClust = dataMat[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)# axis=0列方向

    return centroids, clusterAssment

def kmeanShow(dataMat,centers,clusterAssment):
    plt.scatter(np.array(dataMat)[:, 0], np.array(dataMat)[:, 1], c=np.array(clusterAssment)[:, 0].T)
    plt.scatter(centers[:, 0].tolist(), centers[:, 1].tolist(), marker = "x", c="r")
    plt.show()

def testdata1():
    dataMat = mat(zeros((50, 2)))
    for i in range(25):
        dataMat[i] = mat([random.randint(2,30), random.randint(2,30)])
    for i in range(25,40):
        dataMat[i] = mat([random.randint(30,50), random.randint(50,80)])
    for i in range(40,50):
        dataMat[i] = mat([random.randint(80,100), random.randint(50,80)])
    return dataMat


dataMat = testdata1()
m, n = kMeans(dataMat, 0)
kmeanShow(dataMat,m,n)
m, n = kMeans(dataMat, 2)
kmeanShow(dataMat,m,n)
m, n = kMeans(dataMat, 3)
kmeanShow(dataMat,m,n)
m, n = kMeans(dataMat, 4)
kmeanShow(dataMat,m,n)


