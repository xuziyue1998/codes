import numpy as np
import os
import scipy.io as scio
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--InputDir')
parser.add_argument('--OutputFile')

args = parser.parse_args()
files_input = os.listdir(args.InputDir)
rst = []
for file in files_input:
    with open(os.path.join(args.InputDir, file)) as fp:
        for line in fp:
            data = line.split(" ")
            feature = data[:-1]
            feature = [float(x) for x in feature]
            name = os.path.split(data[-1])[-1] # 取出名字的描述
            if name not in rst.keys():
                rst[name] = feature
            else:
                rst[name] += feature
names = []
F = []
for key, value in rst.items():
    names.append(key)
    F.append(value)
names = np.array(names, dtype=object).reshape(len(names),1)
F = np.array(F)
scio.savemat(args.OutputFile, {'names':names, 'F':F})
