import pandas as pd
bdf=pd.read_csv("example.csv") #This will be predefined in the user input any csv



def inputs(bdf,i):
  s=(bdf.iloc[i]['ttxt'])
  fs= open("temp.txt","w+")
  fs.write(s)
  fs=open('temp.txt',"r+")
  rd=fs.read()
  cleaned=clean(rd)
  return cleaned
  #text_file = open("sample.txt", "wt")
  #n = text_file.write(s)


def clean(btxt):    
    import re, string
    #txt= open("uH3h7NAk.txt", "r+")
    #txt= open(fname, "r+")
    #txt=txt.read()#Reading
    txt=btxt
    print(txt)
    txt=str(txt.encode(encoding = 'UTF-8',errors = 'strict')) #UTF-8 Encoding
    clean = re.sub(r"[0-9,.;@#?/&%"",(),[],!&$]+\ *", " ", txt.replace('b',''))  #Removes unncessary stuff for word vectors
    print(clean)
    s=clean
    exclude = set(string.punctuation)
    table = str.maketrans("","")
    regex = re.compile('[%s]' % re.escape(string.punctuation)) #Punctuations
    text= regex.sub('', s)
    import nltk
    #nltk.download('stopwords')
    from nltk.corpus import stopwords  #Stop Words influencing the game
    cachedStopWords = stopwords.words("english")
    text = '  '.join([word for word in text.split() if word not in cachedStopWords]).lower()
    return text



#Sends the dataframe here and parses for each documnet contained in iloc[0,1,2....n]
for i in range(len(bdf)):
  bdf.iloc[i] =inputs(bdf,i)
  



