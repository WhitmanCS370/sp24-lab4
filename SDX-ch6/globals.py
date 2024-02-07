import pprint
pprint.pprint(globals())

name = None
for name in globals():
    print(name)