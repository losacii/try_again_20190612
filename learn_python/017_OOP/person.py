# coding:utf-8

class Person(object):
    def __init__(self, name, age=None, pay=None, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent=0.01):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return "{} => {}".format(self.__class__.__name__, self.name)


class Manager(Person):
    """
    a person with custom raise
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent=0.01, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == "__main__":
    bob = Person("Bob Smith", 42, 30000, 'software')
    sue = Person("Sue Jones", 45, 40000, 'hardware')

    sue.giveRaise()
    print(sue.pay)

    tom = Manager('Tome Doe', 50, 50000)
    tom.giveRaise(0.1)
    print(tom.pay)

    print(tom)