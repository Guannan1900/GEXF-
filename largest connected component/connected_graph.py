import pandas as pd
import networkx as nx
import numpy as np
import argparse
import time


def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-inputgexf',required=True,help='GEXF network')
    parser.add_argument('-output',required=True,help='network output file')
    return parser.parse_args()


def create_network(inputgexf, output):
    G = nx.read_gexf(inputgexf)
    Gc = max(nx.connected_component_subgraphs(G), key=len)
    nx.write_gexf(Gc, output)



if __name__ == "__main__":

    args = getArgs()
    network = create_network(args.inputgexf, args.output)
    start = time.time()
    end = time.time()

    print ('time elapsed:' + str(end - start))
