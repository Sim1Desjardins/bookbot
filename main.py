def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text) 
    print(f"--- Begin report of books/frankenstein.txt --- ")
    print(f"{num_words} words found in the document")
    
    chars_list = []
    for char, count in chars_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    
    # Add this function to tell sort() what to sort by
    def sort_on(dict):
        return dict["count"]
    
    # Use the key parameter and reverse=True to sort from highest to lowest
    chars_list.sort(reverse=True, key=sort_on)
    
    for c in chars_list:      
        print(f"The '{c['char']}' character was found {c['count']} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
