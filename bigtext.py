import re

# List storing the letter art
alphab = [
    [
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#',' ',' ',' ']
    ],
    [
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#',' ',' ',' ',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','#','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ','#','#','#',' ',' ',' ',' ',' ',' ','#','#','#','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ','#','#','#',' ',' ',' ',' ',' ',' ','#','#','#','#',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ']
    ],
    [
        [' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' '],
        [' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' '],
        [' ','#',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ','#',' '],
        [' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ']
    ],
    [
        [' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ',' ',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ','#',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#','#','#','#','#','#','#','#','#','#','#',' ',' '],
        [' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ','#','#','#',' ',' ',' ',' ',' ',' ','#','#','#','#',' ']
    ],
    [
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' #','#','#','#','#','#','#','#','#',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#','#',' ',' ',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ',' ',' ',' ','#','#','#','#','#','#','#',' ',' ',' ',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' '],
        [' ','#',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ','#',' '],
        [' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' '],
        [' ','#','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#','#',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ']
    ],
    [
        [' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ']
    ],
    [
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#','#','#','#','#','#','#',' ']
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]
]

# Dictionary referencing letter art
alphab_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    ' ': 26
}


# Function to print the word out
def print_word(word):
    print('')
    for i in range (0, 7):
        for k in word.upper():
            for j in range(0, 15):
                if alphab[alphab_dict[k]][i][j] == '#':
                    print('|', end = '')
                else:
                    print(' ', end = '')
        print('')
    print('')


# Function to check if word contains only spaces and letters. Uses Regex
def word_submit(word):
    regex = re.compile('^[a-zA-Z ]+$', re.I)
    match = regex.match(word)
    if bool(match):
        print_word(word)
    else:
        print('Invalid input. Letters and spaces only.')


# Function to get input from user
def get_input():
    word_to_enlarge = input('What word would you like to enlarge? Letters and spaces only: ')
    word_submit(word_to_enlarge)


# Check if main file and only run if it is
if __name__ == '__main__':
    get_input()