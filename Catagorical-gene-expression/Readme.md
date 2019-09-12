# Gene expression addition
Adding catagorical gene expression data from one cell line to the previously build protein protein interaction network


network_gene_expression.py : This code will generate a gexf format file from human STRING interaction file (version 11.0) while adding the gene expression as another attribute for the node.

The edges will be labeled with confidence scores and nodes will be labeled with ensembl protein ID and gene expression example: 
{'ENSP-ID': 'ENSP00000000233', 'Gene-exp': 2.0, 'label': '1'}.

Example input files = 1) example.gexf (The previously build network) 2) ER_pos_T47D (gene expression data from LINCS)

Output file = example-genexp.gexf

Command line usage = 

'python network_gene_expression.py -inputgexf example.gexf -genex ER_pos_T47D -output example-genexp.gexf. 

Python3.6.4 and NetworkX 2.3 are required to run this code.


