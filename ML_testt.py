import numpy as np
import pandas as pd
import re

pd.options.display.max_columns = 11
pd.set_option('display.width', 200)

data = pd.read_csv('titanic.csv', index_col='PassengerId')

print(data.head())
sex_counts = data['Sex'].value_counts()
print('{} {}'.format(sex_counts['male'], sex_counts['female']))

surv_counts = data['Survived'].value_counts()
surv_percent = 100.0 * surv_counts[1] / surv_counts.sum()
print('{:0.2f}'.format(surv_percent))

pcClass_counts = data['Pclass'].value_counts()
pcClass_percent = 100*pcClass_counts[1]/pcClass_counts.sum()
print('{:0.2f}'.format(pcClass_percent))

age_counts = data['Age']
age_median = age_counts.median()
print('{:0.2f} {:0.2f}'.format(age_counts.mean(), age_counts.median()))

#correlation = data[['SibSp', 'Parch']].corr()
k = data['SibSp'].corr(data['Parch'])
print('{:0.2f}'.format(k))

#temp = data.query("Sex != 'male'")
temp = data[data['Sex'] == 'female']
temp = temp['Name'].str.split(r'\. |, ', expand=True)
print(temp[2].value_counts().head(1).index.values[0])

print(data[data['Name'].str.contains(r'Mary')])

