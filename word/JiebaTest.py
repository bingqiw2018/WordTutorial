#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
from word.DictionTool import DictionTools

if __name__ == '__main__':
    
    dt = DictionTools()
    dt.add_dic_temp_words(['保健茶饮'])
    
    list_title = dt.getDataSource("D:\AppData\Local\NLP\DOC_001.txt")
    
    for word_str in list_title:
        print(word_str)
        print("/".join(dt.cut(word_str))+"\n")
    
#     print("[]:"+"/".join( item[0] for item in dt.extract_tags(testSentence)))
    
