#!/usr/bin/python3
def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    best = ''
    for key in a_dictionary.keys():
        scorer = key
        break
    for keys, values in a_dictionary.items():
        if a_dictionary[scorer] < a_dictionary[keys]:
            scorer = keys
            best = scorer
    return best
