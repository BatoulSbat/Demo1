def alternate_characters(string):
    result = ''
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_words(string):
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

def main():
    string = input("Enter a string: ")
    
    # Make each alternate character uppercase and lowercase
    alternate_char_result = alternate_characters(string)
    print("Alternate characters (upper/lower):", alternate_char_result)
    
    # Make each alternate word lowercase and uppercase
    alternate_word_result = alternate_words(string)
    print("Alternate words (lower/upper):", alternate_word_result)

if __name__ == "__main__":
    main()
