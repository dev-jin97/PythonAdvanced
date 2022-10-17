
"""
지도 어플리케이션에서 소요시간을 크롤링하였더니 문자열 데이터였다.
소요시간을 비교하기 위해 모두 분으로 바꾸려고 한다. 다음과 같이 시간이 입력되면 분으로 바꾸어 주는 프로그램을
작성해보자.
"""

input_str_time = input("표준 시간 입력 >> ")

transform_time = 0
transform_min = 0

for item in input_str_time.split():
    if "시간" in item:
        transform_time = int(item.replace('시간', '')) * 60
    elif "분" in item:
        transform_min = int(item.replace("분", ''))

print(transform_time + transform_min)

