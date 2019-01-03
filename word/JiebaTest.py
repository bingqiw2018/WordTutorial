#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
from word.DictionTool import DictionTools

if __name__ == '__main__':
    
    tools = DictionTools()
    tools.add_dic_temp_words(['保健茶饮'])
    
    list_title = tools.getDataSource("D:\AppData\Local\NLP\DOC_001.txt")
    
    for word_str in list_title:
        print(word_str)
        print("[c]:"+"/".join(tools.cut(word_str))+"")
        print("[e]:"+"/".join(item[0] for item in tools.extract_tags(word_str))+"")
        print("[e]:"+"/".join(item[0] for item in tools.extract_tags(word_str,True))+"\n")
        
    
