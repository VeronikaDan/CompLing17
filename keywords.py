from sklearn.feature_extraction.text import TfidfVectorizer
import os
import json

def read_train():
    filenames = []
    dirs = os.walk('maui-semeval2010-train')
    for d in dirs:
        for f in d[2]: 
            filenames.append('maui-semeval2010-train/'+f)
    return(filenames)

def to_tfidf(filenames):
    tf = TfidfVectorizer(input='filename', analyzer='word', token_pattern=r'\b\w+-?\w+\b', ngram_range=(1, 4))
    tf.fit(filenames)
    return(tf)

def writeInJson(tf, name):
    f = open(name+'.json', 'w')
    json.dump(tf, f, indent = 2, ensure_ascii = False)
    f.close()
    

if __name__ == '__main__':
    files = read_train()
    print(files[1])
    file_texts = []
    for f in files:
        if f.endswith('txt'):
            file_texts.append(f)
    tf = to_tfidf(file_texts)
    #for key, value in tf.vocabulary_.items():
    #    print (key, value)
    #matr = tf.transform(file_texts)

