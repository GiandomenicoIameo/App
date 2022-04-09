from password import combinations
from parsing import args

if args.binomial:
    combinations( "binomial_generate" )
elif args.combination:
    combinations( "combination_generate" )
elif args.disposition:
    combinations( "disposition_generate" )
else:
    combinations( "permutation" )
