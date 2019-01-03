#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
from word.DictionTool import DictionTools
from word.ClassTool import ClassTools

def jieba_for_word():
    dt = DictionTools()
    dt.add_dic_temp_words(['保健茶饮'])
    
    list_title = dt.getDataSource("D:\eclipse4.8\workspace_nlp\WordTutorial\data\DOC_001.txt")
    
    for word_str in list_title:
        print(word_str)
        print("/".join(dt.cut(word_str))+"\n")
    
#     print("[]:"+"/".join( item[0] for item in dt.extract_tags(testSentence)))

def class_word():
    
    diction = DictionTools()
    diction.suggest_dic_temp_words([u'沙瑞金',u'易学习',u'王大路',u'京州',u'欧阳菁',('和', '易')])
    classTools = ClassTools(diction)
    words = classTools.getDataSource("D:\eclipse4.8\workspace_nlp\WordTutorial\data\DOC_001.txt")
    docres, components = classTools.LatentDirichletAllocation(2,words)
    print(u"主题分布：")   
    print(docres)
    print(components)  
    
if __name__ == '__main__':
    class_word()
    
    
