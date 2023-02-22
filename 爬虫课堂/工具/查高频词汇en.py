def repeatNum(filename):
    with open(filename)as f:
        word_dict={}
        for i in f:
            i.strip()
            word_list = i.split()
            for j in word_list:
                if not j in word_dict:
                    word_dict[j] = 1
                else:
                    word_dict[j] += 1

    sort_list = []
    for key,num in word_dict.items():
        sort_list.append((num,key))
    sort_list.sort(reverse=True)
    print(sort_list[:10])

if __name__ == '__main__':
    repeatNum( './english.txt')