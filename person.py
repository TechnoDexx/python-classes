from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        """
    The __init__ function is called when the class is instantiated.
    It initializes the data attributes of an instance to default values,
    and it can also initialize other things as well.

    :param self: Represent the instance of the class
    :param name: Initialize the name attribute of the instance
    :param job: Set the job attribute of the object
    :param pay: Set the pay attribute of the object
    :return: An instance of the class
    :doc-author: Trelent
    """
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        """
    The LastName function returns the last name of a person.

    :param self: Refer to the object itself
    :return: The last name of the person
    :doc-author: Trelent
    """
        return self.name.split()[-1]

    def giveRaise(self, percent):
        """
    The giveRaise function takes a percent argument and multiplies the pay attribute by (100 + percent) / 100.
    The result is assigned back to the pay attribute, overwriting its prior value.

    :param self: Represent the instance of the class
    :param percent: Determine the amount of raise given to an employee
    :return: The self
    :doc-author: Trelent
    """
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):
    #     """
    # The __str__ function is called when you use the print function or when you tell Python
    # to convert your object to a string.
    # For example, if I have an object x and I do this:
    # print(x)
    # or this:
    # str(x)
    #
    # :param self: Refer to the instance of the class
    # :return: A string representation of the object
    # :doc-author: Trelent
    # """
    #     return '[Person: {0}, {1}]'.format(self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        """
    The __init__ function is called when the class is instantiated.
    It sets up the instance for use, accepting arguments that will become attributes of the instance.
    The self argument refers to the instance object itself; it must always be included as an argument in __init__.

    :param self: Refer to the instance of the class
    :param name: Initialize the name attribute of the person class
    :param pay: Set the pay attribute of the person class
    :return: The instance object automatically; you don’t need to code a return statement
    :doc-author: Trelent
    """
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        """
    The giveRaise function is a method that takes two arguments, percent and bonus.
    The default value for the bonus argument is .10. The giveRaise function calls the
    giveRaise function from Person with self as an argument and adds percent to it.

    :param self: Refer to the object that is currently being processed
    :param percent: Determine the amount of raise
    :param bonus: Add a bonus to the raise
    :return: The value of the giveRaise function in the person class
    :doc-author: Trelent
    """
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):

        """
    The __init__ function is called when the class is instantiated.
    It takes as arguments any number of objects, and adds them to a list
    called self.members.

    :param self: Represent the instance of the class
    :param *args: Pass a variable number of arguments to the function
    :return: The instance of the class
    :doc-author: Trelent
    """
        self.members = list(args)

    def addMember(self, person):
        """
    The addMember function adds a person to the members list of a group.


    :param self: Represent the instance of the class
    :param person: Add a person to the members list
    :return: Nothing
    :doc-author: Trelent
    """
        self.members.append(person)

    def giveRaises(self, percent):
        """
    The giveRaises function takes a percent argument and applies it to the giveRaise
     function for each member of the Manager class.


    :param self: Refer to the instance of the class
    :param percent: Determine the percentage of raise that is given to each member
    :return: Nothing
    :doc-author: Trelent
    """
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        """
    The showAll function prints out all the members of a given group.
        It takes no arguments, and returns nothing.

    :param self: Access the attributes and methods of the class
    :return: The list of members
    :doc-author: Trelent
    """
        for person in self.members:
            print(person)


def self_test():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
    print('~' * 90)
    development = Department(sue, bob)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    print(bob)


if __name__ == '__main__':
    self_test()
