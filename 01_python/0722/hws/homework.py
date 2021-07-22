# 1. 이름 공간(Namespace)

# LEGB 순서
# Local scope
# Enclosed scope
# Global scope
# Built-in scope


# 2. 매개변수와 인자, 그리고 반환

# (1) 함수는 오직 하나의 객체만 반환할 수 있으므로 'return a, b'와
# 같이 쓸 수 없다.
# (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
# (3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며,
# 전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
# (4) 가변 인자를 설정할 때는 인자 앞에 * 을 붙이고, 이 때는 함수
# 내에서 tuple로 처리 된다.

# 1 예시

def test_func():
    return 1, 2

print(test_func())
print(type(test_func()))


# 3. 재귀 함수

# 장점 1) 코드의 가독성이 반복문보다 더 높다.
# 장점 2) 로직을 표현하기 쉬워질 때가 있다.
# 단점 1) 시간복잡도가 높아지기 쉽다.
# 단점 2) 메모리를 많이 잡아먹는다.