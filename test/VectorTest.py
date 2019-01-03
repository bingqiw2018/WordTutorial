#coding=utf-8 
'''
Created on Jan 2, 2019

@author: g802622
'''
from sklearn.feature_extraction.text import CountVectorizer
from word.DictionTool import DictionTools
from sklearn.decomposition import LatentDirichletAllocation

def vectorforMatrix():
    corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
    ]

    count_vec=CountVectorizer(stop_words=None)
    X = count_vec.fit_transform(corpus)
    print X
    print X.toarray()
    print(count_vec.get_feature_names())
    print '\nvocabulary list:\n\n',count_vec.vocabulary_

    print 'get term id:',count_vec.vocabulary_['document']

def testChinese():
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'沙瑞金',u'易学习',u'王大路',u'京州',u'欧阳菁',('和', '易')])
    words = dictionTools.getDataSource("D:\AppData\Local\NLP\data\DOC_001.txt")
    
    for word_str in words:
        print(word_str)
        print("/".join(dictionTools.cut(word_str))+"\n")
    
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    for key, value in count_vec.vocabulary_.items():
        print key,value

def class_word():
    
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'沙瑞金',u'易学习',u'王大路',u'京州',u'欧阳菁',('和', '易')])
    words = dictionTools.getDataSource("D:\AppData\Local\NLP\data\DOC_001.txt")
    
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    print cntTf.shape,cntTf.toarray()
    
    lda = LatentDirichletAllocation(n_components=2,learning_offset=50.,random_state=0)
        
    docres = lda.fit_transform(cntTf)
    
    print docres
    
    print lda.components_ 
    
def class_zhongyi():
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'中医按摩'])
    words = dictionTools.getDataSource("D:\AppData\Local\NLP\data\DOC_002.txt")
    
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
#     print cntTf.shape,cntTf.toarray()
    
    lda = LatentDirichletAllocation(n_components=2,learning_offset=50.,random_state=0)
        
    docres = lda.fit_transform(cntTf)
    
    for i in range(len(words)):
        print docres[i],words[i], "/".join( word[0] for word in dictionTools.extract_tags(words[i]))
    
#     print lda.components_ 
        
        
if __name__ == '__main__':
    class_zhongyi()
