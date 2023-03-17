class Animal:
    """
    A base class representing an animal.

    :param name: The name of the animal.
    :type name: str
    """

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        """
        Return the sound that the animal makes.

        :return: A string representing the animal's sound.
        :rtype: str
        """
        pass


class Dog(Animal):
    """
    A class representing a dog.

    :param name: The name of the dog.
    :type name: str
    """

    def __init__(self, name: str):
        super().__init__(name)

    def speak(self) -> str:
        """
        Return the sound that the dog makes.

        :return: A string representing the dog's bark.
        :rtype: str
        """
        return "Woof!"


class Cat(Animal):
    """
    A class representing a cat.

    :param name: The name of the cat.
    :type name: str
    """

    def __init__(self, name: str):
        super().__init__(name)

    def speak(self) -> str:
        """
        Return the sound that the cat makes.

        :return: A string representing the cat's meow.
        :rtype: str
        """
        return "Meow!"


class PetStore:
    """
    A class representing a pet store.

    :param pets: A list of Pet objects.
    :type pets: list
    """

    def __init__(self, pets: list):
        self.pets = pets

    def get_pets(self) -> list:
        """
        Return the list of pets in the store.

        :return: A list of Pet objects.
        :rtype: list
        """
        return self.pets

    def add_pet(self, pet: Animal) -> None:
        """
        Add a new pet to the store.

        :param pet: The pet to add.
        :type pet: Animal
        :return: None
        """
        self.pets.append(pet)
