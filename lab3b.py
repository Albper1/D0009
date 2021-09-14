def main_dic_l():
    """Initierar listor"""
    word_lst = []
    des_word_lst = []
    """Körs tills användaren skriver in 4"""
    while True:
        print("1: Insert\n2: Lookup\n3: Delete word\n4: Exit Program\n")
        choice = input("Choose alternative: ")
        if choice == '1':
            """skriver in ord och beskrivning av ord i listorna word_lst och des_word_lst"""
            insert_l(word_lst,des_word_lst)
        elif choice == '2':
            """Kollar upp om ett ord finns i listan och ifall det finns skrivs beskrivning av ordet ut"""
            lookup_l(word_lst,des_word_lst)
        elif choice == '3':
            """Deletar ett ord från listan och dess beskrivning"""
            del_l(word_lst,des_word_lst)
        elif choice == '4':
            print("Byebye")
            return
        else:
            """Ifall nåt annat än 1,2,3 eller 4 skrivs in"""
            print("Wrong input, pls input 1,2,3 or 4")

"""appendar in i listorna"""
def insert_l(word_lst,des_word_lst):
    word_lst.append(input("\nWord to insert: "))
    des_word_lst.append(input("Description of word: "))
    return word_lst,des_word_lst
"""kollar upp ord i listan"""
def lookup_l(word_lst,des_word_lst):
    lookup_word = input("Word to lookup: ")
    if lookup_word in word_lst:
        print("\nDescription of word:",des_word_lst[word_lst.index(lookup_word)],"\n")
    else:
        print(lookup_word, "is not in dictionary")

"""tar bort ord och dess beskrivning från listorna"""
def del_l(word_lst,des_word_lst):
    del_word = input("\nWord to delete: ")
    if del_word in word_lst:
        del des_word_lst[word_lst.index(del_word)]
        word_lst.remove(del_word)
    else:
        print(del_word,"is not in dictionary")
    return word_lst,des_word_lst

#----------------------------------------------------------------------------------------

def main_dic_t():
    word_lst = []
    while True:
        print("Menu for dictionary\n")
        print("1: Insert\n2: Lookup\n3: Delete word\n4: Exit Program\n")
        choice = input("Choose alternative: ")

        if choice == '1':
            insert_t(word_lst)
        elif choice == '2':
            lookup_t(word_lst)
        elif choice == '3':
            delete_t(word_lst)
        elif choice == '4':
            print("Byebye")
            return
        else:
            print("Wrong input, pls input 1,2,3 or 4")

def insert_t(word_lst):
    word_lst.append((input("\nWord to insert: "),input("Description of word: ")))
    return word_lst

def lookup_t(word_lst):
    lookup_word = input("Word to lookup: ")
    found = False
    for i in range(len(word_lst)):
        if word_lst[i][0] == lookup_word:
            found = True
            index = i
    if found:
        print("\nDescription of word:",word_lst[index][1],"\n")
    else:
        print(lookup_word,"not in dictionary\n")

def delete_t(word_lst):
    del_word = input("Word to delete: ")
    index = -1
    for i in range(len(word_lst)):
        if word_lst[i][0] == del_word:
            index = i
    if index != -1:
        del word_lst[index]
    else:
        print(del_word,"not in dictionary\n")
    return word_lst

#----------------------------------------------------------------------------------------



def main_dic_d():
    word_dic = {}
    while True:
        print("Menu for dictionary\n")
        print("1: Insert\n2: Lookup\n3: Delete word\n4: Exit Program\n")
        choice = input("Choose alternative: ")

        if choice == '1':
            insert_d(word_dic)
        elif choice == '2':
            lookup_d(word_dic)
        elif choice == '3':
            delete_d(word_dic)
        elif choice == '4':
            print("Byebye")
            return
        else:
            print("Wrong input, pls input 1,2,3 or 4")

def insert_d(word_dic):
    word = input("\nWord to insert: ")
    des_word = input("Description of word: ")
    word_dic[word] = des_word
    return word_dic

def lookup_d(word_dic):
    lookup_word = input("Word to lookup: ")
    if lookup_word in word_dic:
        print("\nDescription of word:",word_dic[lookup_word],"\n")
    else:
        print(lookup_word,"is not in dictionary\n")

def delete_d(word_dic):
    del_word = input("Word to delete: ")
    if del_word in word_dic:
        del word_dic[del_word]
    else:
        print(del_word,"is not in dictionary\n")
    return word_dic


#main_dic_t()
#main_dic_d()
#main_dic_l()
