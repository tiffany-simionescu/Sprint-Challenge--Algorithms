'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # counter for "th" occurances
    th_count = 0
    # seperate letters in a list format
    character_list = list(word)

    # Base Case: if the word is less than 2 letters, return current count
    if len(character_list) < 2:
        return th_count

    # if indexes 0 and 1 are "th", increase counter
    elif character_list[0] == "t" and character_list[1] == "h":
        th_count += 1

    # recursive call starting at index 1 and keeping track of current count
    return th_count + count_th(character_list[1:])
