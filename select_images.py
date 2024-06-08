import os

file_dir = '/mnt/1TBSSD/lanyunz/data/lerf_ovs/teatime/images'
files = os.listdir(file_dir)
for f in files:
    print(int(f[6:11]))
