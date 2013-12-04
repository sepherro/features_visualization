from numpy import genfromtxt
from pylab import *
import glob
import os
import numpy
import pylab


def get_match_time(dataset_path):
    file_data = genfromtxt(dataset_path, delimiter=';')
    stripped_name = dataset_path.split("\\")[1]
    detector = stripped_name.split("_")[0]
    descriptor =stripped_name.split("_")[1]

    time_per_feature =  (1000*file_data[1:119,29])/(file_data[1:119,2])/(file_data[1:119,3])
    avg_time = sum(time_per_feature)/len(time_per_feature)

    print("time per feature is ", avg_time, "milliseconds")

    return(detector, avg_time)

proc_times = []

labels = ("BRIEF", "BRISK", "FREAK", "ORB", "SIFT", "SURF")

proc_times.append( get_match_time("results_set002\\orb_brief_set002.txt")[1] )
proc_times.append( get_match_time("results_set002\\orb_brisk_set002.txt")[1] )
proc_times.append( get_match_time("results_set002\\orb_freak_set002.txt")[1] )
proc_times.append( get_match_time("results_set002\\orb_orb_set002.txt")[1] )
proc_times.append( get_match_time("results_set002\\orb_sift_set002.txt")[1] )
proc_times.append( get_match_time("results_set002\\orb_surf_set002.txt")[1] )

positions = (1, 2, 3, 4, 5, 6)


plt.bar(positions, proc_times, align='center')
plt.xticks(positions, labels)
plt.ylabel('avg. time/feature [ms]')
plt.show()
