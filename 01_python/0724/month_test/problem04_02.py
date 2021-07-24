def is_id_valid(user_data):
    
    char = ord(user_data['id'][-1])
    if char < ord('0') or char > ord('9'):
        return False
    else:
        return True


if __name__ == '__main__':
    user_data1 = {
        'id': 'jung5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kim!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False