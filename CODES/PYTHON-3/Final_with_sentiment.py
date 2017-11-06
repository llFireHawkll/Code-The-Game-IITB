import json
import pandas as pd
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
  
sentiment = []
score = []
df = pd.read_csv('Final_CSV.csv')
over = df.Overs
ScoreBoard = df.ScoreBoard
Commentry = df.Commentry
Score = df.ScoreBoard
Overs = df.Overs

ScoreNew = []
CommentryNew = []
OversNew = []
for i in range(len(df)):
  if(Score[i] == 'W' or Score[i]=='6' or Score[i]=='4'):
    ScoreNew.append(Score[i])
    OversNew.append(Overs[i])
    CommentryNew.append(Commentry[i])
  if('nb' in Score[i]):
    if('w' in Score[i+1] or '4' in Score[i+1] or '6' in Score[i+1] or Score[i] >= '2'):
      ScoreNew.append(Score[i])
      OversNew.append(Overs[i])
      CommentryNew.append(Commentry[i])
  if(len(ScoreNew)>=50):
    break
if(len(ScoreNew)>=50):
	exit()
#print(len(OversNew) , len(ScoreNew) , len(CommentryNew))
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="**************",
  password="************",
  version="2017-02-27")

for i in Commentry:
  response = natural_language_understanding.analyze(
    text = i,
    features=[
      Features.Sentiment(
        )
    ]
  )

  res = response['sentiment']['document']['score']
  if res <0:
    res = -1*res
  score.append(res)
sover = []
scomm = []
sscore = []
ssenti = []
df1 = pd.DataFrame(data = {'Over' : Overs,'Score' : Score, 'Commentry' : Commentry, 'Sentiment' : score})
df1 = df1.sort_values(['Sentiment'],ascending = [0])
df1.to_csv("./Senti_Score.csv", sep=',',index=False) 
# print(len(Overs) , len(Score) , len(Commentry))
# print(len(df1))
# print(df1.head())
remain = 50 - len(OversNew)
count = 0
df1 = pd.read_csv('Senti_Score.csv')
# print(len(df1.Over))
# print(df1.Over[0] , df1.Score[0] , df1.Commentry[0])
for i in range(len(df1)):
  if count>=remain:
    break
  if df1.Commentry[i] not in CommentryNew:
    # print(df1.Over[i])
    sover.append(df1.Over[i])
    scomm.append(df1.Commentry[i])
    sscore.append(df1.Score[i])
    ssenti.append(df1.Sentiment[i])
    count = count+1
OversNew = OversNew + sover
CommentryNew = CommentryNew +scomm
ScoreNew = ScoreNew + sscore

# print(len(OversNew) , len(ScoreNew) , len(CommentryNew))
df = pd.DataFrame(data = {'Over' : OversNew,'Score' : ScoreNew , 'Commentry' : CommentryNew})
df = df.sort_values(['Over'])
df.to_csv("./Top50Events.csv", sep=',',index=False) 
