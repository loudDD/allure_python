class demo:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError("must longer than 3")
        self.__name = name

    def getname(self):
        return self.__name

    name = property(getname, setname)
    def setadd(self, add):
        if add.startswith("http://"):
            self.__add = add
        else:
            raise ValueError("must start with http")
    def getadd(self):
        return self.__add
    add=property(getadd,setadd)

    def __display(self):
        print(self.__name,self.__add)

test = demo()
test.add="http://www.baidu.com"
test.name="demo"
test.getadd()
print(test.name)
print(test.add)
# demo.__display()
