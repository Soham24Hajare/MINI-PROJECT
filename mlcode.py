#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


housing = pd.read_csv("data.csv")


# In[3]:


#housing.head()


# In[4]:


#housing.info()


# In[5]:


#housing['CHAS'].value_counts()


# In[6]:


#housing.describe()


# In[7]:


# In[8]:


#for histogram
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))


# ## Train- Test Splitting

# In[9]:


import numpy as np
#for learning purpose
def split_train_test(data,test_ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    print(shuffled)
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices= shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


# In[10]:


train_set, test_set = split_train_test(housing,0.2)


# In[11]:


#print(f"Rows in train set: {len(train_set)}\nRows in test set:{len(test_set)}\n" )


# In[12]:


from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
#print(f"Rows in train set: {len(train_set)}\nRows in test set:{len(test_set)}\n" )


# In[13]:


from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# In[14]:


strat_test_set['CHAS'].value_counts()


# In[15]:


strat_train_set['CHAS'].value_counts()


# In[16]:


95/7


# In[17]:


376/28


# In[18]:


housing = strat_train_set.copy()


# # looking for correlations
#

# In[19]:


corr_matrix = housing.corr()
corr_matrix['MEDV'].sort_values(ascending=False)


# In[20]:


from pandas.plotting import scatter_matrix
attributes=["MEDV","RM","ZN","LSTAT"]
scatter_matrix(housing[attributes], figsize=(12,8))


# In[21]:


housing.plot(kind="scatter", x="RM", y="MEDV", alpha=0.8)


# # trying out attribute combinations

# In[22]:


housing["TAXRM"] = housing['TAX']/housing['RM']


# In[23]:


housing.head()


# In[24]:


corr_matrix = housing.corr()
corr_matrix['MEDV'].sort_values(ascending=False)


# In[25]:


housing.plot(kind="scatter", x="TAXRM", y="MEDV", alpha=0.8)


# In[26]:


housing = strat_train_set.drop("MEDV", axis=1)
housing_labels = strat_train_set["MEDV"].copy()


# # missing attributes

# In[27]:


# to take care of missing attributes, you have three options
#  1. To get rid of the missing data points
#  2. Get rid of the whole attribute
#  3. Set the value to some value(0, mean or median)


# In[28]:


a= housing.dropna(subset=["RM"]) #Option1
a.shape
#note that original housing dataframe will remain unchanged


# In[29]:


housing.drop("RM",axis=1).shape  #Option2
#note that original housing dataframe will remain unchanged


# In[30]:


median = housing["RM"].median() #compute median for option 3


# In[31]:


housing["RM"].fillna(median)
#note that original housing dataframe will remain unchanged


# In[32]:


housing.shape


# In[33]:


housing.describe()  #before we started filling missing attributes


# In[34]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "median")
imputer.fit(housing)


# In[35]:


imputer.statistics_


# In[36]:


X = imputer.transform(housing)


# In[37]:


housing_tr = pd.DataFrame(X, columns= housing.columns)


# In[38]:


housing_tr.describe()


# # Scikit-learn Design

# Primarily, three types of objects
# 1. Estimators
# 2. Transformers
# 3. Predictors

# # Feature Scaling

# Primarily, two types of feature scaling methods:
# 1. Min-MAX Scaling(Normalization)
# 2. Standardization

# # Creating a pipeline

# In[39]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    # .......... add as many as you want in your pieline
    ('std_scaler', StandardScaler()),
])


# In[40]:


housing_num_tr = my_pipeline.fit_transform(housing)


# In[41]:


housing_num_tr.shape


# ## Selecting a desired model for real estate predictor

# In[42]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
#model = LinearRegression()
#model = DecisionTreeRegressor()
model= RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)


# In[43]:


some_data = housing.iloc[:5]


# In[44]:


some_labels = housing_labels.iloc[:5]


# In[45]:


prepared_data = my_pipeline.transform(some_data)


# In[46]:


model.predict(prepared_data)


# In[47]:


list(some_labels)


# # Evaluating the model

# In[48]:


from sklearn.metrics import mean_squared_error
housing_predictions = model.predict(housing_num_tr)
mse = mean_squared_error(housing_labels, housing_predictions)
rmse = np.sqrt(mse)


# In[49]:


#print(rmse)


# # Using better evaluation technique - Cross Validation

# In[50]:


# 1 2 3 4 5 6 7 8 9 10
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, housing_num_tr, housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)


# In[51]:


#print(rmse_scores)


# In[52]:


def print_scores(scores):
    print("Scores:",scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


# In[53]:


#print(rmse_scores)


# ...........CWNWDNWID

# ## Saving The Model

# In[54]:


from joblib import dump, load
dump(model, 'Dragon.joblib')


# ## testing the data

# In[55]:


X_test = strat_test_set.drop("MEDV", axis=1)
Y_test = strat_test_set["MEDV"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_predictions = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
#print(final_predictions, list(Y_test))


# In[56]:


print(final_rmse)


# In[57]:


#print(prepared_data[0])


# # Using the model

# In[61]:


#from joblib import dump, load
#import numpy as np
#model= load('Dragon.joblib')
#features = np.array([[0, 3.12628155, 0, 0, 0, -0.24273294, -1.31238772, 0, 0, -0.5778192, 0, 0, 0]])
#a= model.predict(features)

#print(a)

# In[ ]:




