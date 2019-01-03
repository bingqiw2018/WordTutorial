'''
Created on Dec 29, 2018

@author: g802622
'''
from DictionTool import DictionTools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class ClassTools(object):
    
    __diction = None
    
    __vector = None
    
    def __init__(self, diction = DictionTools()):
        self.__diction = diction
        self.__vector = CountVectorizer()
    
    def getDataSource(self, file_name):
        return self.__diction.getDataSource(file_name)
    
    def LatentDirichletAllocation(self, topic, words):
        
        lda = LatentDirichletAllocation(n_components=topic,learning_offset=50.,random_state=0)
        
        cntTf = self.__vector.fit_transform(words)
        
        docres = lda.fit_transform(cntTf)
        
        return docres, lda.components_
    
    
    