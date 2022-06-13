from numpy import load
import numpy as np


def load_data():
    #will create a more generalized version .. right now proof of concept
    ag2l = load('/Users/krol/research/Summer2022/Inversion Benchmark Files/ag1000g_2L_gambiae_full.npz')
    return ag2l

def slide_(allele_counts, windowsize, stepsize):
    print("WINDOWS")
    for y in range(0, allele_counts.shape[0], stepsize):
        for x in range(0, allele_counts.shape[1], stepsize):
            yield allele_counts[y:y + windowsize[1], x:x + windowsize[0]]
            #print(result)
            #yield result

def main():
    #grab the data
    data = load_data()
    counts = data['allele_counts']
    #positions = data['positions']
    #mask = data['mask']
    slide_(counts, np.array([5,5]), 1)



if __name__ == "__main__":
    main()
