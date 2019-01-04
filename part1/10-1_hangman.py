def hangman(word):
    wrong = 0
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね：'
        char = input(msg)
        if char in rletters:  # 入力された文字がrlettersに含まれているかを確認
            cind = rletters.index(char)  # indexメソッドを使って入力された文字の番号を取得
            board[cind] = char  # boardの[cind]番目に入力文字を代入する
            rletters[cind] = '$'  # rlettersの[cind]番目を'$'に置き換える。こうしておくことで同じ文字を含むwordの場合でもindexメソッドが正しく機能する。
        else:
            wrong += 1
        print('hint:',''.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！')
            print(''.join(board))
            win = True
            break
    if not win:
        # print('\n'.join(stages[0:e]))
        print('あなたの負け！正解は{}.'.format(word))

# wordを引数に渡すのではなく、defの中にword=として記載してしまってもよい。
word_list = ['cat', 'dog', 'bird']
from random import randint
random_num = randint(0,2)
hangman(word_list[random_num])
