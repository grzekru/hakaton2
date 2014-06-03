# -*- coding: utf-8 -*-
'''asd'''
import Task904

def classify(bayes, item):
    '''asdfasd'''
    wmax = None
    cmax = None
    for category in bayes.class_count:
        result = Task904.docprob(bayes, item, category)
        if wmax is None:
            wmax = result
            cmax = category
        else:
            if result > wmax:
                wmax = result
                cmax = category
    return cmax
