def add_dots(text): 
   return '.' .join(text)

def remove_dots(text):
    return text.replace('.', '')


print(remove_dots(add_dots('test')))


