import numpy as np
import pandas as pd

## https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0

np.random.seed(0)
inputOne = 3*np.random.rand(1000) + 33
inputTwo = 3*np.random.rand(1000) + 33
residual = 0.5*np.random.randn(1000)
output = 3 + 0.3*inputOne + 0.7*inputTwo + residual

inputOneTrain = inputOne[:-20]
inputTwoTrain = inputTwo[:-20]
outputTrain = output[:-20]

inputOneTest = inputOne[-20:]
inputTwoTest = inputTwo[-20:]
outputTest = output[-20:]

dfTrain = pd.DataFrame(
    {'inputOne': inputOneTrain,
    'inputTwo': inputTwoTrain,
    'output': outputTrain}
)

dfTest = pd.DataFrame(
    {'inputOne': inputOneTest,
    'inputTwo': inputTwoTest,
    'output': outputTest}
)

from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(dfTest[['inputOne','inputTwo']],dfTest['output'])

outputPred = regr.predict(dfTest[['inputOne','inputTwo']])

from matplotlib import pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(inputOneTest,inputTwoTest,outputTest, color = 'black')
ax.plot3D(inputOneTest,inputTwoTest,outputPred,color='blue',linewidth=3)

ax.set_xlabel('inputOne')
ax.set_ylabel('inputTwo')
ax.set_zlabel('output')
plt.show()

