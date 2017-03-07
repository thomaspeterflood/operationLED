'''
Created on 7 Mar 2017

@author: thomasflood
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
