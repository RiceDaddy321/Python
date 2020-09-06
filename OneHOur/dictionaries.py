# You can not easily combine dictionaries using the "+" operator like you can with lists

super_villains = {"Fiddler": "Isaac Bowin",
                  "Captain Cold": "Leonard Snart",
                  "Weather man": "Mark Mandon",
                  "Mirror Master": "Sam Scudder",
                  "Pied Piper": "Thomas Peterson"}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']
print(super_villains)

super_villains['Pied Piper'] = 'Harthy Hathaway'

print(len(super_villains))

print(super_villains.get('Pied Piper '))

print(super_villains.keys())

print(super_villains.values())
