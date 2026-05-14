#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from data_profiling import ProfileReport


import load_data

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--input", type=str, default=load_data.DATA_FILE, help="Input file")


def describe_data(data):
    # TODO
    return

def data_report(data, report_path="reports/autoreport.html"):
    # profile = ProfileReport(data, title="Data Report", explorative=True).to_file(report_path)
    profile = ProfileReport(data, title="Data Report").to_file(report_path)

    profile.to_file(report_path)
    # profile.to_notebook_iframe()
    return report_path

def main(args):
    data = load_data.get_matrix_data(args.input)
    data_report(data)





if __name__ == "__main__":
    args = parser.parse_args()

    main(args)