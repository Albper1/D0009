class TB:
    dic = {}
    alias_dic = {}
    def add(self,name,number):
        TB.dic[name] = number
    def lookup(self,name):
        if name in TB.dic:
            print(TB.dic[name])
        else:
            found = False
            for i in TB.alias_dic:
                if name in TB.alias_dic[i]:
                    found = True
                    break
            print(TB.dic[i] if found else 'name not found')

    def alias(self,name,new_name):
        if name in TB.alias_dic:
            TB.alias_dic[name].append(new_name)
        else:
            TB.alias_dic[name] = [new_name]
    def change(self,name,number):
        TB.dic[name] = number
    def save(self,filename):
        pass
    def load(self,filename):
        pass
    def quit(self):
        return



p = TB()

p.add('Amalia',123)
#p.lookup('Amalia')
p.alias('Amalia','Jenny')
p.lookup('Jenny')
p.lookup('Harald')
print(p.dic)
#print(p.alias_dic)
