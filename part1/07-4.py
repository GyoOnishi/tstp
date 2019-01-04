#p.116-4
list1 = [1,2,3,4,5]
while True:
    a = input('数字を入力するか、qで終了します。：')
    if a == 'q':
        break
    elif a in str(list1):
        print('正解')
    else:
        print('不正解')
