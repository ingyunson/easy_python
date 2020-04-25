import random

print('주사위를 굴립니다')

com = random.randint(1, 6)
user = random.randint(1, 6)

print('컴퓨터의 주사위 눈은 ' + str(com) + '입니다')
print('당신의 주사위 눈은 ' + str(user) + '입니다')

if com > user :
    print('컴퓨터가 승리하였습니다')

elif com == user :
    print('비겼습니다. 다시 굴려보세요.')

else :
    print('당신이 이겼습니다.')