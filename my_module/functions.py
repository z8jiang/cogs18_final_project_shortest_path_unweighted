"""A collection of function for doing my project."""
import pandas as pd
def adjacency_list(graph_csv_file):
    """
    Create adjacency list representation of graph.
    
    Parameters
    ----------
    graph_csv_file : string
        CSV file name of an unweighted and directed or undirected graph represented in lines of
        "u, v", meaning vertex "u" connects to vertex "v". The graph can be some arbitrary points
        or the map of a location like UCSD.
        
        The input can't be empty. Or else what's the point of using this program?
        
        The lines can be in any order. Doesn't have to be sorted. 
        
        Each line can be upper case of lower case (e.g. "A,B", "B,A", "a,b", or "b,a"). Each
        vertex can be represented in snakecase (e.g. ""e_f,g_h" or "i_j,k_l""). Ideally, don't
        include apostrophes (e.g. "carolines_seaside_cafe, trader_joes"). Don't include space(s)
        after the comma.


    Returns
    -------
    adj_lst : dictionary
        Adjacency list representation of the graph. Each vertex, or point, is the key. Each
        vertex's neighboring, or connected, vertices are in a list. This list is the value.


    Examples
    --------
    'small.csv' contains the following:
        A,B
        E,D
        E,A
        B,D
        B,E
        C,E
        C,A
        D,G
        E,F
        F,G
           
    >>> adj_lst = adjacency_list('small.csv')
    
    >>> adj_lst
    {'A': ['B', 'E', 'C'],
     'B': ['A', 'D', 'E'],
     'E': ['D', 'A', 'B', 'C', 'F'],
     'D': ['E', 'B', 'G'],
     'C': ['E', 'A'],
     'G': ['D', 'F'],
     'F': ['E', 'G']}
    
    """
    # Read the graph csv and make a dataframe with "u" and "v" columns
    df = pd.read_csv(graph_csv_file, sep=',', names= ['u','v'])
    
    adj_lst = {}

    for i in range(len(df)):
        # Get the i'th row's "u" vertex in the first column and "v" vertex
        # in the second column as strings
        u = df.loc[i,:][0]
        v = df.loc[i,:][1]
        
        # If adjacency list dictionary already has both vertex "u" and "v" as keys, add "u" to 
        # the list of vertices connected to "v" and vice versa
        if (u in adj_lst) and (v in adj_lst):
            neighbors_of_u = adj_lst[u]
            neighbors_of_u.append(v)
            neighbors_of_v = adj_lst[v]
            neighbors_of_v.append(u)

        # If adjacency list only has vertex "u" as the key, do the same as above
        elif (u in adj_lst) and (v not in adj_lst):
            neighbors_of_u = adj_lst[u]
            neighbors_of_u.append(v)
            
            adj_lst[v] = [u]
        
        elif (u not in adj_lst) and (v in adj_lst):
            neighbors_of_v = adj_lst[v]
            neighbors_of_v.append(u)
            adj_lst[u] = [v]
          
        # Else create a new element of "u" mapped to a list of only "v" and vice versa
        # Then add these two elements to the adjacency list
        else:
            adj_lst[u] = [v]
            adj_lst[v] = [u]
                 
    return adj_lst




def breadth_first_search(start_label, end_label, adj_lst):
    """
    Using breadth first search, traces the graph represented in an adjacency list from the
    starting point to the ending point. Meanwhile, keeps track of visited vertex and its
    previously visited vertex.
    
    Parameters
    ----------
    start_label : string
        The starting point or start.
    end_label : string
        The ending point or destination.
    adj_lst : dictionary
        Adjacency list of a graph. Each vertex, or point, in the graph is mapped to
        a list of strings. This list is the vertices that the vertex connects to (neighbors).


    Returns
    -------
    trace : dictionary
        The path it took from the starting point to the end point with each visited point
        as the key and its previously visited point as the value.


    Examples
    --------
    >>> start_label = 'A'
    >>> end_label = 'B'
    >>> adj_lst = {'A': ['B', 'E', 'C'],
                   'B': ['A', 'D', 'E'],
                   'E': ['D', 'A', 'B', 'C', 'F'],
                   'D': ['E', 'B', 'G'],
                   'C': ['E', 'A'],
                   'G': ['D', 'F'],
                   'F': ['E', 'G']}
           
    >>> trace = breadth_first_search(start_label, end_label, adj_lst)
    
    >>> trace
    {'A': 'null', 'B': 'A', 'E': 'A', 'C': 'A', 'D': 'B', 'F': 'E'}

    """
    queue = []
    trace = {}
    
    queue.append(start_label)
    trace[start_label] = "null"
    
    while len(queue) != 0:
        parent = queue[0]
        queue.remove(parent)
        
        # If end_label has been visited, return the trace dictionary early 
        if parent == end_label:
            return trace

        # Visit every unvisited vertex that are connected to the parent vertex
        for curr in adj_lst[parent]:
            if curr not in trace:    # not in the trace dictionary (unvisited)
                trace[curr] = parent    # adding it to the trace dictionary (visited)
                queue.append(curr)

    if end_label not in trace:
        trace = {}
        return trace
    
    return trace





def shortest_path_unweighted(start_label, end_label, trace):
    """
    Retraces the visited record and finds the shortest path from the starting point to end point.
    If not path exists, returns an empty list.
    
    Parameters
    ----------
    start_label : string
        The starting point or start.
    end_label : string
        The ending point or destination.
    trace : dictionary
        The path it took from the starting point to the end point with each visited point as
        the key and its previously visited point as the value.


    Returns
    -------
    shortest_path : list
        The list of strings that shows the shortest path from A to B. If B is not even in the trace
        disctionary, returns an empty list.


    Examples
    --------
    >>> start_label = 'A'
    >>> end_label = 'C'
    >>> trace = {'A': 'null', 'B': 'A', 'C': 'A', 'E': 'A', 'D': 'B'}
    
    >>> shortest_path_unweighted('A', 'F', trace)
    
    >>> shortest_path 
    ['A', 'E', 'F']
    
    """
    path = []
    
    if (len(trace) == 0) or (end_label not in trace):
        return path
    
    path.append(end_label)
    
    # Trace the path from the end point back to the start. This path is the shortest path
    curr = end_label
    while curr != start_label:
        parent = trace[curr]
        path.append(parent)
        curr = parent
        
    path.reverse()
    
    
    return path
