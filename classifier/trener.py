# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs

import NaiveBayes
from Task901 import train


kucPaths = ["./artykuly/prawica/JKM/*.txt", "./artykuly/prawica/holocher/*.txt"]
lewakPaths = ["./artykuly/lewica/rozbrat/*.txt", "./artykuly/lewica/palikot/*.txt"]




def getfeatures(text):
    """Funkcja do testów."""
    return list(set(text.split()))
        
def trainArticleSet(bayes, paths, category):
    for path in paths:
        for article in glob.glob(path):
            with codecs.open(article, 'r', encoding='utf-8') as f:
                train(bayes, f.read(), category)
    return bayes

bayes = NaiveBayes.NaiveBayes(getfeatures)

bayes = trainArticleSet(bayes, lewakPaths, "lewak");

bayes = trainArticleSet(bayes, kucPaths, "kuc");

outFile = open('featureCount.txt', 'wb')
buff = str(bayes.feature_count)
outFile.write(bytes(buff, 'UTF-8'))
outFile.close()

outFile = open('classCount.txt', 'wb')
buff = str(bayes.class_count)
outFile.write(bytes(buff, 'UTF-8'))
outFile.close()
