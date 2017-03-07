'''
Created on 7 Mar 2017

@author: thomasflood
'''

# code for 'Introducting positional arguments'
# as per Python documentation
# the argparse module will be used in the 'main' function
# it will act as interface between program and user

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
