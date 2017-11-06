import pandas as pd
import re

file = open('test.txt','r')
data = []
data = file.readlines(-1)
end = []
for i in range(21):
	j=0
	small_data = data[i]
	#print(i)
	#print(data[i])
	while(j<100):
		pattern = r"(MCID=\""+str(j)+r"\">)(.*?)(</P>)"
		ext_data = re.search(pattern, small_data)
		if ext_data is None:
			break;
		#print(ext_data.group(2))
		if('|' in ext_data.group(2)):
			end.append(ext_data.group(2))
		j = j+1

end1=[]
j=0
i=0
while i<(len(end)):
	if(len(end[i])<=10):
		end1.append(end[i]+end[i+1])
		i=i+1
	else:
		end1.append(end[i])
	
	j=j+1
	i=i+1

# for i in range(len(end1)):
# 	print(end1[i])

df = pd.DataFrame(data = {"Over":[] , "Runs Scored":[] ,"Wickets": [], "Total":[]})
# print(df.columns)

for i in range(20):
	string = ""
	count = 0
	str2 = ""
	x=0
	string = end1[i]
	for j in string:
		# print(j)
		if(j == '|' and count == 0):
			df["Over"][i] = (str2)
			str2 = ""
			count = count+1
		elif(j == 'R' and count == 1 ):
			df["Runs Scored"][i] = (str2)
			str2 = ""
			count = count+1
		elif(j =="s" and count ==2):
			str2 = ""
			# count = count+1
		elif( j == "W" and count ==2):
			df["Wickets"][i] = str2
			str2 = ""
			x = 1
		elif(j =="|" and count == 2):
			# if(x==0):
			# 	df["Wickets"][i] = 0
			str2 = ""
			count = count+1
		elif(j ==":" and count ==3):
			str2 = ""
			count = count+1
		else:
			str2 = str2+j
	df["Total"][i] = (str2)

df1 = pd.DataFrame(data = {"Overs" : df.Over , "Runs": df["Runs Scored"],"Wickets" : df.Wickets , "Total" : df.Total})
#dataframe.to_csv("end_of_over_scores.csv", sep = ',' , index = False)	
df1.Wickets.fillna(0 , inplace = True)
df1.to_csv("./EOO_Summary.csv", sep=',',index=False) 