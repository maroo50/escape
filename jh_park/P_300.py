'''
1. print 기초

''' 
#  1 
print("Hello, World!")

# 2
print("Mary's cosmeitcs")

# 3 

print('신씨가 소리질렀다. "도둑이야".')

# 4

print("C:\Windows")

# 5
print("안녕하세요. \n만나서\t\t반갑습니다.")

# 6
print("오늘은", "일요일") 

# 7
print("naver", "kakao", "sk", "samsung", sep=";")

# 8
print("naver", "kakao", "sk", "samsung", sep="/")

# 9
print("first\n"), print("second")
#print("first", end=""); print("second")

# 10
print("5/3= ")
print(5/3)

# 11
삼성전자 = 50000
삼성전자_10주 = 삼성전자 * 10

# 12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

# 13
s = "hello"
t = "python"
print(s + "!" + t)

# 14
print(2+2*3)

# 15
a = 128
print(type(a))
# <class 'int'>

b = "132"
print(type(b))

# 16

num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))

# 17

num = 100
num_1int = str(num)
print(num_1int, type(num_1int))

# 18

floating = "15.79"
result = float(floating)
print(result, type(result))

# 19

year = "2020"
year_int = int(year)
year_1 = year_int-1
year_2 = year_int-2
year_3 = year_int-3
print(year_1, year_2, year_3)

''' 
year = "2020"
print(int(year)-3) # 2017
print(int(year)-2) # 2018
print(int(year)-1) # 2019
'''

# 20

Aircon_Credit = 48584*36
print(Aircon_Credit)
'''
월 = 48584
총금액 = 월 * 36
print(총금액)
'''

# 21

letters = 'python'
print(letters[0], letters[2])

# 22

license_plate = "24가 2210"
print(license_plate[-4:])

# 23

string = "홀짝홀짝홀짝"
print(string[::3])

# 24

string1 = 'PYTHON'
print(string1[::-1])

# 25

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 26

phone_number2 = phone_number.replace("-", "")
print(phone_number2) #25's sentence

# 27

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 28

# lang = 'python'
# lang[0] = 'p'
# print(lang)

# 29

# string = 'abcdfe2a354a32a'
# string = string.replace('a', 'A')
# print(string)

# 30

string = 'abcd'
string.replace('b', 'B')
print(string)

# 31

a = "3"
b = "4"
print(a+b)
# "34" 

# 32

print("Hi" * 3)
# HiHiHi 

# 33
print("-" * 80)

# 34

t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 35

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s" %name1, "나이 : %s " %age1)
print("이름 : %s" %name2, "나이 : %s " %age2)

# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 36
# format() method at 35번 repeat
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

# 37
# f-string 사용

print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 38

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40 
data = "  삼성전자  "
data1 = data.strip()
print(data1)

# 41 upper 메서드
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

# 42 lower 메서드
ticker2 = ticker1.lower()
print(ticker2)

# 43 capitalize 메서드
a = 'hello'
a = a.capitalize()
print(a)

# 44 endswith 메서드

file_name = "보고서.xlsx"
file_name2 = file_name.endswith("xlsx")
print(file_name2)

# 45 endswith 메서드 ``` 2 개체 이상은 괄호 두개 ```
file_name3 = file_name.endswith(("xlsx", "xls"))
print(file_name3)

# 46 startswith 메서드
file_name4 = "2020_보고서.xlsx"
file_name5 = file_name4.startswith("2020")
print(file_name5)

# 47 split 메서드

b = "hello world"
b1 = b.split(" ") # b.split()
print(b1)

# 48 split 메서드

ticker3 = "btc_krw"
ticker4 = ticker3.split("_")
print(ticker4)

# 49 split 메서드

date = "2020-05-01"
date1 = date.split("-")
print(date1)

# 50 rstrip 메서드

data = "039490    "
data1 = data.rstrip()
print(data1)

# 51 리스트 생성
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 52 리스트 원소추가
movie_rank.append("배트맨")
print(movie_rank)

# 53 가운데에 원소추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 54 특정 원소 삭제
del movie_rank[3]
print(movie_rank)

# 55
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 56 
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = [lang1+lang2]
# langs = lang1 + lang2
print(langs)

# 57 리스트 최대값, 최소값 출력(min(), max() 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예 :
# max: 7
# min: 1
print("max: ", max(nums))
print("min: ", min(nums))

# 58 리스트의 합 출력
nums1 = [1, 2, 3, 4, 5]
print(sum(nums1))

# 59 저장된 데이터의 개수
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"] 
print(len(cook))

# 60 리스트 평균 출력

average = sum(nums1) / len(nums1)
print(average)

# 61 특정 정보 제외하고 출력하기
