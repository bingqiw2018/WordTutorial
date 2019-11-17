#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
from word.DictionTool import DictionTools
import jieba

def test1():
    file_name = "dic.txt"
    jieba.load_userdict(file_name)
    
    name = "中医按摩"
    print("/".join(jieba.cut(name)))
 
def test2():    
    tools = DictionTools()
    tools.add_dic_temp_words(['你知道','你喜欢'])
    list_title = tools.getDataSource("D:\AppData\Local\NLP\data\DOC_004.txt")
    
    for word_str in list_title:
        print(word_str)
        new_word = tools.remove_word(word_str) 
        print("[c]:"+"/".join(tools.cut(new_word))+"")
#         print("[e]:"+"/".join(item[0] for item in tools.extract_tags(new_word))+"")
        print("[e]:"+"/".join(item[0] for item in tools.extract_tags(new_word,True))+"\n")   

    
if __name__ == '__main__':
    test2()

        
    
