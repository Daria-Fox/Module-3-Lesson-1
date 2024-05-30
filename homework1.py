def single_root_words(root_word, *other_words):
    same_words = []
    for root_word in other_words:
        i = other_words[0]
        if root_word in i:
            same_words.append(i)
            i = other_words[1]
            if root_word in i:
                same_words.append(i)
                i = other_words[2]
                if root_word in i:
                    same_words.append(i)
                    i = other_words[3]
                    if root_word in i:
                        same_words.append(i)
                        i = other_words[4]
                        if root_word in i:
                            same_words.append(i)
                            i = other_words[5]
                            if root_word in i:
                                same_words.append(i)
    print(list(same_words))


single_root_words('клон', 'клон', 'наклон', 'уклониться', 'кланяться', 'укол', 'крен')
