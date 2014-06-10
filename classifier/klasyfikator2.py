# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs
import NaiveBayes
from Task905 import classify

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
    
    return list(set(text.split()))
        
bayes = NaiveBayes.NaiveBayes(getfeatures)


with codecs.open('featureCount.txt', 'r', encoding='utf-8') as f:
    bayes.feature_count = eval(f.read())

with codecs.open('classCount.txt', 'r', encoding='utf-8') as f:
    bayes.class_count = eval(f.read())
    
lewaki = 0;
kuce = 0;

for article in glob.glob("./artykuly/lewica/palikot/*.txt"):
    with codecs.open(article, 'r', encoding='utf-8') as f:
        clas = classify(bayes, f.read())
        if clas == "kuc":
            kuce += 1;
        else:
            lewaki += 1;

print("lewaki " + str(lewaki));
print("kuce " + str(kuce));
        

