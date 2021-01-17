
import numpy as np

# please let me know (alan) if you need any more functions
class repeatabelState:
    # This is the current and state of the game.
    def __init__(self):
               
       #self.communications = [[0]*5] * 5 # 5x5 grid to allow the ais to communicate. (each index will tell the others how much "sus" this player thinks of other players)
        

        self.proposal = [0,0,0,0,0] # we choose to have 5 players so 0 means that they have not been selected 1 means otherwise
        self.proposing = [0,0,0,0,0] # 1 indicates the player that is proposing
        self.hammer = [0,0,0,0,0] # if this gets to [1,1,1,1,1] then the good guys loose

        

    def getCommunications(self):
        #return self.communications
        pass

    def getProposing(self):
        return self.proposing

    def getProposal(self):
        return self.proposal
    
    def getHammer(self):
        return self.proposal

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
        self.agents = players


    def reset_game(self):
        self.points = [0,0,0,0,0]

        self.pointTeams = [[0]*5] * 5 # 5x5 grid to remember who voted for what
        
        self.bad_guys = [0,0,0,0,0] # 1 if is bad, 0 otherwise

        self.repeatable_states = [] # in here we store repeatable states the class

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
        while cur_index < len(self.repeatable_states):
            cur_array = np.array(self.repeatable_states[cur_index].getAsArray())
            return_state = np.concatenate([return_state, cur_array])
            cur_index += 1

        while cur_index < 16:
            return_state = np.concatenate([return_state, np.array([0]*5)])
            cur_index += 1

        return return_state



    def run_loop(self):
        pass

    def proposalPhase(self): # update the gamestate and then ask the proposing agent to propose something
        pass
    
    def communicationPhase(self): # comms phase allow the agents to send their comms
        pass

    def voteOnProposalPhase(self): # gamestate updates and allows all agents to vote
        pass

    def missionPhase(self): # get the choice from every person and 
        pass
