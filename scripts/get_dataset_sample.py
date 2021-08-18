import argparse
from pathlib import Path
from functools import partial
from typing import List, Dict
import json
import random

def get_sample(arguments):
    input_file = Path(arguments.file_path).resolve()
    output_file = Path(arguments.result_path).resolve()
    if not input_file.exists():
        raise Exception("Input file does not exist")
    if output_file.exists():
        raise Exception("Output file exists! Provide non-existent filename")

    N = int(arguments.N)
    with open(input_file, "r") as fin:
        lines = fin.readlines()


    sample = random.sample(lines, N)

    with open(output_file, "w") as fout:
        for line in sample:
            fout.write(line)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description='Create dataset sample'
    )
    parser.add_argument('--file_path', type=str, required=True,
        help='Path to the input file (readable as text, line separated)')
    parser.add_argument('--result_path', type=str, required=True,
        help='Path to the resulting file')
    parser.add_argument('-N', type=str, required=True,
        help='Number of random samples')

    arguments = parser.parse_args()

    get_sample(arguments)