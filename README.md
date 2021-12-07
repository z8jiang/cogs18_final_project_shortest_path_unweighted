# Find unweighted shorest path using adjacency list and breadth first search#

In a directed or undirected unweighted graph containing point A and B, find the shortest from A to B. If this graph is the map of UCSD, you can find the shortest path from your study spot in Geisel to your next lecture at Center Hall. If Geisel is getting too loud and you want to walk to the Biomedical library, this program helps you find the shortest path to get from Geisel to Biomedical.

- Design:
    - `adjacency_list()` : create the adjacency list representation of the input graph
        - inputs: `graph_csv_file` 
        - returns: `adj_lst`
    - `breadth_first_search()` : use the adjacency list to traverse the input graph from the starting point to the end point
        - inputs: `start_label`, `end_label`, `adj_lst`
        - returns: `trace`
    - `shortest_path_unweighted()` : find the direct path from the starting point to the ending point using the trace
        - inputs: `start_label`, `end_label`, `trace`
        - returns `path`
