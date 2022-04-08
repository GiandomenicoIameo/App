from password import combinations
from parsing import args

if args.binomial:
    combinations( "generate_binomial" )
elif args.combination:
    combinations( "combination" )
elif args.disposition:
    combinations( "generate_permutation" )
else:
    combinations( "permutation" )
