# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs
import NaiveBayes
from Task905 import classify

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
    
    return list(set(text.split()))
        
bayes = NaiveBayes.NaiveBayes(getfeatures)


with codecs.open('featureCount.txt', 'r', encoding='utf-8') as f:
    bayes.feature_count = eval(f.read())

with codecs.open('classCount.txt', 'r', encoding='utf-8') as f:
    bayes.class_count = eval(f.read())
    


print(classify(bayes, "Każdy polak zasługuje na honor"));
print(classify(bayes, "Lewak to nie człowiek i zasługuje na chłostę"));
print(classify(bayes, "Kobiety i mężczyźni są równi"));
print(classify(bayes, "Polskę należy bronić przed kościołem"));

