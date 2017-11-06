import re
import pandas as pd

file = open('test.txt','r')
data = []
data = file.readlines(-1)

over = []
score = []
commentry = []
string = []
flag=1
var=0
overcount=0
commOnprevPage=0
test = ""

for i in range(21):
	j=0
	small_data = data[i]
	while(j<100):
		pattern = r"(MCID=\""+str(j)+r"\">)(.*?)(</P>)"
		ext_data = re.search(pattern, small_data)
		string = []
		if ext_data is None:
			break;
		else:
			var=0
			if(len(ext_data.group(2)) >5 and overcount>0):
				if(flag==1):
					while(1):
						if(len(ext_data.group(2)) <=5 and ext_data.group(2)!=""):
							if j==0 and commOnprevPage==1 and len(ext_data.group(2))<=5:
								commentry.append([test])
								print("111111============",test)
								test=""
								commOnprevPage=0
							elif commOnprevPage==1 and len(ext_data.group(2))<=5:
								commentry.append([test])
								print("33333333333============",test)
								test=""
								commOnprevPage=0
							else:
								commentry.append(string)
							if("E" not in ext_data.group(2)):
								#j = j-1
								flag=1
								var=1
								break
							else:
								#j = j-1
								flag=0
								var=1
								break
						else:
							if j==0 and commOnprevPage==1 and len(ext_data.group(2))>5:
								commOnprevPage=0
								test += "".join(ext_data.group(2))
								print("5555555==========",test)
								string.append(test)
								test=""
							else:	
								string.append(ext_data.group(2))
								print(string)
								print("commOnprevPage =  ",commOnprevPage)
							if("|" in "".join(string)):
								var=1
								break
							else:
								None
						if var==1:
							break
						j = j+1
						pattern = r"(MCID=\""+str(j)+r"\">)(.*?)(</P>)"
						ext_data = re.search(pattern, small_data)
						if ext_data is None:
							if(string):
								commOnprevPage=1
								test = "".join(string)
								print("22222================",test)
							else:
								commOnprevPage=0
								#commentry.append(string)
							break

				while(1):
					if ext_data is None:
						break;
					#print(ext_data.group(2))
					if("." not in ext_data.group(2) and len(ext_data.group(2)) >5):
						None
					elif("." in ext_data.group(2) and len(ext_data.group(2))<=5):
						flag=1
						#j = j-1
						break
					j = j+1
					pattern = r"(MCID=\""+str(j)+r"\">)(.*?)(</P>)"
					ext_data = re.search(pattern, small_data)
					if ext_data is None:
						break;
				#commentry.append(ext_data.group(2))
			if(ext_data is None):
				break
			if(len(ext_data.group(2))<=5 and ext_data.group(2)!="" and ext_data.group(2)!=" "):
				if(j==0 or j==1 and commOnprevPage==1):
					commOnprevPage=0
					commentry.append([test])
				#	print("44444444============",test)
					test=""
				if("." not in ext_data.group(2)):
					if(len(ext_data.group(2))==1 and "D" not in ext_data.group(2) and "O" not in ext_data.group(2)):
						score.append(ext_data.group(2))
					elif("lb" not in ext_data.group(2) and "w" not in ext_data.group(2) and "nb" not in ext_data.group(2)):
						None	
					else:
						score.append(ext_data.group(2))
				else:
					x = len(ext_data.group(2))
					overcount=1
					over.append((ext_data.group(2))[:x-1])
			j=j+1

print(len(score))
print(len((over)))
print((len(commentry))
for i in range(len(commentry)):
	x = "".join(commentry[i])
	commentry[i] = x
df = pd.DataFrame(data={"Overs": over, "ScoreBoard": score,"Commentry": commentry})
df.to_csv("./Final_CSV.csv", sep=',',index=False) 
