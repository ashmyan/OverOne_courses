func1 = lambda x, y, z: pow(x, z) - y
print(func1(3, 5, 6))

func2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(func2))

func3 = map(lambda x: "Hello " + x, ["Sasha", "Pasha", "Max"])
print(list(func3))

func4 = map(lambda x: str(x), [2, 4, 5])
print(list(func4))

func5 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(func5))

a = ["Катя", "Саша", "Петя"]

funk6 = filter(lambda x: "т" in x or "Т" in x, ["Катя", "Саша", "Петя", "Толя"])
print(list(funk6))

funk7 = filter(lambda x: "т" in x.lower(), ["Катя", "Саша", "Петя", "Толя"])
print(list(funk7))
