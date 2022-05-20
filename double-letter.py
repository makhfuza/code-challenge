def double_letters(text):
    for index in range(len(text)-1):
        if text[index] == text[index+1]: return True
    return False

print(double_letters('hello'))
print(double_letters('nono')) 
