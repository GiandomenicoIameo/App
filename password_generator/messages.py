def message_disposition():

    message = "generate the dispositions."
    return message

def message_permutation():
    message = "generate the dispositions."
    return message

def message_combination():
    message = "generate the combinations."
    return message

def message_binomial():
    message = "generate all subsets of a given set."
    return message

def message_alphabet():
    message = "font alphabet."
    return message

def message_word():
    message = "custom password."
    return message

def message( msg ):

    arguments = {
        "-a"  : message_alphabet(),
        "-b"  : message_binomial(),
        "-c"  : message_combination(),
        "-d"  : message_disposition(),
        "-p"  : message_permutation(),
        "-w"  : message_word()
    }
    return arguments.get( msg, "null" )
