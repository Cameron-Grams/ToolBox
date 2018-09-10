from Room import Room

class Bravo( Room ):
    def enter( self ):
        print( "In room Bravo" )

        print( "Enter either A, B, C, or D." )
        print( "Enter choice: " ) 

        choice = input( ">> ")

        if choice in [ "A", "B", "C", "D" ]:
            return choice
        else:
            Bravo.wuzzup( choice )
            Bravo.enter( self )








