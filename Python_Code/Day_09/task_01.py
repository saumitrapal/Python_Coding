def fn1(text):
    return text + text

def fn2(text):
    return text.title()

output = fn2(fn1("hello"))

print(output)