import json
from pprint import pprint


def menu_count(restorant):
    
    return len(restorant['menus'])
    

if __name__ == '__main__':
    restorant_json = open('problem02_data.json', encoding='UTF8')
    restorant = json.load(restorant_json)
    print(menu_count(restorant)) 
    # => 4