'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        # base case
        return 0
    elif word[:2] == "th":
        # if first two letters are th, run function again and again from beginning of word to end, going through each letter
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])