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

fast_seq_mean = []
brisk_seq_mean =[]
gftt_seq_mean = []
harris_seq_mean = []
orb_seq_mean = []
sift_seq_mean = []
star_seq_mean = []
surf_seq_mean = []

seq_temp = numpy.zeros(114)


def plot_set(plot_data):
    legend_labels = ("BRIEF", "BRISK", "FREAK", "ORB", "SIFT", "SURF")
    for i in range (0, 6):
        plot(plot_data[i][0:45], label=legend_labels[i])           # tu wystarczy zmienic przedzial, zeby narysowac odpowiednia czesc wykresu




def get_inlier_percentage(dataset_path):
    file_data = genfromtxt(dataset_path, delimiter=';')
    stripped_name = dataset_path.split("\\")[1]
    detector = stripped_name.split("_")[0]
    descriptor =stripped_name.split("_")[1]

    inlier_ratio = []
    inlier_ratio =  file_data[1:115,3]/file_data[1:115, 2]

    return(detector, descriptor, inlier_ratio)

    print("the number is ", i)



for line in glob.glob("results_set001\*.txt"):
    for word in line.split():
        if line.endswith("_stat.txt")==False:
            (det, desc, inl) = get_inlier_percentage(line)
            if det == "brisk":
                brisk_seq1.append(inl)
                print(desc)
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

for line in glob.glob("results_set002\*.txt"):
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

for line in glob.glob("results_set009\*.txt"):
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

for line in glob.glob("results_set011\*.txt"):
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

for line in glob.glob("results_set028\*.txt"):
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

for line in glob.glob("results_set052\*.txt"):
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


for i in range(0, 6):
    seq_temp = (brisk_seq1[0+i] + brisk_seq1[6+i] + brisk_seq1[12+i] + brisk_seq1[18+i] + brisk_seq1[24+i] + brisk_seq1[30+i])/6
    brisk_seq_mean.append(seq_temp)

for i in range(0, 6):
    seq_temp = (fast_seq1[0+i] + fast_seq1[6+i] + fast_seq1[12+i] + fast_seq1[18+i] + fast_seq1[24+i] + fast_seq1[30+i])/6
    fast_seq_mean.append(seq_temp)

for i in range(0, 6):
    seq_temp = (gftt_seq1[0+i] + gftt_seq1[6+i] + gftt_seq1[12+i] + gftt_seq1[18+i] + gftt_seq1[24+i] + gftt_seq1[30+i])/6
    gftt_seq_mean.append(seq_temp)

for i in range(0, 6):
    seq_temp = (harris_seq1[0+i] + harris_seq1[6+i] + harris_seq1[12+i] + harris_seq1[18+i] + harris_seq1[24+i] + harris_seq1[30+i])/6
    harris_seq_mean.append(seq_temp)

for i in range(0, 6):
    seq_temp = (orb_seq1[0+i] + orb_seq1[6+i] + orb_seq1[12+i] + orb_seq1[18+i] + orb_seq1[24+i] + orb_seq1[30+i])/6
    orb_seq_mean.append(seq_temp)

##################### special treatment - no SIFT-ORB, inserting dummy data

#idx = ( 3, 9, 15, 21, 27, 33)
#np.insert(sift_seq1, idx, 0, axis=1)

sift_seq1.insert( 3, np.zeros(116))
sift_seq1.insert( 9, np.zeros(116))
sift_seq1.insert( 15, np.zeros(116))
sift_seq1.insert( 21, np.zeros(116))
sift_seq1.insert( 27, np.zeros(116))
sift_seq1.insert( 33, np.zeros(116))
#print(sift_seq1)
for i in range(0, 6):
    seq_temp = (sift_seq1[0+i] + sift_seq1[6+i] + sift_seq1[12+i] + sift_seq1[18+i] + sift_seq1[24+i] + sift_seq1[30+i])/6
    sift_seq_mean.append(seq_temp)


##################

for i in range(0, 6):
    seq_temp = (star_seq1[0+i] + star_seq1[6+i] + star_seq1[12+i] + star_seq1[18+i] + star_seq1[24+i] + star_seq1[30+i])/6
    star_seq_mean.append(seq_temp)
    
for i in range(0, 6):
    seq_temp = (surf_seq1[0+i] + surf_seq1[6+i] + surf_seq1[12+i] + surf_seq1[18+i] + surf_seq1[24+i] + surf_seq1[30+i])/6
    surf_seq_mean.append(seq_temp)
    



plt.subplot(2, 4, 1)
plt.ylim([0, 1])
plot_set(brisk_seq_mean)
plt.title("BRISK")

plt.subplot(2, 4, 2)
plt.ylim([0, 1])
plot_set(fast_seq_mean)
plt.title("FAST")

plt.subplot(2, 4, 3)
plt.ylim([0, 1])
plot_set(gftt_seq_mean)
plt.title("GFTT")

plt.subplot(2, 4, 4)
plt.ylim([0, 1])
plot_set(harris_seq_mean)
plt.title("HARRIS")

plt.subplot(2, 4, 5)
plt.ylim([0, 1])
plot_set(orb_seq1)
plt.title("ORB")

plt.subplot(2, 4, 6)
plt.ylim([0, 1])
plot_set(sift_seq_mean)
plt.title("SIFT")

plt.subplot(2, 4, 7)
plt.ylim([0, 1])
plot_set(star_seq_mean)
plt.title("STAR")

plt.subplot(2, 4, 8)
plt.ylim([0, 1])
plot_set(surf_seq_mean)
plt.title("SURF")

legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

show()




