from collections import deque


def is_palindrome(characters):
    character_deque = deque(characters)

    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return print('False')

    return print('True')

# test below:
#
# is_palindrome('anona')