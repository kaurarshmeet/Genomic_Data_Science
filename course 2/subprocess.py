import subprocess
import sys

""" .run() is the same thing is putting anything into your terminal.
Only use shell = True if you're typing the args for security. 
-la gives you more information. 
"""
subprocess.run('ls -la', shell = True) # lists everything in the current directory
p1 = subprocess.run(['ls', '-la']) # does the same thing.

print(p1) # completed process object
print(p1.args) # check the args

# CompletedProcess(args=['ls', '-la'], returncode=0)
print(p1.returncode) # shows if you got any errors. 0 means 0 errors.
print(p1.stdout) # None, sending stdout to console.

# won't output anything to the python console.
p2 = subprocess.run(['ls', '-la'], capture_output=True) # makes it so that output is saved
print(p2.stdout) # captured as bytes, odd formatting.
print(p2.stdout.decode()) # decoded bytes.
subprocess.run(['ls', '-la'], capture_output=True, text = True) # decoded from bytes

# this will put it in the terminal, subprocess.PIPE
subprocess.run(['ls', '-la'], stdout = subprocess.PIPE, text = True) # decoded from bytes

# put the output in a file.
with open('output.txt', 'w') as f:

    """
    if you include 'dne' it'll cause an error, which doesn't actually show.
    you have to check for errors at the end and print them out.
    Python won't throw errors on its own. 
    
    If you want it to throw errors on its own 
    """

    with open('errors.log', 'w') as e:
        # p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)  # decoded from bytes

        # if you want the errors in a file, specify inside p1
        p1 = subprocess.run(['ls', '-la', 'dne'], stdout = f, stderr= e, text = True) # decoded from bytes

    if p1.returncode == 0:
        sys.stdout.write('Process finished with exit code 0.')
    else:
        # lets you know that you have to check the error log.
        sys.stdout.write(f'Process finished with exit code {p1.returncode}.')

# another way to do this
p3 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text = True) # text=True decoded from bytes
with open('another_output.txt', 'w') as output:
    output.write(p3.stdout)
with open('another_error.log', 'w') as errorlog:
    errorlog.write(p3.stderr)