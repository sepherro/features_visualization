from numpy import genfromtxt
from pylab import *
import glob
import os
import numpy

#for files in glob.glob("*.txt"):
#    print(files)

inlier_ratio_brisk = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_fast = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_gftt = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_harris = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_orb = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_sift = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_star = numpy.zeros(6*14).reshape(6, 14)
inlier_ratio_surf = numpy.zeros(6*14).reshape(6, 14)

for line in glob.glob("results_set001\*.txt"):
    for word in line.split():
        if line.endswith("_stat.txt")==False:
            my_data = genfromtxt(line, delimiter=';')
            line = line.replace('results_set001\\', '')
            print(line)
            detector = line.split("_")[0]
            descriptor = line.split("_")[1]

            if detector == "brisk":
                if descriptor == "brief":
                    inlier_ratio_brisk[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_brisk[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_brisk[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_brisk[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_brisk[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_brisk[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "fast":
                if descriptor == "brief":
                    inlier_ratio_fast[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_fast[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_fast[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_fast[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_fast[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_fast[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "gftt":
                if descriptor == "brief":
                    inlier_ratio_gftt[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_gftt[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_gftt[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_gftt[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_gftt[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_gftt[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "harris":
                if descriptor == "brief":
                    inlier_ratio_harris[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_harris[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_harris[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_harris[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_harris[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_harris[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "orb":
                if descriptor == "brief":
                    inlier_ratio_orb[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_orb[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_orb[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_orb[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_orb[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_orb[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "sift":
                if descriptor == "brief":
                    inlier_ratio_sift[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_sift[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_sift[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_sift[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_sift[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_sift[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

            if detector == "star":
                if descriptor == "brief":
                    inlier_ratio_star[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_star[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_star[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_star[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_star[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_star[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]


            if detector == "surf":
                if descriptor == "brief":
                    inlier_ratio_surf[0, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "brisk":
                    inlier_ratio_surf[1, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "freak":
                    inlier_ratio_surf[2, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "orb":
                    inlier_ratio_surf[3, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "sift":
                    inlier_ratio_surf[4, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]
                if descriptor == "surf":
                    inlier_ratio_surf[5, 0:14] =  my_data[50:64,3]/my_data[50:64, 2]

legend_labels = ("BRIEF", "BRISK", "FREAK", "ORB", "SIFT", "SURF")


for i in range (0, 5):
    plot(inlier_ratio_fast[i], label = legend_labels[i])
    print(legend_labels[i])

legend(loc='upper right')
plt.figure()

for i in range (0, 5):
    plot(inlier_ratio_sift[i], label = legend_labels[i])
    print(legend_labels[i])

legend(loc='upper right')
plt.figure()

for i in range (0, 5):
    plot(inlier_ratio_star[i], label = legend_labels[i])
    print(legend_labels[i])

legend(loc='upper right')
plt.figure()

for i in range (0, 5):
    plot(inlier_ratio_orb[i], label = legend_labels[i])
    print(legend_labels[i])

legend(loc='upper right')

show()

