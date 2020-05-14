from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn import metrics
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale

data = pd.read_csv('wine.data', header = None)

y = data[0]
X = data.loc[:,1:]
X = scale(X)
print(X)

maximus = 0
max_i = 0
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for i in range(1,51):
    neigh = KNeighborsClassifier(n_neighbors=i)
#    neigh.fit(X, y)
#    for train_index, test_index in kf.split(X):
#        X_train, X_test, y_train, y_test = X.iloc[train_index], X.iloc[test_index], y.iloc[train_index], y.iloc[test_index]
#        X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
#        neigh.fit(X_train, y_train)
    scores = cross_val_score(neigh, X, y, cv = kf, scoring='accuracy').mean()
    if scores > maximus:
       maximus = scores
       max_i = i

print(max_i, maximus)
