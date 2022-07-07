# @OhMeeky

word = 'held'

word_arr = []

for i in word:
    word_arr.append(i)

string = "____________________"
_str = string[0:len(word)]
_str_arr = []
for i in word:
    _str_arr.append(i)


################
print("Guess the word \n")
while True:
    guess_arr = []
    guess = input()

    for s in guess:
        guess_arr.append(s)

    for letters in word_arr:
        for letter_guessed in guess_arr:
            if letter_guessed == letters:
                for i in range(len(word)):
                    if letter_guessed == _str_arr[i]:
                        _str = _str[:i] + letter_guessed + _str[i+1:]


    print(_str)
    if _str == word:
        print("----------")
        print("Word guessed")
        print("----------")

