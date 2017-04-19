import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

train = pd.read_csv('newtrain.csv')
test = pd.read_csv('newtest.csv').drop(['atemp','holiday','year','datetime'],axis=1)
train1 = train.drop(['datetime','registered','casual','atemp','holiday','year'],axis = 1)
x = train1.drop(['count'],axis = 1)
y = train1['count']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=1)
rlf = GradientBoostingRegressor()
rlf.fit(x_train,y_train)
y_pre = rlf.predict(x_test)
print(rlf.score(x_test,y_test))
test_y = rlf.predict(test)

ntest_y = []
for i in test_y:
    if i<0:
        i = 0
    ntest_y.append(i)
