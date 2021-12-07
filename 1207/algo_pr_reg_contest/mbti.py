class Student:
    def __init__(self, mbti:str, blood:str, power:int):
        self.mbti = mbti
        self.blood = blood
        self.power = power

'''
[팀 구성 조건]

같은 MBTI끼리는 팀을 구성할 수 없다.

‘I’끼리는 팀을 구성할 수 없다.

‘T’는 반드시 ‘P’와 팀을 구성하여야 한다.

O형은 O형이 아닌 팀원과만 팀을 이룰 수 있다

반드시 모든 학생이 팀을 구성하여야 한다.
'''

def check(s1, s2):
    flag1 = not (s1.mbti == s2.mbti)
    flag2 = not (s1.mbti[0] == 'I' and s2.mbti[0] == 'I')
    flag3 = not ((s1.mbti[2] == 'T' and s2.mbti[3] == 'J') or (s1.mbti[3] == 'J' and s2.mbti[2] == 'T'))
    flag4 = not (s1.blood == 'O' and s2.blood == 'O')

    return (flag1 and flag2 and flag3 and flag4)


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        students = []
        for n in range(N):
            mbti, blood, power = input().split()
            students.append(Student(mbti, blood, int(power)))
        
        
