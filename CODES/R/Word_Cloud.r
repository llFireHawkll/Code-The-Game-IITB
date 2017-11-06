library("tm")
library("SnowballC")
library("wordcloud2")
library("RColorBrewer")
df = read.csv("Final_CSV.csv")
df1 = df['Commentry']
for (i in df1)
{
  i <- Corpus(VectorSource(i))
  i <- tm_map(i, removeWords, stopwords("english"))
  i <- tm_map(i, stemDocument)
  dtm <- TermDocumentMatrix(i)
  m <- as.matrix(dtm)
  v <- sort(rowSums(m),decreasing=TRUE)
  d <- data.frame(word = names(v),freq=v)  
}
wordcloud2(data = d)

