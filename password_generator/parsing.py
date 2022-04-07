import argparse
from messages import message

version = {
    "short_name"  : "-v",
    "full_name"   : "--version",
    "action"      : "version",
    "description" : "verba version 1.0.0"
}

binomial = {
    "name"        : "binomial",
    "short_name"  : "-b",
    "full_name"   : "--binomial",
    "help"        : message( "-b" ),
    "action"      : "store_true"
}

combination = {
    "name"        : "combination",
    "short_name"  : "-c",
    "full_name"   : "--combination",
    "help"        : message( "-c" ),
    "action"      : "store_true"
}

disposition = {
    "name"        : 'disposition',
    "short_name"  : "-d",
    "full_name"   : "--disposition",
    "help"        : message( "-d" ),
    "action"      : "store_true"
}

permutation = {
    "name"        : 'permutation',
    "short_name"  : "-p",
    "full_name"   : "--permutation",
    "help"        : message( "-p" ),
    "action"      : "store_true"
}

alphabet = {
    "full_name"   : "--alphabet",
    "require"     : True,
    "help"        : message( "-a" )
}

word = {
    "name"        : "word",
    "nargs"       : "?",
    "help"        : message( "-w" )
}

parser = argparse.ArgumentParser()

parser.add_argument(
           word[ "name" ],
   nargs = word[ "nargs" ],
    help = word[ "help" ]
)

parser.add_argument(
           version[ "short_name" ],
           version[ "full_name" ],
  action = version[ "action" ],
 version = version[ 'description' ]
)

parser.add_argument(
           binomial[ "short_name" ],
           binomial[ "full_name" ],
    help = binomial[ "help" ],
  action = binomial[ "action" ]
)

parser.add_argument(
           combination[ "short_name" ],
           combination[ "full_name" ],
    help = combination[ "help" ],
  action = combination[ "action" ]
)

parser.add_argument(
           disposition[ "short_name" ],
           disposition[ "full_name" ],
    help = disposition[ "help" ],
  action = disposition[ "action" ]
)

parser.add_argument(
           permutation[ "short_name" ],
           permutation[ "full_name" ],
    help = permutation[ "help" ],
  action = permutation[ "action" ]
)

parser.add_argument(
           alphabet[ "full_name" ],
required = alphabet[ "require" ],
    help = alphabet[ "help" ]
 )

args = parser.parse_args()
