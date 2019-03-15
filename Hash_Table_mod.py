import string,random
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        input_string=str(value)
        return sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))%self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        value=str(value)
        if None in self.slots:
            slot_adr=self.hash_fun(value)
            print("----------")
            print(slot_adr)
            while self.slots[slot_adr]!=None:
                if self.size-slot_adr-1>=self.step:
                    slot_adr=slot_adr+self.step
                else:
                    slot_adr=self.step-(self.size-slot_adr)
            print(slot_adr,self.size,self.step)
            print("----------")
            return slot_adr
        else: 
            return None
 
    def put(self, value):
         # записываем значение по хэш-функции
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 
        input_string=str(value)
        slot_adr=self.seek_slot(input_string)
        if slot_adr!=None:
            self.slots[slot_adr]=input_string
            return slot_adr
        else:
            return None

    def find(self, value):
         # находит индекс слота со значением, или None
        value=str(value)
        flag=False
        for i in range(len(self.slots)):
            if self.slots[i]==value:
                flag=True
                return i
            else:
                i+=1
        if flag==False:
            return None

"""a=HashTable(23,4)
size=8
st_massive=[]
number_massive=[]
chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
for i in range(23):
    st=''.join(random.choice(chars) for i in range(size))
    st_massive.append(str(st))
    a.put(st)
print(a.slots)
for i in range(len(st_massive)):
    print("цикл 2")
    print(st_massive[i], "Массив входных данных")
    z=a.find(st_massive[i])
    print(i, a.find(st_massive[i]))
    number_massive.append(z)
print(number_massive, "Массив выходных адресов")"""

