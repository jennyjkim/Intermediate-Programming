# Submitter: jisook5(Kim, Jenny)
# Partner: yink3(Yin, Kevim)
#We certified that we worked cooperatively in this programming
#  assignment, according to the rules of pair programming

import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    prefixes= set()
    pos= 1
    for tuple in range(len(fq)):
        prefixes.add(fq[0:pos])
        pos += 1
    return prefixes

def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    pos= 1
    for tuple in range(len(new_query)):
        prefix[new_query[0:pos]].add(new_query)
        pos +=1
    query[new_query] += 1

def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefixes, queries = defaultdict(set), defaultdict(int)
    for line in open_file:
        query= tuple(line.strip('\n').split())
        pos= 1
        for entry in range(len(query)):
            prefixes[query[0:pos]].add(query)
            pos += 1
        queries[query] += 1
    return prefixes, queries

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string= ''
    for key in sorted(d.keys(), key = key, reverse = reverse):
        string= string + ('  {} -> {}\n'.format(key, d[key]))
    return string

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    list_of_entries= {}
    for k,v in query.items():
        if a_prefix not in prefix.keys():
            return []
        if k in prefix[a_prefix]:
            list_of_entries[k]= v
    sort_query= sorted(list_of_entries.items(), key=lambda x: (-x[1], x[0]))
    result= []
    if len(sort_query) < n:
        for entry in sort_query:
            result.append(entry[0])
        return result
    for x in range(n):
        result.append(sort_query[x][0])
    return result
    
# Script
pass

if __name__ == '__main__':
    
    # Write script here
    file1= str(input('Enter file with full queries: '))
    file1= 'googleq0.txt'
    p, q= read_queries(open(file1))
    print('Prefix dictionary: ')
    print(dict_as_str(p))
    print('Query dictionary: ')
    print(dict_as_str(q, key= lambda x: x[1]))
    
    while True:
        query= input('Enter prefix (or quit): ')
        if query == 'quit':
            break
        print('  Top 3 (at most) full queries = {}\n'.format(top_n(tuple(query.split()),3,p,q)))
        new_query= input('Enter full query (or quit): ')
        if new_query == 'quit':
            break
        add_query(p,q,tuple(new_query.split()))
        print('Prefix dictionary: ')
        print(dict_as_str(p))
        print('Query dictionary: ')
        print(dict_as_str(q, key= lambda x:x[1]))

    # For running batch self-tests

    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
