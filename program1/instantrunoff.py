#Submitter: jisook5(Kim, Jisoo)
#Partner: yink3(Yin, Kevin)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from collections import defaultdict

def read_voter_preferences(file : open):
    voters= defaultdict(list)
    for line in file:
        candidate_votes= line.strip('\n').split(';')
        voter= candidate_votes.pop(0)
        for candidate in candidate_votes:
            voters[voter].append(candidate)
    return dict(voters)

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string= ''
    for k, value in sorted(d.items(), key = key, reverse = reverse):
        string= string + ('  {} -> {}\n'.format(k, value))
    print(string)
    return string    
    
def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    votes_recieved= defaultdict(int)
    for voter in vp.keys():
        pos= 0
        while True:
            candidate= vp[voter][pos]
            if candidate in cie:
                votes_recieved[candidate] += 1
                break
            pos += 1
    return dict(votes_recieved)
                
def remaining_candidates(vd : {str:int}) -> {str}:
    losing_value= vd[min(vd, key=vd.get)] #min(vd, key=vd.get) gets the KEY of the item with the corresponding smallest VALUE
    remaining= set()
    if len(set(vd.values())) == True:  #if all values in the set are equal to the same value, then return an empty set
        return remaining
    for candidate in vd.keys():
        if vd[candidate] != losing_value:
            remaining.update(candidate)
    return remaining

def run_election(vp_file : open) -> {str}:
    ballot= read_voter_preferences(vp_file)
    print('Voter Preferences')
    dict_as_str(ballot, (lambda x: x[0]))
    rem_cand= set(list(ballot.values())[0])
    ballot_number= 1
    
    while True:
        print('Vote count on ballot #{} with candidates (alphabetically) = {}'.format(str(ballot_number), rem_cand))
        votes=(evaluate_ballot(ballot, rem_cand))
        dict_as_str(votes, (lambda x: x[0]))
        print('Vote count on ballot #{} with candidates (numerically) = {}'.format(str(ballot_number), rem_cand))
        dict_as_str(votes, lambda x: x[1], reverse=True)
        rem_cand = remaining_candidates(votes)
        if len(rem_cand) == 1:
            print('Winner is {}'.format(rem_cand))
            return rem_cand
        if rem_cand == set():
            print('No winner')
            return rem_cand
  
if __name__ == '__main__':
    file1= str(input('Enter file with voter preferences: '))
    run_election(open(file1))
    
    # Write script here
              
    #For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
