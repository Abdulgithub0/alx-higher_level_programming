#!/usr/bin/python3
def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    best = "None"
    for key, values in a_dictionary.items():
        scorer = key
        break
    for keys, values in a_dictionary.items():
        if a_dictionary[scorer] < a_dictionary[keys]:
            scorer = keys
            best = scorer
    return best
