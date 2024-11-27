def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)

    chars_dict = count_characters(file_contents)
    list_of_dicts = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num":count}
            list_of_dicts.append(char_dict)
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    print(f"{word_count} words found in the document")
    for item in list_of_dicts:
        print(f"The '{item['char']}' character was found {item['num']} times")

def sort_on(dictionary):
    return dictionary["num"]

def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    character_counts = {}
    lowercase_text = text.lower()

    for character in lowercase_text:
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts


# call main function    
main()
    