import random

texts = ['apple', 'banana', 'spam', 'friend']
select = random.choice(texts)
question = []

for x in range(len(select)) :
    question.append('?')

def hangman() :
    user_input = input('추측한 알파벳을 입력하세요 : ')
    while len(user_input) != 1 :
        print('알파벳 한 글자를 입력해 주세요')
        user_input = input('추측한 알파벳을 입력하세요 : ')

    input_check = select.find(user_input)
    location = []

    while input_check != -1:
        location.append(input_check)
        input_check = select.find(user_input, input_check + 1)

    if not location :
        print('이 알파벳은 단어에 포함되어 있지 않습니다')

    else :
        print('이 알파벳이 단어에 포함되어 있습니다!')
        for loc in location :
            question[loc] = user_input


while question.count('?') != 0:
    print('문제 : ')
    print(question)
    hangman()

print('축하합니다! 정답을 맞추셨습니다!')