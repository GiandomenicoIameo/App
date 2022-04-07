from pyswip import Prolog
from parsing import *
from predicates import *

prolog = Prolog()
prolog.consult( "combinatorics.pro" )

match True:
  case args.binomial:
        combinatorics = "binomial"
  case args.combination:
        combinatorics = "combination"
  case args.disposition:
        combinatorics = "disposition"
  case args.permutation:
        combinatorics = "permutation"
  case _:
        combinatorics = "permutation"

alphabet = list( args.alphabet )

if bool( args.word ) == False:
    password_found( combinatorics, alphabet )
else:
    password_not_found( combinatoric,
            alphabet, args, prolog )
