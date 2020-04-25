import random

print('주사위를 굴립니다')

com = random.randint(1, 6)
user = random.randint(1, 6)

print('컴퓨터의 주사위 눈은 ' + str(com) + '입니다')
print('당신의 주사위 눈은 ' + str(user) + '입니다')