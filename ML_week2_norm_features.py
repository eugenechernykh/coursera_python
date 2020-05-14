import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

data_train = pd.read_csv('perceptron-train.csv', header=None)
data_test = pd.read_csv('perceptron-test.csv', header=None)
X = data_train[[1, 2]]
y = data_train[0]
X_test = data_test[[1, 2]]
y_test = data_test[0]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)

clf = Perceptron()
clf.fit(X, y)
predictions = clf.predict(X_test)
score = accuracy_score(y_test, predictions)
print(score)


clf.fit(X_scaled, y)
predictions_scaled = clf.predict(X_test_scaled)
score_scaled = accuracy_score(y_test, predictions_scaled)
print(score_scaled)

print('{:.3f}'.format(score_scaled - score))
