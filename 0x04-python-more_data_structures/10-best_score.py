#!/usr/bin/python3
def best_score(a_dictionary):
    best = "none"
    for key, value in a_dictionary.items():
        max_score = value
        break
    for key, value in a_dictionary.items():
        if max_score < value:
            max_score = value
            best = key
        else:
            if (best == "none"):
                best = "None"
    return (best)
