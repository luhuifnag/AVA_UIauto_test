#coding:utf-8
'''
Created on 2019年05月08日

@author: Aloe
'''
import csv

my_dict = {10: 'E3M12804', 11: 'E3M12798', 12: 'E3M12740', 13: 'E3M13393', 14: 'E3M12402', 15: 'E3M13324', 16: 'E3M12855', 17: 'E3M12971', 18: 'E3M12871', 19: 'E3M13011', 20: 'E3M13418', 21: 'E3M12775', 22: 'E3M12886', 23: 'E3M12994', 24: 'E3M7566', 25: 'E3M12975', 26: 'E3M13405', 27: 'E3M13443', 28: 'E3M12817', 29: 'E3M12771', 30: 'E3M13373', 31: 'E3M12868', 32: 'E3M12767', 33: 'E3M12862', 34: 'E3M12851', 35: 'E3M5014', 36: 'E3M12996', 37: 'E3M11563', 38: 'E3M12756', 39: 'E3M12793', 40: 'E3M13438'}

with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)   #16+6+2+262