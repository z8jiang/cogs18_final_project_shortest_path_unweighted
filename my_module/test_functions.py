"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
from functions import adjacency_list, breadth_first_search, shortest_path_unweighted
##
##

def test_adjacency_list():
    assert callable(adjacency_list)
    assert isinstance(adjacency_list('/home/z8jiang/Project_COGS18_FA21/simple.csv'), dict)
    assert adjacency_list('/home/z8jiang/Project_COGS18_FA21/simple.csv') == {'A': ['B', 'E', 'C'],
                                                                              'B': ['A', 'D', 'E'],
                                                                              'E': ['D', 'A', 'B', 'C', 'F'],
                                                                              'D': ['E', 'B', 'G'],
                                                                              'C': ['E', 'A'],
                                                                              'G': ['D', 'F'],
                                                                              'F': ['E', 'G']}
    assert adjacency_list('/home/z8jiang/Project_COGS18_FA21/ucsd.csv') == {'geisel_library': ['jacobs_hall', 'audreys_cafe', 'SHS'], 'jacobs_hall': ['geisel_library'], 'audreys_cafe': ['geisel_library'], 'chase': ['university_center', 'sunshine_market', 'tapioca_express', 'warren_lecture_hall', 'science_and_engineering_research_facility'], 'university_center': ['chase', 'science_and_engineering_research_facility', 'tapioca_express'], 'SHS': ['target', 'bookstore', 'geisel_library'], 'target': ['SHS', 'bookstore', 'center_hall'], 'dirty_bird': ['startbucks'], 'startbucks': ['dirty_bird'], 'starbucks': ['subway', 'rubios'], 'subway': ['starbucks', 'rubios'], 'rubios': ['subway', 'starbucks'], 'bookstore': ['target', 'SHS', 'center_hall'], 'sunshine_market': ['chase'], 'tapioca_express': ['chase', 'science_and_engineering_research_facility', 'warren_lecture_hall', 'university_center'], 'science_and_engineering_research_facility': ['tapioca_express', 'warren_lecture_hall', 'chase', 'university_center'], 'warren_lecture_hall': ['tapioca_express', 'science_and_engineering_research_facility', 'chase'], 'center_hall': ['target', 'bookstore', 'biomedical_libary'], 'biomedical_libary': ['center_hall']}

    
def test_breadth_first_search():
    assert callable(breadth_first_search)
    
    adj_lst = {'A': ['B', 'E', 'C'],
               'B': ['A', 'D', 'E'],
               'E': ['D', 'A', 'B', 'C', 'F'],
               'D': ['E', 'B', 'G'],
               'C': ['E', 'A'],
               'G': ['D', 'F'],
               'F': ['E', 'G']}
    assert isinstance(breadth_first_search('A', 'C', adj_lst), dict)
    assert breadth_first_search('A', 'C', adj_lst) == {'A': 'null', 'B': 'A', 'E': 'A', 'C': 'A', 'D': 'B', 'F': 'E'}
    
    ucsd_adj_lst = {'geisel_library': ['jacobs_hall', 'audreys_cafe', 'SHS'], 'jacobs_hall': ['geisel_library'], 'audreys_cafe': ['geisel_library'], 'chase': ['university_center', 'sunshine_market', 'tapioca_express', 'warren_lecture_hall', 'science_and_engineering_research_facility'], 'university_center': ['chase', 'science_and_engineering_research_facility', 'tapioca_express'], 'SHS': ['target', 'bookstore', 'geisel_library'], 'target': ['SHS', 'bookstore', 'center_hall'], 'dirty_bird': ['startbucks'], 'startbucks': ['dirty_bird'], 'starbucks': ['subway', 'rubios'], 'subway': ['starbucks', 'rubios'], 'rubios': ['subway', 'starbucks'], 'bookstore': ['target', 'SHS', 'center_hall'], 'sunshine_market': ['chase'], 'tapioca_express': ['chase', 'science_and_engineering_research_facility', 'warren_lecture_hall', 'university_center'], 'science_and_engineering_research_facility': ['tapioca_express', 'warren_lecture_hall', 'chase', 'university_center'], 'warren_lecture_hall': ['tapioca_express', 'science_and_engineering_research_facility', 'chase'], 'center_hall': ['target', 'bookstore', 'biomedical_libary'], 'biomedical_libary': ['center_hall']}
    assert breadth_first_search('geisel_library', 'biomedical_libary', ucsd_adj_lst) == {'geisel_library': 'null',
                                                                                         'jacobs_hall': 'geisel_library',
                                                                                         'audreys_cafe': 'geisel_library',
                                                                                         'SHS': 'geisel_library',
                                                                                         'target': 'SHS',
                                                                                         'bookstore': 'SHS',
                                                                                         'center_hall': 'target',
                                                                                         'biomedical_libary': 'center_hall'}

def test_shortest_path_unweighted():
    assert callable(shortest_path_unweighted)
    trace = {'A': 'null', 'B': 'A', 'E': 'A', 'C': 'A', 'D': 'B', 'F': 'E'}
    assert isinstance(shortest_path_unweighted('A', 'F', trace), list)
    assert shortest_path_unweighted('A', 'F', trace) == ['A', 'E', 'F']
    assert shortest_path_unweighted('A', 'G', trace) == []
    
    ucsd_trace = {'geisel_library': 'null',
                  'jacobs_hall': 'geisel_library',
                  'audreys_cafe': 'geisel_library',
                  'SHS': 'geisel_library',
                  'target': 'SHS',
                  'bookstore': 'SHS',
                  'center_hall': 'target',
                  'biomedical_libary': 'center_hall'}
    assert isinstance(shortest_path_unweighted('geisel_library', 'biomedical_libary', ucsd_trace), list)
    assert shortest_path_unweighted('geisel_library', 'biomedical_libary', ucsd_trace) == ['geisel_library', 'SHS', 'target', 'center_hall', 'biomedical_libary']
    assert shortest_path_unweighted('geisel_library', 'rubios', ucsd_trace) == []
    

                 
    
