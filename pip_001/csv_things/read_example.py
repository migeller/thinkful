#!/usr/bin/env python


"""

 MetaCode _____, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.

"""

__author__ = 'MetaCode, Inc.'
__version__ = 'Revision 1.0'
__date__ = '9/5/14 8:48 AM'
__copyright__ = 'Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.'
__license__ = 'Python'
__ide__ = 'PyCharm'


import csv

def csv_dict_reader(file_obj):
    """

    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print (line["first_name"]),
        print (line["last_name"])

if __name__ == "__main__":
    csv_path = "data.csv"
    with open(csv_path) as f_obj:
        csv_dict_reader(f_obj)