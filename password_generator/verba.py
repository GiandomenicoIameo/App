from parsing import *
from predicates import *

if args.binomial:
    restore_password( "binomial" )
elif args.combination:
    restore_password( "combination" )
elif args.disposition:
    restore_password( "disposition" )
else:
    restore_password( "permutation" )
