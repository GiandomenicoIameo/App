from pyswip import Prolog, Functor, Variable, Query
from parsing import args

def combinations( mode ):

    alphabet = list( args.alphabet )

    if bool( args.password ):
        password_found(
            mode, alphabet
        )
    else:
        password_not_found(
            mode, alphabet
        )

def password_not_found( mode, alphabet ):

    prolog = Prolog()
    prolog.consult( "predicates.pro" )

    mode = Functor( mode, 2 )
    atom = Functor( "atomic_list_concat", 2 )

    X = Variable()
    Y = Variable()

    query = Query( mode( alphabet,X ), atom( X,Y ) )

    while query.nextSolution():
          print( Y.value )
    query.closeQuery()

def toString( passphrase ):

    password = list( passphrase.strip() )
    separator = ","
    password = "[" + separator.join( password ) + "]"

    return password

def password_found( mode, alphabet ):

    prolog = Prolog()
    prolog.consult( "predicates.pro" )

    alphabet = str( alphabet )
    password = toString( args.password )
    separator = ","

    schedule = [
        alphabet, mode,
        password, "Ys"
    ]
    query = "generate( " + separator.join( schedule ) + ")"

    for element in prolog.query( query ):
            print( element[ "Ys" ] )
