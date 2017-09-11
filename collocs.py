import os
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def make_dic():
    with open('rus-wikipedia-sample-companies.txt', encoding='utf-8') as f:
        texts = f.readlines()
    dic = {}
    word_lists = []
    for t in texts:
        words = t.split()
        norms = []
        for w in words:
            w = w.strip('.,:!?/-*+=";()').lower()
            p = morph.parse(w)[0]
            norm = p.normal_form
            if norm in dic:
                dic[norm] +=1
            else:
                dic[norm] = 1
            norms.append(norm)
        if 'apple' in norms:
            word_lists.append(norms)
    #bigrams = get_bigrams(word_lists)
    return(dic) 


def get_bigrams(word_lists):
    bigrams = {}
    for text in word_lists:        
        for i in range(len(text)-1):
            if text[i] == 'apple' :
                bigrams = add_bi(text[i+1], bigrams)
            elif text[i+1] == 'apple':
                bigrams = add_bi(text[i], bigrams)
                
    return(bigrams)


def add_bi(w, bigrams):
    if w in bigrams:
        bigrams[w] += 1
    else:
        bigrams[w] = 1
    return(bigrams)

def write_dic(dic):
    f = open('apple.tsv', 'w', encoding = 'utf-8')
    for k,v in dic.items():
        if k != 'apple':
            f.write('Apple' + '/t' + k + '/t' + str(dic['apple']) + '/t' + str(v)) 
    f.close()


if __name__ == '__main__':
    dic = make_dic()
    write_dic(dic)


    


