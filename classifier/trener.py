# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs

import NaiveBayes
from Task901 import train


kucPaths = ["./artykuly/prawica/JKM/*.txt", "./artykuly/prawica/holocher/*.txt"]
lewakPaths = ["./artykuly/lewica/rozbrat/*.txt", "./artykuly/lewica/palikot/*.txt"]

def recursive_glob(rootdir='.', suffix=''):
    return [os.path.join(rootdir, filename)
            for rootdir, dirnames, filenames in os.walk(rootdir)
            for filename in filenames if filename.endswith(suffix)]


def getfeatures(text):
    """Funkcja do testów."""
    text = text.lower();
    text = re.sub("[\?\!\.\,\:\;$\'\"„”_\(\)\[\]…]", " ", text);
    text = text.replace("ó", "o");
    text = text.replace("ą", "a");
    text = text.replace("ś", "s");
    text = text.replace("ć", "c");
    text = text.replace("ź", "z");
    text = text.replace("ż", "z");
    text = text.replace("ł", "l");
    text = text.replace("ę", "e");
    
    return list(text.split())
        
def trainArticleSet(bayes, paths, category):
    for path in paths:
        for article in glob.glob(path):
            with codecs.open(article, 'r', encoding='utf-8') as f:
                train(bayes, f.read(), category)
    return bayes

bayes = NaiveBayes.NaiveBayes(getfeatures)

'''bayes = trainArticleSet(bayes, lewakPaths, "lew");'''
bayes = trainArticleSet(bayes, recursive_glob("./artykuly/lewica", ".txt"), "lew");
bayes = trainArticleSet(bayes, recursive_glob("./artykuly/prawica", ".txt"), "kuc");

"""bayes = trainArticleSet(bayes, recursive_glob("./artykuly/prawica/nczas", "*.txt"), "kuc");
"""
outFile = open('featureCount.txt', 'wb')
buff = str(bayes.feature_count)
outFile.write(bytes(buff, 'UTF-8'))
outFile.close()

outFile = open('classCount.txt', 'wb')
buff = str(bayes.class_count)
outFile.write(bytes(buff, 'UTF-8'))
outFile.close()
