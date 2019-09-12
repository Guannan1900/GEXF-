
Adding absolute gene expression data to pre-existing STRING network graph.

gexf_file_absolute_gene_exp.py : This code will generate a gexf format file after adding absolute gene expression to the nodes of pre-exsisting STRING neywork graph. After using this code the nodes will get another attribute which is absolute gene expression (example: -0.971084952354).

Example inputgexf = Graph_example.gexf

gene expression = Q9P0X4_DB00381_A375_10.csv

Output file = Graph_example_gene_expression.gexf

Command line usage = 'python gexf_file_absolute_gene_exp.py -inputgexf Graph_example.gexf -geneexp Q9P0X4_DB00381_A375_10.csv -output Graph_example_gene_expression.gexf'. Python3.6.4 and NetworkX 2.3 are required to run this code.
