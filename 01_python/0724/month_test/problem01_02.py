import json


def over(scores):
    cnt = 0
    for score in scores:
        if score >= 60:
            cnt += 1
    
    return cnt


if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(over(scores)) 
    # => 3