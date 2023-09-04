import os.path

import matplotlib.pyplot as plt

from extract_data import extract_data


def plot(filename: str):
    extracted_data, trimmed_file_name = extract_data(filename)
    if not os.path.isdir("results_plot"):
        os.mkdir("results_plot")
    for key, value in extracted_data.items():
        visited_nodes = [int(element[1]) for element in extracted_data[key]]
        plt.plot(visited_nodes, label="Visited nodes for " + key)
        plt.legend()
        plt.savefig("results_plot/" + trimmed_file_name + "_visited_nodes_" + key + ".png")
        plt.clf()
        seconds_elapsed = [float(element[2]) for element in extracted_data[key]]
        plt.plot(seconds_elapsed, label="Seconds elapsed for " + key)
        plt.legend()
        plt.savefig("results_plot/" + trimmed_file_name + "_seconds_elapsed_" + key + ".png")
        plt.clf()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plot results from a file.')
    parser.add_argument('filename', type=str, help='The file to plot.')
    args = parser.parse_args()
    plot(args.filename)
