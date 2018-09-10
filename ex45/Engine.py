class Engine():

    def __init__(self, guideObject):
        self.guideObject = guideObject

    def play(self):
        currentRoom = self.guideObject.opening()
        nextRoom = currentRoom.enter() 

        while nextRoom:

            print( "Next room is %s " % nextRoom )
            currentRoom = self.guideObject.nextRoom( nextRoom )
            nextRoom = currentRoom.enter()

        print( "Leaving the rooms" )
        exit(0)

