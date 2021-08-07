words = "Hello my name is Sasha"
sp1 = []
for i in reversed(words.split()):
    sp1.append(i)
sp1 = " ".join(sp1)
print(sp1)
