class Animal:
    __name = None  # kind of like nil or null
    __height = 0
    __weight = 0
    __sound = 0  # the two leading underscores make the variable private

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):  # the self is there to refer to the animal object
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):  # the self is there to refer to the animal object
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):  # the self is there to refer to the animal object
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):  # the self is there to refer to the animal object
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and weighs {} pounds and says {}.".format(
            self.__name,
            self.__height,
            self.__weight,
            self.__sound)


cat = Animal("Whiskers", 33, 10, 'Meow')

print(cat.toString())


class Dog(Animal):  # the dog class now gets a copy of all of the methods and varibles of the base class: Animal
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


Toby = Dog("Toby", 53, 24, "Ruff", "Juan")

print(Toby.toString())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(Toby)

Toby.multiple_sounds(4)
Toby.multiple_sounds()
