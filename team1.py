import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Matt' # Only 10 chars displayed.
strategy_name = 'Poking with adaption'
strategy_description = 'It uses a variety of things, but mostly decides based off of the percent of the time the opponent returns b.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    b = 'b'
    tenlookb = 0
    
    oppob = 0
    roundsofar = len(my_history) - 1
    for b in their_history:
        oppob += 1
        
    tenlook = my_history[roundsofar - 9: roundsofar + 1]
    
    for b in tenlook:
        tenlookb += 1
    
    if len(my_history) <= 10:
        if len(my_history) == 0 or len(my_history) == 1:
            return 'c'
        if len(my_history) == 2:
            if their_history[0] == 'b' and their_history[1] == 'b':
                return 'b'
            else:
                return 'c'
        if len(my_history) > 2 and len(my_history) < 10:
            if oppob/roundsofar >= .33:
                return 'b'
            if oppob/roundsofar < .33:
                return 'c'
        if len(my_history) == 10:
            if 'b' in their_history:
                return 'b'
            else:
                return 'c'
            
    if len(my_history) > 10:
        if my_score > their_score:
            return 'b'
        if oppob/roundsofar > .33:
            return 'b'
        if oppob/roundsofar == 0:
            return 'c'
        if oppob/roundsofar > 0 and oppob/roundsofar <= .33:
            if 'b' in tenlook:
                if tenlookb > 2:
                    return 'c'
                if oppob/roundsofar >= .155:
                    if b in tenlook [5:10]:
                        return 'c'
                    else:
                        return 'b'
                if oppob/roundsofar < .155:
                    if b in tenlook[3:10]:
                        return 'c'
                    else: return 'b'
            else:
                return 'b'

    
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