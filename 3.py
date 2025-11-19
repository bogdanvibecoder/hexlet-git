def up_long(m):
        return list(map(lambda x: x.upper() if len(x) > 3 else x, m))

word = ['hi', 'hello', 'cat', 'world']
print(up_long(word))
