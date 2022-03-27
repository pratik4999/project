# -*- coding: utf-8 -*-
"""linear_regression_project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aU9-YXtpfJuoipkgYa5-b6HQO4Lwr_3E
"""

# Commented out IPython magic to ensure Python compatibility.
import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
import matplotlib.pyplot as plt

# %matplotlib inline

# !git clone https://github.com/Nitesh167/raw-materials-forecasting.git

# cd raw-materials-forecasting/

df = pd.read_csv('dataset raw value.csv')
df.columns = ['Year', "no_of_cars", "steel", "plastics", "iron", "rubber", "aluminium", "glass", "copper"]
df.head(10)

# delete column
del df["Year"]

df.head()

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

from sklearn import linear_model

model_steel = linear_model.LinearRegression()

train_x = np.asanyarray(train[['no_of_cars']])
train_y_steel = np.asanyarray(train[['steel']])
model_steel.fit(train_x, train_y_steel)

pickle.dump(model_steel, open('steel_model.pkl', 'wb'))
steel_model = pickle.load(open('steel_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.steel, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_steel.coef_[0][0] * train_x + model_steel.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("steel")

y_steel_pred = model_steel.predict(test[['steel']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_steel = np.asanyarray(test[['steel']])
test_y_hat_steel = model_steel.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_steel - test_y_steel)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_steel - test_y_steel) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_steel , test_y_steel) )

output = model_steel.predict([['3500000']])
print("steel : %.2f" % output, " steel")

"""# **PLASTICS**"""

from sklearn import linear_model

model_plastics = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_plastics = np.asanyarray(train[['plastics']])
model_plastics.fit(train_x, train_y_plastics)

pickle.dump(model_plastics, open('plastics_model.pkl', 'wb'))
plastics_model = pickle.load(open('plastics_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.plastics, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_plastics.coef_[0][0] * train_x + model_plastics.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("plastics")

y_plastics_pred = model_plastics.predict(test[['plastics']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_plastics = np.asanyarray(test[['plastics']])
test_y_hat_plastics = model_plastics.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_plastics - test_y_plastics)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_plastics - test_y_plastics) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_plastics , test_y_plastics) )

output = model_plastics.predict([['3500000']])
print("plastics : %.2f" % output, "tonnes")

"""# **IRON**"""

from sklearn import linear_model

model_iron = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_iron = np.asanyarray(train[['iron']])
model_iron.fit(train_x, train_y_iron)

pickle.dump(model_iron, open('iron_model.pkl', 'wb'))
iron_model = pickle.load(open('iron_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.iron, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_iron.coef_[0][0] * train_x + model_iron.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("iron")

y_iron_pred = model_iron.predict(test[['iron']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_iron = np.asanyarray(test[['iron']])
test_y_hat_iron = model_iron.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_iron - test_y_iron)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_iron - test_y_iron) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_iron , test_y_iron) )

output = model_iron.predict([['3500000']])
print("iron : %.2f" % output, " tonnes")

"""# **RUBBER**"""

from sklearn import linear_model

model_rubber = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_rubber = np.asanyarray(train[['rubber']])
model_rubber.fit(train_x, train_y_rubber)

pickle.dump(model_rubber, open('rubber_model.pkl', 'wb'))
rubber_model = pickle.load(open('rubber_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.rubber, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_rubber.coef_[0][0] * train_x + model_rubber.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("rubber")

y_rubber_pred = model_rubber.predict(test[['rubber']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_rubber = np.asanyarray(test[['rubber']])
test_y_hat_rubber = model_rubber.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_rubber - test_y_rubber)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_rubber - test_y_rubber) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_rubber , test_y_rubber) )

output = model_rubber.predict([['3500000']])
print("rubber : %.2f" % output, " tonnes")

"""# **ALUMINIUM**"""

from sklearn import linear_model

model_aluminium = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_aluminium = np.asanyarray(train[['aluminium']])
model_aluminium.fit(train_x, train_y_aluminium)

pickle.dump(model_aluminium, open('aluminium_model.pkl', 'wb'))
aluminium_model = pickle.load(open('aluminium_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.aluminium, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_aluminium.coef_[0][0] * train_x + model_aluminium.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("aluminium")

y_aluminium_pred = model_aluminium.predict(test[['aluminium']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_aluminium = np.asanyarray(test[['aluminium']])
test_y_hat_aluminium = model_aluminium.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_aluminium - test_y_aluminium)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_aluminium - test_y_aluminium) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_aluminium , test_y_aluminium) )

output = model_aluminium.predict([['3500000']])
print("aluminium : %.2f" % output, " tonnes")

"""# **GLASS**"""

from sklearn import linear_model

model_glass = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_glass = np.asanyarray(train[['glass']])
model_glass.fit(train_x, train_y_glass)

pickle.dump(model_glass, open('glass_model.pkl', 'wb'))
glass_model = pickle.load(open('glass_model.pkl', 'rb'))

plt.scatter(train.no_of_cars, train.glass, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_glass.coef_[0][0] * train_x + model_glass.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("glass")

y_glass_pred = model_glass.predict(test[['rubber']])

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_glass = np.asanyarray(test[['glass']])
test_y_hat_glass = model_glass.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_glass - test_y_glass)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_glass - test_y_glass) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_glass , test_y_glass) )

output = model_glass.predict([['3500000']])
print("glass : %.2f" % output, " tonnes")

"""# **COPPER**"""

from sklearn import linear_model

model_copper = linear_model.LinearRegression()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_copper = np.asanyarray(train[['copper']])
model_copper.fit(train_x, train_y_copper)

pickle.dump(model_copper, open('copper_model.pkl', 'wb'))
copper_model = pickle.load(open('copper_model.pkl', 'rb'))



plt.scatter(train.no_of_cars, train.copper, color='blue')
plt.xticks(rotation=45)
plt.plot(train_x, model_copper.coef_[0][0] * train_x + model_copper.intercept_[0], '-r')
plt.xlabel("No_of_cars")
plt.ylabel("copper")

y_copper_pred = model_copper.predict(test[['copper']])

# from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['no_of_cars']])
test_y_copper = np.asanyarray(test[['copper']])
test_y_hat_copper = model_copper.predict(test_x)

# print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat_copper - test_y_copper)))
# print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat_copper - test_y_copper) ** 2))
# print("R2-score: %.2f" % r2_score(test_y_hat_copper , test_y_copper) )

output = model_copper.predict([['3500000']])
print("copper : %.2f" % output, " tonnes")
