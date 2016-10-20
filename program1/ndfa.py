#Submitter: jisook5(Kim, Jisoo)
#Partner: yink3(Yin, Kevin)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from collections import defaultdict
from multiprocessing.managers import State


def read_ndfa(file : open) -> {str:{str:{str}}}:
    ndfa = defaultdict(str)
    for line in file:
        inner_dict = defaultdict(str)
        p = []
        string_list= line.strip('\n').replace(' ', ';').split(';')
        first_key = string_list.pop(0)
        p.append(list(zip(string_list[::2], string_list[1::2])))
        for entry in p[0]:
            if entry[0] in inner_dict:
                inner_dict[entry[0]].add(entry[1])   
            else:
                inner_dict.setdefault(entry[0], {entry[1]})
        ndfa.setdefault(first_key, dict(inner_dict))
    return dict(ndfa)



def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    print('Non-Deterministic Finite Automaton')
    string = ''
    for k, v in sorted(ndfa.items()):
        setlist = []
        for each in sorted(v.items()):
            setlist.append((each[0], sorted(each[1])))
        string+= ('  {} transitions: {}\n'.format(k, setlist))
    #print(string)
    return(string)

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    final_list = [state]
    current_states = [state]
    all_keys = set()
    for element in (ndfa.values()):
        list1 = (list((element).keys()))
        all_keys.update(list1)
        
    for move in inputs:
        if move in all_keys:
            appending_set = [move] #[1, {need these moves}]
            set_moves = set()         # getting the {need these moves}
            for states in current_states:
                try:
                    the_move = ndfa[states][move]
                    set_moves.update(the_move)
                except:
                    continue
            if len(set_moves) == 0:
                appending_set.append(set_moves)
                final_list.append(tuple(appending_set))
                break
            appending_set.append(set_moves)
            final_list.append(tuple(appending_set))
            current_states = (list(set_moves))
        else:
            pass
    return(final_list)
        
                

def interpret(result : [None]) -> str:
    print('Starting new simulation')
    string = ('Start state = {}\n'.format(result[0]))
    for tuplez in result[1:]:
        string += ('  Input = {}; new possible states = {}\n'. format(tuplez[0], sorted(tuplez[1])))
    string+=('Stop state(s) = {}\n'.format(sorted(result[-1][1])))
    return(string)
    

if __name__ == '__main__':
    file_name = str(input('Enter file with non-deterministic finite automaton: '))
    dictionary = read_ndfa(open(file_name))
    print(ndfa_as_str(dictionary))
    input_file = str(input('Enter file with the start-state and input: '))
    text = open(input_file)
    for line in text:
        line_list = line.strip('\n').replace(' ', ';').split(';')
        processed = process(dictionary, line_list[0], line_list[1::])
        print(interpret(processed))

             
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
