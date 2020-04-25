import random
target = random.randint(1,100)

print('1~100 사이의 숫자에서 추측하여 입력하세요')
guess = int(input())
turn = 0

while guess :
    turn = turn + 1
    
    if guess == target :
        print('축하합니다! 맞았습니다!')
        print(str(turn) + '번을 시도해서 맞았습니다')
        break

    elif guess < target :
        print('아쉽네요, 조금 더 높여보세요')
        guess = int(input())

    else :
        print('아쉽네요, 조금 더 낮춰보세요')
        guess = int(input())

