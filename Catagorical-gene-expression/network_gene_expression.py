import pandas as pd
import networkx as nx
import numpy as np
import argparse
import time


def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-inputgexf',required=True,help='GEXF network')
    parser.add_argument('-genexp',required=True,help='gene expression file')
    parser.add_argument('-output',required=True,help='network output file')
    return parser.parse_args()


def create_network(inputgexf, genexp, output):
    G = nx.read_gexf(inputgexf)
    protein_labels = nx.get_node_attributes(G, "ENSP-ID")
    node_labels = nx.get_node_attributes(G, "label")
    protein_dict = pd.DataFrame.from_dict(protein_labels, orient='index', columns=['ENSP-ID'])
    node_dict = pd.DataFrame.from_dict(node_labels, orient='index', columns=['Nodes'])
    dictionary = node_dict.join(protein_dict)
    gene_exp = pd.read_csv(genexp, delim_whitespace=True, header=None)
    gene_exp_transposed = gene_exp.T
    new_header = gene_exp_transposed.iloc[0]
    header_removal = gene_exp_transposed[1:]
    header_removal.columns = ['ENSP-ID', 'Gene-exp']
    final_table = header_removal.copy()
    #final_table['Gene-exp'] = final_table['Gene-exp'].map({'-1.0': 1, '0.0': 2, '1.0':3})
    mapping = dictionary.merge(final_table, on=['ENSP-ID'], how='left')
    #mapping = mapping.fillna(0)
    node_attr1 = dict(zip(mapping.Nodes, mapping['Gene-exp']))
    nx.set_node_attributes(G, node_attr1, 'Gene-exp')
    nx.write_gexf(G, output)



if __name__ == "__main__":

    args = getArgs()
    network = create_network(args.inputgexf, args.genexp, args.output)
    start = time.time()
    end = time.time()

    print ('time elapsed:' + str(end - start))
