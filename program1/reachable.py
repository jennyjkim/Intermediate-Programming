#Submitter: jisook5(Kim, Jisoo)
#Partner: yink3(Yin, Kevin)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    nodes= defaultdict(set)
    for line in file:
        a, b = line.strip('\n').split(';')
        nodes[a].add(b)
        #nodes.update(a, (nodes.get(a, set()).union(b)))
    return dict(nodes)

def graph_as_str(graph : {str:{str}}) -> str:
    print('Graph: source -> {destination} edges')
    string = ''
    for key in sorted(graph):
        string+='  {} -> {}\n'.format(key, sorted(list(graph[key])))   
    return string
        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    reached_nodes= set()
    exploring_list= [start]
    while True:
        if exploring_list == []:
            break
        point= exploring_list.pop()[0]
        reached_nodes.add(point)
        if point not in graph.keys():
            continue
        for node in graph[point]:
            if node not in reached_nodes:
                exploring_list.append(node)
    return reached_nodes


if __name__ == '__main__':
    print(read_graph(open('graph1.txt')))
    
    while True:
        file= str(input('Enter file with graph: '))
        node_dict = read_graph(open(file))
        print(graph_as_str(node_dict))
        break
    while True:
        node= str(input('Enter a starting node name: '))
        if node == 'quit':
            break
        reached_nodes= reachable(node_dict, node)
        if node not in node_dict.keys():
            print("Entry Error: '{}'; Illegal: not a source code\nPLease enter a legal String".format(node))
            continue
        print('From {} the reachable nodes are {}'.format(node, reached_nodes) )
        print('')
               
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
