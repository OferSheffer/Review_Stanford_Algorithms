'''
Created on Nov 4, 2015

@author: Ofer
'''
import pstats

if __name__ == '__main__':
    p = pstats.Stats('restats')
    p.strip_dirs().sort_stats('time').print_stats(10)
