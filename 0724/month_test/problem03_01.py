import json


def turn(temperatures):
    temp_dict = {
        'maximum': [],
        'minimum': [],
    }

    for temp in temperatures:
        temp_dict['maximum'].append(temp[0])
        temp_dict['minimum'].append(temp[1])

    return temp_dict
    
    
if __name__ == '__main__':
    temperatures_json = open('problem03_data.json', encoding='UTF8')
    temperatures = json.load(temperatures_json)
    print(turn(temperatures)) 
    # =>
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }