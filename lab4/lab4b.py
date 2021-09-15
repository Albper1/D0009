import json
class TB:
    dic = {}
    '''Add number to phonebook'''
    def add(self,name,number):
        TB.dic[name] = number
    '''Looks up name in phonebook, prints number if there is one'''
    def lookup(self,name):
        print(TB.dic[name] if name in TB.dic else 'name not found')
    '''Adds an alias a name in the phonebook'''
    def alias(self,name,new_name):
        TB.dic[new_name] = TB.dic[name]
    '''Changes a number in the phonebook'''
    def change(self,name,number):
        TB.dic[name] = number
    '''saves a file as filename, either overwrite a file or create a new one'''
    def save(self,filename):
        f = open(filename, "w")
        f.write(json.dumps(TB.dic, indent = 4))
        f.close()
    '''load the file filename if there is one'''
    def load(self,filename):
        try:
            f = open(filename,'r')
            TB.dic = json.load(f)
            f.close()
        except FileNotFoundError:
            print("There is no file named", filename)
    '''quits the program'''
    def quit(self):
        quit()

p = TB()
