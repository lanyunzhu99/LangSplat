import os

file_dir = '/mnt/1TBSSD/lanyunz/data/lerf_ovs/teatime_train/images'
files = os.listdir(file_dir)
for f in files:
    num = int(f[6:11])
    if num // 10 == 0:
        print(num)