from sklearn.datasets import load_boston
from sklearn.preprocessing import scale

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score

import numpy as np

# Мы будем использовать в данном задании набор данных Boston, где нужно предсказать стоимость жилья на основе различных характеристик расположения (загрязненность воздуха, близость к дорогам и т.д.). Подробнее о признаках можно почитать по адресу https://archive.ics.uci.edu/ml/datasets/Housing
# Загрузите выборку Boston с помощью функции sklearn.datasets.load_boston(). Результатом вызова данной функции является объект, у которого признаки записаны в поле data, а целевой вектор — в поле target.
boston_dataset = load_boston()
observations = boston_dataset.data
targets = boston_dataset.target

# Приведите признаки в выборке к одному масштабу при помощи функции sklearn.preprocessing.scale.
observations_scaled = scale(observations)


p_values = np.linspace(1.0, 10.0, num=200)
kf = KFold(n_splits=5, shuffle=True, random_state=42)

cv_accuracy = [cross_val_score(estimator=KNeighborsRegressor(n_neighbors=5, weights='distance', p=p_i, metric='minkowski'), X=observations_scaled, y=targets, cv=kf, scoring='neg_mean_squared_error').mean() for p_i in p_values]

# Определите, при каком p качество на кросс-валидации оказалось оптимальным (обратите внимание, что cross_val_score возвращает массив показателей качества по блокам; необходимо максимизировать среднее этих показателей). Это значение параметра и будет ответом на задачу.

best_p = p_values[int(max(cv_accuracy))]
min_p = p_values[int(min(cv_accuracy))]
print(best_p, max(cv_accuracy))
print(min_p, min(cv_accuracy))