

class GameState:
    # This is the current and state of the game.
    def __init__(self):
        self.points = [0,0,0,0,0]

        self.pointTeams = [[0]*5] * 5 # 5x5 grid to remember who voted for what
        self.communications = [[0]*5] * 5 # 5x5 grid to allow the ais to communicate. (each index will tell the others how much "sus" this player thinks of other players)

        self.proposal = [0,0,0,0,0] # we choose to have 5 players so 0 means that they have not been selected 1 means otherwise
        self.proposing = [0,0,0,0,0] # 1 indicates the player that is proposing
        self.hammer = [0,0,0,0,0] # if this gets to [1,1,1,1,1] then the good guys loose
        self.bad_guys = [0,0,0,0,0] # 1 if is bad, 0 otherwise
        

    def getPoints(self):
        return self.points

    def getPointTeams(self):
        return self.pointTeams

    def getCommunications(self):
        return self.communications

    def getProposing(self):
        return self.proposing

    def getProposal(self):
        return self.proposal
    
    def getHammer(self):
        return self.proposal

    def getBadGuys(self):
        return self.proposal



class Player:
    def selectTeam(self, gameState):
        pass

    def voteOnTeam(self, gameState):
        pass

    def voteMission(self, gameState):
        pass

class GameLoop:
    def __init__(self):
        #initialize the players ...etc
        pass 

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
