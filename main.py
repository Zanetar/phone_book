class Person:
    def __init__(self,name,last_name,adress,phone):
        self.name=name
        self.last_name=last_name
        self.adress=adress
        self.phone=phone

    def __repr__(self):
        return (f'to jest rekord:{self.name} {self.last_name}, adress:{self.adress} phone number {self.phone}')

    def print_all(self,person):
        print (person)

    def print_adress(self,person):
        print (person.name)
        print( person.last_name)
        print(person.adress)

    def print_phone(self,person):
        print(person.name)
        print(person.last_name)
        print(person.phone)

def make_person():
    record=Person((input('Wpisz imię')),(input('Wpisz nazwisko')),(input('Wpisz adres')),(input('Wpisz nr tel')))
    return record

class Phone_book:
    def __init__(self):
        self.taken_place=[]
        self.max_place=50
        self.list_to_export=[]


    def add_person(self,person):
        if person==0:
            if len(self.taken_place)==self.max_place:
                print('Nie można dodać więcej rekordów.Książka jest pełna!')
            else:
                person=make_person()
                self.taken_place.append(person)
                data=[person.name,person.last_name,person.adress,person.phone]
                for i in data:
                    self.list_to_export.append(i)
        else:
            self.taken_place.append(person)
            data = [person.name, person.last_name, person.adress, person.phone]
            for i in data:
                self.list_to_export.append(i)
        return self.list_to_export


def export_to_file(phone_book):
    list_to_export= phone_book.list_to_export
    file=open('records.txt','a')
    for i in list_to_export:
        file.write(i)
    print('dodano!')
    file.close()

def add_person_to_file(phone_book,person):
    if person==0:
        if len(phone_book.taken_place) == phone_book.max_place:
            print('Nie można dodać więcej rekordów.Książka jest pełna!')
        else:
            person = make_person()
            phone_book.taken_place.append(person)
            data = [person.name, person.last_name, person.adress, person.phone]
            file=open('records.txt','a')
            for i in data:
                file.write(i)
                print('dodano!')
            file.close()
            return
    else:
        phone_book.taken_place.append(person)
        data = [person.name, person.last_name, person.adress, person.phone]
        file=open('records.txt','a')
        for i in data:
            file.write(i)
        print('dodano!')
        file.close()
        return

def export_to_file(phone_book):
    list_to_export = phone_book.list_to_export
    file = open('records.txt', 'a')
    for i in list_to_export:
        file.write(i)
    print('dodano!')
    file.close()

human=Person('Anna','Karis','Katowice ul pazdziocha', '333444555')
test=Phone_book()
'''test.add_person(0)
print(test.taken_place)
export_to_file(test)'''''

add_person_to_file(test,human)