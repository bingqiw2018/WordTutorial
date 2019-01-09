#coding=utf-8 
'''
Created on Jan 2, 2019

@author: g802622
'''
from sklearn.feature_extraction.text import CountVectorizer
from word.DictionTool import DictionTools
from sklearn.decomposition import LatentDirichletAllocation

from config.Config import Location as loc

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
    words = dictionTools.getDataSource(loc.data_file+"DOC_001.txt")
    
    for word_str in words:
        print(word_str)
        print("/".join(dictionTools.cut(word_str))+"\n")
    
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    print cntTf 
    print cntTf.toarray()

    for key, value in count_vec.vocabulary_.items():
        print key,value

def findKey(index, vocabulary):
    result = None
    
    for key , value in vocabulary.items():
        if value == index:
            result = key
            break
        
    return result

def class_word():
    
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'沙瑞金',u'易学习',u'王大路',u'京州',u'欧阳菁',('和', '易')])
    words = dictionTools.getDataSource(loc.data_file+"DOC_001.txt")
    
    for word_str in words:
        print("/".join(word[0] for word in dictionTools.extract_tags(word_str)))
        
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    print cntTf.shape,cntTf.toarray()
    
    lda = LatentDirichletAllocation(n_components=2,learning_offset=50.,random_state=0)
        
    docres = lda.fit_transform(cntTf)
    
    print docres
    
#     print lda.components_ 
    
    for x in range(len(lda.components_)) :
        print 'no ', x
        liss = lda.components_[x]
#         print liss
        
        val_str = ""
        for y in range(len(liss)):
            val = liss[y]
            key = findKey(y,count_vec.vocabulary_)            
            if val > 1.0:
                val_str = val_str + key + ","
        
        print "/".join(v_tr[0] for v_tr in dictionTools.extract_tags(val_str))
                
    '''
    This test get the target to confirm that jieba_extract_tag is available for short sentence classification 
    '''
def find_max_index(item,key_length,max_num):    
    index = -1
    for i in range(key_length):
        if item[i] > max_num:
            index = i
            break   
    return index

def doClassManager(docres, words, dictionTools, key_length, max_num):
    classDiction = []
    count = 0
    for i in range(key_length):
        classDiction.append(0)
    
    for item_index in range(len(docres)):
        item = docres[item_index]
        
        index = find_max_index(item,key_length,max_num)
        
        print index,'\t', "/".join(dic[0] for dic in dictionTools.extract_tags(words[item_index])),'\t',words[item_index]
        
        if index > -1 :       
            classDiction[index] = classDiction[index] + 1
            count = count +1 
            
    print 'count',count*100/len(docres),'%'        
    return classDiction           
        
        
                
def class_zhongyi():
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'中医按摩'])
    words = dictionTools.getDataSource(loc.data_file+"DOC_003.txt")
    print 'words size:',len(words)
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    print 'cnt tf allocation:',cntTf.shape,len(count_vec.vocabulary_.items())
    print cntTf.toarray()
    print 'vocabulary:'
    for key, value in count_vec.vocabulary_.items():
        print key,value
#     print cntTf.shape,cntTf.toarray()
    key_length = 2
    max_num = 0.4
    lda = LatentDirichletAllocation(n_components=key_length,learning_offset=50.,random_state=0)
        
    docres = lda.fit_transform(cntTf)
    #     print lda.components_ 
    classMap = doClassManager(docres, words, dictionTools, key_length, max_num)
    print classMap      

def topic_keywords():
    dictionTools = DictionTools()
    dictionTools.suggest_dic_temp_words([u'沙瑞金',u'易学习',u'王大路',u'京州',u'欧阳菁',('和', '易')])
    words = dictionTools.getDataSource(loc.data_file+"DOC_003.txt")
    
    count_vec=CountVectorizer(stop_words=None)
    cntTf = count_vec.fit_transform(words)
    
    key_size = 3
    lda = LatentDirichletAllocation(n_components=key_size,learning_offset=50.,random_state=0)
        
    docres = lda.fit_transform(cntTf)
    max_num = 1.0
    print 'max_num:',max_num,'key_size:',key_size
    
    print 'doc topic allocation:'
    print docres
    
    print 'topic words allocation:'
    print lda.components_
    
    print 'topic key words allocation:'
    
    for x in range(len(lda.components_)) :
        liss = lda.components_[x]
        val_str = ""
        for y in range(len(liss)):
            val = liss[y]
            key = findKey(y,count_vec.vocabulary_)            
            if val > max_num:
                val_str = val_str + key + ","
        print x, "/".join(v_tr[0] for v_tr in dictionTools.extract_tags(val_str))

if __name__ == '__main__':
    topic_keywords()
