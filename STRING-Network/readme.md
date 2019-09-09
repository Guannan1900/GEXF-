# Network processing

Creating protein-protein interaction network from STRING database.

1. Node_id_gexf.py : This code will generate a gexf format file from human STRING interaction file (version 11.0). The edges will be labeled with confidence scores and nodes will be labeled with ensembl protein ID (example: ENSP00000000233).
 
 
 
 Example input file = example_interaction.csv
 
 Output file = example.gexf
 
 Command line usage = 'python Node_id_gexf.py -infile example_interaction.csv -outfile example.gexf'. Python3.6.4 and NetworkX 2.3   are required to run this code.
