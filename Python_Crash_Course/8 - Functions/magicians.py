def show_magicians(magicians=''):
    if magicians:
        for magician in magicians:
            print(magician)


def make_great(magicians=''):
    for i in range(0, len(magicians)):
        magicians[i] += " the Great"
        print(magicians[i])


magicians = ['brtoher', 'whodini', 'copperlane']
make_great(magicians[:])
show_magicians(magicians)
