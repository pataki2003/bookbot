def get_num_words(file_contents):
    return len(file_contents.split())


def count_characters(file_contents):
    lowercase_contents = file_contents.lower()
    chars = {}
    for letter in lowercase_contents:
        chars[letter] = chars.get(letter, 0) + 1
    return chars


def sort_on(item):
    return item["num"]


def chars_dict_to_sorted_list(chars_dict):
    char_list = []
    for ch, count in chars_dict.items():
        char_list.append({"char": ch, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
