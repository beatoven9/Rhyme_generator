#!/usr/bin/env python

from common_words.histogram import create_histogram
import sys
import os

def main():
    compile_histograms(sys.argv[1])

def compile_histograms(target_dir):
    main_histogram = {}
    
    for file in os.listdir(target_dir):
        histogram = create_histogram(os.path.join(target_dir, file))
        for key in histogram.keys():
            main_histogram[key] = main_histogram.setdefault(key, 0) + histogram[key]
    
    hist_list = []
    for key in main_histogram.keys():
        hist_list.append((main_histogram[key], key))

    hist_list.sort(reverse=True)

    counter = 0
    max_count = 10000
    for word in hist_list:
        if counter <= max_count:
            print(word)
            counter += 1
        else:
            break

if __name__ == "__main__":
    main()