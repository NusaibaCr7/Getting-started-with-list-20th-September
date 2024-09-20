def match_words(words):
    counter = 0
    lst = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            
            counter = counter + 1
            lst.append(word)
            
    print("List of words with same first and last character\n", lst)
    return counter

li = ['abc','cfc', 'xyz','aba','1221','nahian','nabilan','roser','nusaiban']

count = match_words(li)
print("Number of words having same first and last character:", count)
