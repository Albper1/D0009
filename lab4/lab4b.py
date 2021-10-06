import json
class Phonebook:

    def __init__(self)-> None:
        self.dic = {}
        self.a_dic = {}

    def main(self):
        while(True):
            l = input('phonebook> ').split()
            if l[0] == 'add':
                self.add(l[1],l[2])
            elif l[0] == 'lookup':
                print(self.lookup(l[1]))
            elif l[0] == 'alias':
                self.alias(l[1],l[2])
            elif l[0] == 'change':
                self.change(l[1],l[2])
            elif l[0] == 'save':
                self.save(l[1])
            elif l[0] == 'load':
                self.load(l[1])
            elif l[0] == 'quit':
                self.quit()
            else:
                print('wrong input, try again')


    '''Add number to phonebook'''
    def add(self,name,number):
        self.dic[name] = number
    '''Looks up name in phonebook, prints number if there is one'''
    def lookup(self,name):
        if name in self.dic:
            return self.dic[name]
        else:
            for i in self.a_dic:
                if name in self.a_dic[i]:
                    return self.dic[i]
            return "{0} not in phonebook".format(name)
    '''Adds an alias a name in the phonebook'''
    def alias(self,name,new_name):
        self.a_dic[name] = self.a_dic.get(name,[]) + [new_name]
    '''Changes a number in the phonebook'''
    def change(self,name,number):
        self.dic[name] = number
    '''saves a file as filename, either overwrite a file or create a new one'''
    def save(self,filename):
        f = open(filename, "w")
        res = ""
        for i in self.dic:
            res +=f"{i};{self.dic[i]}\n"
        if self.a_dic:
            res +="alias_dic\n"
            for i in self.a_dic:
                res +=f"{i};{self.a_dic[i]}\n"

        f.write(res)
        f.close()
    '''load the file "filename" if there is one'''
    def load(self,filename):
        try:
            with open(filename,'r') as f:
                lines = f.readlines()
            '''Används för att göra skillnad mellan vad som ska vara i dic, och i a_dic'''
            dic_lines = lines[:lines.index('alias_dic\n')]
            a_dic_lines = lines[lines.index('alias_dic\n')+1:]
            for line in dic_lines:
                name,nr = line.split(';')
                self.dic[name] = nr.strip()
            for line in a_dic_lines:
                name,alias_lst = line.split(';')
                self.a_dic[name] = alias_lst.strip()

            f.close()
        except FileNotFoundError:
            print("There is no file named", filename)
    '''quits the program'''
    def quit(self):
        quit()

p = Phonebook().main()
