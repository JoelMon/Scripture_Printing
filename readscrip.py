#!/bin/pythin3
import os
import random
import time 
import sys

def main():
    file_name = 'scrip.txt'

    f = open(file_name, 'r') 
    scripture = f.read()
    split = scripture.split('\n', -1)

    book = split[0].find(':')+1
    book_text = split[0][book:]

    chapter = split[1].find(':')+1
    chapter_text = split[1][chapter:]
    
    verse = split[2].find(':')+1
    verse_text = split[2][verse:]

    text = split[3].find(':')+1
    text_text = split[3][text:]
    
    text2_text = split[4]

    os.system('clear') 
    slow_type('A scripture I like is {} {}:{}\n'.format(book_text, chapter_text, verse_text))
    print('')
    slow_type('It reads,\n')
    slow_type(text_text + '\n')
    slow_type(text2_text + '\n')
    slow_type(':)\n')


def slow_type(x):
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07) # Can use random to vary the speed.
    
if __name__ == '__main__':
    main()
