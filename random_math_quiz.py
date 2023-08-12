def math_quiz():
    import random
    title = '내가 할려고 만든 랜덤 수학 곱하기 퀴즈'
    print('\033[95m' + '{:-^50}'.format(title) + '\033[0m')
    print()

    wrong = 0
    while True:
        if wrong == 1:
            break
        Difficulty = input('난이도를 입력해 주세요| easy  /  normal  /  hard |\n')
        print()
        if Difficulty == 'easy':
            while True:
                number1 = random.randrange(11,20)
                print(number1,'x',number1,'= ?')
                answer = number1 * number1
                try:
                    my_answer = int(input('입력 :'))
                except ValueError:
                    print('숫자를 입력해 주세요')    
                if my_answer == answer:
                    print('\033[32m'+'정답!'+'\033[0m')
                else:
                    print('\033[31m'+'틀림'+'\033[0m')
                    print('올바른 정답:',answer)
                    wrong = 1
                    break
        elif Difficulty == 'normal':
            while True:
                number2 = random.randrange(11,30)
                print(number2,'x',number2,'= ?')
                answer = number2 * number2
                try:
                    my_answer = int(input('입력 :'))
                except ValueError:
                    print('숫자를 입력해 주세요')    
                if my_answer == answer:
                    print('\033[32m'+'정답!'+'\033[0m')
                else:
                    print('\033[31m'+'틀림'+'\033[0m')
                    print('올바른 정답:',answer)
                    wrong = 1
                    break
        elif Difficulty == 'hard':
            while True:
                number3 = random.randrange(11,101)
                print(number3,'x',number3,'= ?')
                answer = number3 * number3
                try:
                    my_answer = int(input('입력 :'))
                except ValueError:
                    print('숫자를 입력해 주세요')    
                if my_answer == answer:
                    print('\033[32m'+'정답!'+'\033[0m')
                else:
                    print('\033[31m'+'틀림'+'\033[0m')
                    print('올바른 정답:',answer)
                    wrong = 1
                    break        

        else:
            print('\033[31m'+'easy , normal , hard 중에서 난이도를 골라 주세요'+'\033[0m')
    