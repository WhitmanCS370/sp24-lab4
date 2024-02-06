import pprint
#my_variable = 123
#pprint.pprint(globals())

'''
for name in globals():
    print(name)
    # RuntimeError: dictionary changed size during iteration
'''
name = None
for name in globals():
    print(name)
    # it works
