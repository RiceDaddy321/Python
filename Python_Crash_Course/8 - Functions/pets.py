# showcases positional arguments: Matching each argument with a parameter.
def describe_pet(animal_type, pet_name='dog'): # dog is a default parameter for pet_name
    """Display information about a pet"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("dog", "katie")
describe_pet("Green anole", "Padme")

#example of keyword argument
describe_pet(animal_type='hamster', pet_name='Toby')