from predicates import *

if args.binomial:
    combinatorial_password( "binomial" )
elif args.combination:
    combinatorial_password( "combination" )
elif args.disposition:
    combinatorial_password( "disposition" )
else:
    combinatorial_password( "permutation" )
