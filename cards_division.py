import cards_sorting
import openapi

type_list=['散牌', '一对', '二对', '连对', '三条', '顺子', '同花', '葫芦', '炸弹', '同花顺']
or_list = []
or_list2 = []
or_list3 = []
list1 = [None]*13
max_list = []
max_score = 0
score_list = [0, 0, 0]
def change_and_sort_cards(list):
    for i in range(0, 13):
        if list[i][1]=='A':
            list[i]=list[i][0]+'14'
        elif list[i][1]=='J':
            list[i] = list[i][0]+'11'
        elif list[i][1]=='Q':
            list[i]=list[i][0]+'12'
        elif list[i][1]=='K':
            list[i]=list[i][0]+'13'
    list.sort(key=lambda x:int(x[1:]))

def rechange(list):
    for i in range(0,13):
        if list[i][1:] == '14':
            list[i]=list[i][0]+'A'
        elif list[i][1:] == '13':
            list[i] = list[i][0] + 'K'
        elif list[i][1:] == '12':
            list[i] = list[i][0] + 'Q'
        elif list[i][1:] == '11':
            list[i] = list[i][0] + 'J'


def divide_cards1(n, m, begin):
    global or_list
    global or_list2
    global list1
    if m > n or m < 1 or n < 1:
        return
    if m == 1:
        for i in range(begin, begin+n):
            list1[5 - m] = or_list[i]
            or_list2 = or_list.copy()
            for j in range(0, 5):
                or_list2.remove(list1[j])
            if cards_sorting.is_continue(list1[0:5]):
                divide_cards2(8, 5, 0)
        return
    for i in range(begin, begin+n-m+1):
        list1[5-m] = or_list[i]
        divide_cards1(n-i-1+begin, m-1, i+1)

def divide_cards2(n,m,begin):
    global or_list2
    global or_list3
    global list1
    global max_score
    global max_list
    global score_list
    if m > n or m < 1 or n < 1:
        return
    if m == 1:
        for i in range(begin, begin+n):
            list1[10 - m] = or_list2[i]
            or_list3 = or_list2.copy()
            for j in range(5, 10):
                or_list3.remove(list1[j])
            list1[10:13] = or_list3
            #占位：比较
            tmp_list = cards_sorting.sort_cards(list1)
            tmp = tmp_list[0]+tmp_list[1]+tmp_list[1]
            if tmp > max_score:
                max_score = tmp
                score_list = tmp_list.copy()
                max_list = list1.copy()
        return
    for i in range(begin, begin+n-m+1):
        list1[10 - m] = or_list2[i]
        divide_cards2(n-i-1+begin, m-1, i+1)

def cards_type(list):
    global type_list
    types=[None]*3
    for i in range(0, 3):
        types[i] = type_list[int(list[i])-1]
    return types


def divide_cards(list):
    global max_score
    global or_list
    global max_list
    max_score = 0
    or_list = list.copy()
    change_and_sort_cards(or_list)
    divide_cards1(13, 5, 0)
    rechange(max_list)
    #front = max_list[10:13]
    #middle = max_list[5:10]
    #rear = max_list[0:5]
    return max_list

def main():
    tmp = openapi.cards_list
    change_and_sort_cards(tmp)
    divide_cards(tmp)
    rechange(tmp)
    print(tmp)
    front = max_list[10:13]
    middle = max_list[5:10]
    rear = max_list[0:5]
    print(front)
    print(middle)
    print(rear)
    print(cards_type(score_list))
