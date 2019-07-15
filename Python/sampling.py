#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
f = open(r'E:\暑期任务\Python\data\oregonf.txt')
out = open(r'E:\暑期任务\Python\data\oregonf.csv', 'w+', newline='')
while True:
    lines = f.readline().replace('\t', ' ').replace('\n', '')
    if not lines:
        break
    x = lines.split(' ')
    csv_write = csv.writer(out, dialect='excel')
    b = [x[0], x[1]]
    print(b)
    csv_write.writerow(b)
