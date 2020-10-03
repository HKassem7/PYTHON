#Hamza Kassem

def main():
    comma = ','
    period = '.'
    input_file = open('first_file.txt', 'r')
    text1 = input_file.read()
    input_file2 = open('second_file.txt', 'r')
    text2 = input_file2.read()
    file1 = text1.split()
    file2 = text2.split()
    set1 = set()
    set2 = set()
    for element in file1:
        element = element.lower()
        element = element.rstrip(comma)
        element = element.rstrip(period)
        set1.add(element)
    for element in file2:
        element = element.lower()
        element = element.rstrip(comma)
        element = element.rstrip(period)
        set2.add(element)
    print('The following unique words are present in both files')
    for words in set1.union(set2):
        print(words)
    print()
    print('The following words only appear in both files.')
    for words in set1.intersection(set2):
        print(words)
    print()
    print('The following words only appear in file 1')
    for words in set1.difference(set2):
        print(words)
    print()
    print('The following words only appear in file 2')
    for words in set2.difference(set1):
        print(words)
    print()
    print('List of words that appear in the first or second file but not both')
    for words in set1.symmetric_difference(set2):
        print(words)

main()
input('')
