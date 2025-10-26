def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_dict = {}
    word_list = text.split()
    for word in word_list:
        for letter in word:
            letter_lower = letter.lower()
            if letter_lower in letter_dict:
                letter_dict[letter_lower] += 1
            else:
                letter_dict[letter_lower] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def letter_sort(dict_to_be_sorted):
    sorted_list = []
    for key in dict_to_be_sorted:
        if key.isalpha():
            new_dict= {}
            new_dict["name"] = key
            new_dict["num"] = dict_to_be_sorted[key]
            sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

""" def main():
    test_dict = {"a": 37, "b": 12, "c": 89, "d": 60}
    print(type(letter_sort(test_dict)))
    print(letter_sort(test_dict))


main() """