import re
import pandas as pd

file = open('test.txt','r')

data = []
data = file.readlines(-1)
#print(data)
pattern = r"([0-9]\.[0-9][0-9]pm)"
time = []
commentary = []

#pdb.set_trace()
for i in range(len(data)):
	ext = re.split(pattern,data[i])
	for j in range(len(ext)):
		if(re.match(pattern,ext[j])):
			time.append(ext[j])
			commentary.append(ext[j+1])

df = pd.DataFrame(data = {"Time":time,"Commentary":commentary})
df.to_csv("./Commentary.csv", sep=',',index=False)
