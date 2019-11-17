#coding=utf-8 
'''
Created on Dec 28, 2018

@author: g802622
'''
import io
import sys
import jieba.analyse

class DictionTools(object):

    __stop_words_filename = "D:\AppData\Local\NLP\data\stop_words.txt"
    
    #stop words diction 
    __dic_files = [
            "D:\AppData\Local\NLP\data\dict_words_china.txt",
            "D:\AppData\Local\NLP\data\dict_words.txt"
        ]
    
    __stopwords = []
    
    def __init__(self):
        
        sys.setrecursionlimit(1000000)
        
        for file_name in self.__dic_files:
            jieba.load_userdict(file_name.strip())
            
        self.__stopwords = self.__stopwordslist()
    
    #sentences from file 
    def getDataSource(self, file_name):
        return [line.strip() for line in io.open(file_name, 'r', encoding='utf-8').readlines()]
    
    # remove the word
    def remove_word(self, word):
        arr = ['安迪']
        result = []
        for item in self.cut(word, True):
            if item not in arr:
                result.append(item)
        
        return "".join(result)
        
    #fetch the stop words
    def get_stop_words(self):
        return self.__stopwords
    
    #divide the sentence into words
    def cut(self, word_str, stop_req = True):  
        
        back_str = ''
        
        if stop_req:
            back_str = self.__cut_by_stop_words(word_str)
        else:
            back_str = jieba.cut(word_str)
            
        return back_str
    
    # 基于TextRank算法的关键词提取
    # jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=(‘ns’, ‘n’, ‘vn’, ‘v’)) 直接使用，接口相同，注意默认过滤词性。
    # jieba.analyse.TextRank() 新建自定义 TextRank 实例 
    # –基本思想： 
    # 1，将待抽取关键词的文本进行分词 
    # 2，以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图 
    # 3，计算图中节点的PageRank，注意是无向带权图
    # 主要思想：将文本内容进行分词，并加权，主要目的是突出文本的主题
    # 这里要注意加权策略       
    # 关注词与词之间的关系，如果词频相同，就不能记入主题列表，对已经划分主题的，进一步区分类型的较好
    def textrank(self, word_str, stop_req = False):
        back_str = ""
        if stop_req:
            back_str = "".join(self.__cut_by_stop_words(word_str))
            return jieba.analyse.textrank(back_str, topK=20, withWeight=True, allowPOS=())
        else:
            return jieba.analyse.textrank(word_str, topK=20, withWeight=True, allowPOS=()) 
    
    # 基于TF-IDF算法的关键词抽取
    # TFIDF的主要思想是：如果某个词或短语在一篇文章中出现的频率TF高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类。
    # jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=()) 
    # –sentence 为待提取的文本 
    # –topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20 
    # –withWeight 为是否一并返回关键词权重值，默认值为 False 
    # –allowPOS 仅包括指定词性的词，默认值为空，即不筛选
    # 主要思想：将文本内容进行分词，并加权，主要目的是突出文本的主题
    # 这里要注意加权策略
    # 1、主语、定语一般为名词，权重高，
    # 2、相同关键字的词频越高，权重就越高；       
    def extract_tags(self, word_str, stop_req = False):
        back_str = ""
        if stop_req:
            back_str = "".join(self.__cut_by_stop_words(word_str))
            return jieba.analyse.extract_tags(back_str, topK=20, withWeight=True, allowPOS=('nt','nz','nr','ns', 'n', 'vn', 'v','j'))
        else:
            return jieba.analyse.extract_tags(word_str, topK=20, withWeight=True, allowPOS=('nt','nz','nr','ns', 'n', 'vn', 'v','j'))    
    
    #add customer diction by temporary definition
    def add_dic_temp_words(self, temp_words = []):
        for word in temp_words:
            jieba.add_word(word)
            
    #add word weight by temporary definition
    def suggest_dic_temp_words(self, temp_words = []):
        for word in temp_words:
            jieba.suggest_freq(word,tune=True)
    
    #get、sentence list from data file       
    def __stopwordslist(self):
        stpwrdlst = [line.strip() for line in io.open(self.__stop_words_filename, 'r', encoding='utf-8').readlines()]
        return stpwrdlst

    #divide the sentence by stop word diction
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

