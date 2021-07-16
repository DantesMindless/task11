# task1
class Person():
    def __init__(self, name, lastname, age):
        self.age = age
        self.lastname = lastname
        self.name = name


class Student(Person):
    def __init__(self, name, lastname, age, marks, ):
        super().__init__(name, lastname, age)
        self.marks = marks
        self.reputation = ''

    def good_student(self):
        self.reputation = 'This students skills are good'
        return self.reputation

    def bad_student(self):
        self.reputation = 'This students skills are bad'
        return self.reputation

    def display_student(self):
        print(f'Students fullname is {self.name} {self.lastname}. He/she is {self.age} years old . His/her average marks are {self.marks}')


class Teacher(Person):
    def __init__(self, name, lastname, age, salary, ):
        super().__init__(name, lastname, age)
        self.salary = salary

    def display_teacher(self):
        print(f'Students fullname is {self.name} {self.lastname}. He/she is {self.age}. His/her salary is {self.salary}$')

    def good_teacher(self):
        print(f'Due to your vote his salary now is  {str(self.salary + 20)}$')

    def bad_teacher(self):
        print(f'Due to your vote his salary is still  {self.salary}$')


teacher = Teacher('Chel', 'Chel', '30', 700)
student = Student('Chel', 'Chel', '15', '11, 12, 10 ,9')
student.display_student()
st_rep = input('Is he/she a good student Y/N? ').capitalize()
if st_rep == 'Y':
    print(student.good_student())
elif st_rep == 'N':
    print(student.bad_student())
teacher.display_teacher()

tchr_rep = input('Is he/she a good teacher Y/N? ').capitalize()
if st_rep == 'Y':
    teacher.good_teacher()
elif st_rep == 'N':
    teacher.bad_teacher()


# # task2

choice = input('Choose operation : Remove positives, square numbers, filter leap years ').lower()
nums = [int(num) for num in input('Enter 2 or more numbers ').split()]


class Mathematician():

    def square_nums(self):
        self.nums = nums
        list = [num ** 2 for num in nums]
        return list

    def remove_positives(self):
        self.nums = nums
        list = [num for num in nums if num <= 0]
        return list

    def filter_leaps(self):
        self.nums = nums
        list = [num for num in nums if num % 4 == 0 and num % 100 != 0 or num % 400 == 0]
        return list


m = Mathematician()
if choice == 'square numbers':
    print(m.square_nums())
if choice == 'remove positives':
    m.remove_positives()
if choice == 'filter leap years':
    m.filter_leaps()


# task3



from typing import Dict

class Product:
    def __init__(self, name, ptype, price):
        self.name = name
        self.ptype = ptype
        self.price = price

    def __repr__(self):
        return f"{self.ptype}\t{self.name}"

class Store:
    nacenka: int
    store: Dict

    def __init__(self, name, nacenka):
        self.name = name
        self.nacenka = nacenka
        self.store = {}
        self.moneys = 0

    def add_product(self, prod: Product, count):
        self.store.update({prod: {"count": count, 'sell_price': self.__calcprice(prod.price)}})

    def display(self):
        print(f"Магазин {self.name} В кассе {self.moneys} денег.")
        for prod, value in self.store.items():
            prod: Product
            value: Dict
            print(prod, value)

    def __calcprice(self, prod_price):
        return round(prod_price * (1 + self.nacenka / 100), 3)

    def __get_product(self, name):
        for prod in self.store:
            if prod.name == name:
                return prod
        return None

    def sell(self, prod_name, p_count):
        prod = self.__get_product(prod_name)
        if prod and self.store[prod]["count"] >= p_count > 0:
            self.store[prod]["count"] -= p_count
            self.moneys += self.store[prod]["sell_price"] * p_count









a1 = Product("Хлеб", "Мучное", 10)
a2 = Product("Булка", "Мучное", 12)
a3 = Product("Батон", "Мучное", 14)

s1 = Store("SuperStore", 15)
s2 = Store("ASHOT", 85)

s1.add_product(a1, 10)
s1.add_product(a2, 10)
s1.add_product(a3, 10)

s2.add_product(a1, 5)
s2.add_product(a2, 6)
s2.add_product(a3, 4)
s1.sell('Хлеб', 4)
s1.display()