from collections import UserDict
import collections 

#user_data = collections.namedtuple('Contacts',['number', 'number_2', 'number_3', 'e-mail'])

#user_dict = {}

class Field:  # логіка роботи з полями
    
    def __init__(self, value):
        self.value = value
        

class Name(Field):
    
    def value(self, value):
        self.value = value


class Phone(Field):
    
    def value(self, phones):
        self.phones = phones


class Email(Field):
    
    def value(self, emai):
        self.emai = emai


class Record: #тут треба організувати запис та збереження за полями 
    
    def __init__(self, name: Name, phones: Phone =[], email: Email='No mail'):
        self.name = name
        self.phones = phones
        self.email = email
        

class AddressBook(UserDict):
            
    def add_record(self, rec:Record):
        self.data[rec.name.value] = rec
        self.data[rec.phones.value] = rec
        self.data[rec.email.value] = rec
        data_digits = {self.data[rec.phones.value]:self.data[rec.email.value]}
        data_full = {self.data[rec.name.value]: data_digits}
        user_dict = UserDict(data_full)
    
    def delete_record(self, rec:Record):
        user_dict = UserDict()
        self.data[rec.name.value] = rec
        for key in user_dict:
            if key == rec:
                del user_dict[key]
    
    def change_record(self, rec:Record):
        user_dict = UserDict()    #!?!?!?!?!?!?!
        self.data[rec.name.value] = rec
        for key in user_dict:
            if key == rec:
                self.data[rec.phones.value] = rec
                self.data[rec.email.value] = rec
                data_digits = {self.data[rec.phones.value]:self.data[rec.email.value]}
                UserDict[key] = data_digits
    
    def search_record(self, rec:Record):
        user_dict = UserDict()
        self.data[rec.name.value] = rec
        for key in user_dict:
            if key == rec:
                print (user_dict[key])
    
    def show_all(self):
        user_dict = UserDict()
        for key,value in user_dict.items():
            a = print(key,':',value)
        # else:
        #     for key,value in user_dict.items():
        #         if what_number == key:
        #             return value

            
#---------
adress_book = UserDict()
ab = AddressBook(adress_book)
n1 = Name
t1 = Phone
e1 = Email
# recf = Field
# r1 = Record(n1, t1, e1)



def finish(some):
    print('Good Bye')
    return False

operations = {
              'delete': ab.delete_record(n1),\
              'phone': ab.search_record(n1),\
              'show': ab.show_all(n1),\
              'good': finish,\
              'close': finish,\
              'exit': finish,\
              '.': finish}

def get_handler(words):
     return operations[words]
       
def parser_func(string_ask):

    if string_ask == 'add' or string_ask == 'change':
        nmd = input('Name: ')
        n1 = Name(nmd)
        tlph = telephone_number()
        t1 = Phone(tlph)
        emla = email_wright()
        e1 = Email(emla)
        r1 = Record(n1, t1, e1)
        ab.add_record(r1)
        
    else :
        handler = get_handler(string_ask)
        nmd = input('Name: ')
        n1 = Name(nmd)
        return handler (n1)
    
def input_error_command(func):
    def inner():
        try:
            string_ask_dec = func()
            if string_ask_dec not in operations:
                raise Exception('I don`t know this command')
        except Exception as e:
            print (e)
        else:
            return string_ask_dec
    return inner

@input_error_command     
def main_func():
    string_ask_main = input('')
    string_ask_main = string_ask_main.lower()
    nmd = input('Name: ')
    n1 = Name(nmd)
    tlph = telephone_number()
    t1 = Phone(tlph)
    emla = email_wright()
    e1 = Email(emla)
    return string_ask_main

def input_error_phone(func):
    def inner():
        try:
            phone_number = func()
            for numb in phone_number:
                if int(numb) == False:
                    raise Exception('Please, enter the digits')
                elif len(numb) != 10:
                    raise Exception('This is not a number. It should be wth 10 digits')
        except Exception as e:
            print (e)
        else:
            return phone_number
    return inner

@input_error_phone
def telephone_number():
    i = 0
    phone_number = []
    while True:
        pho = input ('Phone? (Start to enter or press N) ')
        if pho == "N" or pho == "n":
            if len(phone_number) == 0:
                phone_number.append('No number')
            break
        else:
            phone_number.append(pho)
        return phone_number

def input_error_email(func):
    def inner():
        try:
            string_ask_dec = func()
            if '@' not in string_ask_dec:
                raise Exception('Please, enter the email')
        except Exception as e:
            print (e)
        else:
            return string_ask_dec
    return inner

@input_error_email                    
def email_wright():
    emai = input ('E-mail? (Start to enter or press N) ')
    if emai == "N" or emai == "n":
        emai = 'No mail'
        return emai     
    else:
        return emai


adress_book = UserDict()
ab = AddressBook(adress_book)
while True:    
    start_string = input('Start with hello \n')
    if start_string == 'hello' or start_string == 'Hello':
        print ('How can I help U?')
        break
    else:
        print ('Please, be polite')
        continue
while True:
    string_ask = main_func() #command
    if string_ask == 'None' or string_ask == None or type(string_ask) == 'NoneType':
        continue
    d = parser_func(string_ask)
    if (type(d)) == bool:
        break
    else:
        print(d)


#Now U should check how it works and then to get an exceptions... 
# and to make a dict , that will be pass to classes




# Name.value = name
# #name = Name.value()
# phone_number = []
# i = -1
# while True:
#     i+=1
#     pho = input ('Phone? (Start to enter or press N) ')
#     if pho == "N" or pho == "n":
#         phone_number[i] = pho
#     else:
#         break 
# emai = input ('E-mail? (Start to enter or press N) ')
# if emai == "N" or emai == "n":
#     phone_mail = emai
# phone_draft = Phone(phone_number, phone_mail)

        

# Record(Field())
# AdressBook(Record())