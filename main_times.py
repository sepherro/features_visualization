from numpy import genfromtxt
from pylab import *
import glob
import os
import numpy
import pylab

def get_processing_time(dataset_path):
    file_data = genfromtxt(dataset_path, delimiter=';')
    stripped_name = dataset_path.split("\\")[1]
    detector = stripped_name.split("_")[0]
    descriptor =stripped_name.split("_")[1]

    #do cech
    # 1 nFeatures # 2 processing time

    time_per_feature = []
    time_per_feature =  (file_data[1:115,2]*1000)/file_data[1:115, 1]
    avg_time = sum(time_per_feature)/len(time_per_feature)

    print("time per feature is ", avg_time, "milliseconds")

    return(detector, avg_time)

proc_times = []
labels = ("BRISK", "FAST", "GFTT", "HARRIS", "ORB", "SIFT", "STAR", "SURF")

proc_times.append( get_processing_time("results_set001\\brisk_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\fast_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\gftt_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\harris_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\orb_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\sift_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\star_brisk_set001_stat.txt")[1] )
proc_times.append( get_processing_time("results_set001\\surf_brisk_set001_stat.txt")[1] )

#TODO: Dobrać odpowiednio czasy

positions = (1, 2, 3, 4, 5, 6, 7, 8)

plt.bar(positions, proc_times, align='center')
plt.xticks(positions, labels)
plt.ylabel('avg. time/feature [ms]')
plt.show()


