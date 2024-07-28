

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = len(text.split())
    character_count = get_character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(word_count, "words found in the book.")
    print("")
    for char, count in character_count.items():
        print(f"{char}: {count}")

 
def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()
    
def get_character_count(text):
    character_count = {}
    # Count the number of times each character appears in the text,  only include alphabetic characters
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    # Sort the dictionary by character count
    character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    return character_count

main()