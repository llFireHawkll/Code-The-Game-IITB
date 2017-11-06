import pandas as pd
df = pd.read_csv('Final_CSV.csv')

x = df['Overs'].values
y = df['ScoreBoard'].values

for i in range(len(y)):
    y[i]=y[i][0]
    if(y[i]=='W'):
        y[i]=-1
    else:
        y[i]=int(y[i])


import matplotlib.pyplot as plt
ind = np.arange(min(x)-0.1, max(x)+1,1)
ind = ind.reshape((len(ind), 1))
get_ipython().magic('matplotlib inline')
plt.figure(figsize=(20,10))
plt.plot(x,y,color='blue')
plt.xticks(ind)
plt.title('Score v/s Ball Analysis',fontsize = 40)
plt.xlabel('Balls in Overs 1-20',fontsize = 30)
plt.ylabel('Runs',fontsize = 30)
plt.show()

df1 = pd.read_csv('EOO_Summary.csv')
x = df1['Overs'].values
y = df1['Runs'].values

ind = np.arange(min(x), max(x)+1, 1)
ind = ind.reshape((len(ind), 1))

width = 0.5

fig, ax = plt.subplots(figsize=(20,10))
rects1 = ax.bar(ind, y, width, color='r')
plt.xticks(ind)
plt.title('Overs vs Runs Analysis',fontsize = 40)
plt.xlabel('Over',fontsize = 30)
plt.ylabel('Runs',fontsize = 30)




