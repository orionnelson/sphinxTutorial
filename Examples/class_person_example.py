class Person:
    """
    A class representing a person.

    :param name: The name of the person.
    :type name: str
    :param age: The age of the person.
    :type age: int
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        Return a greeting for the person.

        :return: A greeting string.
        :rtype: str
        """
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    def celebrate_birthday(self) -> None:
        """
        Increment the person's age by one.

        :return: None
        """
        self.age += 1
        print(f"Happy birthday, {self.name}! You're now {self.age} years old.")

    def introduce(self) -> str:
        """
        Introduce the person.

        :return: An introduction string.
        :rtype: str
        """
        return f"My name is {self.name} and I'm {self.age} years old. {self.greet()}"

def create_person(name: str, age: int) -> Person:
    """
    Create a new person object.

    :param name: The name of the person.
    :type name: str
    :param age: The age of the person.
    :type age: int
    :return: A new Person object.
    :rtype: Person
    """
    return Person(name, age)
