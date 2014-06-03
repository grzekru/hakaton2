#!/usr/bin/python # -*- coding: utf-8 -*-

'''Task803'''

import math

def catprob(bayes, category):
    '''catprob'''

    category = float(bayes.class_count.get(category, 0))
    categories_all = float(sum(bayes.class_count.values()))

    if category == 0:
        return -1e300

    return math.log(category/categories_all)
