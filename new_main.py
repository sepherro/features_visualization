from numpy import genfromtxt
from pylab import *
import glob
import os
import numpy

fast_seq1= []
brisk_seq1= []
gftt_seq1= []
harris_seq1= []
orb_seq1= []
sift_seq1= []
star_seq1= []
surf_seq1= []




def plot_set(plot_data):
    legend_labels = ("BRIEF", "BRISK", "FREAK", "ORB", "SIFT", "SURF")
    for i in range (0, 5):
        plot(plot_data[i], label=legend_labels[i])




def get_inlier_percentage(dataset_path):
    file_data = genfromtxt(dataset_path, delimiter=';')
    stripped_name = dataset_path.split("\\")[1]
    detector = stripped_name.split("_")[0]
    descriptor =stripped_name.split("_")[1]

    inlier_ratio = []
    inlier_ratio =  file_data[:,3]/file_data[:, 2]

    return(detector, descriptor, inlier_ratio)




for line in glob.glob("results_set001\*.txt"):
    for word in line.split():
        if line.endswith("_stat.txt")==False:
            (det, desc, inl) = get_inlier_percentage(line)
            if det == "brisk":
                brisk_seq1.append(inl)
            if det == "fast":
                fast_seq1.append(inl)
            if det == "gftt":
                gftt_seq1.append(inl)
            if det == "harris":
                harris_seq1.append(inl)
            if det == "orb":
                orb_seq1.append(inl)
            if det == "sift":
                sift_seq1.append(inl)
            if det == "star":
                star_seq1.append(inl)
            if det == "surf":
                surf_seq1.append(inl)





plt.subplot(2, 4, 1)
plt.ylim([0, 1])
plot_set(brisk_seq1)
plt.title("BRISK")

plt.subplot(2, 4, 2)
plt.ylim([0, 1])
plot_set(fast_seq1)
plt.title("FAST")

plt.subplot(2, 4, 3)
plt.ylim([0, 1])
plot_set(gftt_seq1)
plt.title("GFTT")

plt.subplot(2, 4, 4)
plt.ylim([0, 1])
plot_set(harris_seq1)
plt.title("HARRIS")

plt.subplot(2, 4, 5)
plt.ylim([0, 1])
plot_set(orb_seq1)
plt.title("ORB")

plt.subplot(2, 4, 6)
plt.ylim([0, 1])
plot_set(sift_seq1)
plt.title("SIFT")

plt.subplot(2, 4, 7)
plt.ylim([0, 1])
plot_set(star_seq1)
plt.title("STAR")

plt.subplot(2, 4, 8)
plt.ylim([0, 1])
plot_set(surf_seq1)
plt.title("SURF")

legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

show()




