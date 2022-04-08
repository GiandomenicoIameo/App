from password import combinations
from parsing import args

if args.binomial:
    combinations( "binomial" )
elif args.combination:
    combinations( "combination" )
elif args.disposition:
    combinations( "disposition" )
else:
    combinations( "permutation" )
