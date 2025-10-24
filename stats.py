def sort_on(items):
    return items["num"]

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_chars(text):
    all_chars = list(text)
    all_chars = [i.lower() for i in all_chars]
    unique_chars = set(all_chars)

    final = {}
    for i in unique_chars:
        final[i] = all_chars.count(i)

    return final

def sort_dict(char_dict):
    dict_list = [{"char": i, "num": char_dict[i]} for i in char_dict.keys()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list