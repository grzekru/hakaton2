# -*- coding: utf-8 -*-

def train(bayes, item, cat):

    cechy = bayes.get_features(item)
    if cat not in bayes.class_count:
        bayes.class_count[cat] = 0
    bayes.class_count[cat] += 1

    for cecha in cechy:
        if (cecha, cat) not in bayes.feature_count:
            bayes.feature_count[(cecha, cat)] = 0
        bayes.feature_count[(cecha, cat)] += 1
