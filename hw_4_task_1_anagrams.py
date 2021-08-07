def anagramm(a, b):
    word = ""
    for i in a:
        if i in b:
            word += i
            if len(word) == len(a):
                print(b, word)


anagramm("крот", "корт")
