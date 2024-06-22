""" lifted example from internet to learn about how to use 
stdin and other streams from the command line """ 

import sys

def main():

    """ 
    stdin is like Scanner in = new Scanner(System.in) 
    more like cin >> in C++
    
    You print something to the console and then the user enters 
    something in, ending with an empty line. 
    """
    
    print("Please enter text (end with an empty line):")

    user_input = []
    """ 
    for line in sys.stdin where sys.stdn is a stream object, which 
    is a file-like thing 
    """
    for line in sys.stdin:
        if line.strip() == "":
            break
        user_input.append(line.strip())

    print("This is stdin", sys.stdin) # type is a stream. 

    """ 
    stdout is just another way to print to the terminal instead of 
    saying "print"

    You can reset the location of sys.stdout to another stream 
    like open a file as a stream f
    then set sys.stdout = f
    and now sys.stdout.write() or print() will write to that file. 
    
    to reset, just set it back to sys.__stdout__ and it'll go back
    to the terminal. 
    """ 

    # Open a file to write
    with open('myfile.txt', 'w') as f:
        # Redirect stdout to the file
        sys.stdout = f
        print("This will be written to the file.")
        # Restore stdout to its original value
        sys.stdout = sys.__stdout__
        print("This will be printed to the console.")
        
    sys.stdout.write("You entered:")
    for line in user_input:
        print(line)

    """ you can use stderrr here like this to just write an error 
    just like you would with stdout """ 
    sys.stderr.write("this is an error.") 

if __name__ == "__main__":
    # Open a file to write error messages
    with open('error.log', 'w') as f:
        # Redirect stderr to the file
        sys.stderr = f
        main()
        # Restore stderr to its original value
        sys.stderr = sys.__stderr__
    print("Error logging complete. Check error.log for details.")