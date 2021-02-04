import string
import GetOldTweets3 as got
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 

final_words = [] 


# reading text filexyz

# print('enter the file name you want to analyse:')
# filename = input()

def nameF(file):
    print(type(file))
    text = open(file,encoding='utf-8',errors='ignore').read()

     # converting to lowercase
    text = text.lower()

     #Removing punctuations 
    cleaned_text = text.translate(str.maketrans('','',string.punctuation))
    # print(string.punctuation)

    #split them into a list
    tokenized_words=word_tokenize(cleaned_text,"english")

# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "hey", "hi","he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
                

    for word in tokenized_words:
        if word not in stopwords.words("english"):
            final_words.append(word)

#empty emotion list
    emotion_list = []

    with open('emotions.txt','r') as file:
        for line in file:
            clear_line = line.replace('\n','').replace("'","").replace(',','').strip()
            word, emotion = clear_line.split(':')
            
            if word in final_words:
                emotion_list.append(emotion)

    print(emotion_list)
    # it changes the list into a dictionary in sorted form according to its value  Counter(list)
    w = Counter(emotion_list)

    fig , ax1 = plt.subplots()
    ax1.bar(w.keys(),w.values())
    fig.autofmt_xdate();
    plt.savefig('AnalysedImage.png')
    # plt.show()

# print('file you want to analyse:\n')
# filename = input()
# nameF(filename)
# getting old tweets from tweeter     

def extractedText(text):
     # converting to lowercase
    text = text.lower()

     #Removing punctuations 
    cleaned_text = text.translate(str.maketrans('','',string.punctuation))
    # print(string.punctuation)

    #split them into a list
    tokenized_words=word_tokenize(cleaned_text,"english")

# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "hey", "hi","he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
                

    for word in tokenized_words:
        if word not in stopwords.words("english"):
            final_words.append(word)

#empty emotion list
    emotion_list = []

    with open('emotions.txt','r') as file:
        for line in file:
            clear_line = line.replace('\n','').replace("'","").replace(',','').strip()
            word, emotion = clear_line.split(':')
            
            if word in final_words:
                emotion_list.append(emotion)

    print(emotion_list)
    # it changes the list into a dictionary in sorted form according to its value  Counter(list)
    w = Counter(emotion_list)

    fig , ax1 = plt.subplots()
    ax1.bar(w.keys(),w.values())
    fig.autofmt_xdate();
    plt.savefig('AnalysedImage.png')
    # plt.show()