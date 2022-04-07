from parsing import *
from predicates import *

match True:
  case args.binomial:
        mode = "binomial"
  case args.combination:
        mode = "combination"
  case args.disposition:
        mode = "disposition"
  case args.permutation:
        mode = "permutation"
  case _:
        mode = "permutation"

alphabet = list( args.alphabet )

if bool( args.word ) == False:
    password_found(
        mode, alphabet
    )
else:
    password_not_found(
        mode, alphabet
    )
