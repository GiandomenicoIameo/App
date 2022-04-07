from pyswip import Functor, Variable, Query

def password_found( mode, alphabet ):

    mode  = Functor( mode, 2 )
    atom  = Functor( "atomics", 2 )
    X     = Variable()
    Y     = Variable()
    query = Query( mode( alphabet,X ), atom( X,Y ) )

    while query.nextSolution():
          print( Y.value )
    query.closeQuery()

def password_not_found( mode, alphabet, args, prolog ):

    toString = list( args.word.strip() )
    separator = ","
    toString = "[" + separator.join( toString ) + "]"

    schedule = [
        str( alphabet ), mode,
        toString, "Ys"
    ]
    query = "init( " + separator.join( schedule ) + ")"

    for element in prolog.query( query ):
            print( element[ "Ys" ] )
