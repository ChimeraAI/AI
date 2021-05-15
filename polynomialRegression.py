
import numpy as np
import pandas as pd

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

# test classification dataset
from collections import Counter
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# summarize the dataset
print(X.shape, y.shape)
print(Counter(y))
# define the multinomial logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
# define the model evaluation procedure
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate the model and collect the scores
n_scores = cross_val_score(model, dfTest[['inputOne','inputTwo']], dfTest['output'], scoring='accuracy', cv=cv, n_jobs=-1)
# report the model performance
print('Mean Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))