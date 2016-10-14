#!/usr/bin/env python

import csv
import sys


def convert_csv(file_path):
    file_name = file_path.replace(".csv", "")
    csv_reader = csv.reader(open("%s.csv" % file_name, "r"))
    csv_writer = csv.writer(open("%s.fixed.csv" % file_name, "w"), quoting=csv.QUOTE_ALL, delimiter=';')
    for line in csv_reader:
        csv_writer.writerow(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Usage: python convert_csv.py /path/to/file.csv")
                                                        
    file_path = sys.argv[-1]
    convert_csv(file_path)
                                                                    
    print "Done."
