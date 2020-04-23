import pandas as pd
import numpy
from pandas import read_csv
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def linearModel(X,Y):
    lrModel = LinearRegression()
    lrModel.fit(X, Y)
    # 训练后模型截距
    print("intercept:",lrModel.intercept_)
    # 训练后模型权重
    print("coef:",lrModel.coef_)
data = read_csv("browsing_low_intensity_256_user_2GB.csv")
y = read_csv("browsing_low_intensity_256_user_mem_2GB.csv")
data["productsPerPage"] = 30
#print(data[:10])
x = data.loc[:119,["Load Intensity","productsPerPage"]]
yCPU = y.loc[:119,[" CPU utilized"]]
yMem = y.loc[:119,[" Memory usaged"]]

linearModel(x,yCPU)





