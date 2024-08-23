def single_root_words(root_word, *other_words):
    same_words = []
    lowercase_list = [s.lower() for s in other_words]
    for i in range(len(other_words)):
        if lowercase_list[i].count(root_word.lower()) or lowercase_list[i] in root_word.lower():
            same_words.append(other_words[i])


    return same_words


print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))