"""
p13.py:
    Consider a dictionary as follows, all the value values in the dictionary except duplicate values
    Put it in a list and print it

    speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,
      'july':54, 'Aug':44, 'Sept':54}

    Output:

    [47, 52, 44, 53, 54]
"""

if __name__ == "__main__":
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52,'June': 53,
            'july': 54, 'Aug': 44, 'Sept': 54}

    list = [a for a in set(speed.values())]

    print(sorted(list))