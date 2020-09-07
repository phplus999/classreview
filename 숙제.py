# #로봇 기자 만들기
# stadium = input("경기장은 어디입니까?")
# win = input("이긴팀은 어디입니까?")
# lose = input("진팀은 어디입니까?")
# player = input("우수선수는 누구입니까?")
# score = input("스코어는 몇대몇입니까?")
#
# print("===========================")
#
# print(f"오늘 {stadium} 에서 야구 경기가 열렸습니다.")
# print(f"{win} 과 {lose} 은 치열한 공방전을 펼쳤습니다.")
# print(f"{player} 이 맹활약을 하였습니다.")
# print(f"결국 {win} 가 {lose} 를 {score} 로 이겼습니다.")
#
# print("===========================")

#부동산 광고 만들기

# print("#######################")
# print("#                     #")
# print("#    부동산 매물 광고   #")
# print("#                     #")
# print("#######################")
#
# street = input("주소:")
# type = input("매물:")
# number_of_rooms = int(input("방의수:"))
# price = int(input("가격:"))
#
# print(f"{street} 에 위치한 아주 좋은 {type} 가 매물로 나왔습니다. 이 아파트는 {number_of_rooms} 개의 방을 가지고 있으며 가격은 {price} 입니다.")

# #연습문제 1
# name = input("이름을 입력하시오 : ")
# age = input("나이를 입력하시오: ")
# year = 100 - int(age)
# hundred = 2016 + year
# print(f"{name}씨는 {hundred}년에 100살이시네요!")

#연습문제 2
# first = int(input("첫번째 숫자를 입력하시오."))
# second = int(input("두번째 숫자를 입력하시오."))
# third = int(input("세번째 숫자를 입력하시오."))
# aver = round(int(first + second + third) / 3, ndigits = 1)
# print(f"{first} {second} {third}의 평균은 {aver} 입니다.")

# # 연습문제 3
# r = int(input("반지름을 입력하시오: "))
# area = int(r)* int(r) * 3.141592
#
# print(f"반지름이 {r}인 원의 넓이={area}")

# #커피가게 매출 계산하기
# ameri = int(input("아메리카노 판매 개수:"))
# cafe = int(input("카페라테 판매 개수:"))
# capu = int(input("카푸치노 판매 개수:"))
#
# ameri_price = int(ameri) * 2000
# cafe_price = int(cafe) * 3000
# capu_price = int(capu) * 3500
# total = ameri_price + cafe_price + capu_price
# print(f"총 매출은 {total} 입니다. ")

#BMI 계산하기
# weight = float(input("몸무게를 kg 단위로 입력하시오:"))
# height = float(input("키를 미터 단위로 입력하시오."))
# bmi = float(weight) / float(height) **2
# print(f"당신의 BMI= {bmi}")

# #자동판매기 프로그램
# money = int(input("투입한 돈: "))
# price = int(input("물건값: "))
# change= int(money) - int(price)
# print("거스름돈:",change)
#
# fivehund = change // 500
# onehund = int(change % 500 / 100)
# print("500원 동전의 개수:", fivehund)
# print("100원 동전의 개수:",onehund)

# 연습문제 1
# a ='나는'
# b = '12'
# c = '개의 사과를 먹었다'
#
# print(str(a + b +c))

# #연습문제3
# a = input("문자열을 입력하시오:")
# print(a[0:2]+a[-2:])
#
# #연습문제4
# a = input("문자열을 입력하시오:")
# print(f"{a}하는 중")

# # 연습문제2
# age = 30
# if 30 <= age <= 50:
#     print('30이상이고 50이하이다')
# else:
#     print('해당되는 나이가 아닙니다.')

# # 연습문제 3
# temp = int(input("현재 온도를 입력하시오:"))
# if temp >= 25:
#     print("반바지를 입으세요")
# else:
#     print("긴바지를 입으세요")

# # 연습문제 4
# score = int(input("성적을 입력하시오: "))
# if score >= 90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# # 연습문제 5
# import random
# x = random.randint(1,100)
# y = random.randint(1,100)
# answer = x-y
# print(x,'-',y,'=',end='')
# num = int(input())
# if num == answer:
#     print("맞았습니다.")
# else:
#     print("틀렸습니다.",answer)

