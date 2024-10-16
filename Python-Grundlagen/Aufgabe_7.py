def String_Zerlegung(text):
    text = text.replace(":", "").replace("-", " ")
    list_of_text  = text.split(' ')
    for i in range(len(list_of_text)):
        try:
            list_of_text[i] = int(list_of_text[i])
        except:
            next
    return list_of_text
print(String_Zerlegung("32-16: 5 k: sdkl-ffs"))