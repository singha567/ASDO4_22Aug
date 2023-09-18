""" Write 2 tests that assert whether a list of integers and strings work with this function """

def count(sequence, item):
    """ function """
    ret_output = 0
    for number in sequence:
        if number == item:
            ret_output += 1
    return ret_output
