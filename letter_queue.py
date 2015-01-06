__author__ = 'taras-sereda'

from collections import deque
def letter_queue(commands):
    letters_que = deque()
    for command in commands:
        if command.startswith('PUSH'):
            letters_que.append(command[-1])
        else:
            try:
                letters_que.popleft()
            except:
                continue
    return "".join(letters_que)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"