# # 연습문제6
# a = int(input("정수를 입력하시오: "))
# if a%2 == 0 and a%3 == 0:
#     print("2와 3으로 나누어 떨어집니다.")
# else:
#     print("2와3으로 나누어 떨어지지 않습니다.")

# 연습문제 7
import random

m = random.randint(0, 9)
n = random.randint(0, 9)

while n == m:
    m = random.randint(0, 9)
    n = random.randint(0, 9)
print(m)
print(n)

r = int(input("복권번호를 입력하시오(0에서 9사이):"))
q = int(input("복권번호를 입력하시오(0에서 9사이):"))
while r == q:
    print("복권번호를 다시 입력하시오(0에서 9사이):")
    r = int(input("복권번호를 입력하시오(0에서 9사이):"))
    q = int(input("복권번호를 입력하시오(0에서 9사이):"))
if (n == r or n == q ) and (m == q or m == r):
     print("상금 100만원")
elif (n == r or n == q) or (m == r or m == q):
     print("상금 50만원")
else:
    print("상금없음")

    print(f"당첨번호는 {n},{m}입니다.")

# # 팩토리얼 계산하기
# n = int(input("정수를 입력하시오:"))
# num = 1
# for i in range(1,n+1):
#     num *= i
# print(num)


# #구구단 출력
# n = int(input("원하는 단은:"))
#
# for  i in range(1,10):
#     print(n,"*",i,"=",n*i)

#사용자가 입력하는 숫자의 합 계산하기

# total = 0
# answer = 'yes'

# while answer:
#     n = int(input("숫자를 입력하시오:"))
#     total += n
#     m = input("계속?(yes/no):")
#     if m != answer:
#         break
# print("합계는:",total)

# # 숫자 맞추기 게임
# import random
# a = random.randint(1,100)
# print("1부터 100 사이의 숫자를 맞추시오.")
# print(a)
# q = int(input("숫자를 입력하시오."))
# count = 0
#
# while q != a:
#     count += 1
#     if q < a:
#         print("낮음!")
#         q = int(input("숫자를 입력하시오."))
#     elif q > a:
#         print("높음!")
#         q = int(input("숫자를 입력하시오."))
#
# print("축하합니다. 시도횟수 = ", count)

# 점치는 게임
# import random
# number = random.randint(1,8)
#
# name = input("이름:(종료하려면 엔터키)")
# quest = input("무엇에 대하여 알고 싶은가요?")
# print(f"{name}님 {quest}에 대하여 질문 주셨군요.")
# print("운명의 주사위를 굴려볼게요...")
#
# if number == 1:
#     print("한 점의 의심도 없이 맞습니다.")
# if number == 2:
#     print("앞으로 기대해도 좋습니다.")
# if number == 3:
#     print("조만간 좋은일이 생기겠군요.")
# if number == 4:
#     print("잠시 쉬어가도 좋습니다.")
# if number == 5:
#     print("자신을 믿으세요.")
# if number == 6:
#     print("자신이 생각한대로 행하세요.")
# if number == 7:
#     print("건강에 주의하세요.")
# if number == 8:
#     print("곧 좋은 결실을 맺겠군요.")


# 연습문제 1

# for i in range(1,101):
#     if i %2 == 0:
#         print(i)

# 연습문제 2
# year = 0
# balance = 1000
#
# while balance <= 2000:
#     year = year +1
#     interest = balance * 0.07
#     balance = balance + interest
# print(year, "년이 걸립니다.")

# # 연습문제 4
#
# a = int(input("3*9는"))
# correct = 27
#
# while correct != a:
#     a = int(input("3*9는"))
# print("맞았습니다.")

# # 연습문제 5
# q = int(input("정수를 입력하시오:"))
# total = 0
#
# while q != 0:
#     total += q
#     q = int(input("정수를 입력하시오:"))
# print(f"합은 {total} 입니다.")

# # 연습문제 6
# import random
# a = random.randint(1,6)
# b = random.randint(1,6)
#
# print(f"첫번째 주사위={a}, 두번째 주사위 = {b}")











