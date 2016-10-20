#Submitter: yink3(Yin, Kevin)
#Partner: jisook5(Kim, Jisoo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from collections import defaultdict

def read_fa(file : open) -> {str:{str:str}}:
    finite_automaton = defaultdict(str)
    for line in file:
        string_list= line.strip('\n').replace(' ', ';').split(';')
        state_key = string_list[0]
        key= string_list[1::2]
        value = string_list[2::2]
        dict_entry = dict(zip(key, value))
        finite_automaton.setdefault(state_key, dict_entry)
    return dict(finite_automaton)
            
                  


def fa_as_str(fa : {str:{str:str}}) -> str:
    print('Finite Automaton Description')
    string = ''
    for k, v in sorted(fa.items()):
        string = string + ('  {} transitions: {}\n'.format(k, sorted(v.items())))
    return string
        

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    current_state = state
    all_keys = set()
    for x in list(fa.values()):
        all_keys = list(x.keys())
    
    for each in inputs:
        if each not in all_keys:
            new = (each, None)
            result.append(new)
        else:
            new = (each, fa[current_state][each])
            result.append(new)
            if fa[current_state][each] != current_state:
                current_state = fa[current_state][each]
    return result
    
        
def interpret(fa_result : [None]) -> str:
    print('Starting new simulation')
    string = ('Start state = {}\n'.format(fa_result[0]))
    for pair in fa_result[1:]:
        if pair[1] ==  None:
            string += "  Input = {}; illegal input: simulation terminated\n".format(pair[0])
            string = string + 'Stop state = {}\n'.format(fa_result[-1][1])
            return (string)     
        string = string + "  Input = {}; new state = {}\n".format(pair[0], pair[1])
    string = string + 'Stop state = {}\n'.format(fa_result[-1][1])
    return (string)    
    
    


if __name__ == '__main__':
    open_file = open('fainput1.txt')
    for line in open_file:
        print(line)
    
    
    
    file_name = str(input('Enter file with finite automaton: '))
    dictionary = read_fa(open(file_name))
    print(fa_as_str(dictionary))
    input_file = str(input('Enter file with the start-state and input: '))
    text = open(input_file)
    for line in text:
        line_list = line.strip('\n').replace(' ', ';').split(';')
        processed = process(dictionary, line_list[0], line_list[1::])
        print(interpret(processed))


    
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
