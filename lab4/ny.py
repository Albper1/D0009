from cmd import Cmd

class Phonebook():

    def __init__(self)-> None:
        self.dic = {}
        self.a_dic = {}

    def main(self):
        '''Main loop'''
        while(True):
            l = input('Phonebook> ').split()
            try:
                if l[0] == 'add':
                    print(self.add(l[1],l[2]))
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
            except:
                print(l[0])
                print('wrong input, try again')


    '''Add number to phonebook'''
    def add(self,name,number):


        for nr in self.dic:
            if name in self.dic[nr]:
                return "{0} already exists".format(name)

        if number in self.dic:
            return "{0} already exists".format(number)

        self.dic[number] = [name]
        return "{0} sucessfully added to phonebook".format(name)
    '''Looks up name in phonebook, prints number if there is one'''
    def lookup(self,name):

        for nr in self.dic:
            if name in self.dic[nr]:
                return nr
        return "{0} not in phonebook".format(name)
    '''Adds an alias a name in the phonebook'''
    def alias(self,name,new_name):
        for nr in self.dic:
            if name in self.dic[nr] and new_name not in self.dic[nr]:
                self.dic[nr] += [new_name]
                print(self.dic)
                return
        print("name not found or duplicate name")

    '''Changes a number in the phonebook'''
    def change(self,name,number):
        try:
            self.dic[number] = self.dic.pop(self.get_number(name))
        except:
            print("{0} not in phonebook".format(name))

    '''saves a file as filename, either overwrite a file or create a new one'''
    def save(self,filename):
        f = open(filename, "w")
        res = ""
        for i in self.dic:
            res +=f"{i};{self.dic[i]}\n"

        f.write(res)
        f.close()
    '''load the file "filename" if there is one'''
    def load(self,filename):
        try:
            with open(filename,'r') as f:
                lines = f.readlines()
            for line in lines:
                nr,name = line.split(';')
                self.dic[nr] = name.strip()
            f.close()
        except FileNotFoundError:
            print("There is no file named", filename)
    '''quits the program'''
    def quit(self):
        quit()

    '''Used to get number for change'''
    def get_number(self,name):
        for nr in self.dic:
            if name in self.dic[nr]:
                return nr

p = Phonebook().main()
