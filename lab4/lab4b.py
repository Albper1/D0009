import json
class Phonebook:

    def __init__(self)-> None:
        self.dic = {}
        self.a_dic = {}

    def main(self):
        while(True):
            l = input('phonebook> ').split()
            print(l)
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
        #print(TB.dic[name] if name in TB.dic else 'name not found')
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
        f.write(json.dumps(self.dic, indent = 4))
        f.write(json.dumps(self.a_dic, indent = 4))
        f.close()
    '''load the file "filename" if there is one'''
    def load(self,filename):
        try:
            with open(filename,'r') as f:
                data = f.read()
            self.dic,self.a_dic = data.split(";")
            #print(test)
            print(self.dic)
            #print(self.a_dic)

            f.close()
        except FileNotFoundError:
            print("There is no file named", filename)
    '''quits the program'''
    def quit(self):
        quit()

p = Phonebook().main(

)
