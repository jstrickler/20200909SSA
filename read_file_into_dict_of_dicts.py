"""
Demo script for SSA Python Intro class

This script demonstrates the importance of docstrings.
"""
from pprint import pprint


def main():
    """
    Program entry point
    """
    knight_data = read_data()

    pprint(knight_data)

    print(get_value(knight_data, 'Arthur', "color"))
    print(get_value(knight_data, 'Robin', "quest"))
    print()

    print_titles(knight_data)


def read_data():
    """
    Read knight data from file into dictionary where key is knight name, and value is
    dictionary of knight fields.

    :return: Dictionary of knight info.
    """
    knight_data = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, *_ = line.split(':')
            knight_data[name] = {
                'title': title,
                'color': color,
                'quest': quest, # , comment
            }
    return knight_data


def get_value(data, knight, field_name):
    """
    Retrieve one value from specified knight

    :param data: Dict of knight info
    :param knight: Knight name as string
    :param field_name: field name as string
    :return: field value
    """
    return data[knight][field_name]


def print_titles(data):
    """
    Output knights with their titles.

    :param data: Dict of knight info
    :return: None
    """
    for name, fields in data.items():
        print(fields["title"], name)

if __name__ == '__main__': # if run directly, not imported
    main()
