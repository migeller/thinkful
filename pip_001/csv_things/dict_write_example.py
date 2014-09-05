#!/usr/bin/env python

"""

 MetaCode _____, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.

"""

__author__ = 'MetaCode, Inc.'
__version__ = 'Revision 1.0'
__date__ = '9/5/14 10:55 AM'
__copyright__ = 'Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.'
__license__ = 'Python'
__ide__ = 'PyCharm'

import csv

def csv_dict_writer(path, fieldnames, data):
    """

    Writes a CSV file using DictWriter
    """
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

path = "dict_output.csv"
csv_dict_writer(path, fieldnames, my_list)