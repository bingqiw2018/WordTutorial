#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
import io
import sys
import jieba.analyse

class DictionTools(object):

    __stop_words_filename = "D:\eclipse4.8\workspace_nlp\WordTutorial\data\stop_words.txt"
    
    __dic_files = [
            "D:\eclipse4.8\workspace_nlp\WordTutorial\data\dict_words_china.txt",
            "D:\eclipse4.8\workspace_nlp\WordTutorial\data\dict_words.txt"
        ]
    
    __stopwords = []
    
    def __init__(self):
        
        sys.setrecursionlimit(1000000)
        
        for file_name in self.__dic_files:
            jieba.load_userdict(file_name.strip())
            
        self.__stopwords = self.__stopwordslist()
    
    def getDataSource(self, file_name):
        return [line.strip() for line in io.open(file_name, 'r', encoding='utf-8').readlines()]
    
    def get_stop_words(self):
        return self.__stopwords
    
    def cut(self, word_str, stop_req = True, temp_words = []):  
        
        back_str = ''
        
        if stop_req:
            back_str = self.__cut_by_stop_words(word_str)
        else:
            back_str = jieba.cut(word_str)
            
        return back_str
    
    def textrank(self, word_str, stop_req = False):
        back_str = ""
        if stop_req:
            back_str = "".join(self.__cut_by_stop_words(word_str))
            return jieba.analyse.textrank(back_str, topK=20, withWeight=True, allowPOS=())
        else:
            return jieba.analyse.textrank(word_str, topK=20, withWeight=True, allowPOS=()) 
           
    def extract_tags(self, word_str, stop_req = False):
        back_str = ""
        if stop_req:
            back_str = "".join(self.__cut_by_stop_words(word_str))
            return jieba.analyse.extract_tags(back_str, topK=20, withWeight=True, allowPOS=())
        else:
            return jieba.analyse.extract_tags(word_str, topK=20, withWeight=True, allowPOS=())    

    def add_dic_temp_words(self, temp_words = []):
        for word in temp_words:
            jieba.add_word(word)
    
    def suggest_dic_temp_words(self, temp_words = []):
        for word in temp_words:
            jieba.suggest_freq(word,tune=True)
            
    def __stopwordslist(self):
        return [line.strip() for line in io.open(self.__stop_words_filename, 'r', encoding='utf-8').readlines()]

    def __cut_by_stop_words(self,word_str):  
        
        word_seged = jieba.cut(word_str.strip())
        
        buff = ''  
        for word in word_seged:  
            if word not in self.__stopwords: 
                if word.strip() != '': 
                    buff += word  
                    buff += ' ' 
                    
        back_arr = buff.split(' ')            
        return back_arr  
