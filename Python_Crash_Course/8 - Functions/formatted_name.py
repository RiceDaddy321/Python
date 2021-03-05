def get_formatted_name(first_name, last_name, middle_name=''):
        # making middle_name's default value to be an empty string makes it optional
    """Return a full name, nearly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
