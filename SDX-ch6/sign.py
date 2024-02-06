# [sign]
def sign(value):
     # raise TypeError for invalid input type
    if type(value) != int:
        raise TypeError('value is of invalid type')
    if value < 0:
        return -1
    else:
        return 1
# [/sign]