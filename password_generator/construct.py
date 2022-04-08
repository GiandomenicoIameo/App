from parsing import args

def toString( passphrase ):

    password = list( passphrase.strip() )
    separator = ","
    password = "[" + separator.join( password ) + "]"

    return password

def plasma_predicate( mode, alphabet ):

    alphabet = str( alphabet )
    password = toString( args.password )

    schedule = [
        alphabet, mode,
        password, "Ys"
    ]

    return schedule
