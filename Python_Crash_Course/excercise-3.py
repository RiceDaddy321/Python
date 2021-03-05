# 3.4
dinner_invitations = ['Pestillence', 'Sword', 'Famine', 'Wild Beasts']
print(dinner_invitations[0] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[1] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[2] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[3] + ", you are cordially invited to my dinner tonight!")

# 3.5
print('Unfortunately, ' + dinner_invitations[-1] + ' Couldn\'t make it tonight')

dinner_invitations[-1] = 'War'

print(dinner_invitations[0] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[1] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[2] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[3] + ", you are cordially invited to my dinner tonight!")

# 3.6
print('I found a larger table.')

dinner_invitations.insert(0, 'Beetle')
dinner_invitations.insert(4, 'Beetle')
dinner_invitations.append('brother')

print(dinner_invitations[0] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[1] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[2] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[3] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[4] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[5] + ", you are cordially invited to my dinner tonight!")
print(dinner_invitations[6] + ", you are cordially invited to my dinner tonight!")

# 3.7
print('Table is not coming. Can only have two guests. :(')

print('Sorry ' + dinner_invitations.pop() + ', You are not invited.')
print('Sorry ' + dinner_invitations.pop() + ', You are not invited.')
print('Sorry ' + dinner_invitations.pop() + ', You are not invited.')
print('Sorry ' + dinner_invitations.pop() + ', You are not invited.')
print('Sorry ' + dinner_invitations.pop() + ', You are not invited.')

print(dinner_invitations[0] + ' you are still invited')
print(dinner_invitations[1] + ' you are still invited')

# 3.9
print('There will be ' + str(len(dinner_invitations)) + ' people at my feast')
