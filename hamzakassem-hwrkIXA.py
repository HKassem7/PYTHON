#Hamza Kassem

def main():
    input_file = open('text.txt', 'r')
    text = input_file.read()
    words = text.split()
    unique_words = set(words)
    num = len(unique_words)
    words.sort()
    print('Words in alphabetical order:')
    print(words)
    print('The number of unique words in the text is:', num)

main()
input('')
