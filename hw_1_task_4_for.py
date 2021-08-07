s = [1, 5, 2, 1, 6, 7, 12, 15, 11, 5, 6, 10, 11, 1]
p = ""
m = ""
for i in range(len(s)):
    if s[i-1] < s[i]:
        p += "+"
    else:
        m += "-"

print(p)
print(m)
