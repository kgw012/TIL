def is_user_data_valid(user_data):
    
    return bool(user_data['id']) and bool(user_data['password'])


if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jung',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True