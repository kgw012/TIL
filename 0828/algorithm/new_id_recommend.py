def stage1(new_id):
    tmp_id = new_id.lower()
    return tmp_id


def stage2(new_id):
    tmp_id = ''
    for c in new_id:
        if (c.islower() or c.isdigit() or c == '-' or c == '_' or c == '.'):
            tmp_id += c
    return tmp_id


def stage3(new_id):
    tmp_id = ''
    i = 0
    while i < len(new_id):
        if new_id[i] == '.':
            tmp_id += '.'
            j = i + 1
            while j < len(new_id) and new_id[j] == '.':
                j += 1
            i = j
        else:
            tmp_id += new_id[i]
            i += 1
    
    return tmp_id


def stage4(new_id):
    return new_id.strip('.')


def stage5(new_id):
    if len(new_id) == 0:
        new_id = 'a'

    return new_id


def stage6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
        
    return new_id


def stage7(new_id):
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id

def solution(new_id):

    new_id = stage1(new_id)
    new_id = stage2(new_id)
    new_id = stage3(new_id)
    new_id = stage4(new_id)
    new_id = stage5(new_id)
    new_id = stage6(new_id)
    new_id = stage7(new_id)

    return new_id


if __name__ == '__main__':
    new_id = '...!@BaT#*..y.abcdefghijklm'
    print(solution(new_id))