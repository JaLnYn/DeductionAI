from collections import deque
import copy 
import numpy as np
import random

# please let me know (alan) if you need any more functions
class RepeatableState:
    # This is the current and state of the game.
    def __init__(self):
               
        # self.communications = [[0]*5] * 5 # 5x5 grid to allow the ais to communicate. (each index will tell the others how much "sus" this player thinks of other players)
        
        self.proposal = [0,0,0,0,0] # we choose to have 5 players so 0 means that they have not been selected 1 means otherwise
        self.proposing = [0,0,0,0,0] # 1 indicates the player that is proposing
        self.hammer = [0,0,0,0,0] # if this gets to [1,1,1,1,1] then the good guys loose
        self.votes = [0,0,0,0,0]

    def getAsArray(self):
        return [*self.proposal, *self.proposing, *self.hammer]



class Player:
    def selectTeam(self, gameState):
        pass

    def voteOnTeam(self, gameState):
        pass

    def voteMission(self, gameState):
        pass

    def communicate(self, gameState):
        pass



class GameLoop:
    def __init__(self, players):
        #initialize the players ...etc
        if len(players) != 5:
            print("Expected 5 players got:", len(players))
            # throw error here 
        self.agents = players


    def reset_game(self):
        self.points = [0,0,0,0,0]

        self.pointTeams = [[0]*5] * 5 # 5x5 grid to remember who voted for what
        
        self.bad_guys = [0,0,0,0,0] # 1 if is bad, 0 otherwise

        self.repeatable_states = deque([]) # in here we store repeatable states the class needs to be a FIFO queue

    # returns an array that can be put into a tensor
    def current_state(self):
        """
            [
                points (5),
                point_teams (25): index 5i+j denotes the entry (i,j),
                bad_guys (5)
            ]
        """

        return_state = np.concatenate([
            np.array(self.points),
            np.array(self.pointTeams).flatten(),
            np.array(self.bad_guys)
        ], axis=-1)


        # here we want to loop through repeatable_states and append to the returnstate. if len(repeatable_state) < 16, then we wanna append arrays of [0] *5 

        cur_index = 0
        while cur_index < self.repeatable_states.count():
            cur_array = np.array(self.repeatable_states[cur_index].getAsArray())
            return_state = np.concatenate([return_state, cur_array])
            cur_index += 1

        while cur_index < 16:
            return_state = np.concatenate([return_state, np.array([0]*5)])
            cur_index += 1

        return return_state


    def run_loop(self):
        running = True
        next_hammer = [0] *5
        cur_hammer = 0

        cur_proposing = random.randint(0,4)
        while running == True:
            # first update the states
            if cur_hammer >= 5:
                # hammer down the good guys loose
                running = False
                break

            for i in range(cur_hammer):
                next_hammer[i] = 1
            cur_rep_state = RepeatableState()
            cur_rep_state.hammer = next_hammer
            cur_proposing = (cur_proposing + 1) % 5
            cur_rep_state.proposing = [0] * 5
            cur_rep_state.proposing[cur_proposing] = 1

            self.repeatable_states.append(cur_rep_state)

            if self.repeatable_states.count() > 16:
                self.repeatable_states.popleft()
            
            proposalPhase()
            passed = voteOnProposalPhase()
            if passed:
                missionPhase()
                next_hammer = [0]*5
                cur_hammer = 0
            else:
                cur_hammer = (cur_hammer + 1)


    def proposalPhase(self): # update the gamestate and then ask the proposing agent to propose something
        cur_rep_state = self.repeatable_states[-1]
        cur_proposing = self.agents[cur_rep_state.proposing.index(1)]
        cur_rep_state.proposal = cur_proposing.selectTeam(cur_rep_state)
    
    def communicationPhase(self): # comms phase allow the agents to send their comms
        # none for now
        pass

    def voteOnProposalPhase(self): # gamestate updates and allows all agents to vote
        # get the vote from everyone and update votes
        # returns whether the vote passed (true) or it failed (false)
        players = self.agents
        cur_rep_state = self.repeatable_states[-1]
        for i in range(len(players)):
            cur_rep_state.votes[i] = players[i].voteOnTeam(cur_rep_state)
        # returns whether the vote passed (true) or it failed (false)
        if sum(cur_rep_state.votes)>2:
            return True
        else:
            return False

    def missionPhase(self): 
        # get the choice from every person and 
        # update points 
        pass
