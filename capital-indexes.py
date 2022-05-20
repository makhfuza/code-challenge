def capital_indexes(text):
     final_list = []
     for order, letter in enumerate(text):
        if letter.isupper(): final_list.append(order)
     return final_list

print(capital_indexes('HeLlO'))

