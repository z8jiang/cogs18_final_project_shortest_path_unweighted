"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import adjacency_list, breadth_first_search, shortest_path_unweighted

###
###

# PYTHON SCRIPT HERE
ucsd_adj_lst = adjacency_list('/home/z8jiang/Project_COGS18_FA21/ucsd.csv')
ucsd_trace = breadth_first_search('geisel_library', 'biomedical_libary', ucsd_adj_lst)
ucsd_path = shortest_path_unweighted('geisel_library', 'biomedical_libary', ucsd_trace)
print("Shorest path from Geisel Library to Biomedical Library", ucsd_path)
