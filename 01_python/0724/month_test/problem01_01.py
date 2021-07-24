import json


def max_score(scores):
    max_score = scores[0]
    for score in scores:
        if max_score < score:
            max_score = score
    
    return max_score


if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(max_score(scores)) 
    # => 90