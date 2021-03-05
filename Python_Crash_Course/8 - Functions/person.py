def build_person(first_name, last_name, age=''):
    """return a dictionaryof information about a person"""
    person = {'first': first_name, 'last': last_name, 'age': age}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
