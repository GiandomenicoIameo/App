import argparse
from messages import *

version = {
    "name"        : "version",
    "shortcut"    : "-v",
    "command"     : "--version",
    "action"      : "version",
    "description" : "verba version 1.0.0"
}

binomial = {
    "name"        : "binomial",
    "shortcut"    : "-b",
    "command"     : "--binomial",
    "help"        : message_binomial(),
    "action"      : "store_true"
}

combination = {
    "name"        : "combination",
    "shortcut"    : "-c",
    "command"     : "--combination",
    "help"        : message_combination(),
    "action"      : "store_true"
}

disposition = {
    "name"        : "disposition",
    "shortcut"    : "-d",
    "command"     : "--disposition",
    "help"        : message_disposition(),
    "action"      : "store_true"
}

permutation = {
    "name"        : "permutation",
    "shortcut"    : "-p",
    "command"     : "--permutation",
    "help"        : message_permutation(),
    "action"      : "store_true"
}

alphabet = {
    "command"     : "--alphabet",
    "require"     : True,
    "help"        : message_alphabet()
}

word = {
    "name"        : "word",
    "nargs"       : "?",
    "help"        : message_word()
}

parser = argparse.ArgumentParser()

parser.add_argument(
           word[ "name" ],
   nargs = word[ "nargs" ],
    help = word[ "help" ]
)

parser.add_argument(
           version[ "shortcut" ],
           version[ "command" ],
  action = version[ "action" ],
 version = version[ "description" ]
)

parser.add_argument(
           binomial[ "shortcut" ],
           binomial[ "command" ],
    help = binomial[ "help" ],
  action = binomial[ "action" ]
)

parser.add_argument(
           combination[ "shortcut" ],
           combination[ "command" ],
    help = combination[ "help" ],
  action = combination[ "action" ]
)

parser.add_argument(
           disposition[ "shortcut" ],
           disposition[ "command" ],
    help = disposition[ "help" ],
  action = disposition[ "action" ]
)

parser.add_argument(
           permutation[ "shortcut" ],
           permutation[ "command" ],
    help = permutation[ "help" ],
  action = permutation[ "action" ]
)

parser.add_argument(
           alphabet[ "command" ],
required = alphabet[ "require" ],
    help = alphabet[ "help" ]
 )

args = parser.parse_args()
