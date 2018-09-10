
from Room import Room

class Alpha( Room ):
    def enter(self):
        print( "In room Alpha" )
        print( "Enter either A, B, C, or D." )
        print( "Enter choice: " ) 

        choice = input( ">> ")

        if choice in [ "A", "B", "C", "D" ]:
            return choice
        else:
            Alpha.wuzzup( choice )
            Alpha.enter(self)



