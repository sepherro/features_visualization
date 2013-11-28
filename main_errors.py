from numpy import genfromtxt
from pylab import *
import glob
import os
import numpy


def get_error_dist(dataset_path):
    file_data = genfromtxt(dataset_path, delimiter=';')
    stripped_name = dataset_path.split("\\")[1]
    detector = stripped_name.split("_")[0]
    descriptor =stripped_name.split("_")[1]

    error_dist = []
    error_dist =  file_data[1:115,3]/file_data[1:115, 2]

    return(detector, descriptor, error_dist)


