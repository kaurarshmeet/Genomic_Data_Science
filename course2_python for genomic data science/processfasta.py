import sys # for the command line use. 
import getopt # for optional args

# define a usage function 
def usage():
    """
    Optional arguments are in []
    """
    
    print("""
    processfasta.py: Builds a dictionary with all sequences in 
    a specified file bigger than a given length.
    
    processfasta.py [-h] [-l <length] <filename> 

    -h: print this message

    - l <length>: only build dictionary with sequencies >= the 
    length. Default length = 0.

    <filename>: the FASTA file to read from. 
    """)
    
def main():

    """
    This part uses getopt.getopt(arguments, string)

    It takes in a list of arguments, and a string of characters
    that are optional arguments. Optional arguments are always 
    given bey a -arg mark. 

    If the character should be followed by a value, we follow 
    it with a colon in the string. 

    getopt(['-h', '-l', '250', 'sequence.fasta'], 'l:h')

    Using the getopt method extracts optional params/args as
    one list and neccessary params/args as another. Returns 
    both in that order.
    """ 

    # defaults 
    length = 0 # incase user does not provide any value.

    # the optional arguments
    # the arguments are everything beyond "processfasta.py"
    # l:h because -l <length>

    # list of tupules, list 
    o, a = getopt.getopt(sys.argv[1:], 'l:h')

    
    print("o", o) # o is a list of tupules [('-h', ''), ('-l', '250')] 
    print("a", a) # a ['myfile.txt'] is just a list of the mandatory args. 

    # create a dictionary for the optional params/args
    optional_args = {} 

    # fill in the parameters and args, o is a list of tupules.
    for k,v in o:
        optional_args[k] = v

    # if the user asked for help, call usage function. 
    if '-h' in optional_args.keys():
        usage(); sys.exit()
        
    # actually process args...

    # check that they provided the required non-optional args
    if len(a) < 1:
        usage(); sys.exit("Input fasta file is missing") 
    # if they provided length...
    if '-l' in optional_args: 
        length = int(optional_args['-l'])
        if length < 0:
            sys.exit("length should be positive.")

if __name__ == '__main__':
    main()
    """
    [python]
    
    The if __name__ == "__main__": construct in Python is used to 
    determine if a script is being run as the main program or if it 
    is being imported as a module into another script. It is a 
    common practice to use this construct to execute some code only 
    if the script is run directly."""


