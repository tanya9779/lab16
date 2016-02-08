import sys 
import os

if len(sys.argv)<2:
    print ('Укажите хотя бы один файл')
else:
    for arg in sys.argv[1:]:
        with open (arg, 'r') as f :
            for line in f.read().split('\n'):
                print (line) 
