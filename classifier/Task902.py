# -*- coding: utf-8 -*-
'''df'''
import math

def featprob(bayes, feature, category):
    '''df'''
    if category not in bayes.class_count:
        return -1e300
    if (feature, category) not in bayes.feature_count:
        wynik = (math.log(float(0.001)/float(bayes.class_count[category])))
        return wynik
    wynik = float(bayes.feature_count[(feature, category)])
    wynik = math.log(wynik/float(bayes.class_count[category]))
    return wynik
