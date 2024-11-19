def main():
        path = "books/frankenstein.txt"
        book_text = get_book_text(path)
        word_count = count_words(book_text)
        chars = count_chars(book_text)
        chars_sorted = sort_chars_dict(chars)
        print_report(chars_sorted, word_count)
        #test()

def get_book_text(path):
    with open(path) as f:
        return f.read() 

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    chars = {}
    #text = "Das ist ein Test"
    text_lowered = text.lower()

    # Hier Zugriff über get testen (Python Tutorial, S. 113)
    for c in text_lowered:
        if c.isalpha():
            if c in chars:
                #print(F"{c} ist schon enthalten; alt: {chars[c]}")
                chars[c] = chars[c] + 1            
            else:
                #print(F"{c} ist neu")
                chars[c] = 1
    return chars

def sort_on(dict):
    return dict["anzahl"]

def sort_chars_dict(chars_count):
    liste = []
    for key, value in chars_count.items():
        liste.append({'zeichen':key, 'anzahl':value})
    liste.sort(reverse = True, key=sort_on)
    return liste

def print_report(chars_count, words_count):
    print(F'--- Begin report of books/frankenstein.txt ---')
    print(F'{words_count} words found in the document')
    print(F'')
    for d in chars_count:
        print(F'The {d['zeichen']} character was found {d['anzahl']} times')
    print(F'--- End report ---')

def test():
    dict = {'b':5, 'c':3, 'd':18, 'a': 4}
    liste = []
    for key, value in dict.items():
        liste.append({'zeichen':key, 'anzahl':value})
    liste.sort(reverse = True, key=sort_on)
    print(liste)

main()


     