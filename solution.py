import re
import pandas as pd 

myfile = open("Input", "r")
contents = myfile.read()
myfile.close()

quesans=re.sub(r'(.*[?])',r'##\1@@',contents).split("##")

questions=[]
answers=[]
for i in range(1, len(quesans)):
    questions.append(quesans[i].split("@@")[0])
    answers.append(quesans[i].split("@@")[1])
	


df = pd.DataFrame(list(zip(questions, answers)), columns =['Questions', 'Answers']) 

compression_opts = dict(method='zip', archive_name='out.csv')
df.to_csv('out.zip', index=False, compression=compression_opts)

