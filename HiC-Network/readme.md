# Create Network

creating a network between the interchromosomal contacts and the intrachromosomal contacts


HiC_network.py : This code will generate a gexf format file from interchromosomal and intrachromosomal contacts files. These files were modified using FitHic to generate p-value and q-value for the contacts count.

The edges will be labeled with p-value, q-value and contacts counts and nodes will be labeled with chromosome and start and end position of the fragment example: 
{'chr': '1', 'chunk_start': 0, 'chunk_end': '1000000'}.

Example input files = 1) interchromosomal_contacts 2) intrachromosomal_contacts 3) bias file

Output file = habal.gexf

Command line usage = 

'python HiC_network.py -inter interchromosomal_contacts.csv -intra intrachromosomal_contacts.csv -bias bias_1mb -output habal.gexf. 

Python3.6.4 and NetworkX 2.3 are required to run this code.


