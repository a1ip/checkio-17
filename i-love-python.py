def i_love_python():
    """
        Let's explain why do we love Python.
    """
    #1. it's short
    txt = "python"
    assert txt == txt[::-1][::-1]
    
    #2. and easy to work with
    txt = "pythonino"
    txt_1 = txt[::2]
    txt_2 = txt[1::2]
    res = "".join([a+b for a,b in zip(txt_1,txt_2)])
    if len(txt_1)>len(txt_2):
        res+=txt_1[-1]
    assert txt == res
    
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
