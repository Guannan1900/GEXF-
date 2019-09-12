import pandas as pd
import networkx as nx
import statistics
import numpy as np
import argparse
import time

def missing_value(inputgexf, geneexp, output):
    Graph = nx.read_gexf(inputgexf)
    gene_exp = pd.read_csv(geneexp, sep=",", usecols=['gene', 'expression_value'])
    median = gene_exp['expression_value'].median()
    node_label = nx.get_node_attributes(Graph, 'label')
    gene_exp_label = nx.get_node_attributes(Graph, 'gene-exp')
    node_label_df = pd.DataFrame.from_dict(node_label, orient='index', columns=['Nodes'])
    gene_exp_label_df = pd.DataFrame.from_dict(gene_exp_label, orient='index', columns=['gene-exp'])
    joined_df = node_label_df.join(gene_exp_label_df)
    miss = joined_df.fillna(median)
    new_node_attribute = pd.pivot_table(miss, columns=['Nodes'], values=['gene-exp'])
    nx.set_node_attributes(Graph, new_node_attribute)
    nx.write_gexf(Graph, output)


def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-inputgexf',required=True)
    parser.add_argument('-geneexp',required=True)
    parser.add_argument('-output',required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = getArgs()
    network = missing_value(args.inputgexf, args.geneexp, args.output)
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))




#print (Graph.nodes['10'])