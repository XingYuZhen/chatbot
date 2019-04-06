from tkinter import *
import tkinter as tk
from textblob import TextBlob
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import wordnet

TK = Tk()
TK.geometry("400x400")
var = StringVar()
label = Label( TK, textvariable=var, relief=RAISED )
var.set("These are the sentences in my dataset,please have a look\n")
label.pack()

t = tk.Text(TK,height=2)
t.pack()

TK.mainloop()


#initialize our chat sentences
data={
'major':['math','art','physics','computer science'],
'professor':['YONG GAO','FATEMEH FARD','MOHAMMAD KHALAD HASAN','BOWEN HUI','APURVA NARAYAN'],
'birthday':['october 10th 2000','today,june 17th 1997'],
'food':['pudding','cake','spaghetti','Kung pao chicken'],
'drink':['blood','7 up','Pepsi','orange juice'],
'sport':['soccer','badminton','basketball','archery'],
'color':['red','black','green','yellow'],
'weather':['sunny','snowy','rainy'],
'breakfast':['burger','cereal','corn','bread'],
'homework':['I haven''t finished it yet','Yesterday','uhhh, let''s change a topic'],
'sleep':['at 12:00 pm','at 3:00 am','I have sleep disorder yesterday...'],
'gym':['last month','yesterday','a week ago, I guess....'],
'class':['no, I am a good student','uhh, maybe.''I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'homework':['about 10 hours','about 2 hours'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
'math':'steve',
'art':'Ronny',
'drama':'Abie',
'CS':'Aron',
'Social':'Aaron',
'History':'summer',
'YONG GAO':'Ph.D. University of Alberta',
'FATEMEH FARD':'Ph.D. University of Calgary  ',
'MOHAMMAD KHALAD HASAN':'Ph.D. University of Manitoba',
'BOWEN HUI':'Ph.D. University of Toronto',
'APURVA NARAYAN':'Ph.D. University of Waterloo',
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['vancouver','ontario'],
'game':'LOL',
'Car':'Audi',
'coffee':['yesterday'],

}
synonyms = []
for syn in wordnet.synsets("major"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())

synonyms1 = []
for syn in wordnet.synsets("professor"):
    for lm in syn.lemmas():
             synonyms1.append(lm.name())
             
synonyms2 = []
for syn in wordnet.synsets("birthday"):
    for lm in syn.lemmas():
             synonyms2.append(lm.name())

synonyms3 = []
for syn in wordnet.synsets("food"):
    for lm in syn.lemmas():
             synonyms3.append(lm.name())
             
synonyms4 = []
for syn in wordnet.synsets("drink"):
    for lm in syn.lemmas():
             synonyms4.append(lm.name())             

synonyms5 = []
for syn in wordnet.synsets("sport"):
    for lm in syn.lemmas():
             synonyms5.append(lm.name())
             
stemmer_lancaster = LancasterStemmer()

dataKey=list(data.keys())
play = True
print(data)
print("\n")
number = 0

dataKey2 =[]

for word in dataKey:
    stemmed_word = stemmer_lancaster.stem(word)
    dataKey2.append(stemmed_word)


answer=input("Hi, I am chatBot\n")
while answer!="HI" and answer!="hi":
    print("I can not answer your question, please try again")
    answer=input("Hi, I am chatBot\n")

#ask user input       
name=input("What is your name\n")
print("Nice to meet you "+name+"\n")
print("Ask me some questions "+name+"\n")
#print("if you do not know what to ask, type help")
answer = input("if you do not know what to ask, type help")
if answer=="help":
    print(data.keys())
print("\n")
print('here is a sample question:what''s your major\n')

while play == True:
    question=input("What you want to ask")

    blob = TextBlob(question)
    blob
    blob.sentences
    print(blob.sentiment)

    question_new = nltk.word_tokenize(question)
    tokens = nltk.pos_tag(question_new)

    print("Parts of Speech:", tokens)

    if tokens !=[(question,'NNP')] and tokens !=[(question,'JJ')] and tokens !=[(question,'NN')]:
        print("Please fill in the correct statement containing the noun")
        play = True

    else:
    
        if question in dataKey2 :
            number = dataKey2.index(question)
            print((data[dataKey[number]])[0])
            play = True
        

        elif question in dataKey :
            print((data[question])[0])
            play = True
        

        elif question in synonyms :
            print((data[dataKey[0]])[0])
            play = True
        

        elif question in synonyms1 :
            print((data[dataKey[1]])[0])
            play = True
        

        elif question in synonyms2 :
            print((data[dataKey[2]])[0])
            play = True
        
        elif question in synonyms3 :
            print((data[dataKey[3]])[0])
            play = True

        elif question in synonyms4 :
            print((data[dataKey[4]])[0])
            play = True

        elif question in synonyms5 :
            print((data[dataKey[5]])[0])
            play = True

        elif question == "stop":
            play = False
        else: 
            print("I can not understand the question")
            play = True
            
#play=True

#while play==True:
   
#play=input("Do you still want to play ?")   
 #question=input("What you want to ask")

