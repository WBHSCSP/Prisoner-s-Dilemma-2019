import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'THE A team' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    choices=random.randint(1,4) 
    if choices == 1:
        return 'c'
    if choices == 2:
        if len(my_history) == 0:
            return 'c'
        else:
            if their_history[len(their_history)-1] == 'b':
                return 'b'
            else:
                return 'c'
    if choices == 3:
        a = random.randint(1,2)
        if a == 1:
            return 'c'
        if a == 2:
            return 'b'
        if len(my_history) >= 1 and a == 1:
            return 'b'
        if len(my_history) >= 1 and a == 2:
            return 'c'
    if choices == 4:
        p = 0
        t = 0
        T = 0
        f = 0
        F = 0
        s = 0
        S = 0
        e = 0
        n = 0
        if float(len(my_history))%2 > 0:
            t = 1
        if float(len(my_history))%3 > 0 or  len(my_history) == 3 :
            T =1
        if float(len(my_history))%4 > 0:
            f = 1
        if float(len(my_history))%5 > 0 or  len(my_history) == 5:
            F = 1
        if float(len(my_history))%6 > 0:
            s =1
        if float(len(my_history))%7 > 0 or  len(my_history) == 7:
            S=1
        if float(len(my_history))%8 > 0:
            e = 1
        if float(len(my_history))%9 > 0.:
            n = 1
        if t == 1 and T == 1 and f==1 and F==1 and s==1 and S==1 and e==1 and n ==1: 
            p = 1
        
        if p == 0:
            return 'c'
        else:
            a = random.randint(1,2)
            if a == 1:
                return 'c'
            if a == 2:
                return 'b'
            
 
    
    
            
            
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             