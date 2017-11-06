# Code-The-Game-IITB


STEPS TO EXECUTE THE PROGRAM AND GENERATE THE REQUIRED RESULT

### ALL THE CODES FOR PART-1 AND PART-2 USES PYTHON-2 TO RUN AND THEY WILL NOT WORK WITH PYTHON-3 ###
PART - 1:

In this you are required to install the PDFMINER package for python, which is used to convert the given pdf to text document.
So what you need to do:

1). Unzip the pdfminer-20140328.tar.
2). Use the cd command like this "cd pdfminer-20140328" and go into this directory.
3). Now you have to run the python file PdfMinerInstaller.py using this command in the shell "python PdfMinerInstaller.py" 


PART-2:

In this you are required to run the python file PdfToTxt.py which will convert the given PDF to TXT which will be used to
perform the following analysis.
In the shell run this command "python PdfToTxt.py", and after running this a text file will be generated called test.txt

### ALL THE CODES IN THE FILE WILL RUN ONLY WHEN THEY ARE PUT IN THE SAME DIRECTORY ###



### ALL THE CODES FOR PART-3 WILL RUN ON PYTHON-3 ###
PART-3:

In this part we will use the following python scripts to generate the particular result required for the analysis.

1). Run this script in shell using command "python Commentary_extract.py" , now this script 'Commentary_extract.py' will generate Commentary.csv file which contains Commentary corresponding to time as given in the pdf before the match starts.

2). Run this script in shell using command "python Final_PdfToCsv.py" , now this script 'Final_PdfToCsv.py' will generate 'Final_CSV.csv' which includes the runs, 
commentary corresponding to each ball.

3). Run this script in shell using command "python end_of_over.py" , now this script 'end_of_over.py' will generate 'EOO_Summary.csv' which contains overwise analysis.

4). Run this script in shell using command "python Final_with_sentiment.py" , now this script 'Final_with_sentiment.py' will generate 'Top50Events.csv', which includes final top 50 events selected, and 'Senti_Score.csv' which contains the sentiment score of commentary of each ball.

5). Run this script in shell using command "python score_vs_ball.py" , now this script 'score_vs_ball.py' will generate these graphs 'runs each ball.png' and 'runs in over.png'

6). And the last file 'Word_Cloud.r' will run on any r-console and this will generate 'wordcloud.png'.
