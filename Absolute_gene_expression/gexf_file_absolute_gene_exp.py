import pandas as pd
import networkx as nx
import numpy as np
import argparse
import time

def adding_geneexp_absolute_value(inputgexf, geneexp, output):
    Graph = nx.read_gexf(inputgexf)
    protein_labels = nx.get_node_attributes(Graph, 'ENSP-ID')
    node_labels = nx.get_node_attributes(Graph, 'label')
    protein_dict = pd.DataFrame.from_dict(protein_labels, orient='index', columns=['ENSP-ID'])
    node_dict = pd.DataFrame.from_dict(node_labels, orient='index', columns=['Nodes'])
    dictionary = node_dict.join(protein_dict)
    gene_exp = pd.read_csv(geneexp, sep=",", usecols=['gene', 'expression_value'])
    merged_geneexp_Nodes = pd.merge(gene_exp, dictionary, left_on=['gene'], right_on=['ENSP-ID'], how='right')
    new_df = merged_geneexp_Nodes[['Nodes', 'expression_value']]
    new_df.columns = ['Nodes', 'gene-exp']
    new_df_pivot= pd.pivot_table(new_df, columns=['Nodes'], values=['gene-exp'])
    nx.set_node_attributes(Graph, new_df_pivot)
    nx.write_gexf(Graph, output)



def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-inputgexf',required=True)
    parser.add_argument('-geneexp',required=True)
    parser.add_argument('-output',required=True)
    return parser.parse_args()


if __name__ == "__main__":

    args = getArgs()
    network = adding_geneexp_absolute_value(args.inputgexf, args.geneexp, args.output)
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))






