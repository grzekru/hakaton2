#!/usr/bin/python # -*- coding: utf-8 -*-

''' Tfg '''

def train(bayes, item, cat):

    ''' fg '''

    item = [(x, cat) for x in set(item.split())]

    for ent in item:
        bayes.feature_count[ent] = bayes.feature_count.get(ent, 0) + 1

    bayes.class_count[cat] = bayes.class_count.get(cat, 0) + 1
