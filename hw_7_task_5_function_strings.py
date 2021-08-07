def true_or_false(string):
    text = "".join(el for el in string if el in "〈({[]})〉")

    while text:
        flag = True
        for el in "〈〉", "()", "{}", "[]":
            if el in text:
                text = text.replace(el, "")
                flag = False
        if flag:
            return False
    return True


b = 'ab3(#$%[pop]cvfs{kek}'
print(true_or_false(b))


def brakets(text):
    op_brakets = ['(', '{', '[']
    closse_brakets = [')', '}', ']']
    all_symbol = []
    for char in text:
        if char in op_brakets:
            all_symbol.append(char)
        elif char in closse_brakets:
            index = closse_brakets.index(char)
            if len(text) > 0 and all_symbol[-1] == op_brakets[index]:
                del all_symbol[-1]
            else:
                return False

    if len(all_symbol) == 0:
        return True
    else:
        return False


print(brakets(b))
