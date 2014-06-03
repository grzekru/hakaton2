# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs
import NaiveBayes
from Task905 import classify

def getfeatures(text):
    """Funkcja do testów."""
    return list(set(text.split()))
        
bayes = NaiveBayes.NaiveBayes(getfeatures)


with codecs.open('featureCount.txt', 'r', encoding='utf-8') as f:
    bayes.feature_count = eval(f.read())

with codecs.open('classCount.txt', 'r', encoding='utf-8') as f:
    bayes.class_count = eval(f.read())
    


print(classify(bayes, "Ten tekst zostanie sklasyfikowany jako lewicowy lub prawicowy"));


