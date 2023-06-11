import sys
import string
from collections import defaultdict


# read input file and create interference graph
def get_input(input_file):
    graph = {}
    with open(input_file) as f:
        for line in f:
            node, *neighbors = map(int, line.split())
            graph[node] = set(neighbors)

    # sort the graph in descending order of the number of neighbors
    graph = dict(sorted(graph.items(), key=lambda x: len(x[1]), reverse=True))
    return graph


# color the graph using algorithm
def color(graph):
    colored = defaultdict(int)
    for key, val in graph.items():
        colors = list(string.ascii_uppercase)

        for node in graph[key]:
            # if the neighbor is already colored, remove its color
            # from the list of possible colors
            if colored[node] in colors:
                colors.remove(colored[node])

        try:
            # assign first color in list of remaining colors to node
            colored[key] = colors.pop(0)
        except IndexError:
            # if list is empty, then we have exceeded 26 colors
            return None

    # sort colored dict in ascending order of nodes
    colored = dict(sorted(colored.items()))
    return colored


# write output file with node colors
def write(output_file, colored):
    with open(output_file, 'w') as f:
        for key, val in colored.items():
            f.write(f"{key}{val}\n")


if __name__ == "__main__":
    # validate command line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 program.py input_file output_file")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    # read input file and color graph
    graph = get_input(input_file)
    colored = color(graph)

    if not bool(graph):
        print("Input file is empty! Please provide valid input file.")
        sys.exit(1)

    if not colored:
        print("Error: Cannot color graph with 26 colors or less")
        sys.exit(1)

    write(output_file, colored)
    print(
        f"Least number of colors (registers) used: {len(set(colored.values()))}")
