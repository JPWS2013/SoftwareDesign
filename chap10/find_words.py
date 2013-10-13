"""Test code for palindrome.py.

Author: Allen B. Downey
"""



def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        if double_letters(word):
        	print word

if __name__ == '__main__':
    main()
