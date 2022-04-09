from password import combinations
from parsing import args

if args.permutation:
    combinations( "permutation" )
elif args.binomial:
    combinations( "generate_binomial" )
elif args.disposition:
    combinations( "generate_disposition" )
else:
    combinations( "generate_combination" )
