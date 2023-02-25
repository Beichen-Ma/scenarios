# Multiprocessing Programming

## Problem Statement

You have been given a large dataset of 1 million numbers in the range of 1 to 100. Your task is to find the sum of all the numbers in the dataset.

You need to write a Python program that performs the following steps:

1. Generate the dataset of 1 million random numbers in the range of 1 to 100.
2. Divide the dataset into 4 equal parts.
3. Create 4 separate processes to compute the sum of each part of the dataset in parallel using the `multiprocessing` module.
4. Sum up the results from each process to obtain the total sum of all the numbers in the dataset.

## Requirements

Your Python program should meet the following requirements:

- The program should use the `multiprocessing` module to create and manage the separate processes.
- The program should divide the dataset into 4 equal parts and distribute them among the processes.
- The program should use inter-process communication to collect the results from each process and sum them up to obtain the final result.
- The program should print the final result to the console.