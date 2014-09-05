#!/usr/bin/env python

"""

 MetaCode _____, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.

"""

__author__ = 'MetaCode, Inc.'
__version__ = 'Revision 1.0'
__date__ = '9/5/14 10:43 AM'
__copyright__ = 'Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.'
__license__ = 'Python'
__ide__ = 'PyCharm'

import csv

def csv_writer(data, path):
    """

    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolsaville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)