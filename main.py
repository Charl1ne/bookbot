def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    wordcount = count_words(text)
    character_count = count_characters(text)
    sorted_pairs = sort_dict(character_count)
    report = gen_report(file_path, wordcount, sorted_pairs)
    print (report)

def count_words(f):
    words = f.split()
    return len(words)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(f):
    lowercase_text = f.lower()
    character_dict = {}
    for char in lowercase_text:
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict

def sort_dict(dict):
    sorted_pairs = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_pairs

def gen_report(file_path, wordcount, char_num_pairs):
    header = f"--- Begin report of {file_path} --- \n{wordcount} words found in the document\n\n"
    body = []
    for pair in char_num_pairs:
        letter = pair[0]
        number = pair[1]
        body.append(f"The {letter} character was found {number} times.\n")
    footer = "--- End report ---"
    full_report = header + "".join(body) + footer
    return full_report


main()