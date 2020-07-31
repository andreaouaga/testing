import random

def read_text(file_name):
    list_of_lines = []
    with open(file_name, 'r', encoding='utf') as file:
        list_of_lines = []
        while True:
            line = file.readline() # TODO
            if not line:
                break
            list_of_lines.append(line.strip())

    return list_of_lines

def make_a_choice(ls):
    return random.choice(ls)

def question(s):
    list_of_words = s.split('，')
    return list_of_words

def replace_with_blanc(ls):
    index_of_blanc = random.randint(0, len(ls)-1)
    ls[index_of_blanc] = '_______'
    return '，'.join(ls)

def main_loop():
    running = True
    score = 0
    while running:   
        a = read_text('qianziwen.txt')
        b = make_a_choice(a)
        c = question(b)
        d = replace_with_blanc(c)
        print('问题：' + d)
        user_answer = input()
        if user_answer == str(0):
            running = False
        elif user_answer == 'c':
            score += 1
            print('答案：' + b)
            print('得分：' + str(score))
            print('\n')
        elif user_answer == 'w':
            print('答案：' + b)
            print('得分：' + str(score))
            print('\n')
            

if __name__ == '__main__': 
    main_loop()
