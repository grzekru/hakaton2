# -*- coding: utf-8 -*-
'''ok'''
import Task902
import Task903

def docprob(bayes, item, cat):
    '''ok'''
    attrib = bayes.get_features(item)
    sumall = 0
    for ent in attrib:
        sumall += Task902.featprob(bayes, ent, cat)
    return Task903.catprob(bayes, cat) + sumall
