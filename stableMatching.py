#who wants:mostly wanted, less wanted...

a_wishes = {
'a' : ['e', 'd', 'f'],
'b' : ['f', 'e', 'd'],
'c' : ['f', 'd', 'e']
}

b_wishes = {
'd' : ['c', 'a', 'b'],
'e' : ['b', 'c', 'a'],
'f' : ['a', 'c', 'b']
}

def make_free_list(dict):
    return list(dict.keys())

def keyByValue(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]


def stableMatching(a_wishes, b_wishes, free_a_list, free_b_list):
    couples = {}
    while len(free_a_list) != 0:
        a = free_a_list[0]
        for b in a_wishes[a]:
            if b in free_b_list:
                couples.update({a : b})
                free_a_list = free_a_list[1:]
                free_b_list.remove(b)
                break
            else:
                wish = b_wishes[b]
                pair = keyByValue(couples, b)
                if wish.index(a) < wish.index(pair):
                    del couples[pair]
                    couples.update({a : b})
                    free_a_list = free_a_list[1:]
                    free_a_list.append(pair)
                    break
    return couples

def show(dict):
    for i in dict.keys():
        print(i, '->', dict[i])

def main(a_wishes, b_wishes):
    free_a_list = make_free_list(a_wishes)
    free_b_list = make_free_list(b_wishes)
    couples = stableMatching(a_wishes, b_wishes, free_a_list, free_b_list)
    show(couples)
if __name__ == '__main__':
    main(a_wishes, b_wishes)