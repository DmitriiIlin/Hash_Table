import Hash_Table_mod,unittest,random,string

def string_generator(size=8):
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


class Hash_table_Tests(unittest.TestCase):

    #Тесты для класса Hash_Table

    def test_hash_fun(self):
        #Проверка метода генерации хеша, hash_fun 
        size=19
        input_string=string_generator()
        sum_1=sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))% size
        hash_for_test=Hash_Table_mod.HashTable(size,4)
        self.assertEqual(sum_1,hash_for_test.hash_fun(input_string))
    
    def test_seek_slot_and_put(self):
        #Проверка поиска пустого хеша, seek_fun и test_put
        size=19
        step=4
        massive_1=[None]*size
        print(massive_1)
        hash_for_test=Hash_Table_mod.HashTable(size,step)
        for i in range(size-1):
            input_string=string_generator()
            slot_address_1=sum(ord(input_string[j])**(j+1) for j in range(len(input_string)))% size
            print(input_string,slot_address_1)
            while massive_1[slot_address_1]!=None:
                if size-slot_address_1-1>=step:
                    slot_address_1=slot_address_1+step
                else:
                    slot_address_1=step-(size-slot_address_1)
            massive_1[slot_address_1]=input_string
            number_2=hash_for_test.put(input_string)
            print(slot_address_1,number_2)
            self.assertEqual(slot_address_1,number_2)
            i+=1
        for i in range(len(massive_1)):
             
    
    




 







if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
