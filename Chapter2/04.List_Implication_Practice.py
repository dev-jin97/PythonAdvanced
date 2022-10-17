
# Let's practice

"""
리스트 내포를 사용해서 word_list에 들어 있는 문자열 중 첫 글자가 a인 것만 뽑아서 리스트로 만드세요.
"""
import glob

before_list = ["apple", "watch", "apolo", "star", "abocado"]

after_list = [i for i in before_list if i[0] == "a"]

print(after_list)


"""
리스트 내포를 사용해서 다음과 같이 변경해보자.
"""

before_list = ["오메가3", None, "비타민c500", None, "홍삼절편"]

after_list = [i if i is not None else '' for i in before_list]
print(after_list)
