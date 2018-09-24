from Room import Room

class Delta( Room ):
    def enter( self ):
        print( "In room Delta" )

        print( "Enter either A, B, C, or D." )
        print( "Enter choice: " ) 

        choice = input( ">> ")

        if choice in [ "A", "B", "C", "D" ]:
            return choice
        else:
            Delta.wuzzup( choice )
            Delta.enter( self )



