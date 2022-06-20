import random


def read_file(filename):
    f = open(filename, encoding='UTF-8')
    data = f.readlines()
    f.close()
    return data


def str_trans_dict(data):
    n_list = []
    for lines in data:
        new_dict = {}
        lines = lines.strip('\n')
        lines = lines.split('@')
        new_dict[lines[0]] = lines[1]
        n_list.append(new_dict)
    return n_list


s = 'data'
choice = input("选择章数(1,2,3,4,5,6,all)\n")
s += choice
s += '.txt'
data = read_file(s)
a = str_trans_dict(data)
tr = 0
tot = 0
choice2 = input("test?\n")
if choice2 != '1':
    b = int(input("英语、中文、全要(0,1,2)\n"))
    i = 0
    for item in a:
        item = dict(item)
        word = list(item.keys())[0]
        ch = list(item.values())[0]
        if i == 4:
            print()
            i = 0
        if b == 0:
            print(word, end=', ')
        elif b == 1:
            print(ch, end=', ')
        else:
            print(item, end=', ')
        i += 1
else:
    word_list = []
    ch_list = []
    for item in a:
        item = dict(item)
        word_list.append(list(item.keys())[0])
        ch_list.append(list(item.values())[0])
    choice3 = input("英写中或中写英(0,1)\n")
    print("--------------------------------------")
    if choice3 == '0':
        while True:
            n = random.randint(0, len(word_list)-1)
            print(word_list[n])
            ans = input("请输入中文意思！（输入0结束）\n")
            tot += 1
            if ans != ch_list[n]:
                if ans == '0':
                    tot -= 1
                    print("共{}题，正确{}，正确率为{}%".format(tot, tr, float(tr/tot) * 100))
                    break
                print("Wrong Answer!")
                print("正确答案是{}".format(ch_list[n]))
            else:
                tr += 1
    else:
        while True:
            n = random.randint(0, len(ch_list)-1)
            print(ch_list[n])
            ans = input("请输入英文！（输入0结束）\n")
            tot += 1
            if ans != word_list[n]:
                if ans == '0':
                    tot -= 1
                    print("共{}题，正确{}，正确率为{}%".format(tot, tr, float(tr/tot) * 100))
                    break
                print("Wrong Answer!")
                print("正确答案是{}".format(word_list[n]))
            else:
                tr += 1


