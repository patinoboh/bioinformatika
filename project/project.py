#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

from load_data import get_matrix_data

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--input", type=str, help="Input file")




def describe_data(data):
    # TODO
    return

def data_report(data, report_path="report/autoreport.pdf"):
    from report_path = "report/autoreport.txt"

def main(args):
    data = get_matrix_data(args.input)
    











if __name__ == "__main__":
    args = parser.parse_args()

    main(args)