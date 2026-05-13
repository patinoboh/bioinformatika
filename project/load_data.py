#!/usr/bin/env python3
import pandas as pd
import argparse


DATA_FILE = "data/GSE45827_series_matrix.txt"

def get_matrix_data(DATA_FILE=DATA_FILE):
    # TODO read file and return it"
    data = pd.read_csv(DATA_FILE, sep="\t", comment="!", index_col=0)

    return data



if __name__ == "__main__":
    data = get_matrix_data()
    print(data)
