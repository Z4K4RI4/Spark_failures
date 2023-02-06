import sys
import os
import pandas

def file2dict(path: str):
    filelist = os.listdir(path)
    output = dict()
    for file in filelist:
        with open(f'{path}/{file}', 'r' ) as f:
            lines = f.read().split('\n')
            # print(lines)
            for line in lines:
                test = line.split(',')
                if len(test) != 2:
                    continue
                k = test[0].split("'")[1]
                v = test[1].split(')')[0]
                output[k] = v
    return output

refdict = file2dict("outputTrue")
WorkerDowndict = file2dict("outputWorkerDown")
JobWorkerDowndict = file2dict("outputWorkerDownWithJob")
NamenodeDowndict = file2dict("outputNamenodeDown")

for k in refdict:
    if refdict[k] != WorkerDowndict[k]:
        assert len(refdict) == len(WorkerDowndict)
        print(f'WorkerDown: {k} {refdict[k]} {WorkerDowndict[k]}')

    if refdict[k] != JobWorkerDowndict[k]:
        assert len(refdict) == len(JobWorkerDowndict)
        print(f'JobWorkerDown: {k} {refdict[k]} {JobWorkerDowndict[k]}')

    if refdict[k] != NamenodeDowndict[k]:
        assert len(refdict) == len(NamenodeDowndict)
        print(f'NamenodeDown: {k} {refdict[k]} {NamenodeDowndict[k]}')
