#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if ((N%2 == 1) & (N >= 1) & (N <= 100)):
        print("Weird")
    elif ((N%2 == 0) & (N >= 2) & (N <= 5)):
        print("Not Wierd")
    elif ((N%2 == 0) & (N >= 6) & (N <= 20)):
        print("Weird")
    elif ((N%2 == 0) & (N > 20) & (N <= 100)):
        print("Not Weird")