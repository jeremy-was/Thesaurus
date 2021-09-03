import json
data = json.load(open("data.json"))
from difflib import get_close_matches

# print(f'Dictionary items: {len(data.items()):,}')

def thesaurus(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word not in data and len(get_close_matches(word, data.keys())) > 0:
        close_matches = get_close_matches(word, data.keys())
        print(f'\nClose matches: {close_matches}')
        print(f"Didn't find {word}. Did you mean {close_matches[0]}?")
        while True:
            answer = input('Enter yes (y) or no (n): ')
            if answer.lower()[0] == 'y':
                return data[close_matches[0]]
            elif answer.lower()[0] == 'n':
                return ''
                break
            else:
                continue
    else:
        print("\nDon't know that word, please try again...")

while True:
    user_input = input('\nEnter a word:  ')
    if user_input == 'q':
        print('\nThanks for using Thesaurus\n')
        break
    else:
        result = thesaurus(user_input)
        print('\n')
        if type(result) == list:
            for value in result:
                print(value)
        else:
            print(result)