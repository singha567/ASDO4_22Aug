""" lab  score 10/10 for pylint"""

def count(sequence, item):
    """ function """
    ret_output = 0
    for number in sequence:
        if number == item:
            ret_output += 1
    return ret_output
