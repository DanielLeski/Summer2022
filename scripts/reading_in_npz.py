#!/usr/bin/env python3
from numpy import load 
import numpy as np
import os


def process_npz():
    dir = "/home/smol/Inversion Benchmark Files/"
    dir_list = os.listdir(dir)
    print("Printing files in the directory'", dir, "' :")
    print(dir_list)




if __name__ == '__main__':
    process_npz()
