# the main will handle the calls to the various rooms
# each room will have options on the next room to enter
# choice will be a string that returns a value from a dictionary

from Alpha import Alpha
from Bravo import Bravo
from Charlie import Charlie
from Delta import Delta

class Main():
    rooms = {
        'A': Alpha(),
        'B': Bravo(),
        'C': Charlie(),
        'D': Delta()
    }

    def __init__(self):
        pass

#confirm that this has to be before the opening since it is referenced 
# in the opening function
    def nextRoom(self, next_room):
        actionRoom = Main.rooms.get( next_room )
        return actionRoom

    def opening(self):
        print( "in main opening") 
        return self.nextRoom( "A" )  





